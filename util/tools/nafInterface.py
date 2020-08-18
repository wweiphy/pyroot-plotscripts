import sys
import os
import nafSubmit

fastLane = True
#############################
# parallel plotting
#############################
def plotInterface(jobData, skipPlotParallel = False, maxTries = 10, nTries = 0):
    print("NUMBER OF JOBS TO BE SUBMITTED: {}".format(len(jobData["scripts"])))
    if skipPlotParallel:
        print("skip plot parallel was activated")
        jobData = plotTerminationCheck( jobData )
        print("NUMBER OF JOBS TO BE RESUBMITTED: {}".format(len(jobData["scripts"])))

        if len(jobData["scripts"]) > 0 or len(jobData["outputs"]) > 0:
            print("not all plotParallel scripts did terminate successfully - resubmitting")
        else:
            print("all plotParallel scripts have terminated successfully - skipping plotParallel")
            return

    submitOptions = {"+RequestRuntime": 10800, "RequestMemory": "1000M"}
    if nTries == 0:
        print("submitting plotParallel scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobData["scripts"], "makeTemplates", submitOptions = submitOptions)
    elif nTries < maxTries:
        submitOptions["+RequestRuntime"]=21600
        submitOptions["RequestMemory"]="1000M"
        print("resubmitting plotParallel scripts as single jobs")
        jobIDs = nafSubmit.submitArrayToNAF(jobData["scripts"], "makeTemplates_resubmit", submitOptions = submitOptions)
    else:
        print("plotParallel did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)

    # monitor running
    nafSubmit.monitorJobStatus(jobIDs) 
    # check fo termination of jobs
    undoneJobData = plotTerminationCheck(jobData)

    if len(undoneJobData["scripts"]) > 0 or len(undoneJobData["outputs"]) > 0:
        return plotInterface( undoneJobData, maxTries = maxTries, nTries = nTries+1 )

    print("plotParallel submit interface has terminated successfully")

def plotTerminationCheck(jobData):
    # counters
    undoneJobData = {}
    undoneJobData["scripts"] = []
    undoneJobData["outputs"] = []
    undoneJobData["entries"] = []
    noCutflow = 0
    wrongEntry = 0

    for script, output, entries in zip(jobData["scripts"], jobData["outputs"], jobData["entries"]):
        if os.path.exists(output+".cutflow.txt"):
            cfFile = open(output+".cutflow.txt")
            processedEntries = -1
            for line in cfFile:
                splitLine = line.split(" : ")
                if len(splitLine) > 2 and "all" in splitLine[1]:
                    processedEntries = int(splitLine[2])
                    break
            if entries == processedEntries:
                continue
            else:
                wrongEntry += 1            
        else:
            noCutflow += 1
        
        undoneJobData["scripts"].append( script )
        undoneJobData["outputs"].append( output ) 
        undoneJobData["entries"].append( entries ) 

    undoneJobData["maps"] = jobData["maps"]
    print("-"*50)
    print("done checking job outputs after plotpara - results:")
    print("jobs without cutflow file:     " +str(noCutflow))
    print("jobs with wrong entry in file: " +str(wrongEntry))
    print("-"*50)
    return undoneJobData




def cleanupInterface(jobsToSubmit, rootFiles, skipCleanup = False, maxTries = 10, nTries = 0):
    if skipCleanup:
        undoneJobs, undoneRootFiles = cleanupTerminationCheck(jobsToSubmit, rootFiles)       
        if len(undoneJobs) > 0: return cleanupInterface( undoneJobs, undoneRootFiles )
        else:
            print("cleanup histos has terminated successfully")
            return

    submitOptions = {"+RequestRuntime": 1800, "RequestMemory": "500M"}

    if nTries == 0:
        print("submitting cleanup jobs as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "cleanupHistos", submitOptions = submitOptions)
    elif nTries < maxTries:
        submitOptions["+RequestRuntime"]=3600
        submitOptions["RequestMemory"]="1000M"
        print("resubmitting cleanup jobs")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "cleanup_resubmit", submitOptions = submitOptions)
    else:
        print("cleaning up histograms did not work after {} tries - ABORTING".format(maxTries))
        sys.exit(1)

    # monitor running
    nafSubmit.monitorJobStatus(jobIDs)
    # check for termination of jobs
    undoneJobs, undoneRootFiles = cleanupTerminationCheck(jobsToSubmit, rootFiles)

    if len(undoneJobs) > 0:
        return cleanupInterface( undoneJobs, undoneRootFiles, maxTries = maxTries, nTries = nTries+1 )
    
    print("cleanup histos interface has terminated successfully")

def cleanupTerminationCheck(jobs, outputFiles):
    undoneJobs = []
    undoneRootFiles = []
    
    for job, out in zip(jobs, outputFiles):
        if not os.path.exists(out.replace('.root','_original_cleanedUp.txt')):
            undoneJobs.append(job)
            undoneRootFiles.append(out)

    print("-"*50)
    print("done checking outputs of cleanup scripts - results:")
    print("jobs without cleanup file: {}".format(len(undoneJobs)))
    print("-"*50)
    return undoneJobs, undoneRootFiles



#############################
# parallel hadding
#############################
def haddInterface(jobsToSubmit, outfilesFromSubmit, maxTries = 10, nTries = 0):
    submitOptions = {"+RequestRuntime": 1800, "RequestMemory": "500M"}
    if nTries == 0:
        print("submitting haddParallel scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "hadding", submitOptions = submitOptions)
    elif nTries < maxTries:
        submitOptions["+RequestRuntime"]=3600
        submitOptions["RequestMemory"]="1000M"
        print("resubmitting haddParallel scripts as single jobs")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "hadding_resubmit", submitOptions = submitOptions)
    else:
        print("hadding did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)

    # monitor running
    nafSubmit.monitorJobStatus(jobIDs)
    # check for termination of jobs
    undoneJobs, undoneOutFiles = haddTerminationCheck(jobsToSubmit, outfilesFromSubmit)

    if len(undoneJobs) > 0 or len(undoneOutFiles) > 0:
        return haddInterface( undoneJobs, undoneOutFiles, maxTries, nTries+1 )
    
    print("haddParallel submit interface has terminated successfully")

def haddTerminationCheck(outputScripts, outputFiles):
    # counters
    undoneJobs = []
    undoneOutFiles = []
    noFile = 0
    wrongEntry = 0
    wrongLen = 0

    # looping over jobs to find missing pieces
    for job, jobscript in zip(outputFiles, outputScripts):
        log = job.replace(".root", ".log")
        if os.path.exists(job) and os.path.exists(log):
            with open(log, "r") as logf:
                jobfile = list(logf)
            if len(jobfile) == 1:
                if jobfile[0] == "OK":
                    continue
                else:
                    wrongEntry += 1
            else:
                wrongLen += 1
        else:
            noFile += 1

        undoneJobs.append(jobscript)
        undoneOutFiles.append(job)

    print("-"*50)
    print("done checking job outputs after haddpara - results:")
    print("jobs without log file:       " + str(noFile))
    print("jobs with wrong log file:    " +str(wrongLen))
    print("jobs with ERROR in log file: " + str(wrongEntry))
    print("-"*50)
    return undoneJobs, undoneOutFiles


    



#############################
# checking histos
#############################
def checkHistoInterface(jobsToSubmit, outfilesFromSubmit, maxTries = 10, nTries = 0):
    # shellList = renamescriptlist = listOfJobsToSubmit
    # outFileList = outnamelist = listOfJobOutFilesToGetFromSubmit
    if len(jobsToSubmit) != len(outfilesFromSubmit):
        print("number of jobs should be equal to number of output files - ABORTING")
        sys.exit(1)
    
    submitOptions = {"+RequestRuntime": 1800, "RequestMemory": "500M"}

    if nTries == 0:
        print("submitting rename scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, arrayName = "checkingHistos", submitOptions = submitOptions)
    elif nTries < maxTries:
        submitOptions["+RequestRuntime"]=3600
        submitOptions["RequestMemory"]="1000M"
        print("resubmitting rename scripts as single jobs")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, arrayName = "checkingHistos_resubmit", submitOptions = submitOptions)
    else:
        print("renaming did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)

    # monitor running of jobs
    nafSubmit.monitorJobStatus(jobIDs)
    # checking for undone jobs
    undoneJobs, undoneFiles = checkHistoTerminationCheck(jobsToSubmit, outfilesFromSubmit)

    if len(undoneJobs) > 0 or len(undoneFiles) > 0:
        return checkHistoInterface(undoneJobs, undoneFiles, maxTries, nTries+1)

    print("renamingHistos submit interface has terminated successfully")

def checkHistoTerminationCheck(shellScripts, outputFiles):
    # count undone jobs
    undoneJobs = []
    undoneOutFiles = []
    noFile = 0

    for job, outFile in zip(shellScripts, outputFiles):
        if not os.path.exists(outFile):
            noFile += 1
            undoneJobs.append( job )
            undoneOutFiles.append( outFile )

    print("-"*50)
    print("done checking job outputs after renaming histos - results:")
    print("jobs without output file: " + str(noFile))
    print("-"*50)
    return undoneJobs, undoneOutFiles





#############################
# making datacards
#############################
def datacardInterface(jobsToSubmit, datacardFiles, maxTries = 10, nTries = 0):
    if nTries == 0:
        print("submitting datacardmaking scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, arrayName = "makeDatacards")
    elif nTries < maxTries:
        print("resubmitting datacardmaking scripts as single jobs")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, arrayName = "makeDatacards_resubmit")
    else:
        print("making datacards did not work after "+str(maxTries)+" tries -ABORTING")
        sys.exit(1)

    # monitoring running of jobs
    if fastLane:
        print("monitoring of datacards is disabled to speed up the script")
        return

    nafSubmit.monitorJobStatus(jobIDs)
    # checking output
    undoneJobs, undoneCards = datacardTerminationCheck(jobsToSubmit, datacardFiles)

    if len(undoneCards) > 0 or len(undoneJobs) > 0:
        return datacardInterface(undoneJobs, undoneCards, maxTries, nTries+1)
    
    print("makingDatacards submit interface has terminated successfully")

def datacardTerminationCheck(shellScripts, datacardFiles):
    undoneJobs = []
    undoneCards = []
    noCard = 0

    for job, card in zip(shellScripts, datacardFiles):
        if not os.path.exists(card):
            noCard += 1
            undoneJobs.append( job )
            undoneCards.append( card )

    print("-"*50)
    print("done checking job outputs after making datacards - results:")
    print("jobs without datacard file: " + str(noCard))
    print("-"*50)
    return undoneJobs, undoneCards





#############################
# make Plots
#############################
def drawInterface(jobsToSubmit, outputPlots, nTries = 0):
    submitOptions = {"+RequestRuntime": 600, "RequestMemory": "500M"}
    if nTries == 0:
        print("submitting makePlots scripts as array job")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "makePlots", submitOptions)
    elif nTries < maxTries:
        print("resubmitting makePlots scripts as single jobs")
        jobIDs = nafSubmit.submitArrayToNAF(jobsToSubmit, "makePlots_resubmit", submitOptions)
    else:
        print("make Plots did not work after "+str(maxTries)+" tries - ABORTING")
        sys.exit(1)
    
    # monitoring running jobs
    if fastLane:
        print("monitoring of plotting jobs disabled to speed up the script")
        return

    nafSubmit.monitorJobStatus(jobIDs)
    # checking output
    undoneScripts, undonePlots = drawTerminationCheck(jobsToSubmit, outputPlots)

    if len(undoneScripts) > 0 or len(undonePlots) > 0:
        return drawInterface(undoneScripts, undonePlots, maxTries, nTries+1)

    print("makePlots submit interface has terminated successfully")

def drawTerminationCheck(jobsToSubmit, outputPlots):
    print("no check for the termination of draw Parallel has been implemented yet...")
    undoneJobs = []
    undonePlots = []
    return undoneJobs, undonePlots




