
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


memexp = ""


def plots_ge4j_ge4t(data = None):
    label = "\geq 4 jets, \geq 4 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM>=4)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_CSV_0","Jet CSV[0]",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_ge4t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots



def plots_ge4j_3t(data = None):
    label = "\geq 4 jets, 3 b-tags"
    selection = "(N_Jets>=4&&N_BTagsM==3)&&(1.)"

    plots = [
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_HT_tag","H_{T}(tags)",30,100.0,900.0),"BDT_common5_input_HT_tag",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",30,0.0,400.0),"BDT_common5_input_closest_tagged_dijet_mass",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_dev_from_avg_disc_btags","deviation from average btag value for tagged jets",30,0.0,0.13),"BDT_common5_input_dev_from_avg_disc_btags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_max_dR_jj","max #DeltaR(jet jet)",30,2.0,5.0),"BDT_common5_input_max_dR_jj",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_sphericity_jets","sphericity of jets",30,0.0,1.0),"BDT_common5_input_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_sphericity_tags","sphericity of tagged jets",30,0.0,1.0),"BDT_common5_input_sphericity_tags",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_BDT_common5_input_transverse_sphericity_jets","transverse sphericity of jets",30,0.0,1.0),"BDT_common5_input_transverse_sphericity_jets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_CSV_1","second highest btag value",30,0.3,1.0),"CSV[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Average","average btag value",30,0.3,1.0),"Evt_CSV_Average",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Average_Tagged","average btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Average_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Min","min btag value",30,0.0,0.6),"Evt_CSV_Min",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_CSV_Min_Tagged","min btag value of tagged jets",30,0.3,1.0),"Evt_CSV_Min_Tagged",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Deta_TaggedJetsAverage","average #Delta#eta(tags)",30,0.0,3.0),"Evt_Deta_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRLeptonTaggedJet","min #DeltaR (lep tag)",30,0.3,3.0),"Evt_Dr_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_MinDeltaRTaggedJets","min #DeltaR(tag tag)",30,0.3,3.5),"Evt_Dr_MinDeltaRTaggedJets",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_Dr_TaggedJetsAverage","average #DeltaR(tags)",30,0.5,3.5),"Evt_Dr_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_HT","H_{T}",30,200.0,1700.0),"Evt_HT",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_JetPtOverJetE","p_{T}(jets)/E(jets)",30,0.2,1.0),"Evt_JetPtOverJetE",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M2_TaggedJetsAverage","average M_{2}(tags)",30,50.0,550.0),"Evt_M2_TaggedJetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_JetsAverage","average M(jets)",30,2.0,20.0),"Evt_M_JetsAverage",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_M_MinDeltaRLeptonTaggedJet","mass of min #DeltaR(lep tag)",30,20.0,300.0),"Evt_M_MinDeltaRLeptonTaggedJet",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_blr_ETH","btag likelihood ratio",30,0.0,1.0),"Evt_blr_ETH",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Evt_blr_ETH_transformed","transformed btag likelihood ratio",30,-6.0,12.0),"Evt_blr_ETH_transformed",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_CSV_0","Jet CSV[0]",30,0.0,1.0),"Jet_CSV[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_CSV_3","Jet CSV[3]",30,0.0,1.0),"Jet_CSV[3]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_0","p_{T} of leading jet",30,0.0,600.0),"Jet_Pt[0]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_1","p_{T} of subleading jet",30,0.0,500.0),"Jet_Pt[1]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_Jet_Pt_2","p_{T} of third jet",30,30.0,300.0),"Jet_Pt[2]",selection,label),
        plotClasses.Plot(ROOT.TH1D("ge4j_3t_N_BTagsT","number of btags (tight)",6,-0.5,5.5),"N_BTagsT",selection,label),
        ]

    if data:
        add_data_plots(plots=plots,data=data)
    return plots




