
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import ROOT



def evtYieldCategories():
    return [
    ("(N_Jets>=6&&N_BTagsM==2)","6j2t",""),
    ("(N_Jets==4&&N_BTagsM==3)","4j3t",""),
    ("(N_Jets==5&&N_BTagsM==3)","5j3t",""),
    ("(N_Jets>=6&&N_BTagsM==3)","6j3t",""),
    ("(N_Jets==4&&N_BTagsM>=4)","4j4t",""),
    ("(N_Jets==5&&N_BTagsM>=4)","5j4t",""),
    ("(N_Jets>=6&&N_BTagsM>=4)","6j4t","")
    ]

memexp = ""


def plots_ge4j_ge4t():
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_0","#phi of leading jet",30,-3.14159265359,3.14159265359),"Jet_Phi[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_E_3","energy of fourth jet",30,20.0,500.0),"Jet_E[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_LooseLepton_Eta_0","#eta(lep)",30,-2.4,2.4),"LooseLepton_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Phi_2","#phi of third jet",30,-3.14159265359,3.14159265359),"Jet_Phi[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_2","#eta of third jet",30,-2.4,2.4),"Jet_Eta[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Eta_0","#eta of leading jet",30,-2.4,2.4),"Jet_Eta[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_pt_all_jets_over_E_all_jets_tags","p_{T}(tags)/E(tags)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_blr","btag likelihood ratio",30,0.0,1.0),"MVA_blr",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsL","number of btags (loose)",6,2.5,8.5),"N_BTagsL",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots

def plots_le5j_ge3t():
    label = "\leq 5 jets, \geq 3 b-tags"
    selection = "(N_Jets<=5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("le5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots

def plots_5j_ge3t():
    label = "5 jets, \geq 3 b-tags"
    selection = "(N_Jets==5&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_h1","second fox wolfram moment",30,-0.2,0.4),"MVA_h1",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("5j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots

def plots_ge6j_ge3t():
    label = "\geq 6 jets, \geq 3 b-tags"
    selection = "(N_Jets>=6&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_4","p_{T} of fifth jet",30,30.0,150.0),"Jet_Pt[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_h2","third fox wolfram moment",30,-0.15,0.3),"MVA_h2",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_pt_all_jets_over_E_all_jets_tags","p_{T}(tags)/E(tags)",30,0.2,1.0),"MVA_pt_all_jets_over_E_all_jets_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_1","DeepJet btag value of subleading jet",30,0.0,1.0),"Jet_DeepJetCSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_4","fifth highest btag value",30,0.0,1.0),"CSV[4]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_5","p_{T} of sixth jet",30,30.0,100.0),"Jet_Pt[5]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge6j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots

def plots_ge4j_ge3t():
    label = "\geq 4 jets, \geq 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_BTagsM","number of btags (medium)",6,1.5,7.5),"N_BTagsM",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_CSV_3","fourth highest btag value",30,0.0,1.0),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        ]

    return plots

def plots_4j_ge3t():
    label = "4 jets, \geq 3 b-tags"
    selection = "(N_Jets==4&&N_BTagsM>=3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_CSV_2","third highest btag value",30,0.3,1.0),"CSV[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_3","mass of fourth jet",30,0.0,30.0),"Jet_M[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRJets","min #DeltaR(jet jet)",30,0.4,2.2),"Evt_Dr_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_delta_eta_l_bhad","#Delta#eta(lep b_{had})",30,0.0,4.0),"MVA_delta_eta_l_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_MHT","missing H_{T}",30,0.0,300.0),"MVA_MHT",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_delta_eta_blep_bhad","#Delta#eta(b_{lep} b_{had})",30,0.0,4.0),"MVA_delta_eta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("4j_ge3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        ]

    return plots

