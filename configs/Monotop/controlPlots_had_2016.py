import sys
import os

filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT
from array import array
from copy import deepcopy

fast = True

#discr_binning = [250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 1000, 1500]
discr_binning = [250.0, 270.0, 290.0, 310.0, 330.0, 360.0, 390.0, 430.0, 480.0, 560.0, 1000.]

# met/recoil + 1 ak15jet phase space
generalselection = "(Hadr_Recoil_Pt>250.)*(N_AK15Jets==1)*(AK15Jet_Pt[0]>200.)*(N_Jets>=1)*(N_Taus==0)"#*(AK15Jet_NHF[0]>0.04 || CaloMET_PFMET_Recoil_ratio<0.2)"
generalselection += "*(DeltaPhi_AK15Jet_Hadr_Recoil[0]>1.5)"
# QCD rejection
#generalselection += "*(DeltaPhi_AK4Jets_MET_Larger_0p5)"
# MET quality cut???
#generalselection += "*(CaloMET_PFMET_Recoil_ratio<0.2)"
# ak15 jet quality cuts
#generalselection += "*(AK15Jet_CHF[0]>0.1)*(AK15Jet_NHF[0]<0.8)*(AK15Jet_CEMF[0]<0.8)*(AK15Jet_NEMF[0]<0.7)*(AK15Jet_MF[0]<0.2)"
# top mass window
generalselection += "*(AK15Jet_PuppiSoftDropMass[0]>105.)*(AK15Jet_PuppiSoftDropMass[0]<210.)"
generalselection += "*(AK15Jet_DeepAK15_TvsQCD[0]>0.3)"