def plots_dnn(data, discrname):

    ndefaultbins = 1
    category_dict = {}
    this_dict = {}




    # plots for ge4j_ge4t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.18,
				#0.22,
				0.26,
				#0.3,
				0.34,
				#0.38,
				0.42,
				#0.46,
				0.5,
				0.54,
				0.58,
				0.62,
				0.66,
				0.7,
				0.74,
				0.76
				]
    this_dict["ljets_ge4j_ge4t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttb_bb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttb_bb"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1836,
				#0.2164,
				0.2493,
				#0.2821,
				0.315,
				#0.3479,
				0.3807,
				#0.4136,
				0.4464,
				0.4793,
				0.5121,
				0.545,
				0.5779,
				0.6107,
				0.6436,
				0.66
				]
    this_dict["ljets_ge4j_ge4t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1861,
				#0.2139,
				0.2418,
				#0.2696,
				0.2975,
				#0.3254,
				0.3532,
				#0.3811,
				0.4089,
				0.4368,
				0.4646,
				0.4925,
				0.5204,
				0.5482,
				0.5761,
				0.59
				]
    this_dict["ljets_ge4j_ge4t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.45
    this_dict["ljets_ge4j_ge4t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_ge4t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, \geq 4 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.65
    this_dict["ljets_ge4j_ge4t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    


    # plots for ge4j_3t

    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_ttH_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttH"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1775,
				#0.2225,
				0.2675,
				#0.3125,
				0.3575,
				#0.4025,
				0.4475,
				#0.4925,
				0.5375,
				0.5825,
				0.6275,
				0.6725,
				0.7175,
				0.7625,
				0.8075,
				0.83
				]
    this_dict["ljets_ge4j_3t_ttH_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttb_bb_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttb_bb"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.1843,
				#0.2157,
				0.2471,
				#0.2786,
				0.31,
				#0.3414,
				0.3729,
				#0.4043,
				0.4357,
				0.4671,
				0.4986,
				0.53,
				0.5614,
				0.5929,
				0.6243,
				0.64
				]
    this_dict["ljets_ge4j_3t_ttb_bb_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_tt2b_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_tt2b"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["bin_edges"] = [ 
				0.175,
				#0.225,
				0.275,
				#0.325,
				0.375,
				#0.425,
				0.475,
				#0.525,
				0.575,
				0.625,
				0.675,
				0.725,
				0.775,
				0.825,
				0.875,
				0.9
				]
    this_dict["ljets_ge4j_3t_tt2b_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttcc_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttcc"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.45
    this_dict["ljets_ge4j_3t_ttcc_node"] = deepcopy(category_dict)
    category_dict.clear()
    
    category_dict["category"] = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttlf_node","")
    category_dict["discr"] = "DNNOutput_ge4j_3t_node_ttlf"
    category_dict["catlabel"] = "\geq 4 jets, 3 b-tags"
    category_dict["nhistobins"] = ndefaultbins
    category_dict["minxval"] = 0.2
    category_dict["maxxval"] = 0.69
    this_dict["ljets_ge4j_3t_ttlf_node"] = deepcopy(category_dict)
    category_dict.clear()
    

    for l in this_dict:
        this_dict[l]["histoname"] = discrname+"_"+l
        this_dict[l]["histotitle"] = "final discriminator ({})".format(l)
        this_dict[l]["plotPreselections"] = this_dict[l]["category"][0]

    DNNPlots = init_plots(dictionary = this_dict, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_ge4j_ge4t(data)
    discriminatorPlots += plots_ge4j_3t(data)
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(dictionary, data = None):
    plots = [] #init list of plotClasses objects to return
    for label in dictionary:
        subdict     = dictionary[label] #for easy access
        discr       = subdict["discr"] # load discriminator name
        sel         = subdict["plotPreselections"] # load selection
        histoname   = subdict["histoname"] # load histogram name
        histotitle  = subdict["histotitle"] # load histogram title
        catlabel    = subdict["catlabel"] # category label

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if "bin_edges" in subdict:
            bins  = array("f", subdict["bin_edges"])
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            subdict["nhistobins"] = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname,histotitle,nbins,bins),
                    discr,sel,catlabel))

        elif "minxval" in subdict and "maxxval" in subdict:
            nbins = subdict["nhistobins"]
            xmax  = subdict["maxxval"]
            xmin  = subdict["minxval"]
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(histoname, histotitle,nbins,xmin, xmax),
                    discr,sel,catlabel))

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    