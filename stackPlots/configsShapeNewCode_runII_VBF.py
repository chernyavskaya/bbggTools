
##################################################
##################################################
## Configuration parameters to run MakeShape.py ##
##################################################
##################################################

doBlind = True
doShape = False
doDataMCShape = False
doJetCR = False


useJsonWeighting=True

isPhoCR = False
addHiggs = False
addggHttH = False
hideData = False
addbbH = False
dyjets = False


doSignal = True
addData = True   ############NEW

hideStat = False

BTAG = 0.

#Luminosity to normalize backgrounds
flashggLumi = 1000.#pb
MCSF = 1.0
#List of datasets to be used (cross section information defined there)
#data_file = open("datasets/datasets80X_Moriond_onlyNRSM.json")
#data_file = open("datasets/datasets80X_newcode_Moriond_onlyNRSM_diphoton_Gjets.json")
#data_file = open("datasets/datasets80X_2017_nodata_hhbbgg.json")
#data_file = open("datasets/datasets80X_newcode_Moriond_onlyNRSM_diphoton_Gjets_hhbbgg.json")
#data_file = open("datasets/datasets_signal_2016_2017.json")
data_file = open("datasets/datasets_28_05_2020_VBFHH_2018.json")

#number of bins in histograms
nbin = 30
leadingPhoton_pt_Over_CMS_hgg_mass = "(leadingPhoton_pt/CMS_hgg_mass)"
subleadingPhoton_pt_Over_CMS_hgg_mass = "(subleadingPhoton_pt/CMS_hgg_mass)"
leadingJet_pt_Over_Mjj = "(leadingJet_pt/Mjj)"
subleadingJet_pt_Over_Mjj = "(subleadingJet_pt/Mjj)"
VBFleadingJet_pt_Over_VBFJet_mjj = "(VBFleadJet_pt/VBFJet_mjj)"
VBFsubleadingJet_pt_Over_VBFJet_mjj = "(VBFsubleadJet_pt/VBFJet_mjj)"

#leadingPhoton_pt_Over_CMS_hgg_mass = "leadingPhoton_pt_Over_CMS_hgg_mass"
#subleadingPhoton_pt_Over_CMS_hgg_mass = "subleadingPhoton_pt_Over_CMS_hgg_mass"
#leadingJet_pt_Over_Mjj = "leadingJet_pt_Over_Mjj"
#subleadingJet_pt_Over_Mjj = "subleadingJet_pt_Over_Mjj"

#year = "2017"
#lumi = 41500.#pb
#year = "2016+2017+2018"
year = "2018"
#lumi = 136790.#pb
lumi = 59000.#pb
#plots will be saved in dirName
prefix = ""
#dirSuffix = "18_02_2020_shape_MCbgbjets"
#dirSuffix = "18_02_2020_shape_MCbg"
dirSuffix = "28_05_2020_VBFHH_DataMC_2018"
dirPrefix = "plots/"
dirName = dirPrefix + dirSuffix
treename="tagsDumper/trees/"
#treename=""

#Location of root files for each invidivual samples. Name of the root files is defined in datasets/datasets(76).json
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/root_files/ntuples_2017data_20181023/'
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/root_files/ntuples_2017_20181210/'
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/root_files/ntuples_2016_20181210/'
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/outfiles/20181210_common_2017/'
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/outfiles/20181210_common_2016/'
filesDir = '/eos/user/n/nchernya/HHbbgg_ntuples/HHbbgg_preselection_ntuples/VBFHH_28_05_2020_2018_preselection/'
higgsoLocation=filesDir
bkgLocation=filesDir
dataLocation=filesDir
signalLocation=filesDir



#plots to be made
plots = []

