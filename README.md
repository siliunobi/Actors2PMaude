# Artifact Overview

Here are the artifacts used to (re)produce the experimental results in paper234 "Bridging the Semantic Gap between Qualitative and Quantitative Models of Distributed Systems". After describing the repo organization and dependency/system requirements, we show how to quickly get started with reproducing our experimental results.

# Repo Organization

- **query/**: the Maude spec of the running example presented in the paper (Example 8.1, Section 8) and its SMC analysis of the latency property. 

- **table1-exp/**: the Maude spec of the extended running example, and both qualitative and quantitative analyses using six different tools (Table 1, Section 8).

- **fig2-exp/**: the Maude spec of N-Tube, the RAMP family protocols, and Cassandra designs, and the SMC analysis of different properties for each case study (Figure 2, Section 9.1)

- **fig3-exp-smc/**: the Maude spec of the RAMP-F and RAMP-S, and the SMC analysis of system throughput (Figure 3 a,b,d, and e, Section 9.2)

- **fig3-exp-impl/**: the script to run the acutal RAMP-F/S implementations on a cluster (Figure 3 c, Section 9.2)

- **others/**: the Maude spec of other case studies (i.e., token ring, FBAR, and AODV) we have considered in the paper (see the beginning of Section 9.1).

**Note:** Detailed instructions for reproducing each set of experiments are given in readme.md in each repo, respectively.

# Tool and Dependency Install

- [Maude 2.7.1 for Linux64 or Mac OS X](http://maude.cs.illinois.edu/w/index.php/All_Maude_2_versions) 

- [PVeStA](http://maude.cs.uiuc.edu/tools/pvesta/download.html) (already included in the associated repositories)

-  [MultiVesta](https://alumnisssup-my.sharepoint.com/personal/andrea_vandin_santannapisa_it/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fandrea%5Fvandin%5Fsantannapisa%5Fit%2FDocuments%2FDISTR%2FMultiVeStA%2Fmultivesta%2Ejar&parent=%2Fpersonal%2Fandrea%5Fvandin%5Fsantannapisa%5Fit%2FDocuments%2FDISTR%2FMultiVeStA&ga=1) (already included)

- [MC2](http://people.brunel.ac.uk/~csstdrg/courses/glasgow_courses/website_sysbiomres/software/mc2/) (already included)

- [umaudemc](https://github.com/fadoss/umaudemc)

- [LTSmin](https://ltsmin.utwente.nl/)

- [Spot](https://spot.lrde.epita.fr/)

- Python 3.7 or above

- Java 8

**Notes** 
1. Make the command ***maude*** globally executable (on each experimental machine).
2. Althought the PVesta developer claims that any platform with JVM 1.6 (or later) installed should be able to run PVesta, we found in our experiments that PVesta is **not** compatible with newer versions than Java 8.
3. MultiVesta, MC2, LTSmin, and Spot are only required to (re)produce the **table1-exp/** experiments, which rely on the third party tool [umaudemc](https://github.com/fadoss/umaudemc).


# System Requirement

- Machine type in our experiments
    - Local analysis (**query/**, **table1-exp/**, and **others/**): a single machine with a 2.1 GHz 32 cores Intel Xeon Silver 4216 processor and 16 GB RAM.
    
    - Cloud analysis (**fig3-exp-impl/**): a Utah cluster of 10 xl170 nodes on [CloudLab](https://www.cloudlab.us/), each with 3.4GHz dual 10-Core Xeon E5-2640 v4 CPUs.
    
    - Parallelized analysis (all the other experiments): a cluster of 50 [Emulab](https://www.emulab.net) d710 nodes, each with a 2.4GHz Quad Core Xeon processor and 12 GB RAM.
    


- Operating System: Ubuntu 18.04.1 LTS

**Notes**
1. We highly recommend re-creating the experimental environment close to the above settings to get close experimental results and time.
2. Parallelized analysis is doable on a local machine (which is probably expensive!)
3. Cloud analysis is expected to be performed on a cluster. In case a cluster is needed (also for  parallelized analysis), we have created a CloudLab account (let us know via hotcrp so that we could share the username and pwd). 

# Instructions
- Getting started: go to the following repos  and check the readme files
	- query/ 
	- others/
  
  This set of experiments is expected to be finished in seconds.

- Moderate: go to the following repo and follow the instruction
	- table1-exp/
    
  The time varies (from ~1s, ~10min, to ~2hrs) depending on the property and tool: Checking *strong consistency* by *statistical model checking* takes much more time (especially by MultiVesta) than the other analyses (~1s). See Table 1 for reference.
    
- Large-scale: go to the following repos and follow the instructions
	- fig2-exp/

	- fig3-exp-smc/

	- fig3-exp-impl/

  Regarding *statistical model checking analysis* (i.e., **fig2-exp/** and **fig3-exp-smc/**), the time varies depending on the property and system model. See Table 2 for reference. Note that the time reported in each case is the average time of computing all the data points in the plot, e.g., 1hr 40min for Cassandra is the average time of computing 16 data points in Figure 2 (f).

