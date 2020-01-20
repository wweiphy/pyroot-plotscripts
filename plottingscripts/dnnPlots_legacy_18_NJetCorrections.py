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
import util.monitorTools as monitorTools
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
    name = 'discriminatorPlots/v1_2018'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # signal process
    signalProcess = "ttH"
    nSigSamples   = 1

    # dataera
    dataera = "2018"

    # Name of final discriminator, should not contain underscore
    discrName = 'finaldiscr'
    nom_histname_template = "$PROCESS__$CHANNEL"
    syst_histname_template = nom_histname_template + "__$SYSTEMATIC"
    histname_separator = "__"
    # hotfix for datacards
    nom_histname_template_dc = "$PROCESS__"+discrName+"_$CHANNEL"
    syst_histname_template_dc = nom_histname_template_dc + "__$SYSTEMATIC"


    # define MEM discriminator variable
    # memexp = '(memDBp>=0.0)*(memDBp)+(memDBp<0.0)*(0.01)+(memDBp==1.0)*(0.01)'
    memexp = ''
    # configs
    config          = "legacyAnalysis/samples_2018_4FS_5FS_NJetCorrections_JECgroups"
    variable_cfg    = "legacyAnalysis/additionalVariables_2018"
    plot_cfg        = "legacyAnalysis/discrPlots"
    syst_cfg        = "legacyAnalysis/systs_4FS_5FS_NJetCorrections_JECgroups_2018"

    # file for rate factors
    #rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    rateFactorsFile = pyrootdir + "/data/rateFactors/rateFactors_2018.csv"

    # script options
    analysisOptions = {
        # general options
        "usePseudoData":        True,
        "testrun":              False,  # test run with less samples
        "stopAfterCompile":     False,   # stop script after compiling
        # options to activate parts of the script
        "haddFromWildcard":     True,
        "makeDataCards":        True,
        "makeInputDatacards":   False, # create datacards also for all defined plots
        "addData":              True,  # adding real data 
        "makePlots":            True,
        # options for makePlots
        "signalScaling":        -1,
        "lumiLabel":            True,
        "CMSlabel":             "private Work",
        "ratio":                "#frac{pseudo data}{simulation}",
        "shape":                False,
        "logarithmic":          False,
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

    plotJson = ""
    # plotDataBases = [["memDB","/nfs/dust/cms/user/swieland/ttH_legacy/MEMdatabase/databases/2017_/",True]] 
    # memDataBase = "/nfs/dust/cms/user/swieland/ttH_legacy/MEMdatabase/CodeforScriptGenerator/MEMDataBase/MEMDataBase"
    dnnInterface = {"interfacePath":    pyrootdir+"/util/dNNInterfaces/MLfoyInterface.py",
                   "checkpointFiles":  "/nfs/dust/cms/user/vdlinden/legacyTTH/DNNSets/legacyAnalysis_v1"}

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

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

    print '''
    # ========================================================
    # prepare configdata
    # ========================================================
    '''

    configData = configClass.configData(
        analysisClass   = analysis,
        variable_config = variable_cfg,
        plot_config     = plot_cfg,
        execute_file    = os.path.realpath(inspect.getsourcefile(lambda:0)))

    configData.initSystematics(systconfig = syst_cfg)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp, dnnInterface)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")
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
    
    with monitor.Timer("plotParallel"):
        # initialize plotParallel class 
        pP = plotParallel.plotParallel(
            analysis = analysis,
            configData = configData,
            nominalHistKey = nom_histname_template,
            systHistKey = syst_histname_template,
            separator = histname_separator)

        monitor.printClass(pP, "init")
        # set some changed values
        pP.setJson(plotJson)
        #pP.setDataBases(plotDataBases)
        #pP.setMEMDataBase(memDataBase)
        pP.setDNNInterface(dnnInterface)
        pP.setMaxEvts(500000)
        pP.setRateFactorsFile(rateFactorsFile)
        pP.setSampleForVariableSetup(configData.samples[nSigSamples])

        # run plotParallel
        pP.run()

    pP.checkTermination()
    monitor.printClass(pP, "after plotParallel")

    # hadd histo files before renaming. The histograms are actually already renamed. 
    # But the checkbins thingy will not have been done yet.
    print '''
    # ========================================================
    # hadding from wildcard
    # ========================================================
    '''
    with monitor.Timer("haddFilesFromWildCard"):
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

        with monitor.Timer("checkHistos"):
            checkHistos.checkHistsManager(
                inFiles         = pP.getRenameInput(),
                outFile         = analysis.renamedPath,
                checkBins       = True,
                eps             = 0.0,
                skipHistoCheck  = analysis.skipHistoCheck)


    if analysis.addData:
        print '''
        # ========================================================
        # adding data with plotParallel
        # ========================================================
        '''
        with monitor.Timer("addRealData"):
            if analysis.usePseudoData:
                print("adding data_obs histograms as pseudo data")
                # pseudo data without ttH
                pP.addData( samples = configData.samples[:-1], 
                            discrName = discrName)
                # pseudo data with signal
                #pP.addData(samples = configData.samples)
            else:
                print("adding data_obs histograms as real data")
                # real data with ttH
                pP.addData( samples = configData.controlSamples, 
                            discrName = discrName)

    

    pP.checkTermination()       
    monitor.printClass(pP, "after plotParallel completely done")

    print("########## DONE WITH PLOTPARALLEL STEP ##########")
    print("at the moment the outputpath is "+str(analysis.renamedPath))
    print("#################################################")

    if analysis.makeDataCards or analysis.makeInputDatacards and not opts.skipDatacards:
        print '''
        # ========================================================
        # Making Datacards.
        # ========================================================
        '''
        with monitor.Timer("makeDatacardsParallel"):
            makeDatacards.makeDatacardsParallel(
                filePath            = analysis.renamedPath,
                workdir             = analysis.workdir,
                categories          = configData.getDatacardLabels(analysis.makeInputDatacards),
                doHdecay            = True,
                discrname           = analysis.discrName,
                datacardmaker       = datacardmaker,
                signalTag           = analysis.signalProcess,
                skipDatacards       = analysis.skipDatacards,
                nominal_key         = nom_histname_template_dc,
                syst_key            = syst_histname_template_dc
                )
    
    if analysis.makePlots:
        print '''
        # ========================================================
        # Making Plots
        # ========================================================
        '''
        with monitor.Timer("makePlots"):
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

    (opts, args) = parser.parse_args()
    main(pyrootdir, opts)