plots.append(["ttHScore","ttHScore","ttHScore",40,0.26,1.])
plots.append(["MX", "MX", "#tilde{M}_{X} (GeV)", 40, 200, 1000])
plots.append(["PhotonIDMVA2", "customSubLeadingPhotonIDMVA", "SubLeading Photon Id MVA", nbin, -1, 1])
plots.append(["MVAOutputTransformed","MVAOutputTransformed","MVA Output Transformed",40,0.37,1.])
plots.append(["ttHScore","ttHScore","ttHScore",40,0.26,1.])
plots.append(["diPho_Mass", "CMS_hgg_mass", "m_{#gamma#gamma} [GeV]", 80, 100, 180])
plots.append(["Mjj", "Mjj", "m_{jj} (GeV)", 40, 70, 190])
plots.append(["MX", "MX", "#tilde{M}_{X} (GeV)", 40, 200, 1000])
plots.append(["CosTheta_gg", "absCosTheta_gg", "|Cos(#theta_{#gamma#gamma})|", nbin, 0, 1])
plots.append(["CosTheta_bb", "absCosTheta_bb", "|Cos(#theta_{bb})|", nbin, 0, 1])
plots.append(["costhetastar_cs", "absCosThetaStar_CS", "|cos#theta*|_{CS}", nbin, 0, 1])
plots.append(["diPhoton_pt_overM", "diphotonCandidatePtOverdiHiggsM", "p_{T}(#gamma#gamma)/M_{jj#gamma#gamma}", nbin, 0, 1] )
plots.append(["diJet_pt_overM", "dijetCandidatePtOverdiHiggsM", "p_{T}(jj)/M_{jj#gamma#gamma}", nbin, 0, 1] )
plots.append(["leadingJet_DeepFlavour", "leadingJet_DeepFlavour", "Deep Flavour leading jet", nbin, 0, 1])
plots.append(["subleadingJet_DeepFlavour", "subleadingJet_DeepFlavour", "Deep Flavour subleading jet", nbin, 0, 1])
plots.append(["sigmaMOverM", "sigmaMOverM", "#sigma_{m_{#gamma#gamma}}/m_{#gamma#gamma}", nbin, 0, 0.1])
plots.append(["sigmaMJets_gauss", "sigmaMJets", "#sigma_{m_{jj}}/m_{jj}", nbin, 0, 0.4])
plots.append(["PhoJetMinDr","PhoJetMinDr", "min DR(#gamma,jet)", nbin, 0, 6])
plots.append(["leadingPhotonSigOverE", "leadingPhotonSigOverE", "Leading Photon #sigma_{E}/E", nbin, 0, 0.1])
plots.append(["subleadingPhotonSigOverE", "subleadingPhotonSigOverE", "Subleading Photon #sigma_{E}/E", nbin, 0, 0.1])
plots.append(["leadingJet_bRegNNResolution", "leadingJet_bRegNNResolution","Leading Jet #sigma_{p_{T}}/p_{T}",nbin,0,0.4]) 
plots.append(["subleadingJet_bRegNNResolution", "subleadingJet_bRegNNResolution","SubLeading Jet #sigma_{p_{T}}/p_{T}",nbin,0,0.4]) 
plots.append(["PhoJetMinDr", "PhoJetMinDr", "min #DeltaR(#gamma,j)", 40, 0, 5])
plots.append(["PhoJetOtherDr", "PhoJetOtherDr", "other #DeltaR(#gamma,j)", 40, 0, 5])
plots.append(["leadingJet_pt_Over_Mjj", leadingJet_pt_Over_Mjj, "p_{T}(j_{1})/m_{jj}", nbin, 0,3] ) 
plots.append(["subleadingJet_pt_Over_Mjj", subleadingJet_pt_Over_Mjj, "p_{T}(j_{2})/m_{jj}", nbin, 0,3] ) 
plots.append(["diVBFjet_pt", "diVBFjet_pt", "p_{T} (VBF jj) (GeV)", nbin, 0, 1000])
plots.append(["VBFJet_mjj", "VBFJet_mjj", " m_{VBF jj} (GeV)", nbin, 0, 3500])
plots.append(["diHiggs_pt", "diHiggs_pt", "p_{T} (HH) (GeV)", nbin, 0, 1000])
plots.append(["VBFleadJet_pt", "VBFleadJet_pt", "p_{T} (VBF j_{1}) (GeV)", nbin, 0, 300])
plots.append(["VBFsubleadJet_pt", "VBFsubleadJet_pt", "p_{T} (VBF j_{2}) (GeV)", nbin, 0, 300])
plots.append(["VBFleadJet_pt_Over_VBFJet_mjj", "VBFleadJet_pt_Over_VBFJet_mjj", "p_{T} (VBF j_{1})/m_{VBF jj}", nbin, 0, 7])
plots.append(["VBFsubleadJet_pt_Over_VBFJet_mjj", "VBFsubleadJet_pt_Over_VBFJet_mjj", "p_{T} (VBF j_{2})/m_{VBF jj}", nbin, 0, 3])
plots.append(["VBFleadJet_eta", "VBFleadJet_eta", "#eta (VBF j_{1})", nbin, -5, 5])
plots.append(["VBFsubleadJet_eta", "VBFsubleadJet_eta", "#eta (VBF j_{2})", nbin, -5, 5])
plots.append(["VBFProd_eta", "VBFProd_eta", "#eta_{1}x#eta_{2}", nbin, -20, 20])
plots.append(["VBFJet_Delta_eta", "VBFJet_Delta_eta", "|#Delta#eta|", nbin, 0, 10])
plots.append(["VBFCentrality_jg", "VBFCentrality_jg", "C_{j gg}", nbin, 0, 1])
plots.append(["VBFCentrality_jb", "VBFCentrality_jb", "C_{j bb}", nbin, 0, 1])
plots.append(["VBFDeltaR_jg", "VBFDeltaR_jg", "min(#DeltaR_{j gg})", nbin, 0, 6])
plots.append(["VBFDeltaR_jb", "VBFDeltaR_jb", "min(#DeltaR_{j bb})", nbin, 0, 6])
plots.append(["VBFleadJet_QGL", "VBFleadJet_QGL", "QGL VBF leading jet", nbin, 0, 1])
plots.append(["VBFsubleadJet_QGL", "VBFsubleadJet_QGL", "QGL VBF subleading jet", nbin, 0, 1])


