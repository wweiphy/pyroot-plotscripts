#!/usr/bin/python2
import sys
import os
import imp
import inspect
import ROOT

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])

sys.path.append(pyrootdir)

# local imports
import util.analysisClass as analysisClass
import util.optBinning as optBinning
import util.genPlots as genPlots
import util.configClass as configClass
import util.monitorTools as monitorTools
import util.plotParallel as plotParallel
import util.drawParallel as drawParallel
import util.haddParallel as haddParallel
import util.renameHistos as renameHistos
import util.makeDatacards as makeDatacards

def main(pyrootdir, argv):
    print '''
    # ========================================================
	# welcome to main function - defining some variables
    # ========================================================
    '''
    # name of the analysis (i.e. workdir name)
    name = 'ttbb-GENstudies'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
    
    # path to root file
    rootPathForAnalysis = workdir+'/output_limitInput.root'

    # signal process
    signalProcess = "ttbb"

    # Name of final discriminator, should not contain underscore
    discrName = ''

    # define MEM discriminator variable
    memexp = ''

    # name of the csv files used in configdata folder
    configDataBaseName = "ttbb-GENstudies"

    # name of plotconfig
    pltcfgName = "GEN"

    # file for rate factors
    #rateFactorsFile = pyrootdir + "/data/rate_factors_onlyinternal_powhegpythia.csv"
    #rateFactorsFile = ""

    # script options
    analysisOptions = {
        # general options
        "plotBlinded":          False,  # blind region
        "cirun":                False,  # test run with less samples
        "haddParallel":         True,  # parallel hadding instead of non-parallel
        "useOldRoot":           False,   # use existing root file if it exists (skips plotParallel)
        # options to activate parts of the script
        "optimizedRebinning":   False, # e.g. "SoverB", "Significance"
        "haddFromWildcard":     True,
        "makeDataCards":        False,
        "addData":              False,  # adding real data 
        "singleExecute":        False,  # for non parallel drawing
        "drawParallel":         True,
        # options for drawParallel/singleExecute sub programs
        "makeSimplePlots":      True,
        "makeMCControlPlots":   False,
        "makeEventYields":      False,
        # the skipX options try to skip the submission of files to the batch system
        # before skipping the output is crosschecked
        # if the output is not complete, the skipped part is done anyways
        "stopAfterCompile":     False,   # stop script after compiling
        "skipPlotParallel":     False,
        "skipHaddParallel":     False,
        "skipHaddFromWildcard": False,
        "skipRenaming":         False,
        "skipDatacards":        False}

    plotJson = "" #"/nfs/dust/cms/user/mhorzela/DPGjson.json"
    #plotDataBases = [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_ttH_2018",True]] 
    #memDataBase = "/nfs/dust/cms/user/kelmorab/DataBaseCodeForScriptGenerator/MEMDataBase_ttH2018/MEMDataBase/MEMDataBase/"

    # datacardmaker
    datacardmaker = "mk_datacard_JESTest13TeVPara"

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # save a lot of useful information concerning the analysis
    analysis = analysisClass.analysisConfig(
        workdir = workdir, 
        pyrootdir = pyrootdir, 
        rootPath = rootPathForAnalysis, 
        signalProcess = signalProcess, 
        pltcfgName = pltcfgName,
        discrName = discrName)

    analysis.initArguments( argv )
    analysis.initAnalysisOptions( analysisOptions )

    pltcfg = analysis.initPlotConfig()
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    analysis.printChosenOptions()

    # loading monitorTools module locally
    monitor = monitorTools.init(analysis.workdir)
    monitor.printClass(analysis, "init")

    print '''
    # ========================================================
    # prepare configdata
    # ========================================================
    '''

    configData = configClass.configData(
        analysisClass = analysis,
        configDataBaseName = configDataBaseName)

    configData.initData()

    # get the discriminator plots
    configData.genDiscriminatorPlots(memexp)
    configData.writeConfigDataToWorkdir()
    monitor.printClass(configData, "init")

    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables() # also adds DNN variables
    #configData.getMEPDFAddVariables(MEPDFCSVFile)

    # save addition variables information to workdir and print
    configData.printAddVariables()
    monitor.printClass(configData, "after getting additional Variables")

    #print '''
    # ========================================================
    # Check if additional (input) variables should be plotted
    # if necessary add them here to the discriminatorPlots
    # ========================================================
    #'''
    # Construct list with additional plot variables, 
    # will need name of discrs and plotPreselections for this
    #print( "add additional plot variables")
    #configData.getAdditionalDiscriminatorPlots() # TODO
    

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

    if analysis.plotNumber == None or analysis.singleExecute:
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
                configData = configData)

            monitor.printClass(pP, "init")
            # set some changed values
            pP.setJson(plotJson)
            #pP.setDataBases(plotDataBases)
            #pP.setMEMDataBase(memDataBase)
            pP.setCatNames([''])
            pP.setCatSelections(['1.'])
            pP.setMaxEvts(350000)
            #pP.setRateFactorsFile(rateFactorsFile)
            pP.setSampleForVariableSetup(configData.samples[0])

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
            haddParallel.haddSplitter( input = pP.getHaddOutPath(),
                outName = analysis.ppRootPath,
                subName = "haddParts",
                nHistosRemainSame = True,
                skipHadd = analysis.skipHaddFromWildcard)
        


        if analysis.optimizedRebinning:
            print '''
            # ========================================================
            # Doing OptimizedRebinning
            # ========================================================
            '''
            #TODO rework
            if analysis.signalProcess == 'ttbb':
                # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                # TODO check the optimizedBinning function and adjust arguments to new structure
                # TODO rework samples splitting to be automated in samplesDataClass?
                # TODO call this only once and determine bkg/signal samples in the function itself
                with monitor.Timer("optimizeBinning"):
                    optBinning.optimizeBinning(
                        infname = analysis.ppRootPath,
                        signalsamples = [configData.samples[0]], 
                        backgroundsamples = configData.samples[1:],
                        additionalSamples= [],
                        plots = configData.getDiscriminatorPlots(), 
                        systnames = configData.allSystNames, 
                        minBkgPerBin = 2.0, 
                        optMode = "Stats",
                        considerStatUnc = False, 
                        maxBins = 20, 
                        minBins = 2,
                        verbosity = 2)

            elif analysis.signalProcess == 'ttH':
                # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. 
                # Rest: background samples
                with monitor.Timer("optimizeBinning"):
                    optBinning.optimizeBinning(
                        analysis.ppRootPath,
                        signalsamples = [configData.samples[0]], 
                        backgroundsamples = configData.samples[9:],
                        additionalSamples= configData.samples[1:9] + configData.controlSamples, 
                        plots = configData.getDiscriminatorPlots(), 
                        systnames = configData.allSystNames, 
                        minBkgPerBin = 2.0, 
                        optMode = analysis.optimizedRebinning,
                        considerStatUnc = False, 
                        maxBins = 20, 
                        minBins = 2,
                        verbosity = 2)
            else:
                print("WARNING - could not find signal process")
                print("not doing optimized rebinning")



         


        # Deactivate check bins functionality in renameHistos 
        #   if additional plot variables are added via analysis class
        if os.path.exists( analysis.setRenamedPath(name = "limitInput") ):
            print( "renamed file already exists - skipping renaming histos" )
        elif analysis.skipRenaming:
            print("skipping renaming TODO")
            # WIP rename skip TODO
        else:
            print '''
            # ========================================================
            # renaming Histograms
            # ========================================================
            '''

            pP.setRenameInput()
            # in this function the variable self.renameInput is set
            # if hadd files were created during plotParallel
            #       (which is equivalent to THEoutputpath == list) 
            #       the renameInput is set to pP.getHaddFiles 
            #       (a.k.a. the list of hadd files)
            # if no hadd files were created during plotparallel
            #       (which is equivalent to THEoutputlath == str)
            #       the renameInput is set to pp.getOutPath 
            #       (a.ka. the path to output.root)

            with monitor.Timer("renameHistos"):
                renameHistos.renameHistos(
                    inFiles = pP.getRenameInput(),
                    outFile = analysis.renamedPath,
                    systNames = configData.allSystNames,
                    checkBins = True,
                    prune = False,
                    Epsilon = 0.0,
                    skipRenaming = analysis.skipRenaming)

        if analysis.addData:
            print '''
            # ========================================================
            # adding data with plotParallel
            # ========================================================
            '''
            with monitor.Timer("addRealData"):
                # real data with ttH
                # pP.addData(samples = configData.controlSamples)

                # pseudo data without ttH
                pP.addData(samples = configData.samples[9:])
        

        pP.checkTermination()       
        monitor.printClass(pP, "after plotParallel completely done")

        print("########## DONE WITH PLOTPARALLEL STEP ##########")
        print("at the moment the outputpath is "+str(analysis.renamedPath))
        print("#################################################")

        if analysis.makeDatacards:
            print '''
            # ========================================================
            # Making Datacards.
            # ========================================================
            '''
            # init datacards path
            datacardsPath = analysis.workdir+"/datacards"
            if not os.path.exists(datacardsPath):
                os.makedirs(datacardsPath)

            with monitor.Timer("makeDatacardsParallel"):
                makeDatacards.makeDatacardsParallel(
                    filePath = analysis.renamedPath,
                    outPath = datacardsPath,
                    categories = configData.getBinlabels(),
                    doHdecay = True,
                    discrname = analysis.discrName,
                    datacardmaker = datacardmaker,
                    skipDatacards = analysis.skipDatacards)


        # =============================================================================================
        # Invoke drawParallel step
        # =============================================================================================
        if analysis.drawParallel:
            print '''
            # ========================================================
            # Starting DrawParallel
            # ========================================================
            '''
            with monitor.Timer("DrawParallel"):
                drawParallel.drawParallel(
                    ListOfPlots = configData.getDiscriminatorPlots(),
                    workdir = analysis.workdir,
                    PathToSelf = os.path.realpath(inspect.getsourcefile(lambda:0)),
                    # Hand over opts to keep commandline options
                    opts = analysis.opts)
            print '''
            # ========================================================
            # this is the end of the script 
            # ========================================================
            '''





    # =============================================================================================
    # everything beyond this point is called by the secondary scripts
    # =============================================================================================
    elif analysis.plotNumber != None or analysis.singleExecute:
        print("not doing plotParallel step")
        if analysis.drawParallel:
            print("we have a plotNumber --- changing discriminatorPlots")
            configData.getDiscriminatorPlotByNumber()

        if analysis.makeSimplePlots or analysis.makeMCControlPlots or analysis.makeEventYields:
            print '''
            # ========================================================
            # Creating lists for later use
            # ========================================================
            '''
            # print analysis.renamedPath
            analysis.renamedPath=analysis.renamedPath.replace("_limitInput","")

            gP = genPlots.genPlots( 
                outPath = analysis.renamedPath,
                plots   = configData.getDiscriminatorPlots(),
                plotdir = analysis.getPlotPath(),
                rebin   = 1)

            histoList       = gP.genList(samples = configData.samples[0:])
            dataList        = gP.genList(samples = configData.controlSamples)
            # pseudodataList  = gP.genList(samples = [configData.samples[0]]+configData.samples[9:])
            pseudodataList = gP.genList(samples = configData.samples[0:])
            monitor.printClass(gP, "after creating init lists")






        if analysis.makeSimplePlots:
            print '''
            # ========================================================
            # Making simple MC plots
            # ========================================================
            '''
            with monitor.Timer("makingSimpleMCplots"):
                # creating control plots
                

                
                
                #controlPlotOptions = {
                    #"factor":           -1,
                    #"logscale":         True,
                    #"canvasOptions":    "histo",
                    #"normalize":        False,
                    #"stack":            False, # not default
                    #"ratio":            False,
                    #"sepaTest":         False}
                #sampleConfig = genPlots.Config(
                    #histograms  = histoList,
                    #sampleIndex = 0)
                #gP.makeSimpleControlPlots( sampleConfig, controlPlotOptions )

                # creating shape plots
                shapePlotOptions = {
                    "logscale":         True,
                    "canvasOptions":    "histo",
                    "normalize":        True, # not default
                    "stack":            False,
                    "ratio":            True,
                    "errorband":        True,
                    "statTest":         False,
                    "sepaTest":         False,
                    "privateWork":      True}
                sampleConfig = genPlots.Config(
                    histograms  = histoList,
                    sampleIndex = 0)
                # generate the llloflist internally
                sampleConfig.addNestedHistList(
                    genPlotsClass = gP,
                    systNames = pltcfg.errorSystNames)
                sampleConfig.addErrorbandConfig({
                    "style":        1001, 
                    "color":        ROOT.kRed, 
                    "doRateSysts":  False})
                gP.makeSimpleShapePlots( sampleConfig, label = "", options = shapePlotOptions )

                monitor.printClass(gP, "after making simple MC plots")



        if analysis.makeMCControlPlots:
            print '''
            # ========================================================
            # Making MC Control plots
            # ========================================================
            '''
            with monitor.Timer("makingMCControlPlots"):
                sampleConfig = genPlots.Config(
                    histograms  = histoList,
                    sampleIndex = 0)

                # generate the llloflist internally
                sampleConfig.genNestedHistList(
                    genPlotsClass = gP,
                    systNames = pltcfg.errorSystNames)
                sampleConfig.setErrorbandConfig({
                    "style":        3354, 
                    "color":        ROOT.kBlack, 
                    "doRateSysts":  False})
        

                pseudodataConfig = genPlots.Config(
                    histograms  = pseudodataList,
                    sampleIndex = 0)

                #set general plotoption
                controlPlotOptions = {
                    "factor":           -2, #not default
                    "logscale":         False,
                    "canvasOptions":    "histo",
                    "ratio":            True, # not default
                    "blinded":          analysis.plotBlinded} #not default
                # making the control plots
                gP.makeControlPlots(
                    sampleConfig = sampleConfig,
                    dataConfig   = pseudodataConfig,
                    options      = controlPlotOptions,
                    outName      = "controlPlots_pseudodata")


                controlPlotOptions["logscale"] = True
                gP.makeControlPlots(
                    sampleConfig = sampleConfig,
                    dataConfig   = pseudodataConfig,
                    options      = controlPlotOptions,
                    outName      = "controlPlots_pseudodata_LOG")

            monitor.printClass(gP, "after making control plots")

        if analysis.makeEventYields:
            print '''
            # ========================================================
            # Making Event Yields
            # ========================================================
            '''
            with monitor.Timer("makeEventYields"):
                gP.makeEventYields(
                    categories    = configData.getEventYieldCategories(),
                    samplesConfig = histoList,
                    dataConfig    = pseudodataList,
                    nameRequirements = ["node"]
                    )


if __name__ == "__main__":

    main(pyrootdir, sys.argv[1:])