def plots_ge4j_3t():
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_HT","H_{T}",30,100.0,1500.0),"MVA_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRJets","mass of min #DeltaR(jet jet)",30,20.0,200.0),"Evt_M_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_JetsAverage","average M_{2}(jets)",30,50.0,500.0),"Evt_M2_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_cos_theta_blep_bhad","cos#theta(b_{lep} b_{had})",30,-1.0,1.0),"MVA_cos_theta_blep_bhad",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_LooseLepton_Pt_0","p_{T}(lep)",30,0.0,400.0),"LooseLepton_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MedianTaggedJets","median M(tags)",30,50.0,500.0),"Evt_M_MedianTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_CSV_Average","average btag value",30,0.2,1.0),"MVA_Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_3","fourth highest btag value",30,0.0,0.3),"CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_LooseJets","N(LooseJets)",7,3.5,10.5),"N_LooseJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_3","p_{T} of fourth jet",30,30.0,200.0),"Jet_Pt[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_MinDeltaRJets","p_{T} of min #DeltaR(jet jet)",30,20.0,600.0),"Evt_Pt_MinDeltaRJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_JetsAverage","average #DeltaR(jets)",30,0.7,3.5),"Evt_Dr_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,0.0,600.0),"MVA_Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_invariant_mass_of_everything","invariant mass of everything",30,200.0,2500.0),"MVA_invariant_mass_of_everything",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"MVA_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_M3","M_{3}",30,100.0,1000.0),"MVA_M3",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_tagged_dijet_mass_closest_to_125","M_{2}(tags) closest to 125 GeV",30,50.0,250.0),"MVA_tagged_dijet_mass_closest_to_125",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"MVA_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_M_0","mass of leading jet",30,0.0,100.0),"Jet_M[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_HT_tag","H_{T}(tags)",30,100.0,900.0),"MVA_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRTaggedJets","mass of min #DeltaR(tag tag)",30,20.0,400.0),"Evt_M_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_DeepJetCSV_0","DeepJet btag value of leading jet",30,0.0,1.0),"Jet_DeepJetCSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"MVA_Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_MVA_Evt_Deta_JetsAverage","average #Delta#eta(jets)",30,0.25,2.5),"MVA_Evt_Deta_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Pt_MinDeltaRTaggedJets","p_{T} of min #DeltaR(tag tag)",30,20.0,500.0),"Evt_Pt_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_TaggedJetsAverage","average M(tags)",30,5.0,50.0),"Evt_M_TaggedJetsAverage",selection,label),
        ]

    return plots


