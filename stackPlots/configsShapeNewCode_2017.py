
##################################################
##################################################
## Configuration parameters to run MakeShape.py ##
##################################################
##################################################

doBlind = False
doShape = True
doJetCR = False


useJsonWeighting=False

isPhoCR = False
addHiggs = False
addggHttH = False
hideData = True
addbbH = False
dyjets = False


doSignal = True
addData = False   ############NEW

hideStat = True

#btagging working poing
# 0.46 - loose
# 0.80 - medium
# 0.935 - tight
BTAG = 0.

#Luminosity to normalize backgrounds
flashggLumi = 1000.#pb
MCSF = 1.0
#List of datasets to be used (cross section information defined there)
#data_file = open("datasets/datasets80X_Moriond_onlyNRSM.json")
#data_file = open("datasets/datasets80X_newcode_Moriond_onlyNRSM_diphoton_Gjets.json")
#data_file = open("datasets/datasets80X_2017_nodata.json")
data_file = open("datasets/datasets80X_newcode_Moriond_onlyNRSM_diphoton_Gjets.json")

#number of bins in histograms
nbin = 30
leadingJet_noreg_pt = "(leadingJet_pt/leadingJet_bRegNNCorr)"
subleadingJet_noreg_pt = "(subleadingJet_pt/subleadingJet_bRegNNCorr)"

#year = "2017"
#lumi = 41500.#pb
year = "2016"
lumi = 35900.#pb
#plots will be saved in dirName
prefix = ""
#dirSuffix = "20181213_2017"
dirSuffix = "20181213_2016"
#dirPrefix = "/afs/cern.ch/user/n/nchernya/www/HHbbgg/MVA_training/2017plots/"
dirPrefix = "/afs/cern.ch/user/n/nchernya/www/HHbbgg/MVA_training/2016plots/"
dirName = dirPrefix + dirSuffix
treename="tagsDumper/trees/"

#Location of root files for each invidivual samples. Name of the root files is defined in datasets/datasets(76).json
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/root_files/ntuples_2017data_20181023/'
#filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/root_files/ntuples_2017_20181210/'
filesDir = '/mnt/t3nfs01/data01/shome/nchernya/HHbbgg_ETH_devel/root_files/ntuples_2016_20181210/'
higgsoLocation=filesDir
bkgLocation=filesDir
dataLocation=filesDir
signalLocation=filesDir



#plots to be made
plots = []

#Masses
plots.append(["diPho_Mass", "CMS_hgg_mass", "M(#gamma#gamma) [GeV]", 80, 100, 180])
plots.append(["PhotonIDMVA2", "(customSubLeadingPhotonIDMVA)", "SubLeading Photon Id MVA", nbin, -1, 1])
plots.append(["PhotonIDMVA1", "(customLeadingPhotonIDMVA)", "Leading Photon Id MVA ", nbin, -1, 1])
plots.append(["CosTheta_gg", "absCosTheta_gg", "|Cos(#theta_{#gamma#gamma})|", nbin, 0, 1])
plots.append(["CosTheta_bb", "absCosTheta_bb", "|Cos(#theta_{bb})|", nbin, 0, 1])
plots.append(["costhetastar_cs", "absCosThetaStar_CS", "|cos#theta*|_{CS}", nbin, 0, 1])
plots.append(["diPhoton_pt_overM", "diphotonCandidatePtOverdiHiggsM", "p_{T}(#gamma#gamma)/M_{jj#gamma#gamma}", nbin, 0, 1] )
plots.append(["diJet_pt_overM", "dijetCandidatePtOverdiHiggsM", "p_{T}(jj)/M_{jj#gamma#gamma}", nbin, 0, 1] )
plots.append(["leadingJet_btag", "leadingJet_bDis", "b-tag leading jet", nbin, 0, 1])
plots.append(["subleadingJet_btag", "subleadingJet_bDis", "b-tag subleading jet", nbin, 0, 1])
plots.append(["leadingJet_DeepCSV", "leadingJet_DeepCSV", "Deep CSV leading jet", nbin, 0, 1])
plots.append(["subleadingJet_DeepCSV", "subleadingJet_DeepCSV", "Deep CSV subleading jet", nbin, 0, 1])
plots.append(["sigmaMOverMDecorr", "sigmaMOverMDecorr", "#sigma_{M_{decorr}}/M", nbin, 0, 0.1])
plots.append(["sigmaMOverM", "sigmaMOverM", "#sigma_{M}/M", nbin, 0, 0.1])
plots.append(["PhoJetMinDr","PhoJetMinDr", "min DR(#gamma,jet)", nbin, 0, 6])
plots.append(["leadingPhotonSigOverE", "leadingPhotonSigOverE", "Leading Photon #sigma_{E}/E", nbin, 0, 0.1])
plots.append(["subleadingPhotonSigOverE", "subleadingPhotonSigOverE", "Subleading Photon #sigma_{E}/E", nbin, 0, 0.1])
#bregression
plots.append(["leadingJet_bRegNNResolution", "leadingJet_bRegNNResolution","Leading Jet #sigma_{p_{T}}/p_{T}",nbin,0,0.4]) 
plots.append(["subleadingJet_bRegNNResolution", "subleadingJet_bRegNNResolution","SubLeading Jet #sigma_{p_{T}}/p_{T}",nbin,0,0.4]) 
plots.append(["dijetSigmaMOverM","sigmaMJets","dijet #sigma_{M}/M ",nbin,0.,0.4])
plots.append(["subleadingJet_bRegNNCorr", "subleadingJet_bRegNNCorr","SubLeading Jet regression corr",nbin,-0.1,2.]) 
plots.append(["leadingJet_bRegNNCorr", "leadingJet_bRegNNCorr","Leading Jet regression corr",nbin,-0.1,2.]) 

