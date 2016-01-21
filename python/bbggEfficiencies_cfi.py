import FWCore.ParameterSet.Config as cms
import flashgg.bbggTools.parameters as param
import flashgg.Taggers.flashggTags_cff as flashggTags

### For more information on each parameter, see parameters.py

bbggefficiencies = cms.EDAnalyzer('bbggEfficiencies',
	DiPhotonTag=param._DiPhotonTag,
	JetTag=param._JetTag,
	inputTagJets= flashggTags.UnpackedJetCollectionVInputTag, #param._inputTagJets,
	GenTag=param._GenTag,
	rhoFixedGridCollection=param._rhoFixedGridCollection,
	PhotonPtOverDiPhotonMass=param._PhotonPtOverDiPhotonMass,
	PhotonEta=param._PhotonEta,
	PhotonR9=param._PhotonR9,
	PhotonElectronVeto=param._PhotonElectronVeto,
	PhotonDoElectronVeto=param._PhotonDoElectronVeto,
	PhotonDoID=param._PhotonDoID,
	PhotonDoISO=param._PhotonDoISO,
	DiPhotonPt=param._DiPhotonPt,
	DiPhotonEta=param._DiPhotonEta,
	DiPhotonMassWindow=param._DiPhotonMassWindow,
	DiPhotonOnlyFirst=param._DiPhotonOnlyFirst,
	JetPtOverDiJetMass=param._JetPtOverDiJetMass,
	JetEta=param._JetEta,
	JetBDiscriminant=param._JetBDiscriminant,
	JetDoPUID=param._JetDoPUID,
	JetDrPho=param._JetDrPho,
	n_bJets=param._n_bJets,
	DiJetPt=param._DiJetPt,
	DiJetEta=param._DiJetEta,
	DiJetMassWindow=param._DiJetMassWindow,
	CandidateMassWindow=param._CandidateMassWindow,
	CandidatePt=param._CandidatePt,
	CandidateEta=param._CandidateEta,
	bTagType=param._bTagType,
	phoIDlooseEB=param._phoIDlooseEB,
	phoIDmediumEB=param._phoIDmediumEB,
	phoIDtightEB=param._phoIDtightEB,
	phoIDlooseEE=param._phoIDlooseEE,
	phoIDmediumEE=param._phoIDmediumEE,
	phoIDtightEE=param._phoIDtightEE,
	phoISOlooseEB=param._phoISOlooseEB,
	phoISOmediumEB=param._phoISOmediumEB,
	phoISOtightEB=param._phoISOtightEB,
	phoISOlooseEE=param._phoISOlooseEE,
	phoISOmediumEE=param._phoISOmediumEE,
	phoISOtightEE=param._phoISOtightEE,
	nhCorrEB=param._nhCorrEB,
	phCorrEB=param._phCorrEB,
	nhCorrEE=param._nhCorrEE,
	phCorrEE=param._phCorrEE,
	PhotonWhichID=param._PhotonWhichID,
	PhotonWhichISO=param._PhotonWhichISO,
	JetDoID=param._JetDoID,
	doPhotonCR=param._doPhotonCR
#	doSelectionTree=param._doSelectionTree
)
