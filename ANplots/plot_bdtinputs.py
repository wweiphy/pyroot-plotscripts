from plotconfig import *
sys.path.insert(0, '../limittools')
from limittools import renameHistos

#path='/nfs/dust/cms/user/hmildner/treesMEM0126/'
name='bdtInputPlots'
sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

# selections for categories
sel1="((N_TightLeptons==1)*(N_LooseLeptons==1)*(N_BTagsM>=2)*(N_Jets>=4))" # l+jets channel
name1="1lge4ge2"

s43="(N_Jets==4&&N_BTagsM==3)"
s44="(N_Jets==4&&N_BTagsM>=4)"
s53="(N_Jets==5&&N_BTagsM==3)"
s54="(N_Jets==5&&N_BTagsM>=4)"
s62="(N_Jets>=6&&N_BTagsM==2)"
s63="(N_Jets>=6&&N_BTagsM==3)"
s64="(N_Jets>=6&&N_BTagsM>=4)"


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples=samplesControlPlots
samples_data=samples_data_controlplots
systsamples=[]
for sample in samples:
  for sysname,sysfilename in zip(othersystnames,othersystfilenames):
    thisnewsel=sample.selection
    if sysname=="_CMS_ttH_PSscaleUp":
      thisnewsel=thisnewsel.replace('*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS','*(0.003106675*(N_GenTopHad==1 && N_GenTopLep==1)+0.002512789*(N_GenTopLep==2 && N_GenTopHad==0)+0.0171752783*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS')
      print "weights for scaleUp sample ", thisnewsel
    if sysname=="_CMS_ttH_PSscaleDown":
      thisnewsel=thisnewsel.replace('*(0.000919641*(N_GenTopHad==1 && N_GenTopLep==1)+0.000707116*(N_GenTopLep==2 && N_GenTopHad==0)+0.0084896859*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS','*(0.0051290727*(N_GenTopHad==1 && N_GenTopLep==1)+0.0025191514*(N_GenTopLep==2 && N_GenTopHad==0)+0.0168392844*(N_GenTopHad==2 && N_GenTopLep==0))/Weight_XS')
      print "weights for scaleDown sample ", thisnewsel
    systsamples.append(Sample(sample.name+sysname,sample.color,sample.path.replace("nominal",sysfilename),thisnewsel,sample.nick+sysname))
    
allsamples=samples+systsamples
allsystnames=weightsystnames+othersystnames

allplots=[]
TwoDimPlots=[]
plots=[]


# weights_Final_43_MEMBDTv2.xml
label="1 lepton, 4 jets, 3 b-tags"
plots43=[
	Plot(ROOT.TH1F("s43_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_HT","HT",20,0,1000),"BDT_common5_input_HT","(N_Jets==4&&N_BTagsM==3)",label),
        #Plot(ROOT.TH1F("s43_MEM_transformed","MEM discriminator",24,0,1.2),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_third_highest_btag","third highest btag",22,0.79,1),"BDT_common5_input_third_highest_btag","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_Evt_CSV_Average","avg CSV (jets)",20,0.5,0.9),"Evt_CSV_Average","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_M3","M3",30,0,600),"BDT_common5_input_M3","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",20,0,1000),"BDT_common5_input_all_sum_pt_with_met","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_h1","H_{1}",30,-0.2,0.4),"BDT_common5_input_h1","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",35,0,3.5),"BDT_common5_input_dr_between_lep_and_closest_jet","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_first_jet_pt","jet 1 p_{T}",50,0,500),"BDT_common5_input_first_jet_pt","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",20,0,400),"BDT_common5_input_closest_tagged_dijet_mass","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_blr","B-tagging likelihood ratio",30,-3,8),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM==3)',label),
	Plot(ROOT.TH1F("s43_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",20,0,4),"BDT_common5_input_avg_dr_tagged_jets","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_min_dr_tagged_jets","min #Delta R(tag,tag)",30,0.3,3.5),"BDT_common5_input_min_dr_tagged_jets","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_h3","H_{3}",30,-0.2,0.9),"BDT_common5_input_h3","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_second_jet_pt","jet 2 p_{T}",40,0,300),"BDT_common5_input_second_jet_pt","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",40,0,200),"BDT_common5_input_fourth_jet_pt","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_maxeta_tag_tag","max #Delta #eta(tag,tag)",20,0.,1.6),"BDT_common5_input_maxeta_tag_tag","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",20,0.,1.6),"BDT_common5_input_maxeta_jet_tag","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",20,0,3),"Evt_Deta_JetsAverage","(N_Jets==4&&N_BTagsM==3)",label),
        Plot(ROOT.TH1F("s43_BDT_common5_input_third_jet_pt","jet 1 p_{T}",40,0,500),"BDT_common5_input_third_jet_pt","(N_Jets==4&&N_BTagsM==3)",label),
        ]

        