#additional

plots.append(["leadingJet_pt", "leadingJet_pt", "p_{T}(j_{1}) [GeV]", nbin, 15, 195] )
plots.append(["subleadingJet_pt", "subleadingJet_pt", "p_{T}(j_{2}) (GeV)", nbin, 15, 195] )
plots.append(["leadingJet_eta", "leadingJet_eta", "#eta(j_{1})", nbin, -3, 3] )
plots.append(["subleadingJet_eta", "subleadingJet_eta", "#eta(j_{1})", nbin, -3, 3] )
plots.append(["MX", "MX", "#tilde{M}_{X} (GeV)", 40, 200, 1000])
plots.append(["leadingJet_noreg_pt", leadingJet_noreg_pt, "p_{T}(j_{1}) w/o regression [GeV]", nbin, 15, 195] ) # non regressed
plots.append(["subleadingJet_noreg_pt", subleadingJet_noreg_pt, "p_{T}(j_{2}) w/o regression (GeV)", nbin, 15, 195] ) # non regressed
plots.append(["subleadingPhoton_pt", "subleadingPhoton_pt", "p_{T}(#gamma_{2}) [GeV]", nbin, 30, 150])
plots.append(["leadingPhoton_pt", "leadingPhoton_pt", "p_{T}(#gamma_{1}) [GeV]", nbin, 30, 150])
plots.append(["Mgg", "CMS_hgg_mass", "{M}_{#gamma#gamma} (GeV)", 40, 100, 180])
plots.append(["Mjj", "Mjj", "{M}_{jj} (GeV)", 40, 60, 180])



