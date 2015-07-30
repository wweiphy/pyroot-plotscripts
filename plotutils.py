import ROOT
import math
from itertools import product
from collections import namedtuple

Sample = namedtuple("Sample", "name color path selection")
Plot = namedtuple("Plot", "histo variable selection")

# sets up the style of a histo and its axes. options for data and stackplots will follow.
def setupHisto(histo,color,yTitle=None,filled=False):
    if isinstance(histo,ROOT.TH1):
        histo.SetStats(False)
    if histo.GetTitle()!='':
        histo.GetXaxis().SetTitle(histo.GetTitle())
        histo.SetTitle('')
    if yTitle!=None:
        histo.GetYaxis().SetTitle(yTitle)
    histo.GetYaxis().SetTitleOffset(1.3)
    histo.GetYaxis().SetTitleSize(0.05)
    histo.GetXaxis().SetTitleSize(0.05)
    histo.GetYaxis().SetLabelSize(0.05)
    histo.GetXaxis().SetLabelSize(0.05)
    if filled:
        histo.SetLineColor( ROOT.kBlack )
        histo.SetFillColor( color )
        histo.SetLineWidth(2)
    else:
        histo.SetLineColor(color)
        histo.SetLineWidth(3)

# creates canvas. option to add ratiopad will follow
def getCanvas(name):
    c=ROOT.TCanvas(name,name,1000,800)
    c.SetRightMargin(0.05)
    c.SetTopMargin(0.05)
    c.SetLeftMargin(0.15)
    c.SetBottomMargin(0.12)
    return c

# creates legend
def getLegend(): 
    legend=ROOT.TLegend()
    legend.SetX1NDC(0.65)
    legend.SetX2NDC(0.93)
    legend.SetY1NDC(0.92)
    legend.SetY2NDC(0.93)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.05);
    legend.SetFillStyle(0);
    return legend

def getStatTests(h1,h2):
    ksprob = h1.KolmogorovTest(h2)
    chi2prob = h1.Chi2Test(h2,"WW")
    print ksprob,chi2prob
    tests = ROOT.TLatex(0.2, 0.85, '#splitline{p(KS): '+str(round(ksprob,3))+'}{p(chi2): '+str(round(chi2prob,3))+'}'  );
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests

def getSepaTests(h1,h2):
    pair=getSuperHistoPair([h1],[h2],'tmp')
    roc=getROC(*pair)
    rocint=roc.Integral()+0.5
    print rocint
    tests = ROOT.TLatex(0.2, 0.9, 'ROC integral: '+str(round(rocint,3)));
    tests.SetTextFont(42);
    tests.SetTextSize(0.05);
    tests.SetNDC()
    return tests


# draws a list of histos on a canvas and returns canvas. options for stackplots, ratioplot, etc will be implemented soon
def drawHistosOnCanvas(listOfHistos_,normalize=True,stack=False,logscale=False,options_='histo'):
    listOfHistos=[h.Clone(h.GetName()+'_drawclone') for h in listOfHistos_]
    canvas=getCanvas(listOfHistos[0].GetName())        
    #prepare drawing

    # mover over/underflow
    for h in listOfHistos:
        h.SetBinContent(1,h.GetBinContent(0)+h.GetBinContent(1));
        h.SetBinContent(h.GetNbinsX(),h.GetBinContent(h.GetNbinsX()+1)+h.GetBinContent(h.GetNbinsX()));
        h.SetBinError(1,ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(0),2)+ROOT.TMath.Power(h.GetBinError(1),2)));
        h.SetBinError(h.GetNbinsX(),ROOT.TMath.Sqrt(ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()+1),2)+ROOT.TMath.Power(h.GetBinError(h.GetNbinsX()),2)));

    if normalize and not stack:
        for h in listOfHistos:
            if h.Integral()>0.:
                h.Scale(1./h.Integral())

    if stack:
        for i in range(len(listOfHistos)-1,0,-1):
            print 'add',i,'to',i-1
            listOfHistos[i-1].Add(listOfHistos[i])
        if normalize:
            integral0=listOfHistos[0].Integral()
            for h in listOfHistos:
                h.Scale(1./integral0)

            

    yMax=1e-9
    yMinMax=1000.
    for h in listOfHistos:
        yMax=max(h.GetBinContent(h.GetMaximumBin()),yMax)
        if h.GetBinContent(h.GetMaximumBin())>0:
            yMinMax=min(h.GetBinContent(h.GetMaximumBin()),yMinMax)
    #draw first
    h=listOfHistos[0]
    if logscale:
        h.GetYaxis().SetRangeUser(yMinMax/10000,yMax*10)
        canvas.SetLogy()
    else:
        h.GetYaxis().SetRangeUser(0,yMax*1.3)
    option='histo'
    option+=options_
    h.DrawCopy(option)
    #draw remaining
    for h in listOfHistos[1:]:
        h.DrawCopy(option+'same')
    h.DrawCopy('axissame')
    return canvas