def control_plots_had_SR(data=None):
    label = "#scale[0.8]{signal region (hadronic)}"
    extension = "_had_SR"
    
    selection = generalselection
    selection += "*(N_LooseMuons==0 && N_LooseElectrons==0 && N_LoosePhotons==0)"
    selection += "*((Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_vX == 1) || (Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_vX == 1))"
    selection += "*(N_AK4JetsLooseTagged_outside_AK15Jets[0]==0)"
    selection += "*(DeltaPhi_AK4Jets_MET_Larger_0p5)"
    #selection += "*(CaloMET>200.)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)
    
    plots = [
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("N1_N2_Mass" + extension, "Mediator Mass", 50, 0.0, 5000.0),
            #"N1_N2_Mass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("N1_N2_Pt" + extension, "Mediator p_{t}", 50, 0.0, 5000.0),
            #"N1_N2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Neutralino_Pt" + extension, "Neutralino p_{t}", 40, 0.0, 2000.0),
            #"Neutralino_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Neutralino_Mass" + extension, "Neutralino Mass", 40, 0.0, 2000.0
            #),
            #"Neutralino_Mass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("GenTopHad_B_DR" + extension, "GenTopHad_B_DR", 30, 0.0, 4.0),
            #"GenTopHad_B_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("GenTopHad_Q1_DR" + extension, "GenTopHad_Q1_DR", 30, 0.0, 4.0),
            #"GenTopHad_Q1_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("GenTopHad_Q2_DR" + extension, "GenTopHad_Q2_DR", 30, 0.0, 4.0),
            #"GenTopHad_Q2_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"GenTopHad_B_Q1_DR" + extension, "GenTopHad_B_Q1_DR", 30, 0.0, 4.0
            #),
            #"GenTopHad_B_Q1_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"GenTopHad_B_Q2_DR" + extension, "GenTopHad_B_Q2_DR", 30, 0.0, 4.0
            #),
            #"GenTopHad_B_Q2_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"GenTopHad_Q1_Q2_DR" + extension, "GenTopHad_Q1_Q2_DR", 30, 0.0, 4.0
            #),
            #"GenTopHad_Q1_Q2_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"GenTopHad_W_Q1_DR" + extension, "GenTopHad_W_Q1_DR", 30, 0.0, 4.0
            #),
            #"GenTopHad_W_Q1_DR",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"GenTopHad_W_Q2_DR" + extension, "GenTopHad_W_Q2_DR", 30, 0.0, 4.0
            #),
            #"GenTopHad_W_Q2_DR",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 25, 0.0, 500.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),    
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_CHF" + extension, "AK8 Jet CHF", 20, 0.0, 1.0),
            #"AK8Jet_CHF",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_NHF" + extension, "AK8 Jet NHF", 20, 0.0, 1.0),
            #"AK8Jet_NHF",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Weight_TopPt" + extension, "Weight Top Pt", 20, 0.0, 2.0),
            "Weight_TopPt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK4Jet_AK15Jet_pt_ratio" + extension,
                "AK4Jet/AK15Jet pt ratio",
                40,
                0.0,
                2.0,
            ),
            "Jet_Pt[0]/AK15Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,
            1.0,  
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                40,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_had_CR_ZMuMu(data=None):
    label = "#scale[0.8]{Z(#mu#bar{#mu}) control region}"
    extension = "_had_CR_ZMuMu"
    
    selection = generalselection
    selection += "*(N_LooseMuons==2 && N_TightMuons>=1 && N_LooseElectrons==0 && N_LoosePhotons==0)"
    selection += "*((Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_vX == 1) || (Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_vX == 1))"
    selection += "*(DiMuon_Mass>60.)*(DiMuon_Mass<120.)"
    selection += "*(N_AK4JetsLooseTagged_outside_AK15Jets[0]==0)"
    selection += "*(DiMuon_Pt>200.)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("LooseMuon_Pt" + extension, "Loose Muon p_{T} [GeV]", 49, 10.0, 500.0),
            "LooseMuon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseMuon_Eta" + extension, "Loose Muon #eta", 25, -2.5, 2.5),
            "LooseMuon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("LooseMuon_Phi" + extension, "Loose Muon #phi", 30, -3.14, 3.14),
            "LooseMuon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{T} [GeV]", 49, 10.0, 500.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta" + extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Pt" + extension, "DiMuon p_{T} [GeV]", 40, 10.0, 810.0),
            "DiMuon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Eta" + extension, "DiMuon #eta", 25, -2.5, 2.5),
            "DiMuon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Phi" + extension, "DiMuon #phi", 30, -3.14, 3.14),
            "DiMuon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiMuon_Mass" + extension, "DiMuon mass [GeV]", 40, 0.0, 200.0),
            "DiMuon_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_DiMuon" + extension,
                "DeltaR_AK15Jet_DiMuon",
                50,
                0.0,
                5.0,
            ),
            "sqrt(pow(AK15Jet_Eta[0]-DiMuon_Eta,2)+pow(AK15Jet_Phi[0]-DiMuon_Phi,2))",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_had_CR_ZElEl(data=None):
    label = "#scale[0.8]{Z(e#bar{e}) control region}"
    extension = "_had_CR_ZElEl"
    
    selection = generalselection
    selection += "*(N_LooseElectrons==2 && N_TightElectrons>=1 && N_LooseMuons==0 && N_LoosePhotons==0)"
    selection += "*(Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1)"
    selection += "*(DiElectron_Mass>60.)*(DiElectron_Mass<120.)"
    selection += "*(N_AK4JetsLooseTagged_outside_AK15Jets[0]==0)"
    selection += "*(DiElectron_Pt>200.)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "LooseElectron_Pt" + extension, "Loose Electron p_{T} [GeV]", 49, 10.0, 500.0
            ),
            "LooseElectron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "LooseElectron_Eta" + extension, "Loose Electron #eta", 25, -2.5, 2.5
            ),
            "LooseElectron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "LooseElectron_Phi" + extension, "Loose Electron #phi", 30, -3.14, 3.14
            ),
            "LooseElectron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Pt" + extension, "Tight Electron p_{T} [GeV]", 49, 10.0, 500.0
            ),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta" + extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Phi" + extension, "Tight Electron #phi", 30, -3.14, 3.14
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Pt" + extension, "DiElectron p_{T} [GeV]", 40, 10.0, 810.0),
            "DiElectron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Eta" + extension, "DiElectron #eta", 25, -2.5, 2.5),
            "DiElectron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Phi" + extension, "DiElectron #phi", 30, -3.14, 3.14),
            "DiElectron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("DiElectron_Mass" + extension, "DiElectron mass [GeV]", 40, 0.0, 200.0),
            "DiElectron_Mass",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_DiElectron" + extension,
                "DeltaR_AK15Jet_DiElectron",
                50,
                0.0,
                5.0,
            ),
            "sqrt(pow(AK15Jet_Eta[0]-DiElectron_Eta,2)+pow(AK15Jet_Phi[0]-DiElectron_Phi,2))",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def control_plots_had_CR_ttbarEl(data=None):
    label = "#scale[0.8]{t#bar{t} control region (e)}"
    extension = "_had_CR_ttbarEl"
    
    selection = generalselection
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1))"
    selection += "*(N_LoosePhotons==0)"
    selection += "*(N_AK4JetsTagged_outside_AK15Jets[0]>=1)"
    selection += "*(M_W_transverse[0]<150.)"
    #selection += "*(DeltaPhi_AK4Jets_MET_Larger_0p5)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Pt" + extension, "Tight Electron p_{T} [GeV]", 49, 10.0, 500.0
            ),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta" + extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Phi" + extension, "Tight Electron #phi", 30, -3.14, 3.14
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_had_CR_ttbarMu(data=None):
    label = "#scale[0.8]{t#bar{t} control region (mu)}"
    extension = "_had_CR_ttbarMu"
    
    selection = generalselection
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && ((Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_vX == 1) || (Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_vX == 1)))"
    selection += "*(N_LoosePhotons==0)"
    selection += "*(N_AK4JetsTagged_outside_AK15Jets[0]>=1)"
    selection += "*(M_W_transverse[0]<150.)"
    #selection += "*(DeltaPhi_AK4Jets_MET_Larger_0p5)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{T} [GeV]", 49, 10.0, 500.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta" + extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_had_CR_WEl(data=None):
    label = "#scale[0.8]{W control region (e)}"
    extension = "_had_CR_WEl"
    
    selection = generalselection
    selection += "*(N_LooseElectrons==1 && N_TightElectrons==1 && N_LooseMuons==0 && (Triggered_HLT_Ele27_WPTight_Gsf_vX==1 || Triggered_HLT_Photon175_vX==1))"
    selection += "*(N_LoosePhotons==0)"
    selection += "*(N_AK4JetsLooseTagged_outside_AK15Jets[0]==0)"
    selection += "*(M_W_transverse[0]<150.)"
    selection += "*(Evt_Pt_MET>50.)"
    #selection += "*(DeltaPhi_AK4Jets_MET_Larger_0p5)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Pt" + extension, "Tight Electron p_{T} [GeV]", 49, 10.0, 500.0
            ),
            "Electron_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Electron_Eta" + extension, "Tight Electron #eta", 25, -2.5, 2.5),
            "Electron_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Electron_Phi" + extension, "Tight Electron #phi", 30, -3.14, 3.14
            ),
            "Electron_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_had_CR_WMu(data=None):
    label = "#scale[0.8]{W control region (mu)}"
    extension = "_had_CR_WMu"
    
    selection = generalselection
    selection += "*(N_LooseMuons==1 && N_TightMuons==1 && N_LooseElectrons==0 && ((Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_vX == 1) || (Triggered_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_vX == 1)))"
    selection += "*(N_LoosePhotons==0)"
    selection += "*(N_AK4JetsLooseTagged_outside_AK15Jets[0]==0)"
    selection += "*(M_W_transverse[0]<150.)"
    #selection += "*(DeltaPhi_AK4Jets_MET_Larger_0p5)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Pt" + extension, "Tight Muon p_{T} [GeV]", 49, 10.0, 500.0),
            "Muon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Eta" + extension, "Tight Muon #eta", 25, -2.5, 2.5),
            "Muon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Muon_Phi" + extension, "Tight Muon #phi", 30, -3.14, 3.14),
            "Muon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots

def control_plots_had_CR_Gamma(data=None):
    label = "#scale[0.8]{#gamma control region}"
    extension = "_had_CR_Gamma"
    
    selection = generalselection
    selection += "*(N_TightPhotons==1 && N_LoosePhotons==1 && N_LooseMuons==0 && N_LooseElectrons==0 && Triggered_HLT_Photon175_vX==1 && Photon_Pt[0]>=200.)"
    selection += "*(N_AK4JetsLooseTagged_outside_AK15Jets[0]==0)"
    #selection += "*((AK15Jet_DeepAK15_probTbqq[0]+AK15Jet_DeepAK15_probTbcq[0])>0.5)

    plots = [
        plotClasses.Plot(
            ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Pt_MET" + extension, "#slash{E}{T} [GeV]", 20, 0.0, 200.0),
            "Evt_Pt_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Evt_Phi_MET" + extension, "#phi(#slash{E}{T})", 30, -3.14, 3.14),
            "Evt_Phi_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("CaloMET" + extension, "Calo #slash{E}{T} [GeV]", 50, 0.0, 1000.0),
            "CaloMET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/Calo #slash{E}{T}", 50, 0.0, 10.0
            ),
            "CaloMET_PFMET_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_Hadr_Recoil_ratio" + extension,
                "CaloMET_Hadr_Recoil_ratio",
                50,
                0.0,
                10.0,
            ),
            "CaloMET_Hadr_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension,
                "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
            ),
            "CaloMET_PFMET_Recoil_ratio",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
            "AK15Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Eta" + extension, "AK15 Jet #eta", 25, -2.5, 2.5),
            "AK15Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_Phi" + extension, "AK15 Jet #phi", 30, -3.14, 3.14),
            "AK15Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Pt" + extension,
                "AK15 SD Jet p_{T} [GeV]",
                20,
                200.0,
                1200.0,
            ),
            "AK15Jet_SoftDrop_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Eta" + extension, "AK15 SD Jet #eta", 25, -2.5, 2.5
            ),
            "AK15Jet_SoftDrop_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Phi" + extension, "AK15 SD Jet #phi", 30, -3.14, 3.14
            ),
            "AK15Jet_SoftDrop_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDrop_Mass" + extension, "AK15 SD Jet mass [GeV]", 20, 0.0, 400.0
            ),
            "AK15Jet_SoftDrop_M",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_Pt" + extension,
                "AK15 SD Jet1 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet1_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_Pt" + extension,
                "AK15 SD Jet2 p_{T} [GeV]",
                20,
                0.0,
                1000.0,
            ),
            "AK15Jet_SoftDropJet2_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet1_DeepJetCSV" + extension,
                "AK15 SD Jet1 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet1_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_SoftDropJet2_DeepJetCSV" + extension,
                "AK15 SD Jet2 DeepJet",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_SoftDropJet2_DeepJetCSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_TvsQCD",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbc" + extension,
                "AK15 Jet DeepAK15 probTbc",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbc",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbcq" + extension,
                "AK15 Jet DeepAK15 probTbcq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbq" + extension,
                "AK15 Jet DeepAK15 probTbq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_DeepAK15_probTbqq" + extension,
                "AK15 Jet DeepAK15 probTbqq",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_TopTagger" + extension,
                "AK15 top tagger",
                20,
                0.0,
                1.0,
            ),
            "AK15Jet_DeepAK15_probTbqq+AK15Jet_DeepAK15_probTbcq",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15pJet_Njettiness_tau3_AK15Jet_Njettiness_tau2" + extension,
                #"AK15 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau3/AK15Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK15Jet_Njettiness_tau2_AK15Jet_Njettiness_tau1" + extension,
                #"AK15 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK15Jet_Njettiness_tau2/AK15Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                20,
                0.0,
                400.0,
            ),
            "AK15Jet_PuppiSoftDropMass",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Pt" + extension, "AK8 Jet p_{t}", 40, 200.0, 1200.0),
            #"AK8Jet_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Eta" + extension, "AK8 Jet #eta", 25, -2.5, 2.5),
            #"AK8Jet_Eta",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("AK8Jet_Phi" + extension, "AK8 Jet #phi", 30, -3.14, 3.14),
            #"AK8Jet_Phi",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_Pt" + extension,
                #"AK8 SD Jet1 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet1_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_Pt" + extension,
                #"AK8 SD Jet2 p_{t}",
                #40,
                #0.0,
                #1000.0,
            #),
            #"AK8Jet_SoftDropJet2_Pt",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet1_DeepJetCSV" + extension,
                #"AK8 SD Jet1 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet1_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_SoftDropJet2_DeepJetCSV" + extension,
                #"AK8 SD Jet2 DeepJetCSV",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_SoftDropJet2_DeepJetCSV",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_TvsQCD" + extension,
                #"AK8 Jet DeepAK8 TvsQCD",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_TvsQCD",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbc" + extension,
                #"AK8 Jet DeepAK8 probTbc",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbc",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbcq" + extension,
                #"AK8 Jet DeepAK8 probTbcq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbcq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbq" + extension,
                #"AK8 Jet DeepAK8 probTbq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_DeepAK8_probTbqq" + extension,
                #"AK8 Jet DeepAK8 probTbqq",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_DeepAK8_probTbqq",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau3_AK8Jet_Njettiness_tau2" + extension,
                #"AK8 Jet #tau_{3}/#tau_{2}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau3/AK8Jet_Njettiness_tau2",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_Njettiness_tau2_AK8Jet_Njettiness_tau1" + extension,
                #"AK8 Jet #tau_{2}/#tau_{1}",
                #20,
                #0.0,
                #1.0,
            #),
            #"AK8Jet_Njettiness_tau2/AK8Jet_Njettiness_tau1",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK8Jet_PuppiSoftDropMass" + extension,
                #"AK8 Jet SD mass",
                #25,
                #0.0,
                #250.0,
            #),
            #"AK8Jet_PuppiSoftDropMass",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("Evt_Pt_GenMET" + extension, "Puppi GEN MET", 40, 0.0, 1000.0),
            #"Evt_Pt_GenMET",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D("NaiveMET" + extension, "Naive GEN MET", 40, 0.0, 1000.0),
            #"NaiveMET",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
            ),
            "Hadr_Recoil_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Hadr_Recoil_Phi" + extension, "#phi(#slash{U}_{T})", 30, -3.14, 3.14
            ),
            "Hadr_Recoil_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_MET" + extension,
                "#Delta#phi(AK15 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK15Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK15 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK15Jet_Hadr_Recoil",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension, "#Delta#phi(AK4 Jet, #slash{E}_{T})", 30, 0.0, 3.14
            ),
            "DeltaPhi_AK4Jet_MET",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_Hadr_Recoil" + extension,
                "#Delta#phi(AK4 Jet, #slash{U}_{T})",
                30,
                0.0,
                3.14,
            ),
            "DeltaPhi_AK4Jet_Hadr_Recoil",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"Weight_GEN_nom" + extension, "Generator weight", 1100, -100.0, 1000.0
            #),
            #"Weight_GEN_nom",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("Photon_Pt" + extension, "Tight Photon p_{T} [GeV]", 49, 10.0, 500.0),
            "Photon_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Photon_Eta" + extension, "Tight Photon #eta", 25, -2.5, 2.5),
            "Photon_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Photon_Phi" + extension, "Tight Photon #phi", 30, -3.14, 3.14),
            "Photon_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsM" + extension, "medium btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsM",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsL" + extension, "loose btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsL",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_BTagsT" + extension, "tight btag multiplicity", 6, -0.5, 5.5),
            "N_BTagsT",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt" + extension, "AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_0" + extension, "leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[0]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Pt_1" + extension, "sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770),
            "Jet_Pt[1]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "Jet_Pt_2" + extension, "sub-sub-leading AK4 Jet p_{T} [GeV]", 25, 20, 770
            ),
            "Jet_Pt[2]",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Eta" + extension, "AK4 Jet #eta", 25, -2.5, 2.5),
            "Jet_Eta",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_Phi" + extension, "AK4 Jet #phi", 30, -3.14, 3.14),
            "Jet_Phi",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("Jet_CSV" + extension, "AK4 Jet DeepJet", 20, 0.0, 1.0),
            "Jet_CSV",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Jets" + extension, "number of AK4 jets", 6, -0.5, 5.5),
            "N_Jets",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("N_Taus" + extension, "number of taus", 6, -0.5, 5.5),
            "N_Taus",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4JetTagged" + extension,
                "DeltaR_AK15Jet_AK4JetTagged",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4JetTagged",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "DeltaR_AK15Jet_AK4Jet" + extension,
                "DeltaR_AK15Jet_AK4Jet",
                40,
                0.0,
                4.0,
            ),
            "DeltaR_AK15Jet_AK4Jet",
            selection,
            label,
        ),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4JetTagged" + extension,
                #"DeltaR_AK8Jet_AK4JetTagged",
                #40,
                #0.0,
                #4.0,
            #),
            #"DeltaR_AK8Jet_AK4JetTagged",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"DeltaR_AK8Jet_AK4Jet" + extension, "DeltaR_AK8Jet_AK4Jet", 40, 0.0, 4.0
            #),
            #"DeltaR_AK8Jet_AK4Jet",
            #selection,
            #label,
        #),
        #plotClasses.Plot(
            #ROOT.TH1D(
                #"AK4Jet_AK15Jet_pt_ratio" + extension,
                #"AK4Jet/AK15Jet pt ratio",
                #40,
                #0.0,
                #2.0,
            #),
            #"Jet_Pt[0]/AK15Jet_Pt[0]",
            #selection,
            #label,
        #),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CHF" + extension, "AK15 Jet CHF", 40, 0.0, 1.0),
            "AK15Jet_CHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
            "AK15Jet_NHF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_CEMF" + extension, "AK15 Jet CEMF", 40, 0.0, 1.0),
            "AK15Jet_CEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_NEMF" + extension, "AK15 Jet NEMF", 40, 0.0, 1.0),
            "AK15Jet_NEMF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("AK15Jet_MF" + extension, "AK15 Jet MF", 40, 0.0, 1.0),
            "AK15Jet_MF",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
                "N_PVs" + extension, "number of primary vertices", 20, 0.0, 100.0
            ),
            "N_PrimaryVertices",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("M_W_transverse" + extension, "m_{W,transverse}", 30, 0., 600.),
            "M_W_transverse",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D("internalBosonWeight" + extension, "internalBosonWeight", 20, 0.0, 2.0),
            "internalBosonWeight",
            selection,
            label,
        ),
        plotClasses.Plot(
            ROOT.TH1D(
            "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
            40,
            -1.0,   
            1.0,
            ),
            "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
            selection,
            label,
        ),
    ]
    if fast:
        plots = [
            plotClasses.Plot(
                ROOT.TH1D(
                    "Hadr_Recoil_Pt" + extension, "#slash{U}_{T} [GeV]", len(discr_binning)-1, array('d',discr_binning)
                ),
                "Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("yield" + extension, "yield", 1, 0.0, 2.0), "1.", selection, label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_Pt" + extension, "AK15 Jet p_{T} [GeV]", 20, 200.0, 1200.0),
                "AK15Jet_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D("AK15Jet_NHF" + extension, "AK15 Jet NHF", 40, 0.0, 1.0),
                "AK15Jet_NHF",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "CaloMET_PFMET_Recoil_ratio" + extension, "|Calo #slash{E}{T} - #slash{E}{T}|/#slash{U}{T}",
                40,
                0.0,
                2.0,
                ),
                "CaloMET_PFMET_Recoil_ratio",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "Hadr_Recoil_AK15Jet_Pt_ratio" + extension, "Hadr_Recoil_AK15Jet_Pt_ratio",
                20,
                -1.0,
                1.0,
                ),
                "(Hadr_Recoil_Pt-AK15Jet_Pt)/Hadr_Recoil_Pt",
                selection,
                label,
            ),
            plotClasses.Plot(
                ROOT.TH1D(
                "AK15Jet_DeepAK15_TvsQCD" + extension,
                "AK15 Jet DeepAK15 TvsQCD",
                40,
                0.0,
                1.0,
                ),
                "AK15Jet_DeepAK15_TvsQCD",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "AK15Jet_PuppiSoftDropMass" + extension,
                "AK15 Jet SD mass [GeV]",
                40,
                0.0,
                400.0,
                ),
                "AK15Jet_PuppiSoftDropMass",
                selection,
                label,
            ),
            plotClasses.Plot(
            ROOT.TH1D(
                "DeltaPhi_AK4Jet_MET" + extension,
                "#Delta#phi(AK4 Jet, #slash{E}_{T})",
                30,
                0.0,
                3.14,
                ),
                "DeltaPhi_AK4Jet_MET",
                selection,
                label,
            ),
            ]
    if data:
        add_data_plots(plots=plots, data=data)

    return plots


def getDiscriminatorPlots(data=None, discrname=""):
    discriminatorPlots = []
    discriminatorPlots += control_plots_had_SR(data)
    discriminatorPlots += control_plots_had_CR_ZMuMu(data)
    discriminatorPlots += control_plots_had_CR_ZElEl(data)
    discriminatorPlots += control_plots_had_CR_ttbarEl(data)
    discriminatorPlots += control_plots_had_CR_ttbarMu(data)
    discriminatorPlots += control_plots_had_CR_WEl(data)
    discriminatorPlots += control_plots_had_CR_WMu(data)
    discriminatorPlots += control_plots_had_CR_Gamma(data)

    return discriminatorPlots


def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
