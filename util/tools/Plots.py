import ROOT
ROOT.gROOT.SetBatch(True)
import re
import numpy as np
debug=0
"""
Class handling the Plotting
Contains the Name and the Histogram
label is for the legend naming
if color is not set uses dictionary defined here
OverUnderFlowInc as flag if Overflow and Underflow were already merged in the hist
Errorband should be all uncertainties
specific error band as list of error bands
"""
class Plot:
    def __init__(self, hist, name, label = None, 
                    color=None, typ='bkg', OverUnderFlowInc=False, 
                    errorband=None, specificerrorband=None):
        self.hist=hist
        self.name=name
        self.label=label
        if not label:
            self.label=name
        self.color=color
        if not color:
            self.GetPlotColor
        self.typ=typ
        self.OverUnderFlowInc=OverUnderFlowInc
        self.errorband=errorband
        self.specificerrorband=specificerrorband
        if specificerrorband:
            if not isinstance(specificerrorband, list):
                self.specificerrorband=[specificerrorband]
            self.sebColor=[ROOT.kCyan,ROOT.kYellow, 
                                    ROOT.kMagenta,ROOT.kOrange,
                                    ROOT.kPink, ROOT.kViolet]
    # dictionary for colors
    def GetPlotColor(self ):
        color_dict = {
            "ttZ":          ROOT.kCyan,
            "ttH":          ROOT.kBlue+1,
            "ttlf":         ROOT.kRed-7,
            "ttcc":         ROOT.kRed+1,
            "ttbb":         ROOT.kRed+3,
            "tt2b":         ROOT.kRed+2,
            "ttb":          ROOT.kRed-2,
            "tthf":         ROOT.kRed-3,
            "ttbar":        ROOT.kOrange,
            "ttmergedb":    ROOT.kRed-1,
        
            "sig":   ROOT.kCyan,
            "bkg":   ROOT.kOrange,
            }
        cls=self.name
        if "ttZ" in cls: cls = "ttZ"
        if "ttH" in cls: cls = "ttH"
        self.color=color_dict[cls]

    def handleOverUnderFlow(self):
        moveOverUnderFlow(self.hist)
        # set flag that over and underflow werde merged into the histogram
        self.OverUnderFlowInc=True

    def setStyle(self):
        #Sets style for Histogram, filled for background, line for signal
        if self.typ=="bkg":
            self.hist.SetLineColor(ROOT.kBlack )
            self.hist.SetFillColor(self.color)
            self.hist.SetLineWidth(1)
        elif self.typ=="signal":
            self.hist.SetLineColor(self.color )
            self.hist.SetFillColor(0)
            self.hist.SetLineWidth(2)
        else:
            print("ERROR! Type wrong!")
        #sets style for error band
        if self.errorband:
            self.errorband.SetFillStyle(3004)
            self.errorband.SetLineColor(ROOT.kBlack)
            self.errorband.SetFillColor(ROOT.kBlack)
        #sets style for error band
        if self.specificerrorband:
            for n,seb in enumerate(specificerrorband):
                seb.SetFillStyle(3004)
                seb.SetLineColor(self.sebColor[n])
                seb.SetFillColor(self.sebColor[n])