# writes canvases to pdf 
def printCanvases(canvases,name):
    canvas=getCanvas('canvas')
    canvas.Print(name+'.pdf[')
    for c in canvases:
        canvas=c
        canvas.Print(name+'.pdf')
        
    canvas.Print(name+'.pdf]')

# writes canvases to root file 
def writeCanvases(canvases,name):
    outfile=ROOT.TFile(name+'.root','recreate')
    for c in canvases:
        c.Write()

# for a list of booked plots trees are opened and the histograms are filled using the TTree::Project function
def createHistoLists_fromTree(plots,samples,treename,weightexpression='Weight'):    
    listOfhistoLists=[]
    for plot in plots:
        histoList=[]
        for sample in samples:
            h=plot.histo.Clone()
            h.Sumw2()
            h.SetName(h.GetName()+'_'+sample.name)
#            setupHisto(h,sample.color)
            histoList.append(h)
        listOfhistoLists.append(histoList)

    for sample in samples:
        f=ROOT.TFile(sample.path, "readonly")
        tree = f.Get(treename)
        ROOT.gDirectory.cd('PyROOT:/')
        for plot in plots:
            ss='('+sample.selection+')'
            if sample.selection == '':
                ss='1'
            ps='('+plot.selection+')'
            if plot.selection == '':
                ps='1'
            project_name=plot.histo.GetName()+'_'+sample.name
            project_var=plot.variable
            project_sel='('+ps+'*'+ss+')*('+weightexpression+')'
            print "projecting",project_name,"--",project_var,"--",project_sel
            tree.Project(project_name,project_var,project_sel)

    return listOfhistoLists

def transposeLOL(lol):
    return [list(x) for x  in zip(*lol)]

def GetKeyNames( self, dir = "" ):
    self.cd(dir)
    return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
ROOT.TFile.GetKeyNames = GetKeyNames

def AddEntry2( self, histo, label, stacked=False):
    option='L'
    if stacked:
        option='F'
    self.SetY1NDC(self.GetY1NDC()-0.045)
    width=self.GetX2NDC()-self.GetX1NDC()
    ts=self.GetTextSize()
    newwidth=max(len(label)*0.015*0.05/ts+0.1,width)
    self.SetX1NDC(self.GetX2NDC()-newwidth)
    
    self.AddEntry(histo, label, option)
ROOT.TLegend.AddEntry2 = AddEntry2


def createHistoLists_fromHistoFile(samples,rebin=1):
    listOfhistoListsT=[]
    listLength=-1
    for sample in samples:
        f=ROOT.TFile(sample.path, "readonly")       
        keyList = f.GetKeyNames()
        ROOT.gDirectory.cd('PyROOT:/')
        if listLength>0:
            assert len(keyList) == listLength
        listLength=len(keyList)
        histoList = []
        for key in keyList:
            o=f.Get(key)
            if isinstance(o,ROOT.TH1): 
                o.Rebin(rebin)
                histoList.append(o.Clone())
                histoList[-1].SetName(o.GetName()+'_'+sample.name)
        listOfhistoListsT.append(histoList)
    listOfhistoLists=transposeLOL(listOfhistoListsT)
    return listOfhistoLists

# for a list of selections (and a list of their names) and a list of histos (and the variable expressions to fill them) the cartesian product is created and plots are booked
def plotsForSelections_cross_Histos(selections,selectionnames,histos,variables):
    selection_histos=product(zip(selections,selectionnames),zip(histos,variables))
    plots=[]
    for selectionpair,histopair in selection_histos:
        histopair=(histopair[0].Clone(),histopair[1])
        histopair[0].SetName(histopair[0].GetName()+'_'+selectionpair[1])
        histopair[0].SetTitle(histopair[0].GetTitle()+' '+selectionpair[1])
        plots.append(Plot(histopair[0],histopair[1],selectionpair[0]))
    return plots