label="1 lepton, 4 jets, 4 b-tags"
thiscatsel="(N_Jets==4&&N_BTagsM>=4)"
catsuf="s44"
# weights_Final_44_MEMBDTv2.xml
plots44=[
  #Plot(ROOT.TH1F("s44_MEM_transformed","MEM discriminator",6,0,1.2),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)","(N_Jets==4&&N_BTagsM>=4)",label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",6,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",7,30,100),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_first_jet_pt","jet 1 p_{T}",15,0,400),"BDT_common5_input_first_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",15,0,3),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth-highest CSV",11,0.8,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_M3","M3",15,0,800),"BDT_common5_input_M3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",10,-4,12),"Evt_blr_ETH_transformed",'(N_Jets==4&&N_BTagsM>=4)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1.6,3.6),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",10,0,1000),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",15,0,1000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",15,-0.2,0.4),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third-highest CSV",11,0.8,1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",15,-0.2,1.0),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_Mlb","mass(lepton,closest tag)",15,0,250),"BDT_common5_input_Mlb",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_highest_btag","second-highest CSV",11,0.8,1),"BDT_common5_input_second_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta(jet,jet)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h0","H_{0}",15,0.2,0.4),"BDT_common5_input_h0",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,250),"BDT_common5_input_second_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dev_from_avg_disc_btags","dev from avg CSV (tags)",15,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",15,-0.2,0.4),"BDT_common5_input_h2",thiscatsel,label),
      ]

label="1 lepton, 5 jets, 3 b-tags"
thiscatsel="(N_Jets==5&&N_BTagsM==3)"
catsuf="s53"
    # weights_Final_53_MEMBDTv2.xml
plots53=[
	#Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",20,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",20,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum p_{T} (lepton,jet,met)",30,0,1500),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",22,.8,1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest CSV",22,-.1,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_CSV_Average","avg CSV",25,0.5,0.9),"Evt_CSV_Average",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",20,-2,10),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM==3)',label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",30,0.5,3.5),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",25,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",25,0,1000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",25,0,2.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV tagged",25,0.8,1.05),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",25,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",25,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",25,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_jet_pt","jet 2 p_{T}",20,0,300),"BDT_common5_input_second_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",20,0,0.3),"BDT_common5_input_h2",thiscatsel,label),
]

label="1 lepton, 5 jets, #geq4 b-tags"
thiscatsel="(N_Jets==5&&N_BTagsM>=4)"
catsuf="s54"

# weights_Final_54_MEMBDTv2.xml
plots54=[
	#Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",7,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",10,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",15,0,150),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",12,0,1200),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",15,-.15,0.3),"BDT_common5_input_h2",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",10,1,4),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",10,-2,12),"Evt_blr_ETH_transformed",'(N_Jets==5&&N_BTagsM>=4)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",10,0,200),"BDT_common5_input_closest_tagged_dijet_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",10,80,180),"BDT_common5_input_tagged_dijet_mass_closest_to_125",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",10,0,1000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",10,-.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_best_higgs_mass","best higgs mass",10,0,400),"BDT_common5_input_best_higgs_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",10,.8,1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",10,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",10,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest CSV",10,0.79,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",10,-.1,.91),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",9,0,0.3),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",15,0,1500),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",12,0,2.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_highest_btag","second highest btag",10,.8,1),"BDT_common5_input_second_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h0","H_{0}",10,0.2,1.0),"BDT_common5_input_h0",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_CSV_Average","avg CSV",10,0.5,1),"Evt_CSV_Average",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_jet_pt","jet 3 p_{T}",15,0,200),"BDT_common5_input_third_jet_pt",thiscatsel,label),
   ]
label="1 lepton, #geq6 jets, 2 b-tags"
thiscatsel="(N_Jets>=6&&N_BTagsM==2)"
catsuf="s62"
# /nfs/dust/cms/user/kelmorab/newTrain/3makeHistosAndCards/weights/CommonWeights/weights_Final_62_v5_OldVars.xml
plots62=[
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",27,-0.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,0,5),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",22,0,1.1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",20,0,1400),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_Mlb","mass(lepton,closest tag)",20,0,250),"BDT_common5_input_Mlb",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",20,-.1,.91),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest CSV",20,-.1,.9),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",20,-5,3),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==2)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",30,0.5,3.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.04),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",30,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",30,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",30,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",30,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",30,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",30,200,1300),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",30,-.15,0.3),"BDT_common5_input_h2",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",30,0,0.3),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_CSV_Average","avg CSV",25,0.2,0.65),"Evt_CSV_Average",thiscatsel,label),
]


label="1 lepton, #geq6 jets, 3 b-tags"
thiscatsel="(N_Jets>=6&&N_BTagsM==3)"
catsuf="s63"
# weights_Final_63_MEMBDTv2.xml
plots63=[
	#Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",20,0.,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","#Delta R (lepton,jet)",16,0,3.2),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dev_from_avg_disc_btags","dev from ave CSV (tags)",25,0,0.008),"BDT_common5_input_dev_from_avg_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta jets",25,0,2.5),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",25,0,2000),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth-highest b-tag",18,0,0.9),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_btag_disc_btags","avg CSV (tags)",30,.8,1.05),"BDT_common5_input_avg_btag_disc_btags",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",28,0.5,3.9),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,160),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",30,0,300),"BDT_common5_input_tagged_dijet_mass_closest_to_125",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h2","H_{2}",20,-.1,.3),"BDT_common5_input_h2",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth-highest CSV",20,-.1,.8),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",20,-2,8),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM==3)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_min_dr_tagged_jets","min #Delta R (tag,tag)",17,0,3.4),"BDT_common5_input_min_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dEta_fn","#sqrt{#Delta #eta(t^{lep}, bb) #times #Delta #eta(t^{had}, bb)}",20,0,5),"BDT_common5_input_dEta_fn",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h1","H_{1}",27,-.2,.34),"BDT_common5_input_h1",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third highest CSV",22,0.79,1.1),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.1),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
]
   
label="1 lepton, #geq6 jets, #geq4 b-tags"
thiscatsel="(N_Jets>=6&&N_BTagsM>=4)"
catsuf="s64"
# weights_Final_64_MEMBDTv2.xml
plots64=[
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_highest_btag","third-highest CSV",16,.8,1.05),"BDT_common5_input_third_highest_btag",thiscatsel,label),
        #Plot(ROOT.TH1F(catsuf+"_MEM_transformed","MEM discriminator",10,0,1),"(MEM_p>=0.0)*(MEM_p_sig/(MEM_p_sig+0.15*MEM_p_bkg))+(MEM_p<0.0)*(0.01)",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_Evt_Deta_JetsAverage","avg #Delta #eta (jet,jet)",14,0,2.8),"Evt_Deta_JetsAverage",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_sphericity","sphericity",20,0,1),"BDT_common5_input_sphericity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_jet_pt","jet 4 p_{T}",20,0,200),"BDT_common5_input_fourth_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_aplanarity","aplanarity",20,0,0.4),"BDT_common5_input_aplanarity",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_M3","M3",20,0,1000),"BDT_common5_input_M3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_third_jet_pt","jet 3 p_{T}",20,0,250),"BDT_common5_input_third_jet_pt",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_blr","B-tagging likelihood ratio",14,0,12),"Evt_blr_ETH_transformed",'(N_Jets>=6&&N_BTagsM>=4)',label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_avg_dr_tagged_jets","avg #Delta R (tag,tag)",25,1,3.5),"BDT_common5_input_avg_dr_tagged_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_best_higgs_mass","best higgs mass",30,0,600),"BDT_common5_input_best_higgs_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_tagged_dijet_mass_closest_to_125","tagged dijet mass closest to 125",17,40,210),"BDT_common5_input_tagged_dijet_mass_closest_to_125",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fourth_highest_btag","fourth highest btag",22,.8,1),"BDT_common5_input_fourth_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_closest_tagged_dijet_mass","closest tagged dijet mass",25,0,250),"BDT_common5_input_closest_tagged_dijet_mass",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_fifth_highest_CSV","fifth highest CSV",22,-.1,1),"BDT_common5_input_fifth_highest_CSV",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_second_highest_btag","second highest btag",22,.8,1),"BDT_common5_input_second_highest_btag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_dr_between_lep_and_closest_jet","min #Delta R (lepton,jet)",25,0,2.5),"BDT_common5_input_dr_between_lep_and_closest_jet",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_h3","H_{3}",20,0,1),"BDT_common5_input_h3",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_HT","HT",10,0,2000),"BDT_common5_input_HT",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_all_sum_pt_with_met","#sum (lepton pt,jet pt,met)",10,200,2000),"BDT_common5_input_all_sum_pt_with_met",thiscatsel,label),
	Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_pt_all_jets_over_E_all_jets","(#sum jet p_{T})/(#sum jet E))",10,0.2,1.2),"BDT_common5_input_pt_all_jets_over_E_all_jets",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_invariant_mass_of_everything","mass(jets,lepton,MET)",10,400,1600),"BDT_common5_input_invariant_mass_of_everything",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_tag","max #Delta #eta(jet,tag)",14,0.2,1.6),"BDT_common5_input_maxeta_jet_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_tag_tag","max #Delta #eta (tag,tag)",15,0,1.5),"BDT_common5_input_maxeta_tag_tag",thiscatsel,label),
        Plot(ROOT.TH1F(catsuf+"_BDT_common5_input_maxeta_jet_jet","max #Delta #eta (jet,jet)",15,0,1.5),"BDT_common5_input_maxeta_jet_jet",thiscatsel,label),
]

listOf1DPlotLists=[plots64,plots63,plots62,plots54,plots53,plots44,plots43]
#TwoDimPlots=[]
#for plotlist in listOf1DPlotLists:
  ##print plotlist
  #for ipl1, plot1 in enumerate(plotlist):
    #for plot2 in plotlist:
      #newName=plot1.name+"VS"+plot2.name
      #newTitle=plot1.histo.GetTitle()+" VS "+plot2.histo.GetTitle()
      #bins1=plot1.histo.GetNbinsX()
      #minX1=plot1.histo.GetXaxis().GetXmin()
      #maxX1=plot1.histo.GetXaxis().GetXmax()
      #bins2=plot2.histo.GetNbinsX()
      #minX2=plot2.histo.GetXaxis().GetXmin()
      #maxX2=plot2.histo.GetXaxis().GetXmax()
      ##newvarexp=plot2.variable+":"+plot1.variable
      #newsel=plot1.selection
      #newlabel=plot1.label
      #TwoDimPlots+=[TwoDimPlot(ROOT.TH2F(newName,newTitle+";"+plot1.histo.GetTitle()+";"+plot2.histo.GetTitle(),bins1,minX1,maxX1,bins2,minX2,maxX2),plot1.variable,plot2.variable,newsel,newlabel)]

OneDimplots=[]
for plotlist in listOf1DPlotLists:
  OneDimplots+=plotlist
#allplots=OneDimplots+TwoDimPlots

# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,OneDimplots,samples+samples_data+systsamples,[''],['1.'],weightsystnames, systweights)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,OneDimplots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,OneDimplots,1)
if not os.path.exists(outputpath[:-4]+'_syst.root') or not askYesNo('reuse systematic histofile?'):
    renameHistos(outputpath,outputpath[:-4]+'_syst.root',allsystnames)

lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],OneDimplots,errorSystnames)
lllforPS=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],OneDimplots,PSSystnames)
#lllforPU=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],OneDimplots,PUSystnames)

labels=[plot.label for plot in OneDimplots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,[[lll,3354,ROOT.kGray+1,True],[lllforPS,3545,ROOT.kYellow,False]],False,labels)

#listOfHistoListsDataForGenerators=createHistoLists_fromSuperHistoFile(outputpath,samples_data,allplots,1,[""],True)
#listOfHistoListsGenerators=createHistoLists_fromSuperHistoFile(outputpath,samplesGenerators,allplots,1,[""],True)
#print "genData"
#print listOfHistoListsDataForGenerators
#print "Generators"
#print listOfHistoListsGenerators

##TlistOfHistoListsDataForGenerators=transposeLOL(listOfHistoListsDataForGenerators)
##TlistOfHistoListsGenerators=transposeLOL(listOfHistoListsGenerators)
##print TlistOfHistoListsDataForGenerators
##print TlistOfHistoListsGenerators

#listOfComparisonLists=[]
#for histolistData, histoListGenerators in zip(listOfHistoListsDataForGenerators, listOfHistoListsGenerators):
  #thishisto=histolistData[0].Clone()
  #thishisto.Add(histolistData[1])
  #thislist=[thishisto]
  #for histo in histoListGenerators:
    #thislist.append(histo)
  #listOfComparisonLists.append(thislist)
#print listOfComparisonLists
##raw_input()
#labels=[plot.label for plot in allplots]

#samplesForComparison=[Sample('data',ROOT.kBlack,path_76x+'/mu_*/*nominal*.root','','SingleMu'),]+samplesGenerators
#writeListOfHistoLists(listOfComparisonLists,samplesForComparison,labels,"comparisonsBDT",True,False,False,'histoE',False,False,True,True)


##listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
#listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
#lll=createLLL_fromSuperHistoFileSyst(outputpath[:-4]+'_syst.root',samples[1:],plots,allsystnames)
#labels=[plot.label for plot in plots]
#lolT=transposeLOL(listOfHistoLists)
#plotDataMCanWsyst(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',lll,True,labels)