def buildHistogramAndErrorBand(rootFile,sample,nominalKey,procIden,systematicKey,sysIden):
    print("NEW SAMPLE"+str(sample.nick))
    # replace keys to get histogram key
    if procIden in nominalKey:
        sampleKey = nominalKey.replace(procIden, sample.nick)
    else:
        sampleKey=nominalKey
    rootHist = rootFile.Get(sampleKey)
    print("type of hist is: "+str(type(rootHist)) )
    if not isinstance(rootHist, ROOT.TH1):
        return "ERROR"
    #moves underflow in the first and overflow in the last bin
    moveOverUnderFlow(rootHist)
    # replace keys to get systematic key
    print("STARTING WITH SYSTEMATICS - building Errorband")
    if procIden in systematicKey:
        sampleSystKey = systematicKey.replace(procIden, sample.nick)
    else:
        sampleSystKey = systematicKey
    #Lists for error band values
    upErrors=None
    downErrors=None
    """
    Loop over systematics to get Error band for sample
    """
    for systematic in sample.getShapes():
        print systematic
        """
        create empty Error Band for sample to fill 
        """
        if not upErrors and not downErrors:
            upErrors=[0]*rootHist.GetNbinsX()
            downErrors=[0]*rootHist.GetNbinsX()
        """
        Get Key for Sytematic (up and down variation)
        """
        if sysIden in sampleSystKey:
            sampleHistKey = sampleSystKey.replace(sysIden, systematic)
        else:
            sampleHistKey = sampleSystKey
        upname=sampleHistKey+"Up"
        up= rootFile.Get(upname)
        downname=sampleHistKey+"Down"
        down= rootFile.Get(downname)
        
        """
        check if histogram is TH1 type, else skip uncertainty
        """
        if isinstance(up, ROOT.TH1) and isinstance(down, ROOT.TH1):
            moveOverUnderFlow(up)
            moveOverUnderFlow(down)

            for ibin in range(0, rootHist.GetNbinsX()):
                # get up down variations
                u_=up[ibin+1]-rootHist[ibin+1]
                d_=down[ibin+1]-rootHist[ibin+1]
                 # set max as up and min as down
                u = max(u_,d_)
                d = min(u_,d_)
                # only consider positive up and negative down variations
                u = max(0.,u)
                d = min(0.,d)
                upErrors[ibin]=ROOT.TMath.Sqrt( upErrors[ibin]*upErrors[ibin] + u*u )
                downErrors[ibin] = ROOT.TMath.Sqrt( downErrors[ibin]*downErrors[ibin] + d*d)
                if debug>99:
                    print "adding up/down ", u, d
                    print "total up/down now: ", upErrors[ibin], downErrors[ibin]
                    print "-"*50
        else:
            print("ERROR! can not use: "+str(systematic) )
            print("->type of up shape hist is: "+str(type(up)) )
            print("->type of down shape is: "+str(type(down)) )

    if upErrors:
        errorband = ROOT.TGraphAsymmErrors(rootHist)
        for i in range(len(upErrors)):
            errorband.SetPointEYlow(i, downErrors[i])
            errorband.SetPointEYhigh(i, upErrors[i])
            errorband.SetPointEXlow(i, rootHist.GetBinWidth(i+1)/2.)
            errorband.SetPointEXhigh(i, rootHist.GetBinWidth(i+1)/2.)
        PlotObject=Plot(rootHist,sample.nick,label=sample.name,
                                    color=sample.color,typ=sample.typ,
                                    errorband=errorband,OverUnderFlowInc=True)
    else:
        PlotObject=Plot(rootHist,sample.nick,label=sample.name,
                                    color=sample.color,typ=sample.typ,
                                    OverUnderFlowInc=True)
    return PlotObject

def addSamples(sample,PlotList):
    combinedErrorbands=[]
    combinedHist = None
    print("Adding samples for summarized process %s" % sample.nick)
    for process in sample.addsamples:
        print process
        if combinedHist:
            combinedHist.Add(PlotList[process].hist)
            combinedErrorbands.append(PlotList[process].errorband)
            del PlotList[process]
        else:
            combinedHist    = PlotList[process].hist 
            combinedErrorbands.append(PlotList[process].errorband)
            del PlotList[process]
    errorband=addErrorbands(combinedErrorbands,combinedHist)
    PlotList[sample.nick]=Plot(combinedHist, sample.nick, color=sample.color, typ=sample.typ, label=sample.name, errorband=errorband)
    return PlotList

def addErrorbands(combinedErrorbands,combinedHist,correlated=False):
    newErrorband = ROOT.TGraphAsymmErrors(combinedHist)
    for i in range (newErrorband.GetN()):
        up=0
        down=0
        for errorband in combinedErrorbands:
                if correlated:
                   up=up+errorband.GetErrorYhigh(i)
                   down=down+errorband.GetErrorYlow(i)
                else:
                    up=ROOT.TMath.Sqrt(up*up+errorband.GetErrorYhigh(i)*errorband.GetErrorYhigh(i))
                    down=ROOT.TMath.Sqrt(down*down+errorband.GetErrorYlow(i)*errorband.GetErrorYlow(i))
        newErrorband.SetPointEYlow(i, down)
        newErrorband.SetPointEYhigh(i, up)
        newErrorband.SetPointEXlow(i, combinedHist.GetBinWidth(i+1)/2.)
        newErrorband.SetPointEXhigh(i, combinedHist.GetBinWidth(i+1)/2.)
    return newErrorband

def moveOverUnderFlow(hist):
    # move underflow
    hist.SetBinContent(1, hist.GetBinContent(0)+hist.GetBinContent(1))
    # move overflow
    hist.SetBinContent(hist.GetNbinsX(), hist.GetBinContent(hist.GetNbinsX()+1)+hist.GetBinContent(hist.GetNbinsX()))

    # set underflow error
    hist.SetBinError(1, ROOT.TMath.Sqrt(
        ROOT.TMath.Power(hist.GetBinError(0),2) + ROOT.TMath.Power(hist.GetBinError(1),2) ))
    # set overflow error
    hist.SetBinError(hist.GetNbinsX(), ROOT.TMath.Sqrt(
        ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()),2) + 
        ROOT.TMath.Power(hist.GetBinError(hist.GetNbinsX()+1),2) ))

