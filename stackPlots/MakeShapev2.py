from pullClass import *
from ROOT import *
import json, os
import shutil
from configsShapeNewCode_runII import *
import resource

#SetMemoryPolicy( kMemoryStrict )
gROOT.SetBatch(1)

gStyle.SetOptStat(0)
dummyTFile = TFile("dummy.root", "RECREATE")

if not os.path.exists(dirName):
        print dirName, "doesn't exist, creating it..."
        os.makedirs(dirName)
       # shutil.copy2(dirPrefix + "index.php", dirName+"/index.php")
        if os.path.exists(dirName):
                print dirName, "now exists!"

datasets = json.load(data_file)

Trees = {}

if doBlind == True:
#	Cut += " && !((diphotonCandidate.M() > 115 && diphotonCandidate.M() < 135))"
	Cut += " && !((CMS_hgg_mass > 115 && CMS_hgg_mass < 135)) && !((Mjj > 105 && Mjj < 145)) "
weightedcut = ""
weightedcut += "(weight)"
weightedcut += "*(%s)"%Cut
weightedCut = TCut(weightedcut)
cut_data = TCut(Cut)
#cut_signal = TCut(weightedcut.replace("!((diphotonCandidate.M() > 115 && diphotonCandidate.M() < 135))", "(1>0)"))
cut_signal = TCut(weightedcut.replace("!((CMS_hgg_mass > 115 && CMS_hgg_mass < 135))", "(1>0)").replace("!((Mjj > 105 && Mjj < 145))", "(1>0)")) #to see how signal is distributed

for plot in plots:
    Histos = []
    variable = plot[1]
    varName = plot[2]
    thisStack = 0
    thisHist = 0
    thisStack = myStack('test'+plot[0], varName, varName, dirName, lumi)
    if hideData == True:
        thisStack.hideData()
    if hideStat == True:
        thisStack.hideStat()
    if isPhoCR == 1:
        thisStack.makePhoCR()
    if doJetCR == 1:
        thisStack.makeJetCR()
    if doShape == True:
        thisStack.doShape()
    if useJsonWeighting == True:
        thisStack.useJsonWeighting()



    thisStack.setYear(year)

    modelHist = TH1F(plot[0]+"_hist", "", plot[3], plot[4], plot[5])

    dataIntegral=0.
    print 'Data to be used : ',datasets['data']
    dataName = plot[0]+"_hist"+"_data"
    modelHist.Clear()
    dataHist = 0 
#   dataHist = modelHist
    dataHist = modelHist.Clone(dataName)
    for idata in range(0,len(datasets['data'])):
      thisTreeLoc = (datasets['data'][idata])['file']
      chainName = (datasets['data'][idata])["chainName"]
     # dataHist.Sumw2()
      if thisTreeLoc not in Trees:
          Trees[thisTreeLoc] = TChain(treename+chainName)
          Trees[thisTreeLoc].AddFile(dataLocation+thisTreeLoc)
          SetOwnership( Trees[thisTreeLoc], True )
      print 'Data Entries : ',Trees[thisTreeLoc].GetEntries()        
      Trees[thisTreeLoc].Draw(plot[1]+">>+"+dataName, cut_data)
      dataHist.SetMarkerStyle(20)
      dataHist.SetMarkerSize(0.8)
      dataHist.SetMarkerColor(1)
      dataHist.SetLineColor(1)
      dataHist.SetLineWidth(2)
      dataIntegral+=dataHist.Integral()
      thisStack.addData(dataHist, "Data")
       #  thisFile = TFile(plot[0]+"_data.root", "RECREATE")
       #  thisFile.cd()
       #  dataHist.Write()
       #  thisFile.Close()
       #  dummyTFile.cd()


    backgroundHists = []
    backgroundIntegral = 0.
    for background in datasets["background"]:
        if not addbbH and 'bbH' in background: continue
        if not addHiggs and 'VH' in background: continue
        if not addggHttH and 'ttH' in background: continue
        if not addggHttH and 'ggH' in background: continue
        if not addHiggs and 'VBF' in background: continue
        if not dyjets and "DYJ" in background: continue
        if "QCD" in background: continue
        print background
        thisName = plot[0]+"_hist"+"_"+background
        thisHist = modelHist.Clone(thisName)
