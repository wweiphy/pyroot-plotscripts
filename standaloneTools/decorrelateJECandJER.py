import sys
import ROOT
ROOT.gDirectory.cd('PyROOT:/')
ROOT.gROOT.SetBatch(True)

#DISCLAIMER due to the merge of script1D and script2D this file need the flag '1D', '2D' or 'Split' as first argument to decide whether it is executed as 1D or 2D or as the decorrelateSplitJECandJER.py
dim = sys.argv[1]
if not dim=="1D" or dim=="2D" or dim=="Split":
    sys.exit("choose '1D', '2D' or 'Split' as first argument - everything else is unchanged")

if dim == "1D" or dim == "Split":
    cats=["ljets_j4_t2","ljets_j5_t2","ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t2","ljets_jge6_t3","ljets_jge6_tge4",]
elif dim == "2D":
    singlecats=["ljets_j4_t3","ljets_j4_t4","ljets_j5_t3","ljets_j5_tge4","ljets_jge6_t3","ljets_jge6_tge4",]
    cats=["ljets_j4_t2","ljets_j5_t2","ljets_jge6_t2"]
    for c in singlecats:
        cats.append(c+"_high")
        cats.append(c+"_low")

procs=['ttH','ttH_hbb', 'ttH_hcc', 'ttH_hww', 'ttH_hzz', 'ttH_htt', 'ttH_hgg', 'ttH_hgluglu', 'ttH_hzg', 'ttbarOther', 'ttbarPlusB', 'ttbarPlus2B', 'ttbarPlusBBbar', 'ttbarPlusCCbar', 'singlet', 'wjets', 'zjets', 'ttbarW', 'ttbarZ', 'diboson']

#print procs

groups=[["LF",['ttH_hww', 'ttH_hzz', 'ttH_htt', 'ttH_hgg', 'ttH_hgluglu', 'ttH_hzg','ttbarOther','singlet', 'wjets', 'zjets', 'ttbarW', 'ttbarZ', 'diboson']],
	 ["CF",['ttH_hcc','ttbarPlusCCbar']],
	 ["HF",['ttH','ttH_hbb','ttbarPlusB', 'ttbarPlus2B', 'ttbarPlusBBbar']]
	 ]

if dim == "1D" or dim == "2D":
    systs=["CMS_scale_jUp","CMS_scale_jDown","CMS_res_jUp","CMS_res_jDown"]
    datacardsysts=["CMS_scale_j","CMS_res_j"]
elif dim == "Split":
    systs=["CMS_shape_scale_jUp","CMS_shape_scale_jDown","CMS_shape_res_jUp","CMS_shape_res_jDown","CMS_rate_scale_jUp","CMS_rate_scale_jDown","CMS_rate_res_jUp","CMS_rate_res_jDown"]
    datacardsysts=["CMS_shape_scale_j","CMS_shape_res_j","CMS_rate_scale_j","CMS_rate_res_j"]

disc="_finaldiscr_"

infiles=sys.argv[2:]

for inf in infiles:
  if ".root" in inf:
    f=ROOT.TFile(inf,"Update")
    for g in groups:
      typ=g[0]
      for p in g[1]:
	for c in cats:
	  for s in systs:
	    h=f.Get(p+disc+c+"_"+s)
	    newh=h.Clone()
	    newh.SetTitle(p+disc+c+"_"+s.replace("CMS_","CMS_"+typ+"_"))
	    newh.SetName(p+disc+c+"_"+s.replace("CMS_","CMS_"+typ+"_"))
	    newh.Write()
	    print "wrote ", newh
    f.Close()

  else:
    infl=open(inf,"r")
    outf=open("JECdeco_"+inf,"w")
    inlist=list(infl)
    infprocs=[]
    for line in inlist:
      if "process" in line and infprocs==[]:
	print "found process line"
	sl=line.replace("\n","").replace("\t","").replace("  "," ").split(" ")
	print sl
	for pl in sl[1:]:
	  infprocs.append(pl)
	print infprocs
      # now replace jes
      foundOne=False
      for s in datacardsysts:
	  if s in line:
	    foundOne=True
      if foundOne:
	for s in datacardsysts:
	  if s in line:
	    sl=line.replace("\n","").replace("\t","").replace("  "," ").split(" ")
	    print sl
	    for g in groups:
	      newline=sl[0].replace("CMS_","CMS_"+g[0]+"_")+" "+sl[1]
	      for im,m in enumerate(sl[2:]):
		if infprocs[im] in g[1]:
          if dim == "1D" or dim == "Split":
		    newline+=" "+"1"
          elif dim == "2D":
            if m=="-":
              newline+=" "+"-"
            else:
              newline+=" "+"1"
		else:
		  newline+=" "+"-"
	      newline+="\n"
	      print newline
	      outf.write(newline)
	      
      else:
	outf.write(line)