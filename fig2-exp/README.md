# Reproducing experimental results in Figure 2

- We organize this repo in terms of experiments in Figure 2, e.g., sub-repo **fig2-a/** refers to the experiment in Figure 2 (a).

- We recommend starting with **fig2-a/** as this set of experiments is quite affordable on a local machine. 

- For the other subdirectories, we give instructions to reproduce the corresponding experimental results on an Emulab/CloudLab cluster. The procedure is:
	1. Run **launch.sh** to launch the remote servers (currently 50 Emulab nodes as specified in **emulabnodes** which can be tuned according to the available resource).
    2. Go to each subdirectory (e.g., **fig2-d/**) and run **run.sh** to start the client.
    3. The statistical model checking results  will be stored in **result.out**.  The results may vary due to randomly chosen seeds. For reference, we also give our *normalized* results obtained on Emulab in the  **.dat** file.
    4. Always run **killserver.sh** to kill the remote server processes before any new experiment.
    
**Note**: Please change **PATH** in each script (**launch.sh**, **server.sh**, and **getpid.py**) accordingly for each set of experiments.
 