# gets a list of histogramlist and creates a plot for every list
def writeListOfhistoLists(listOfhistoLists,samples,name,normalize=True,stack=False,logscale=False,options='histo',statTest=False, sepaTest=False):
    canvases=[]
    objects=[]   
    i=0
    for listOfHistos in listOfhistoLists:
        i+=1
        for histo,sample in zip(listOfHistos,samples):
            yTitle='Events'
            if normalize:
                yTitle='normalized'
            setupHisto(histo,sample.color,yTitle,stack)        
        c=drawHistosOnCanvas(listOfHistos,normalize,stack,logscale,options)
        c.SetName('c'+str(i))
        l=getLegend()
        for h,sample in zip(listOfHistos,samples):
            l.AddEntry2(h,sample.name,stack)
        canvases.append(c)
        l.Draw('same')
        objects.append(l)
        if statTest:
            tests=getStatTests(listOfHistos[0],listOfHistos[1])
            tests.Draw()
            objects.append(tests)
        if sepaTest:
            stests=getSepaTests(listOfHistos[0],listOfHistos[1])
            stests.Draw()
            objects.append(stests)


    printCanvases(canvases,name)
    writeCanvases(canvases,name)

def writeListOfROCs(graphs,names,colors,filename,logscale=False,rej=True):
    c=getCanvas('ROC')
    if logscale:
        c.SetLogy()
    l=getLegend()
    first=True
    for graph,name,color in zip(graphs,names,colors):
        l.AddEntry2(graph,name)
        if first:
            graph.Draw('ALP')
            first=False
        else:
            graph.Draw('LP')
        setupHisto(graph,color)
        graph.GetXaxis().SetTitle('Signal efficiency')
        if rej:
             graph.GetYaxis().SetTitle('Background rejection')
        else:
            graph.GetYaxis().SetTitle('Background efficiency')
        graph.SetMarkerStyle(20)
    l.Draw('same')
    printCanvases([c],filename)
    writeCanvases([c],filename)


#from lists of background and signalhistos one signal and one background histo are created
def getSuperHistoPair(histosS,histosB,name):
    superbins=[]
    for hs,hb in zip(histosS,histosB):
        nBins=hs.GetNbinsX()
        for i in range(1,nBins+1):
            s=hs.GetBinContent(i)
            b=hb.GetBinContent(i)
            if(b!=0):
                superbins.append( (s/b,s,b) )
            elif(s!=0):
                superbins.append( (float("inf"),s,b) )
    superbins_sorted=sorted(superbins,key=lambda b: b[0])
    superhistoS=ROOT.TH1F('superhistoS_'+name,'superhistoS_'+name,len(superbins_sorted),-0.5,len(superbins_sorted)-0.5)
    superhistoB=ROOT.TH1F('superhistoB_'+name,'superhistoB_'+name,len(superbins_sorted),-0.5,len(superbins_sorted)-0.5)
    for i in range(len(superbins)):
        superhistoS.SetBinContent(i+1,superbins_sorted[i][1])
        superhistoB.SetBinContent(i+1,superbins_sorted[i][2])
    return (superhistoS,superhistoB)

# calculate significance for cuts at bins in signal and background histogram
# histogram bins are expected to be sorted by increasing S/B (e.g. BDT output)
def getSignifCurve(histoS,histoB):
    nBins=histoS.GetNbinsX()
    nonZeroBins=[]
    for i in range(nBins):
        if histoS.GetBinContent(i)>0. or histoB.GetBinContent(i)>0.:
            nonZeroBins.append(i)     
    sigs=ROOT.TGraphAsymmErrors(len(nonZeroBins))
    point=0
    for i in nonZeroBins:
        intS=histoS.Integral(i,nBins)
        intB=histoB.Integral(i,nBins)#*6000000./61974084.
        sigs.SetPoint(point,intS/histoS.Integral(0,nBins),intS/math.sqrt(intS+intB))
        point+=1
    return sigs

