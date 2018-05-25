import ROOT
from array import array
from subprocess import call
import time as timer
import sys
import os
dirpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dirpath+"/../../")
import nafSubmit
datacard= sys.argv[1]
currentPath = sys.path[0]


# configurables
minmu=0.0
maxmu=7.0
stepsize=1.0
nToysBatch=500
nIterations=1
repetitionsPerPoint=1
nCalcsPerJob=1

#-----------------------
deltamu=maxmu-minmu
currentmu=minmu
seed=200

listOfJobs=[]
listofCalcs=[]
while currentmu<=maxmu:
  for rep in range(repetitionsPerPoint):
    listofCalcs.append([currentmu,seed])
    seed+=1
  currentmu+=stepsize

ijob=0
for icalc, calc in enumerate(listofCalcs):
  if icalc==0 or icalc%nCalcsPerJob==0:
    ijob+=1
    jobname="ToyMC"+str(ijob)+".sh"
    jobfile=open(jobname ,"w")
    jobfile.write("#!/bin/bash\n")
    jobfile.write(". /etc/profile.d/modules.sh\n")
    jobfile.write("module use -a /afs/desy.de/group/cms/modulefiles/\n")
    jobfile.write("module load cmssw/slc6_amd64_gcc481\n")
    jobfile.write("export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch/\n")
    jobfile.write("export SCRAM_ARCH=slc6_amd64_gcc481\n")
    jobfile.write("source $VO_CMS_SW_DIR/cmsset_default.sh\n")
    jobfile.write("cd /nfs/dust/cms/user/kelmorab/CMSSW_7_1_5/src\n")
    jobfile.write("eval `scram runtime -sh`\n")
    jobfile.write("cd "+currentPath+"/\n")
    
    #jobfile.write("/nfs/dust/cms/user/kelmorab/CMSSW_7_1_5/bin/slc6_amd64_gcc481/combine "+datacard+" -M HybridNew  --frequentist --testStat LHC --clsAcc 0 -T "+str(nToysBatch)+" -i "+str(nIterations)+" -s "+str(seed)+" --singlePoint "+str(currentmu)+" --saveToys --saveHybridResult\n")
  jobfile.write("/nfs/dust/cms/user/kelmorab/CMSSW_7_1_5/bin/slc6_amd64_gcc481/combine "+datacard+" -v 99 -M HybridNew  --generateExternalMeasurements 1 --generateNuisances 0 --testStat LHC --clsAcc 0 -T "+str(nToysBatch)+" -i "+str(nIterations)+" -s "+str(calc[1])+" --singlePoint "+str(calc[0])+" --fullBToys  --saveToys --saveHybridResult\n")
  if icalc%nCalcsPerJob==nCalcsPerJob-1 or icalc==len(listofCalcs)-1:
    print "wrote job ", str(ijob), "with point ", str(calc[0])
    jobfile.close()
    listOfJobs.append(jobname)


arrayPath = nafSubmit.writeArrayCode( [currentPath + "/" + job for job in listOfJobs], "runAll")
submitPath = nafSubmit.writeSubmitCode( arrayPath, currentPath+"/logs/", isArray = True, nScripts = len(listOfJobs) )

# immediately submits generated script if you want
# jobID = nafSubmit.condorSubmit(submitPath)

# otherwise, there should be two files present now: 
#       runAll.sh which is an array-script file for all jobs in listOfJobs
#       runAll.sub which is the submit scrpit to submit runAll.sh to the batch system
#       use it like 'condor_submit runAll.sub' (nafSubmit.condorSubmit(submitPath) does the same)
# you can also use the generated runAll.sh file with the 'submit.py' script located in tools/

'''
runfile=open("runAll.sh","w")
runfile.write("#!/bin/bash\n")
for job in listOfJobs:
  submitPath = nafSubmit.writeArrayCode( currentPath + "/" + job, currentPath + "/logs")
  runfile.write("condor_submit -terse " + submitPath + "\n")
runfile.close()
'''

# after all jobs are finished do
# hadd the single output files to mygrid.root
# combine datacard_Combined_ThesisSTD.txt -M HybridNew --testStat LHC  --generateExternalMeasurements 1 --generateNuisances 0 --grid=mygrid.root  --expectedFromGrid 0.5
# for median prefit expected