'''
plots.append(["diPho_Mass", "diphotonCandidate.M()", "M(#gamma#gamma) [GeV]", 80, 100, 180])
plots.append(["diJet_Mass", "dijetCandidate.M()", "M(jj) [GeV]", 36, 70, 178])


#MVA variables
plots.append(["PhotonIDMVA2", "(customSubLeadingPhotonIDMVA)", "SubLeading Photon Id MVA", nbin, -1, 1])
plots.append(["PhotonIDMVA1", "(customLeadingPhotonIDMVA)", "Leading Photon Id MVA ", nbin, -1, 1])

plots.append(["costhetastar_cs", "fabs(CosThetaStar_CS)", "|cos#theta*|_{CS}", nbin, 0, 1])

plots.append(["CosTheta_gg", "fabs(CosTheta_gg)", "|Cos(#theta_{#gamma#gamma})|", nbin, 0, 1])
plots.append(["CosTheta_bb", "fabs(CosTheta_bb)", "|Cos(#theta_{bb})|", nbin, 0, 1])

plots.append(["diPhoton_pt_overM", "diphotonCandidate.Pt()/diHiggsCandidate.M()", "p_{T}(#gamma#gamma)/M_{jj#gamma#gamma}", nbin, 0, 1] )
plots.append(["diJet_pt_overM", "dijetCandidate.Pt()/diHiggsCandidate.M()", "p_{T}(jj)/M_{jj#gamma#gamma}", nbin, 0, 1] )
plots.append(["leadingJet_btag", "leadingJet_bDis", "b-tag leading jet", nbin, 0, 1])
plots.append(["subleadingJet_btag", "subleadingJet_bDis", "b-tag subleading jet", nbin, 0, 1])

plots.append(["leadingPhotonSigOverE", "leadingPhotonSigOverE", "Leading Photon #sigma_{E}/E", nbin, 0, 0.1])
plots.append(["subleadingPhotonSigOverE", "subleadingPhotonSigOverE", "Subleading Photon #sigma_{E}/E", nbin, 0, 0.1])
plots.append(["sigmaMOverMDecorr", "sigmaMOverMDecorr", "#sigma_{M_{decorr}}/M", nbin, 0, 0.1])
plots.append(["sigmaMOverM", "sigmaMOverM", "#sigma_{M}/M", nbin, 0, 0.1])



#possible MVA variables
plots.append(["Phi", "Phi0", "#Phi", nbin, -3.5, 3.5])
plots.append(["Phi1", "Phi1", "#Phi_{1}", nbin, -3.5, 3.5])
plots.append(["PhoJetMinDr","PhoJetMinDr", "min DR(#gamma,jet)", nbin, 0, 6])
plots.append(["DiJetEta", "dijetCandidate.Eta()", "#eta(jj)", nbin, -3, 3] )
plots.append(["DiPhotonEta", "diphotonCandidate.Eta()", "#eta(#gamma#gamma)", nbin, -3, 3] )

#additional variables
plots.append(["leadingJet_pt", "leadingJet.Pt()", "p_{T}(j_{1}) [GeV]", nbin, 15, 200] )
plots.append(["subleadingJet_pt", "subleadingJet.Pt()", "p_{T}(j_{2}) (GeV)", nbin, 15, 80] )
plots.append(["leadingJet_eta", "leadingJet.Eta()", "#eta(j_{1})", nbin, -3, 3] )
plots.append(["subleadingJet_eta", "subleadingJet.Eta()", "#eta(j_{1})", nbin, -3, 3] )
plots.append(["diPhoton_pt", "diphotonCandidate.Pt()", "p_{T}(#gamma#gamma) [GeV]", nbin, 15, 400] )
plots.append(["diJet_pt", "dijetCandidate.Pt()", "p_{T}(jj) [GeV]", nbin, 15, 400] )
plots.append(["diHiggs_pt", "diHiggsCandidate.Pt()", "p_{T}(#gamma#gamma jj) [GeV]", nbin, 15, 800] )

plots.append(["MX", "diHiggsCandidate.M() - dijetCandidate.M() + 125.", "#tilde{M}_{X} (GeV)", 40, 200, 1000])

#bregression

plots.append(["diJet_pt_breg", "dijetCandidateCorr.Pt()", "p_{T}(jj) [GeV] regressed", nbin, 15, 400] )
plots.append(["leadingJet_bRegNNResolution", "leadingJet_bRegNNResolution","Leading Jet #sigma_{p_{T}}/p_{T}",nbin,0,0.4]) 
plots.append(["subleadingJet_bRegNNResolution", "subleadingJet_bRegNNResolution","SubLeading Jet #sigma_{p_{T}}/p_{T}",nbin,0,0.4]) 
plots.append(["dijetSigmaMOverM","dijetSigmaMOverM","dijet #sigma_{M}/M ",nbin,0.,0.4])
plots.append(["diHiggsCandidateCorrMass", "diHiggsCandidateCorr.M()", "M(jj#gamma#gamma) [GeV] regressed", nbin, 100, 1000])
plots.append(["diHiggsCandidateCorrPt", "diHiggsCandidateCorr.Pt()", "p_T(jj#gamma#gamma) [GeV] regressed", nbin, 15, 800])
'''
#cuts to be used to make plots
#Cut = " isSignal && diphotonCandidate.M() > 100 && diphotonCandidate.M() < 180"
#Cut += " && dijetCandidate.M() > 60 && dijetCandidate.M() < 180"
#Cut = "((leadingJet_pt/leadingJet_bRegNNCorr) >20) && ((subleadingJet_pt/subleadingJet_bRegNNCorr)>20) && leadingJet_pt>20 && subleadingJet_pt> 20"
Cut = "(1>0)"
#Cut = "(( ((EGMLeadingPhotonIDMVA>0.27) && (TMath::Abs(leadingPhoton_eta)<1.48)) ||  ((EGMLeadingPhotonIDMVA>0.14) && (TMath::Abs(leadingPhoton_eta)>1.48 && (TMath::Abs(leadingPhoton_eta)<3.0)))) &&  (((EGMSubLeadingPhotonIDMVA>0.27) && (TMath::Abs(subleadingPhoton_eta)<1.48)) ||  ((EGMSubLeadingPhotonIDMVA>0.14) && (TMath::Abs(subleadingPhoton_eta)>1.48 && (TMath::Abs(subleadingPhoton_eta)<3.0)))) )" #2017
#Cut = "((EGMLeadingPhotonIDMVA>0.20) && (EGMSubLeadingPhotonIDMVA>0.20))" #2016