def GetyTitle(privateWork = False):
    # if privateWork flag is enabled, normalize plots to unit area
    if privateWork:
        return "normalized to unit area"
    return "Events expected"


# ===============================================
# DRAW HISTOGRAMS ON CANVAS
# ===============================================

def drawHistsOnCanvas(PlotList, canvasName,ratio=False, errorband=None, displayname=None, logoption=False):
    if not displayname: 
        displayname=canvasName
        
    canvas = getCanvas(canvasName, ratio)
    """
    set the Style for the Signal and Background Plots
    """
    Signal={}
    Background={}
    for sample in PlotList:
        PlotObject=PlotList[sample]
        PlotObject.setStyle()
        if PlotObject.typ=="signal":
            Signal[PlotObject.name]=PlotObject.hist.Integral()
        elif PlotObject.typ=="bkg":
            Background[PlotObject.name]=PlotObject.hist.Integral()
    """
    set the Style for the Signal and Background Plots
    sort it by Event Yield, lowest to highest
    """
    sortedSignal=sorted(Signal, key=Signal.get)
    sortedBackground=sorted(Background, key=Background.get)

    # stack bakcground Histograms
    # TODO: all the same 
    bkgHists=[]
    for i,background in enumerate(sortedBackground):
        PlotObject=PlotList[background]
        if i==0:
            hist=PlotObject.hist
            hist.SetLineColor(ROOT.kBlack )
            hist.SetFillColor(PlotObject.color)
            hist.SetLineWidth(1)
            bkgHists.append(hist)
        else:
            hist=bkgHists[i-1]
            hist.Add(PlotObject.hist)
            hist.SetLineColor(ROOT.kBlack )
            hist.SetFillColor(PlotObject.color)
            hist.SetLineWidth(1)
            bkgHists.insert(0,hist)
            
    print bkgHists

    # signal Histograms
    sigHists=[]
    for signal in sortedSignal:
        PlotObject=PlotList[signal]
        hist.SetLineColor(PlotObject.color )
        hist.SetFillColor(0)
        hist.SetLineWidth(2)
        sigHists.append(hist)
    # figure out plotrange
    canvas.cd(1)
    yMax = 1e-9
    yMinMax = 1000.
    for h in bkgHists:
        yMax = max(h.GetBinContent(h.GetMaximumBin()), yMax)
        if h.GetBinContent(h.GetMaximumBin()) > 0:
            yMinMax = min(h.GetBinContent(h.GetMaximumBin()), yMinMax)
    
    # draw the first histogram
    if len(bkgHists) == 0:
        firstHist = PlotList[sortedSignal[0]].hist
    else:
        firstHist = bkgHists[0]
    if logoption:
        firstHist.GetYaxis().SetRangeUser(yMinMax/10000, yMax*10)
        canvas.SetLogy()
    else:
        firstHist.GetYaxis().SetRangeUser(0, yMax*1.5)
    firstHist.GetXaxis().SetTitle(displayname)

    option = "histo"
    firstHist.DrawCopy(option+"E0")

    # draw the other histograms
    for h in bkgHists[1:]:
        h.DrawCopy(option+"same")

    #if errorband:
    #    errorband.Draw("same2")

    canvas.cd(1)
    # redraw axis
    firstHist.DrawCopy("axissame")

    
    # draw signal histograms
    for signal in sigHists:
        # draw signal histogram
        signal.DrawCopy(option+" E0 same")
    

    if ratio:
        canvas.cd(2)
        line = sigHists[0].Clone()
        line.Divide(sigHists[0])
        line.GetYaxis().SetRangeUser(0.5,1.5)
        line.GetYaxis().SetTitle(ratio)

        line.GetXaxis().SetLabelSize(line.GetXaxis().GetLabelSize()*2.4)
        line.GetYaxis().SetLabelSize(line.GetYaxis().GetLabelSize()*2.2)
        line.GetXaxis().SetTitle(displayname)

        line.GetXaxis().SetTitleSize(line.GetXaxis().GetTitleSize()*3)
        line.GetYaxis().SetTitleSize(line.GetYaxis().GetTitleSize()*2.5)

        line.GetYaxis().SetTitleOffset(0.5)
        line.GetYaxis().SetNdivisions(505)
        for i in range(line.GetNbinsX()+1):
            line.SetBinContent(i, 1)
            line.SetBinError(i, 1)
        line.SetLineWidth(1)
        line.SetLineColor(ROOT.kBlack)
        line.DrawCopy("histo")
        # ratio plots
        for sigHist in sigHists:
            ratioPlot = sigHist.Clone()
            ratioPlot.Divide(bkgHists[0])
            ratioPlot.SetTitle(displayname)
            ratioPlot.SetLineColor(sigHist.GetLineColor())
            ratioPlot.SetLineWidth(1)
            ratioPlot.SetMarkerStyle(20)
            ratioPlot.SetMarkerColor(sigHist.GetMarkerColor())
            ROOT.gStyle.SetErrorX(0)
            ratioPlot.DrawCopy("sameP")
        canvas.cd(1)

    legend = getLegend()
    for i,signal in enumerate(sortedSignal):
        legend.AddEntry(sigHists[i], PlotList[signal].label, "L")
    for i,background in enumerate(sortedBackground):
        legend.AddEntry(bkgHists[i], PlotList[background].label, "F")
    legend.Draw("same")

    return canvas
    


# ===============================================
# GENERATE CANVAS AND LEGENDS
# ===============================================
def getCanvas(name, ratiopad = False):
    if ratiopad:
        canvas = ROOT.TCanvas(name, name, 1024, 1024)
        canvas.Divide(1,2)
        canvas.cd(1).SetPad(0.,0.3,1.0,1.0)
        canvas.cd(1).SetTopMargin(0.07)
        canvas.cd(1).SetBottomMargin(0.0)

        canvas.cd(2).SetPad(0.,0.0,1.0,0.3)
        canvas.cd(2).SetTopMargin(0.0)
        canvas.cd(2).SetBottomMargin(0.4)

        canvas.cd(1).SetRightMargin(0.05)
        canvas.cd(1).SetLeftMargin(0.15)
        canvas.cd(1).SetTicks(1,1)

        canvas.cd(2).SetRightMargin(0.05)
        canvas.cd(2).SetLeftMargin(0.15)
        canvas.cd(2).SetTicks(1,1)
    else:
        canvas = ROOT.TCanvas(name, name, 1024, 768)
        canvas.SetTopMargin(0.07)
        canvas.SetBottomMargin(0.15)
        canvas.SetRightMargin(0.05)
        canvas.SetLeftMargin(0.15)
        canvas.SetTicks(1,1)

    return canvas

def getLegend():
    legend=ROOT.TLegend(0.70,0.6,0.95,0.9)
    legend.SetBorderSize(0);
    legend.SetLineStyle(0);
    legend.SetTextFont(42);
    legend.SetTextSize(0.05);
    legend.SetFillStyle(0);
    return legend

def saveCanvas(canvas, path):
    canvas.SaveAs(path)
    canvas.SaveAs(path.replace(".pdf",".png"))
    canvas.Clear()


# ===============================================
# PRINT STUFF ON CANVAS
# ===============================================
def printLumi(pad, lumi = 41.5, ratio = False, twoDim = False):
    if lumi == 0.: return

    lumi_text = str(lumi)+" fb^{-1} (13 TeV)"

    pad.cd(1)
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextColor(ROOT.kBlack)
    
    if twoDim:  latex.DrawLatex(l+0.40,1.-t+0.01,lumi_text)
    elif ratio: latex.DrawLatex(l+0.60,1.-t+0.04,lumi_text)
    else:       latex.DrawLatex(l+0.53,1.-t+0.02,lumi_text)

def printCategoryLabel(pad, catLabel, ratio = False):
    pad.cd(1)
    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextColor(ROOT.kBlack)

    if ratio:   latex.DrawLatex(l+0.07,1.-t-0.04, catLabel)
    else:       latex.DrawLatex(l+0.02,1.-t-0.06, catLabel)

def printPrivateWork(pad, ratio = False, twoDim = False, nodePlot = False):
    pad.cd(1) 
    l = pad.GetLeftMargin() 
    t = pad.GetTopMargin() 
    r = pad.GetRightMargin() 
    b = pad.GetBottomMargin() 
 
    latex = ROOT.TLatex() 
    latex.SetNDC() 
    latex.SetTextColor(ROOT.kBlack) 
    latex.SetTextSize(0.04)

    text = "CMS private work" 

    if nodePlot:    latex.DrawLatex(l+0.57,1.-t+0.01, text)
    elif twoDim:    latex.DrawLatex(l+0.39,1.-t+0.01, text)
    elif ratio:     latex.DrawLatex(l+0.05,1.-t+0.04, text) 
    else:           latex.DrawLatex(l,1.-t+0.01, text)
