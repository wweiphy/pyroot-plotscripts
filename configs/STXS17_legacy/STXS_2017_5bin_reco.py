
import sys
import os
filedir = os.path.dirname(os.path.realpath(__file__))
pyrootdir = os.path.dirname(filedir)
basedir = os.path.dirname(pyrootdir)
sys.path.append(pyrootdir)
sys.path.append(basedir)

import util.tools.plotClasses as plotClasses
import util.variableHistoInterface as vhi
import ROOT
from array import array
from copy import deepcopy


memexp = ""



def plots_dnn(data, discrname):

    ndefaultbins = 7
    interfaces = []



    # plots for ge4j_ge4t_ttH
    interf_ljets_ge4j_ge4t_inclTTH_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_inclTTH_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))")
    interf_ljets_ge4j_ge4t_inclTTH_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0))","ljets_ge4j_ge4t_inclTTH_node","")
    interf_ljets_ge4j_ge4t_inclTTH_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_inclTTH_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_inclTTH_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_inclTTH_node)

    interf_ljets_ge4j_ge4t_noReco_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_noReco_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&(Reco_ttH_h_pt<=0))")
    interf_ljets_ge4j_ge4t_noReco_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&(Reco_ttH_h_pt<0))","ljets_ge4j_ge4t_noReco_node","")
    interf_ljets_ge4j_ge4t_noReco_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_noReco_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_noReco_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_noReco_node)

    interf_ljets_ge4j_ge4t_ttH_1_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_ttH_1_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>0)&&(Reco_ttH_h_pt<60)))")
    interf_ljets_ge4j_ge4t_ttH_1_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=0)&&(Reco_ttH_h_pt<60)))","ljets_ge4j_ge4t_ttH_1_node","")
    interf_ljets_ge4j_ge4t_ttH_1_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_ttH_1_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_ttH_1_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_1_node)
    
    interf_ljets_ge4j_ge4t_ttH_2_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_ttH_2_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=60)&&(Reco_ttH_h_pt<120)))")
    interf_ljets_ge4j_ge4t_ttH_2_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=60)&&(Reco_ttH_h_pt<120)))","ljets_ge4j_ge4t_ttH_2_node","")
    interf_ljets_ge4j_ge4t_ttH_2_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_ttH_2_node.maxxval = 0.68
    interf_ljets_ge4j_ge4t_ttH_2_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_2_node)
    
    interf_ljets_ge4j_ge4t_ttH_3_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_ttH_3_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=120)&&(Reco_ttH_h_pt<200)))")
    interf_ljets_ge4j_ge4t_ttH_3_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=120)&&(Reco_ttH_h_pt<200)))","ljets_ge4j_ge4t_ttH_3_node","")
    interf_ljets_ge4j_ge4t_ttH_3_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_ttH_3_node.maxxval = 0.67
    interf_ljets_ge4j_ge4t_ttH_3_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_3_node)
    
    interf_ljets_ge4j_ge4t_ttH_4_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_ttH_4_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=200)&&(Reco_ttH_h_pt<300)))")
    interf_ljets_ge4j_ge4t_ttH_4_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=200)&&(Reco_ttH_h_pt<300)))","ljets_ge4j_ge4t_ttH_4_node","")
    interf_ljets_ge4j_ge4t_ttH_4_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_ttH_4_node.maxxval = 0.7
    interf_ljets_ge4j_ge4t_ttH_4_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_4_node)
    
    interf_ljets_ge4j_ge4t_ttH_5_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttH",
                                            label          = "ljets_ge4j_ge4t_ttH_5_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=300)))")
    interf_ljets_ge4j_ge4t_ttH_5_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==0)&&((Reco_ttH_h_pt>=300)))","ljets_ge4j_ge4t_ttH_5_node","")
    interf_ljets_ge4j_ge4t_ttH_5_node.minxval = 0.24
    interf_ljets_ge4j_ge4t_ttH_5_node.maxxval = 0.72
    interf_ljets_ge4j_ge4t_ttH_5_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_5_node)
    
    interf_ljets_ge4j_ge4t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttb_bb",
                                            label          = "ljets_ge4j_ge4t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))")
    interf_ljets_ge4j_ge4t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==1))","ljets_ge4j_ge4t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_ge4t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_ttH_ttb_bb_node.maxxval = 0.72
    interf_ljets_ge4j_ge4t_ttH_ttb_bb_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_ttb_bb_node)
    
    interf_ljets_ge4j_ge4t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_tt2b",
                                            label          = "ljets_ge4j_ge4t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))")
    interf_ljets_ge4j_ge4t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==2))","ljets_ge4j_ge4t_ttH_tt2b_node","")
    interf_ljets_ge4j_ge4t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_ttH_tt2b_node.maxxval = 0.66
    interf_ljets_ge4j_ge4t_ttH_tt2b_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_tt2b_node)
    
    interf_ljets_ge4j_ge4t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttcc",
                                            label          = "ljets_ge4j_ge4t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))")
    interf_ljets_ge4j_ge4t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==3))","ljets_ge4j_ge4t_ttH_ttcc_node","")
    interf_ljets_ge4j_ge4t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_ttH_ttcc_node.maxxval = 0.52
    interf_ljets_ge4j_ge4t_ttH_ttcc_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_ttcc_node)
    
    interf_ljets_ge4j_ge4t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_ge4t_node_ttlf",
                                            label          = "ljets_ge4j_ge4t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))")
    interf_ljets_ge4j_ge4t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM>=4)&&(1.)&&(DNNPredictedClass_ge4j_ge4t==4))","ljets_ge4j_ge4t_ttH_ttlf_node","")
    interf_ljets_ge4j_ge4t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_ge4t_ttH_ttlf_node.maxxval = 0.69
    interf_ljets_ge4j_ge4t_ttH_ttlf_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_ge4t_ttH_ttlf_node)
    


    # plots for ge4j_3t_ttH

    interf_ljets_ge4j_3t_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttH",
                                            label          = "ljets_ge4j_3t_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))")
    interf_ljets_ge4j_3t_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==0))","ljets_ge4j_3t_node","")
    interf_ljets_ge4j_3t_node.minxval = 0.2
    interf_ljets_ge4j_3t_node.maxxval = 0.65
    interf_ljets_ge4j_3t_node.nhistobins = ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_node)
    
    interf_ljets_ge4j_3t_ttH_ttb_bb_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttb_bb",
                                            label          = "ljets_ge4j_3t_ttH_ttb_bb_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))")
    interf_ljets_ge4j_3t_ttH_ttb_bb_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==1))","ljets_ge4j_3t_ttH_ttb_bb_node","")
    interf_ljets_ge4j_3t_ttH_ttb_bb_node.minxval = 0.2
    interf_ljets_ge4j_3t_ttH_ttb_bb_node.maxxval = 0.71
    interf_ljets_ge4j_3t_ttH_ttb_bb_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_ttb_bb_node)
    
    interf_ljets_ge4j_3t_ttH_tt2b_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_tt2b",
                                            label          = "ljets_ge4j_3t_ttH_tt2b_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))")
    interf_ljets_ge4j_3t_ttH_tt2b_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==2))","ljets_ge4j_3t_ttH_tt2b_node","")
    interf_ljets_ge4j_3t_ttH_tt2b_node.minxval = 0.2
    interf_ljets_ge4j_3t_ttH_tt2b_node.maxxval = 0.81
    interf_ljets_ge4j_3t_ttH_tt2b_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_tt2b_node)
    
    interf_ljets_ge4j_3t_ttH_ttcc_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttcc",
                                            label          = "ljets_ge4j_3t_ttH_ttcc_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))")
    interf_ljets_ge4j_3t_ttH_ttcc_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==3))","ljets_ge4j_3t_ttH_ttcc_node","")
    interf_ljets_ge4j_3t_ttH_ttcc_node.minxval = 0.2
    interf_ljets_ge4j_3t_ttH_ttcc_node.maxxval = 0.48
    interf_ljets_ge4j_3t_ttH_ttcc_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_ttcc_node)
    
    interf_ljets_ge4j_3t_ttH_ttlf_node = vhi.variableHistoInterface(variable_name  = "DNNOutput_ge4j_3t_node_ttlf",
                                            label          = "ljets_ge4j_3t_ttH_ttlf_node",
                                            selection      = "((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))")
    interf_ljets_ge4j_3t_ttH_ttlf_node.category = ("((N_Jets>=4&&N_BTagsM==3)&&(1.)&&(DNNPredictedClass_ge4j_3t==4))","ljets_ge4j_3t_ttH_ttlf_node","")
    interf_ljets_ge4j_3t_ttH_ttlf_node.minxval = 0.2
    interf_ljets_ge4j_3t_ttH_ttlf_node.maxxval = 0.7
    interf_ljets_ge4j_3t_ttH_ttlf_node.nhistobins = 1#ndefaultbins
    interfaces.append(interf_ljets_ge4j_3t_ttH_ttlf_node)
    

    for interf in interfaces:
        l = interf.label
        interf.histoname = discrname+"_"+l
        interf.histotitle = "final discriminator ({})".format(l)
        interf.selection = interf.category[0]

    DNNPlots = init_plots(interfaces = interfaces, data = data)
    return DNNPlots