# calculate ROC for signal(1) and bkg(2) histo
def getROC(histo1,histo2,rej=True):
    nBins=histo1.GetNbinsX()
    nBins2=histo2.GetNbinsX()
    integral1=histo1.Integral(0,nBins+1)
    integral2=histo2.Integral(0,nBins2+1)

    nonZeroBins=[]
    for i in range(nBins,-1,-1):
        if histo1.GetBinContent(i)>0. or histo2.GetBinContent(i)>0.:
            nonZeroBins.append(i)           

    roc = ROOT.TGraphAsymmErrors(len(nonZeroBins)+1)
    if rej:
        roc.SetPoint(0,0,1)
    else:
        roc.SetPoint(0,0,0)
    point=1
    for i in nonZeroBins:
        eff1=histo1.Integral(i,nBins+1)/integral1
        eff2=histo2.Integral(i,nBins+1)/integral2
        if rej:
            roc.SetPoint(point,eff1,1-eff2)
        else:
            roc.SetPoint(point,eff1,eff2)
        point+=1
    
    return roc

def getEff(histo1):
    nBins=histo1.GetNbinsX()
    integral1=histo1.Integral(0,nBins+1)

    nonZeroBins=[]
    for i in range(nBins+2):
        if histo1.GetBinContent(i)>0.:
            nonZeroBins.append(i)
    eff = ROOT.TGraphAsymmErrors(len(nonZeroBins)+1)
    point=0
    for i in nonZeroBins:
        eff1=histo1.Integral(i,nBins+1)/integral1
        print i, histo1.GetBinLowEdge(i), eff1
        eff.SetPoint(point,histo1.GetBinLowEdge(i),eff1)
        point+=1
    print "###"
    return eff



def writeSyst(file,value):
    for val in value[:-1]:
        file.write(val+" &")
    file.write(value[-1])
    file.write('\\\\ \n')

def writeFoot(file):
    file.write('\\hline\n')
    file.write('\end{tabular}\n')
    file.write('\\end{center}\n')

def writeHead(file,columns):
    #print columns
    file.write('\\begin{center}\n')
    file.write('\\begin{tabular}{l')
    for entry in columns[1:]:
        file.write('c')
    file.write('}\n')
    file.write('\\hline\n')
    for entry in columns[:-1]:
        file.write(entry+' &')
    file.write(columns[-1]+' \\\\ \n')
    file.write('\\hline\n')

def writeHistoToTable(histo,outfile):
    out=open(outfile+".tex","w")
    out.write( '\\documentclass{article}\n')
    out.write( '\\begin{document}\n')
    out.write( '\\thispagestyle{empty}\n')
    nx=histo.GetNbinsX()
    ny=histo.GetNbinsY()
    xtitle=[""]
    for i in range(1,nx+1):
        xtitle.append(histo.GetXaxis().GetBinLabel(i))
    ytitle=[]
    for i in range(1,ny+1):
        ytitle.append(histo.GetYaxis().GetBinLabel(i))

    writeHead(out,xtitle)
    for y in range(1,ny+1):
        contents=[ytitle[y-1]]
        for x in range(1,nx+1):
            contents.append("%.1f"%(histo.GetBinContent(x,y)))
        writeSyst(out,contents)
    writeFoot(out)
    out.write("\\end{document}")
    out.close()

def writeHistoListToTable(histos,names,outfile):
    names=["$"+n.replace("#","\\")+"$" for n in names]
    out=open(outfile+".tex","w")
    out.write( '\\documentclass{article}\n')
    out.write( '\\begin{document}\n')
    out.write( '\\thispagestyle{empty}\n')
    nx=histos[0].GetNbinsX()
    ny=histos[0].GetNbinsY()
    xtitle1=[""]
    xtitle2=[""]
    for i in range(1,nx+1):
        xtitle1.append(histos[0].GetXaxis().GetBinLabel(i))
        xtitle2.append(names[0])
        for i in range(1,len(histos)):
            xtitle1.append("")
            xtitle2.append(names[i])
    ytitle=[]
    for i in range(1,ny+1):
        ytitle.append(histos[0].GetYaxis().GetBinLabel(i))

    writeHead(out,xtitle1)
    writeSyst(out,xtitle2)
    for y in range(1,ny+1):
        contents=[ytitle[y-1]]
        for x in range(1,nx+1):
            for histo in histos:
                contents.append("%.1f"%(histo.GetBinContent(x,y)))
        writeSyst(out,contents)
    writeFoot(out)
    out.write("\\end{document}")
    out.close()
