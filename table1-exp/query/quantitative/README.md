#  Instruction on running the quantitative analysis

1. We have included in the repo the following tools (four jar files):
  	- PVeStA
  	- MultiVesta
  	- MC2
  
	**Note**: the above are all third party tools which we have managed to run on our end. We are unable to predict any install or running errors on a different setup. 

  2. Run **all.sh**  (for all three tools).
  
  
  3. The statistical model checking results for *eventual consistency* (i.e., 1.0) are expected to be consistent with Table 1. The results for *strong consistency*  may vary (due to the randomly chosen seed; in particular, for PVesta, please take the result of the third run).
 The actual time and memory usage could be different as well.    For reference, the directory **results/** shows the results obtained on our end for both *strong consistency* and *eventual consistency* with different tools. 