#        thisHist.Clear()
#        thisHist.Sumw2()
        thisHist.SetLineColor(TColor.GetColor(datasets["background"][background]["color"]))
        thisHist.SetFillColor(TColor.GetColor(datasets["background"][background]["color"]))
        for i,fi in enumerate(datasets["background"][background]["files"]):
            print 'file : ',fi
            thisTreeLoc = fi["file"]
            chainName = fi["chainName"]
            skipEmptyFile = False
            if thisTreeLoc not in Trees:
                print 'adding ',thisTreeLoc
                Trees[thisTreeLoc] = TChain(treename+chainName)
                Trees[thisTreeLoc].AddFile(bkgLocation+thisTreeLoc)
                SetOwnership( Trees[thisTreeLoc], True )
            locName = thisName+str(i)
            locHist = thisHist.Clone(locName)
            thisWeightedCut = weightedCut
            if "QCD" in thisTreeLoc:
                 thisWeightedCut = TCut(weightedcut.replace("isSignal == 1", "isSignal == 0"))
            if 'additional_weight' in fi:
                 thisWeightedCut = TCut(weightedcut.replace("(weight)", "(weight)*(%s)"%fi["additional_weight"]))
            print thisWeightedCut
            Trees[thisTreeLoc].Draw(plot[1]+">>"+locName, thisWeightedCut)

            if useJsonWeighting:
      	     locHist.Scale(MCSF*lumi*fi["xsec"]*fi["sfactor"]/fi["weight"]/flashggLumi)
            if doShape:
    	        if not locHist.Integral() == 0:
    		        locHist.Scale(1./locHist.Integral())
	    		    
            if not skipEmptyFile: #fixme! needs to be implemented
    	        thisHist.Add(locHist)
    	        Histos.append(locHist)
    	        backgroundIntegral+=thisHist.Integral()


#            thisFile = TFile(plot[0]+"_"+fi["file"], "RECREATE")
#            thisFile.cd()
#            thisHist.Write()
#            thisFile.Close()
#            dummyTFile.cd()
            
        backgroundHists.append([thisHist, datasets["background"][background]["legend"], datasets["background"][background]["position"]])

    OrderedBackgrounds = sorted(backgroundHists, key=lambda x: x[2], reverse=True)
    print OrderedBackgrounds
    if doShape:
	    for background in OrderedBackgrounds: 
		    background[0].Scale(1./background[0].Integral())
		    background[0].SetFillStyle(3004)
		    background[0].SetLineWidth(2)
		    thisStack.addBackground(background[0], background[1], 1.)

    if doDataMCShape:
	    for background in OrderedBackgrounds: 
		    if (dataIntegral!=0) and (backgroundIntegral!=0):
		    	background[0].Scale(dataIntegral/backgroundIntegral)
		    	thisStack.addHist(background[0], background[1], background[2])
    del thisHist
    for background in OrderedBackgrounds: thisStack.addHist(background[0], background[1], background[2])
    
    if doSignal : 
     thisName = plot[0]+"_Signal_"
     thisHist = modelHist.Clone(thisName)
     thisHist.SetLineColor(datasets["signal"][0]["color"])
     thisHist.SetLineWidth(2)
     for isignal,signal in enumerate(datasets["signal"]):
#        modelHist.Clear()
#        thisHist = 0
 #       thisHist = modelHist
#        thisHist.SetName(thisName)
#        thisHist.Sumw2()
        thisTreeLoc = signal["file"]
        chainName = signal["chainName"]
        locName = thisName+str(isignal)
        locHist = thisHist.Clone(locName)
        if thisTreeLoc not in Trees:
            Trees[thisTreeLoc] = TChain(treename+chainName)
            Trees[thisTreeLoc].AddFile(signalLocation+thisTreeLoc)
            SetOwnership( Trees[thisTreeLoc], True )
        Trees[thisTreeLoc].Draw(plot[1]+">>"+locName, cut_signal)
        if useJsonWeighting:
            locHist.Scale(lumi*signal["xsec"]*signal["sfactor"]/signal["weight"]/flashggLumi)
        if doShape:
    	    if not locHist.Integral() == 0:
             locHist.Scale(1./locHist.Integral())

        thisHist.Add(locHist)
	
     thisStack.addSignal(thisHist, signal["legend"], 1.)

     del thisHist
    
    thisStack.drawStack(prefix + plot[0])
    
    del dataHist
    del thisStack 


dummyTFile.Close()
os.system("rm dummy.root")

#for tt in Trees:
#    Trees[tt].IsA().Destructor( Trees[tt] )

#    gROOT.GetListOfCanvases().Delete()
#    print Trees
#    print 'Memory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
#    gROOT.GetListOfCleanups().Delete()
    