def plots_dnn(data, discrname):
    categories = []
    nhistobins = []
    minxvals = []
    maxxvals = []
    discrs = []

    ndefaultbins = 15




    # plots for ge4j_ge4t
    categories += [
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==0)","ljets_ge4j_ge4t_ttZ_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==1)","ljets_ge4j_ge4t_ttH_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==2)","ljets_ge4j_ge4t_tthf_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==3)","ljets_ge4j_ge4t_ttcc_node",""),
        ("((N_Jets>=4&&N_BTagsM>=4)&&DNNPredictedClass_ge4j_ge4t==4)","ljets_ge4j_ge4t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge4j_ge4t_node_ttZ",
        "DNNOutput_ge4j_ge4t_node_ttH",
        "DNNOutput_ge4j_ge4t_node_tthf",
        "DNNOutput_ge4j_ge4t_node_ttcc",
        "DNNOutput_ge4j_ge4t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, 10, 10, 10, 10]
    minxvals += [0.25, 0.25, 0.3, 0.25, 0.3]
    maxxvals += [0.7, 0.65, 0.7, 0.6, 0.6]





    # plots for le5j_ge3t
    categories += [
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==0)","ljets_le5j_ge3t_ttZ_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==1)","ljets_le5j_ge3t_ttH_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==2)","ljets_le5j_ge3t_tthf_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==3)","ljets_le5j_ge3t_ttcc_node",""),
        ("((N_Jets<=5&&N_BTagsM>=3)&&DNNPredictedClass_le5j_ge3t==4)","ljets_le5j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_le5j_ge3t_node_ttZ",
        "DNNOutput_le5j_ge3t_node_ttH",
        "DNNOutput_le5j_ge3t_node_tthf",
        "DNNOutput_le5j_ge3t_node_ttcc",
        "DNNOutput_le5j_ge3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, 10, 10, 10, 10]
    minxvals += [0.25, 0.25, 0.25, 0.25, 0.25]
    maxxvals += [0.7, 0.6, 0.65, 0.45, 0.6]



    # plots for ge6j_ge3t
    categories += [
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==0)","ljets_ge6j_ge3t_ttZ_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==1)","ljets_ge6j_ge3t_ttH_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==2)","ljets_ge6j_ge3t_tthf_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==3)","ljets_ge6j_ge3t_ttcc_node",""),
        ("((N_Jets>=6&&N_BTagsM>=3)&&DNNPredictedClass_ge6j_ge3t==4)","ljets_ge6j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge6j_ge3t_node_ttZ",
        "DNNOutput_ge6j_ge3t_node_ttH",
        "DNNOutput_ge6j_ge3t_node_tthf",
        "DNNOutput_ge6j_ge3t_node_ttcc",
        "DNNOutput_ge6j_ge3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, 10, ndefaultbins, 10, 10]
    minxvals += [0.25, 0.25, 0.25, 0.25, 0.25]
    maxxvals += [0.7, 0.6, 0.7, 0.4, 0.55]




    # plots for 5j_ge3t
    categories += [
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==0)","ljets_5j_ge3t_ttZ_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==1)","ljets_5j_ge3t_ttH_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==2)","ljets_5j_ge3t_tthf_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==3)","ljets_5j_ge3t_ttcc_node",""),
        ("((N_Jets==5&&N_BTagsM>=3)&&DNNPredictedClass_5j_ge3t==4)","ljets_5j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_5j_ge3t_node_ttZ",
        "DNNOutput_5j_ge3t_node_ttH",
        "DNNOutput_5j_ge3t_node_tthf",
        "DNNOutput_5j_ge3t_node_ttcc",
        "DNNOutput_5j_ge3t_node_ttlf",
        ]
    nhistobins += [10, 10, 10, 5, 10]
    minxvals += [0.25, 0.25, 0.25, 0.25, 0.25]
    maxxvals += [0.77, 0.6, 0.65, 0.45, 0.55]





    # plots for ge4j_ge3t
    categories += [
        ("((N_Jets>=4&&N_BTagsM>=3)&&DNNPredictedClass_ge4j_ge3t==0)","ljets_ge4j_ge3t_ttZ_node",""),
        ("((N_Jets>=4&&N_BTagsM>=3)&&DNNPredictedClass_ge4j_ge3t==1)","ljets_ge4j_ge3t_ttH_node",""),
        ("((N_Jets>=4&&N_BTagsM>=3)&&DNNPredictedClass_ge4j_ge3t==2)","ljets_ge4j_ge3t_tthf_node",""),
        ("((N_Jets>=4&&N_BTagsM>=3)&&DNNPredictedClass_ge4j_ge3t==3)","ljets_ge4j_ge3t_ttcc_node",""),
        ("((N_Jets>=4&&N_BTagsM>=3)&&DNNPredictedClass_ge4j_ge3t==4)","ljets_ge4j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge4j_ge3t_node_ttZ",
        "DNNOutput_ge4j_ge3t_node_ttH",
        "DNNOutput_ge4j_ge3t_node_tthf",
        "DNNOutput_ge4j_ge3t_node_ttcc",
        "DNNOutput_ge4j_ge3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, 10, 10, 10, 10]
    minxvals += [0.25, 0.25, 0.25, 0.25, 0.3]
    maxxvals += [0.65, 0.65, 0.65, 0.45, 0.7]





    # plots for 4j_ge3t
    categories += [
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==0)","ljets_4j_ge3t_ttZ_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==1)","ljets_4j_ge3t_ttH_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==2)","ljets_4j_ge3t_tthf_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==3)","ljets_4j_ge3t_ttcc_node",""),
        ("((N_Jets==4&&N_BTagsM>=3)&&DNNPredictedClass_4j_ge3t==4)","ljets_4j_ge3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_4j_ge3t_node_ttZ",
        "DNNOutput_4j_ge3t_node_ttH",
        "DNNOutput_4j_ge3t_node_tthf",
        "DNNOutput_4j_ge3t_node_ttcc",
        "DNNOutput_4j_ge3t_node_ttlf",
        ]
    nhistobins += [ndefaultbins, 10, 10, 10, 10]
    minxvals += [0.25, 0.25, 0.25, 0.25, 0.25]
    maxxvals += [0.7, 0.6, 0.65, 0.5, 0.6]





    # plots for ge4j_3t
    categories += [
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==0)","ljets_ge4j_3t_ttZ_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==1)","ljets_ge4j_3t_ttH_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==2)","ljets_ge4j_3t_tthf_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==3)","ljets_ge4j_3t_ttcc_node",""),
        ("((N_Jets>=4&&N_BTagsM==3)&&DNNPredictedClass_ge4j_3t==4)","ljets_ge4j_3t_ttlf_node",""),
        ]
    discrs += [
        "DNNOutput_ge4j_3t_node_ttZ",
        "DNNOutput_ge4j_3t_node_ttH",
        "DNNOutput_ge4j_3t_node_tthf",
        "DNNOutput_ge4j_3t_node_ttcc",
        "DNNOutput_ge4j_3t_node_ttlf",
        ]
    nhistobins += [10, 10, 10, 5, 5]
    minxvals += [0.25, 0.25, 0.25, 0.25, 0.25]
    maxxvals += [0.7, 0.55, 0.65, 0.45, 0.6]



    plotPreselections = [c[0] for c in categories]
    binlabels =         [c[1] for c in categories]

    DNNPlots = []
    for discr, sel, label, nbins, minx, maxx in zip(discrs,plotPreselections,binlabels,nhistobins,minxvals,maxxvals):
        DNNPlots.append(
            plotClasses.Plot(
                ROOT.TH1F(discrname+"_"+label,"final discriminator ("+label+")",nbins,minx,maxx),
                discr,sel,label))

    data.categories += categories
    data.discrs     += discrs
    data.nhistobins += nhistobins
    data.minxvals   += minxvals
    data.maxxvals   += maxxvals
    
    data.plotPreselections  += plotPreselections
    data.binlabels          += binlabels

    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = None):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t()
    discriminatorPlots += plots_le5j_ge3t()
    discriminatorPlots += plots_5j_ge3t()
    discriminatorPlots += plots_ge4j_ge3t()
    discriminatorPlots += plots_4j_ge3t()
    discriminatorPlots += plots_ge4j_3t()
    discriminatorPlots += plots_ge6j_ge3t()
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots