
## Producing the weights (by Alexandra)
The input files in lxplus are in
inputLM = "/afs/cern.ch/work/z/zghiche/public/ForXanda/NRDir_LM_350/"
inputHM = "/afs/cern.ch/work/z/zghiche/public/ForXanda/NRDir_HM_350/"

We have 13 samples, to each one we have two limit-trees, one for each category (LOWMASS/HIGHMASS). 
We do the new samples in 3 steps

1) read all the 2D histos from root files where they are saved, save them in multidimensional matrices

2) pass over all the events, make a matrix with the same binning of the input. (this is fast)
All the events here are added to the 2D matrix. NO weighting at this point. 

  => We have now  64190.0 in the low mass category and 138303.0 in the high mass one

3) pass over all the events, event-by-event I find in each bin it is, and make the weights dividing the matrix of point (1), by the ones from point (2) and fill new limit-trees for the new samples. 
They will be saved in 3 folders:

lambdaonly 
V3outliers
V3benchmarks

I hope the names inside are self explanatory
In the "V3benchmarks" folder are created as well a file 

V3_LT_output_GluGluToHHTo2B2G_box_validation0_13TeV-madgraph_LOWMASS.root (HIGHMASS)

This is just the sample 0 of v1 (box-only) made with the steps 1,2,3. To we test against the real sample. 