'''
#additional
plots.append(["rho", "rho", "#rho [GeV]", 40, 0, 60])
plots.append(["PhotonIDMVA1", "customLeadingPhotonIDMVA", "Leading Photon Id MVA ", nbin, -1, 1])
plots.append(["leadingJet_pt", "leadingJet_pt", "p_{T}(j_{1}) [GeV]", nbin, 15, 195] )
plots.append(["subleadingJet_pt", "subleadingJet_pt", "p_{T}(j_{2}) (GeV)", nbin, 15, 195] )
plots.append(["leadingJet_eta", "leadingJet_eta", "#eta(j_{1})", nbin, -3, 3] )
plots.append(["subleadingJet_eta", "subleadingJet_eta", "#eta(j_{1})", nbin, -3, 3] )
plots.append(["subleadingPhoton_pt", "subleadingPhoton_pt", "p_{T}(#gamma_{2}) [GeV]", nbin, 30, 150])
plots.append(["leadingPhoton_pt", "leadingPhoton_pt", "p_{T}(#gamma_{1}) [GeV]", nbin, 30, 150])
plots.append(["PhotonIDMVA2", "customSubLeadingPhotonIDMVA", "SubLeading Photon Id MVA", nbin, -1, 1])
plots.append(["PhotonIDMVA1", "customLeadingPhotonIDMVA", "Leading Photon Id MVA ", nbin, -1, 1])
plots.append(["MVAOutputTransformed","MVAOutputTransformed","MVA Output Transformed",40,0.,1.])
'''
#cuts to be used to make plots
#Cut = " isSignal && diphotonCandidate.M() > 100 && diphotonCandidate.M() < 180"
#Cut += " && dijetCandidate.M() > 60 && dijetCandidate.M() < 180"
#Cut = "((leadingJet_pt/leadingJet_bRegNNCorr) >20) && ((subleadingJet_pt/subleadingJet_bRegNNCorr)>20) && leadingJet_pt>20 && subleadingJet_pt> 20"
#Cut = "(MVAOutputTransformed>0.37)&&(ttHScore>=0)"
#Cut = "(MVAOutputTransformed>0.37)&&(ttHScore>=0.26)"
Cut = "(ttHScore>=0.26)"
#Cut = "(ttHScore>=0)"
#Cut = "(( ((EGMLeadingPhotonIDMVA>0.27) && (TMath::Abs(leadingPhoton_eta)<1.48)) ||  ((EGMLeadingPhotonIDMVA>0.14) && (TMath::Abs(leadingPhoton_eta)>1.48 && (TMath::Abs(leadingPhoton_eta)<3.0)))) &&  (((EGMSubLeadingPhotonIDMVA>0.27) && (TMath::Abs(subleadingPhoton_eta)<1.48)) ||  ((EGMSubLeadingPhotonIDMVA>0.14) && (TMath::Abs(subleadingPhoton_eta)>1.48 && (TMath::Abs(subleadingPhoton_eta)<3.0)))) )" #2017
#Cut = "((EGMLeadingPhotonIDMVA>0.20) && (EGMSubLeadingPhotonIDMVA>0.20))" #2016