def getDiscriminatorPlots(data = None, discrname = ''):
    discriminatorPlots = []
    discriminatorPlots += plots_dnn(data, discrname)

    return discriminatorPlots


def init_plots(interfaces, data = None):
    plots = [] #init list of plotClasses objects to return
    dictionary = {}
    for interf in interfaces:

        # check if initialization uses bin edges or min/max vals
        # if 'subdict' contains the keyword 'bin_edges', an array
        # of type float is created from the corresponding python list.
        # Else, the min/maxvals are used 
        if not interf.bin_edges is None:
            bins  = array("f", interf.bin_edges)
            nbins = len(bins)-1 # last bin edge in array is overflow bin => subtract for nbins
            interf.nhistobins = nbins # update number of bins
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,bins),
                    interf.varname,interf.selection,interf.category_label))

        elif not (interf.minxval is None or interf.maxxval is None):
            nbins = interf.nhistobins
            xmax  = interf.maxxval
            xmin  = interf.minxval
            plots.append(
                plotClasses.Plot(
                    ROOT.TH1F(interf.histoname,interf.histotitle,nbins,xmin, xmax),
                    interf.varname,interf.selection,interf.category_label))
        else:
            print("FATAL ERROR: Unable to load bin edges or min/max values for histogram!")
            print(interf)
            raise ValueError
        dictionary[interf.label] = interf.getDictionary()

    if not data is None:
        data.categories.update(dictionary)

    return plots

def add_data_plots(plots, data):
    plotnames = []
    for plot in plots:
        plotnames.append(plot.name)
    data.datavariables.extend(plotnames)
    