#!/usr/bin/python2

import sys
import getopt
import os
import imp
#import importlib
import inspect
import ROOT
import pandas 
import ast

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = "/".join(filedir.split("/")[:-1])
workdir = pyrootdir+"/"+"workdir"

sys.path.append(pyrootdir+'/util')
sys.path.append(filedir+"/configs")

import plotutils
import tmputils
import PDFutils
import runTimer
import limittools
import plotParallel

import analysisClass
import plotconfig_v14 as pltcfg

def main(pyrootdir, argv):
    print '''
    # ========================================================
    # welcome to main function - defining some variables
    # ========================================================
    '''
    # BIG TODO: decide what needs to be initialized by the secondary scripts
    # maybe give some information as an argument instead of doing it all over again
    # initializing everything only takes < 1 minute per script but takes a lot of disk i think

    # name of the analysis (i.e. workdir name)
    name='testrun'

    # path to workdir subfolder where all information should be saved
    workdir = pyrootdir + "/workdir/" + name

    # creating workdir subfolder
    if not os.path.exists(workdir):
        os.makedirs(workdir)
        print("created workdir at "+str(workdir))
        
    # path to root file
    anaRootPath=workdir+'/output_limitInput.root'

    # Name of final discriminator, should not contain underscore
    discrname='finaldiscr'

    # define MEM discriminator variable
    # this is not used anymore as the information is written in the csv files in configdata
    # keep it for clarity
    # memexp='(memDBp>0.0)*(memDBp)+(memDBp<=0.0)*(0.01)+(memDBp==1.0)*(0.01)'

    # define BDT output variables
    bdtweightpath="/nfs/dust/cms/user/kelmorab/Spring17BDTWeights/"
    bdtset="Spring17v2"
    alternativebdtset="Spring17v3_ttbb"

    # name of the csv files used in configdata folder
    configDataBaseName = "limitsAllv20"

    # used categories in configdata to be added
    usedCategories = ["JTBDT", "JT2D", "JTMEM", "MultiDNN", "JT_control"] 
    # usedCategories += ["JT2DOPTIMIZED", "JTBDTOPTIMIZED"]
    
    # signal process
    signalProcess = "ttH"
    #############################################################################
    # there should be no information that needs hard coded adjusting below this #
    #############################################################################

    print '''
    # ========================================================
    # initializing analysisClass 
    # ========================================================
    '''

    # TODO make the analysisClass more essential - atm it is not really needed
    analysis = analysisClass.Analysis(workdir, argv, anaRootPath, signalProcess = signalProcess)

    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/mharrend/doktorarbeit/latest/ttbb-cutbased-analysis_limitInput.root')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/kelmorab/plotscriptsSpring17/Sep17/pyroot-plotscripts/NOTDEFINED/output_limitInput.root ', signalProcess='ttH')
    #analysis=analysisClass.Analysis(name,argv,
        #'/nfs/dust/cms/user/mharrend/doktorarbeit/output20170626-reference/workdir/ttbb-cutbased-analysis/output_limitInput.root')
    
    # TODO these options should be set automatically ?
    analysis.plotBlinded = True
    analysis.makeSimplePlots = True
    analysis.makeMCControlPlots = True
    analysis.makeDataCards = True
    analysis.additionalPlotVariables = False

    # Make sure proper plotconfig is loaded for either ttbb or ttH
    # TODO how is this determined?
    print "We will import the following plotconfig: ", analysis.getPlotConfig()

    # TODO maybe print chosen functions into a .json file in workdir
    analysis.printChosenOptions()



    #print '''    
    ## ========================================================
    ## NNFlow interface
    ## ========================================================
    #'''
    #
    # Create and configure NNFlow interface
    # NNFlowInterfacePath=os.getcwd()+'../util/dNNInterfaces/NNFlowInterface.py'
    # NNFlowInterface = imp.load_source("NNFlowInterface",NNFlowInterfacePath).theInterface()
    # NNFlowInterface.setDebugOutput(True)
    # NNFlowInterface.setModelFolderPath(
    #    '/nfs/dust/cms/user/mharrend/doktorarbeit/tensorflowModels/neural_network_v3/multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20/model')
    # NNFlowInterface.setModelName('multiclass_ttlight_ttcc_ttb_tt2b_ttbb_ttH_top_20.ckpt')
    # NNFlowInterface.update()
    #
    # print "NNFlowInterfacePath: ", NNFlowInterfacePath


    print '''
    # ========================================================
    # prepare configdata
    #
    # access the information via
    # configData.Data.categories
    # configData.Data.nhistobins
    # configData.Data.minxvals
    # configData.Data.maxxvals
    # configData.Data.discrs
    # configData.Data.plotPreselection
    # configData.Data.binlabels
    # configData.Data.discriminatorPlots
    # configData.addVars
    # ========================================================
    '''

    configData = tmputils.configData(pyrootdir = pyrootdir, 
                                    analysisClass = analysis,
                                    configDataBaseName = configDataBaseName, 
                                    usedCategories = usedCategories)
    configData.writeConfigDataToWorkdir(analysis.workdir)
    configData.assertData()

    configData.printLengths()
    configData.genDiscriminatorPlots(discrname)

    print '''    
    # ========================================================
    # define additional variables necessary for selection in plotparallel
    # ========================================================
    '''
    configData.getAddVariables()
    configData.getMEPDFAddVariables(
        "/nfs/dust/cms/user/kelmorab/DataFilesForScriptGenerator/rate_factors_onlyinternal_powhegpythia.csv")
    #additionalvariables.extend(NNFlowInterface.getAdditionalVariablesList())

    # save addition variables information to workdir and print
    configData.printAddVariables(analysis.workdir)


    print '''    
    # ========================================================
    # loading samples and samples data
    # ========================================================
    '''
    samplesData = tmputils.samplesData(pltcfg)
    
    print '''
    # ========================================================
    # add systematic samples
    # ========================================================
    '''
    samplesData.addSystSamples(
                        pltcfg.otherSystNames, pltcfg.otherSystFileNames,
                        pathReplace = ["'nominal'","filename"]
                        )
    ## WARNING: Adjust Slice for samples if changing ttbar contributions
    
    print '''
    # ========================================================
    # add Parton shower variation samples to systematic samples
    # ========================================================
    '''
    nicks = ['ttbarOther', 'ttbarPlusCCbar','ttbarPlusBBbar','ttbarPlusB','ttbarPlus2B']
    samplesData.addSystSamples(
                        pltcfg.PSSystNames, pltcfg.PSSystFileNames,
                        pathReplace = ["self.pltcfg.ttbarPathS",
                            "'self.pltcfg.path_additionalSamples+'/ttbar_'+filename+'/*nominal*.root'"],
                        selReplace = ["self.pltcfg.ttbarMCWeight","'*1.0'"],
                        selReplace2 = ["self.pltcfg.mcWeight+self.pltcfg.evenSel","self.pltcfg.mcWeightAll"],
                        filternicks = nicks)

    #for sample in samples[analysis.getTtbarSamplesLower() : analysis.getTtbarSamplesUpper()]: # only for ttbar samples
    print '''
    # ========================================================
    # add QCD sytematic for QCD sample to systematic samples
    # ========================================================
    '''
    samplesData.addSystSamples(
                        pltcfg.QCDSystNames, pltcfg.QCDSystReplacementStrings,
                        selReplace = ["'internalQCDweight'", "filename"],
                        filtername = "QCD")
    
    print '''
    # ========================================================
    # finish up sample gathering
    #
    # information accesible via
    # samplesData.samples = pltcfg.samplesLimits
    # samplesData.controlSamples  = pltcfg.samplesDataControlPlots
    # samplesData.allNames = addNames + self.systNames
    # samplesData.allSamples = self.samples + self.controlSamples + self.systSamples
    # samplesData.allSystSamples = self.samples + self.systSamples
    #
    # ========================================================
    '''
    samplesData.addAllSamples(addNames = pltcfg.weightSystNames)
    
    print '''
    # ========================================================
    # Check if additional (input) variables should be plotted and if necessary add them here to the discriminatorPlots
    # ========================================================
    '''
    if analysis.additionalPlotVariables:
        #  Construct list with additional plot variables, will need name of discrs and plotPreselections for this
        print( "add additional plot variables")
        configData.getAdditionalDiscriminatorPlots(analysis)

    

    
    # plot everything, except during drawParallel step
    # Create file for data cards
    if analysis.doDrawParallel == False or analysis.plotNumber == None :
        #if not os.path.exists(analysis.rootFilePath):
            print '''
            # ========================================================
            # Doing plotParallel step since root file was not found.
             ========================================================
            '''
            
            with runTimer.Timer("plotParallel"):
                # initialize plotParallel class 
                pP = plotParallel.plotParallel(workdir = analysis.workdir,
                                        pltcfg = pltcfg,
                                        configData = configData,
                                        samplesData = samplesData)

                # set some changed values
                pP.setJson("/nfs/dust/cms/user/kelmorab/treeJsons/treejson_Spring17_latestAndGreatest.json")
                pP.setDataBases( [["memDB","/nfs/dust/cms/user/kelmorab/DataBases/MemDataBase_Spring17_V1",False]] )
                pP.setAddInterfaces( ["../util/dNNInterfaces/dNNInterface_V6.py"] )
                
                # set options
                pP.setOptions( {"cirun": True,  "haddParallel": True, "useOldRoot": True} )
    
                # run plotParallel
                pP.run()

            # if pp.haddFiles is a list we are probably in the first iteration

            # cross check if plotParallel has terminated successfully
            # program exits if not
            pP.checkTermination()

            if analysis.getActivatedOptimizedRebinning():
                print '''
                # ========================================================
                # Doing OptimizedRebinning
                # ========================================================
                '''
                if analysis.getSignalProcess() == 'ttbb':
                    # samples[0:2]: tt+bb, tt+b, tt+2b as signal for S over b normalization
                    # TODO check the optimizedBinning function and adjust arguments to new structure
                    # TODO rework samples splitting to be automated in samplesDataClass?
                    with runTimer.Timer("optimizeBinning"):
                        plotutils.optimizeBinning(pP.getRootPath(),
                                            signalsamples = [samplesData.samples[0:3]], 
                                            backgroundsamples = samplesData.samples[3:],
                                            additionalSamples = samplesData.controlSamples, 
                                            plots = configData.getDiscriminatorPlots(), 
                                            systnames = samplesData.allNames, 
                                            minBkgPerBin = 2.0, 
                                            optMode = analysis.getOptimzedRebinning(),
                                            considerStatUnc = False, 
                                            maxBins = 20, 
                                            minBins = 2,
                                            verbosity = 2)

                elif analysis.getSignalProcess() == 'ttH':
                    # samples: ttH as signal. ttH_bb, ttH_XX as additional samples together with data. 
                    # Rest: background samples
                    with runTimer.Timer("optimizeBinning"):
                        plotutils.optimizeBinning(pP.getRootPath(),
                                            signalsamples = [samplesData.samples[0]], 
                                            backgroundsamples = samplesData.samples[9:],
                                            additionalSamples= samplesData.samples[1:9] + samplesData.controlSamples, 
                                            plots = configData.getDiscriminatorPlots(), 
                                            systnames = samplesData.allNames, 
                                            minBkgPerBin = 2.0, 
                                            optMode = analysis.getOptimzedRebinning(),
                                            considerStatUnc = False, 
                                            maxBins = 20, 
                                            minBins = 2,
                                            verbosity = 2)
                else:
                    print 'Warning: Could not find signal process.'



            # hadd histo files before renaming. The histograms are actually already renamed. But the checkbins thingy will not have been done yet.
            print '''
            # ========================================================
            # hadding from wildcard
            # ========================================================
            '''
            # TODO look at this function and adjust arguments
            with runTimer.Timer("haddFilesFromWildCard"):
                plotParallel.haddFilesFromWildCard(outname = pP.getRootPath(),
                                                    inwildcard = pP.getHaddOutPath(),
                                                    totalNumberOfHistosNeedsToRemainTheSame = True)

            
            # Deactivate check bins functionality in renameHistos 
            #   if additional plot variables are added via analysis class
            if pP.initlimitPath_exists():
                print( "renamed file already exists - skipping renaming histos" )
            else:
                print '''
                # ========================================================
                # renaming Histograms
                # ========================================================
                '''
                # this function evaluates to True if haddFiles were created
                # otherwise it is false
                if pP.checkHaddFiles():
                    # now we know, that haddFiles have been generated during the plotParallel run
                    # we can now call the renameHistos step
                    with runTimer.Timer("renameHistos-withHaddFiles"):
                        limittools.renameHistos(
                                infname = pP.getHaddFiles(),
                                outfname = pP.getLimitPath(),
                                sysnames = samplesData.allNames,
                                checkBins = True,
                                prune = False,
                                Epsilon = 0.0)
                else:
                    # now we konw, that no haddFiles have been generated during plotParallel run
                    # we can now call the renamedHistos step
                    with runTimer.Timer("renameHistos-noHaddFiles"):
                        limittools.renameHistos(
                                infname = pP.getRootPath(),
                                outfname = pP.getLimitPath(),
                                sysnames = samplesData.allNames,
                                checkBins = True,
                                prune = False,
                                Epsilon = 0.0)
            
            print '''
            # ========================================================
            # adding real data with limittools
            # ========================================================
            '''
            with runTimer.Timer("addRealData"):
                limittools.addRealData(
                            infname = pP.getLimitPath(),
                            samplesData = [s.nick for s in samplesData.controlSamples],
                            categories = configData.getBinlabels(),
                            disc = discrname)

                #limittools.addPseudoData(
                #            infname = pP.getLimitPath(),
                #            samplesWOttH = [s.nick for s in samplesData.samples[9:]],
                #            categories = configData.getBinlabels(),
                #            sysnames = samplesData.allNames,
                #            discr = discrname)

            # the path that is referenced in following parts as 
            # outputpath is the result of pP.getLimitPath()

    # ---- plotparallel step is done here ----
    else:
        print "not doing plotParallel step"
        # initialize empty plotParalllel instance to reference pP.getLimitPath()
        pP = plotParallel.plotParallel.empty(analysis.workdir, analysis.rootFilePath)

    print("###### DONE WITH PLOTPARALLEL STEP ######")
    pP.checkTermination()       
    print("at the moment the outputpath is "+str(pP.getLimitPath()))
    print("#########################################")


    # make datacards
    if (analysis.doDrawParallel==False or analysis.plotNumber == None) and analysis.makeDataCards == True :
        #TODO
        # 1. Implement small Epsilon case
        # 2. Implement consisted Bin-by-Bin uncertainties
        #limittools.addRealData(outputpath,[s.nick for s in samples_data],binlabels,discrname)
        print '''
        # ========================================================
        # Making Data cards.
        # ========================================================
        '''
        # TODO look at function and update variables
        with runTimer.Timer("makeDatacardsParallel"):
            limittools.makeDatacardsParallel(
                            filename = pP.getLimitPath(),
                            # TODO make sure this references the right place
                            outname = name+'/datacard',
                            categories = configData.getBinlabels(),
                            doHdecay = True,
                            discrname = discrname,
                            datacardmaker = "mk_datacard_JESTest13TeVPara")


    # =============================================================================================
    # Invoke drawParallel step
    # =============================================================================================
    if analysis.doDrawParallel==True and analysis.plotNumber == None :
        # Hand over opts to keep commandline options
        print '''
        # ========================================================
        # Starting DrawParallel
        # ========================================================
        '''
        # TODO look at function and update variables
        with runTimer.Timer("DrawParallel"):
            # TODO this is the function that calls this script again with various shell scripts
            plotParallel.DrawParallel(
                                ListOfPlots = configData.getDiscriminatorPlots(),
                                workdir = analysis.workdir,
                                PathToSelf = os.path.realpath(inspect.getsourcefile(lambda:0)),
                                opts = analysis.opts)

    # belongs to DrawParallel
    if analysis.doDrawParallel==True and analysis.plotNumber != None :
        # this is called by the secondary scripts
        print("we have a plotNumber --- changing discriminatorPlots")
        configData.adjustDiscriminatorPlots(plotNumber = analysis.plotNumber)

    # =============================================================================================


    # Lists needed later, produce them only if needed, so check if subsequent step comes
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and (analysis.makeSimplePlots==True or analysis.makeMCControlPlots==True or analysis.makeEventYields==True):
        # this is called by the secondary scripts
        print '''
        # ========================================================
        # Creating lists for later use
        # ========================================================
        '''
        # TODO this sucks - rework in any case, put the information into a DataFrame for example
        with runTimer.Timer("adjustingLists-createHistoLists_fromSuperHistoFile"):
            listOfHistoLists = plotutils.createHistoLists_fromSuperHistoFile(
                                    path = pP.getLimitPath(),
                                    samples = samplesData.samples,
                                    plots = configData.getDiscriminatorPlots(),
                                    rebin = 1)
        with runTimer.Timer("adjustingLists-transposeLOL"):
            lolT=plotutils.transposeLOL(listOfHistoLists)
        with runTimer.Timer("adjustingLists-createHistoLists_fromSuperHistoFile"):
            listOfHistoListsData = plotutils.createHistoLists_fromSuperHistoFile(
                                    path = pP.getLimitPath(),
                                    samples = samplesData.controlSamples,
                                    plots = configData.getDiscriminatorPlots(),
                                    rebin = 1)


    # plot simple MC plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeSimplePlots==True :
        # this is called by the secondary scripts
        print '''
        # ========================================================
        # Making simple MC plots
        # ========================================================
        print '''
        # TODO this sucks - rework in any case
        with runTimer.Timer("simpleMCplots-writeLOLAndOneOnTop"):
            plotutils.writeLOLAndOneOnTop(
                            listOfHistoLists = plotutils.transposeLOL(lolT[9:]),
                            samples = samplesData.samples[9:],
                            listOfhistosOnTop = lolT[0],
                            sampleOnTop = samplesData.samples[0],
                            factor = -1,
                            name = name+'/'+name+'_controlplots')
        with runTimer.Timer("simpleMCplots-writeListOfHistoListsAn"):
            plotutils.writeListOfHistoListsAN(
                            listOfHistoLists = plotutils.transposeLOL([lolT[0]]+lolT[9:]),
                            samples = [samplesData.samples[0]]+samplesData.samples[9:],
                            label = "",
                            name = name+'/'+name+'_shapes',
                            normalize = True, 
                            stack = False, 
                            logscale = False, 
                            options = 'histo', 
                            statTest = False, 
                            sepaTest = True, 
                            ratio = False)


    # Make MC Control plots
    if (analysis.doDrawParallel==False or analysis.plotNumber != None) and analysis.makeMCControlPlots==True :
        # this is called by the secondary scripts
        print '''
        # ========================================================
        # Making MC Control plots
        # ========================================================
        '''
        # TODO this sucks - rework in any case
        with runTimer.Timer("MCControlPlots-createLLL_fromSuperHistoFileSyst"):
            lll = plotutils.createLLL_fromSuperHistoFileSyst(
                                    path = pP.getLimitPath(),
                                    samples = samplesData.samples[9:],
                                    plots = configData.getDiscriminatorPlots(),
                                    systnames = pltcfg.errorSystNamesNoQCD)

            labels = [plot.label for plot in configData.discriminatorPlots]
        with runTimer.Timer("MCControlPlots-plotDataMCanWsyst"):
            plotutils.plotDataMCanWsyst(
                                    listOfHistoListsData = listOfHistoListsData,
                                    listOfHistoLists = plotutils.transposeLOL(lolT[9:]),
                                    samples = samplesData.samples[9:],
                                    listOfHistosOnTop = lolT[0],
                                    sampleOnTop = samples[0],
                                    factor = -2,
                                    name = name,
                                    listOflll = [[lll,3354,ROOT.kBlack,True]],
                                    logscale = False,
                                    label = labels,
                                    ratio = True,
                                    blinded = analysis.plotBlinded)



if __name__ == "__main__":

    with runTimer.Timer("main"):
        main(pyrootdir, sys.argv[1:])

