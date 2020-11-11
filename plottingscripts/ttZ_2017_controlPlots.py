#!/usr/bin/python2
import sys
import os
import imp
import inspect
import optparse
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)

# local imports
import util.analysisClass as analysisClass
import util.configClass as configClass
import util.plotParallel as plotParallel
import util.makePlots as makePlots
import util.haddParallel as haddParallel
import util.checkHistos as checkHistos
import util.makeDatacards as makeDatacards

def main(pyrootdir, opts):
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''
    # name of the analysis (i.e. workdir name)
    name = 'controlPlots/2017/v9'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # signal process
    signalProcess = "ttZ"
    nSigSamples   = 1

    # dataera
    dataera = "2017"

    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'
    nom_histname_template = "$CHANNEL__$PROCESS"
    syst_histname_template = nom_histname_template + "__$SYSTEMATIC"
    histname_separator = "__"

    # define MEM discriminator variable
    memexp = ''
    # configs
    config          = "runII_ttZ/samples_2017"
    variable_cfg    = "runII_ttZ/additionalVariables"
    plot_cfg        = "runII_ttZ/controlPlots"
    syst_cfg        = "runII_ttZ/systs_2017"
    replace_cfg     = None

    # script options
    analysisOptions = {
        # general options
        "usePseudoData":        False,
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,   # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard":     True,
        "makeDataCards":        False,
        "makeInputDatacards":   False, # create datacards also for all defined plots
        "addData":              True,  # adding real data 
        "makePlots":            True,
        # options for makePlots
        "signalScaling":        -1,
        "lumiLabel":            True,
        "cmslabel":             "private Work",
        "ratio":                "#frac{data}{exp. background}",
        "shape":                False,
        "logarithmic":          True,
        "splitLegend":          True,
        "normalize":            False,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "skipPlotParallel":     opts.skipPlotParallel,
        "skipHaddParallel":     opts.skipHaddParallel,
        "skipHaddFromWildcard": opts.skipHaddFromWildcard,
        "skipHistoCheck":       opts.skipHistoCheck,
        "skipDatacards":        opts.skipDatacards}

    #dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
    #               "checkpointFiles":  "/nfs/dust/cms/user/vdlinden/legacyTTH/DNNSets/massCorrection_v3/"}
    dnnInterface = None
    
    # path to datacardMaker directory
    datacardmaker = "/nfs/dust/cms/user/lreuter/forPhilip/datacardMaker"

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # save a lot of useful information concerning the analysis
    analysis = analysisClass.analysisConfig(
        workdir         = workdir, 
        pyrootdir       = pyrootdir, 
        signalProcess   = signalProcess, 
        pltcfgName      = config,
        discrName       = discrName,
        dataera         = dataera)

    
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    print '''
    # ========================================================
    # prepare configdata
    # ========================================================
    '''

    configData = configClass.configData(
        analysisClass   = analysis,
        variable_config = variable_cfg,
        plot_config     = plot_cfg,
        replace_config  = replace_cfg,
        execute_file    = os.path.realpath(__file__),
        )

    configData.initSystematics(systconfig = syst_cfg)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp, dnnInterface)
    configData.writeConfigDataToWorkdir()
    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables() # also adds DNN variables

    print '''    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    '''
    configData.initSamples()
    

    print '''
    # ========================================================
    # done with preprocessing
    # ========================================================
    '''

    # plot everything, except during drawParallel step
    # Create file for data cards
    print '''
    # ========================================================
    # starting with plotParallel step
    # ========================================================
    '''
    
    # initialize plotParallel class 
    pP = plotParallel.plotParallel(
        analysis        = analysis,
        configData      = configData,
        nominalHistKey  = nom_histname_template,
        systHistKey     = syst_histname_template,
        separator       = histname_separator)

    # set some changed values
    #pP.setDNNInterface(dnnInterface)
    pP.setMaxEvts_nom(200000)
    pP.setMaxEvts_systs(500000)
    pP.setSampleForVariableSetup(configData.samples)
    pP.setUseFriendTrees(True)
    # run plotParallel
    pP.run()

    pP.checkTermination()

    # hadd histo files before renaming. The histograms are actually already renamed. 
    # But the checkbins thingy will not have been done yet.
    print '''
    # ========================================================
    # hadding from wildcard
    # ========================================================
    '''
    haddParallel.haddSplitter( 
        input               = pP.getHaddOutPath(),
        outName             = analysis.ppRootPath,
        subName             = "haddParts",
        nHistosRemainSame   = True,
        skipHadd            = analysis.skipHaddFromWildcard)
 


    # Deactivate check bins functionality in renameHistos 
    #   if additional plot variables are added via analysis class
    if os.path.exists( analysis.setRenamedPath(name = "limitInput") ):
        print( "renamed file already exists - skipping renaming histos" )
    else:
        print '''
        # ========================================================
        # renaming Histograms
        # ========================================================
        '''

        pP.setRenameInput()
        # in this function the variable self.renameInput is set
        # if hadd files were created during plotParallel
        #       the renameInput is set to pP.getHaddFiles 
        #       (a.k.a. the list of hadd files)
        # if no hadd files were created during plotparallel
        #       the renameInput is set to pp.getOutPath 
        #       (a.ka. the path to output.root)

        checkHistos.checkHistsManager(
            inFiles         = pP.getRenameInput(),
            outFile         = analysis.renamedPath,
            checkBins       = True,
            eps             = 0.0,
            skipHistoCheck  = analysis.skipHistoCheck)

    if pP.configData.replace_config and not analysis.skipMergeSysts:
        print("merging systematics")
        pP.mergeSystematics()

    if analysis.addData:
        print '''
        # ========================================================
        # adding data with plotParallel
        # ========================================================
        '''
        if analysis.usePseudoData:
            print("adding data_obs histograms as pseudo data")
            pseudoDataSamples = [s for s in configData.samples if not ("ttZ_" in s.nick or "ttH_" in s.nick or "5FS" in s.nick)]
            pP.addData( samples = pseudoDataSamples, 
                        discrName = discrName)
        else:
            print("adding data_obs histograms as real data")
            pP.addData( samples = configData.controlSamples, 
                            discrName = discrName)

    

    pP.checkTermination()       

    print("########## DONE WITH PLOTPARALLEL STEP ##########")
    print("at the moment the outputpath is "+str(analysis.renamedPath))
    print("#################################################")

    if analysis.makeDataCards or analysis.makeInputDatacards and not opts.skipDatacards:
        print '''
        # ========================================================
        # Making Datacards.
        # ========================================================
        '''
        makeDatacards.makeDatacardsParallel(
            filePath            = analysis.renamedPath,
            workdir             = analysis.workdir,
            categories          = configData.getDatacardLabels(analysis.makeInputDatacards),
            doHdecay            = True,
            discrname           = analysis.discrName,
            datacardmaker       = datacardmaker,
            signalTag           = analysis.signalProcess,
            skipDatacards       = analysis.skipDatacards,
            nominal_key         = nom_histname_template,
            syst_key            = syst_histname_template
            )

    if analysis.makePlots:
        print '''
        # ========================================================
        # Making Plots
        # ========================================================
        '''
        makePlots.makePlots(configData  = configData,
            nominal_key = nom_histname_template,
            syst_key    = syst_histname_template)


    print '''
    # ========================================================
    # this is the end of the script 
    # ========================================================
    '''

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--skipPlotParallel",     dest = "skipPlotParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddParallel",     dest = "skipHaddParallel",      action = "store_true", default = False)
    parser.add_option("--skipHaddFromWildcard", dest = "skipHaddFromWildcard",  action = "store_true", default = False)
    parser.add_option("--skipHistoCheck",       dest = "skipHistoCheck",        action = "store_true", default = False)
    parser.add_option("--skipDatacards",        dest = "skipDatacards",         action = "store_true", default = False)
    parser.add_option("--skip",                 dest = "skip",                  default = 0,            type = "int",
        help = "skip first INT parallel stages. plotParallel (1), haddParallel (2), haddFromWildcard (3), histoCheck (4), Datacards (5)")

    (opts, args) = parser.parse_args()

    if opts.skip >= 1: opts.skipPlotParallel        = True
    if opts.skip >= 2: opts.skipHaddParallel        = True
    if opts.skip >= 3: opts.skipHaddFromWildcard    = True
    if opts.skip >= 4: opts.skipHistoCheck          = True
    if opts.skip >= 5: opts.skipDatacards           = True


    main(pyrootdir, opts)
