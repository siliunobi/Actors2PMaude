# Reproducing experimental results in Figure 3 (a), (b), (d), and (e)

- We organize this directory in terms of the four SMC experiments in Figure 3, e.g., subdirectory **fig3-a/** refers to the experiment in Figure 3 (a).

- We give instructions to reproduce the corresponding experimental results on an Emulab/CloudLab cluster. The procedure is:
	1. Run **launch.sh** to launch the remote servers (currently 50 Emulab nodes as specified in the **emulabnodes** file which can be tuned according to the available resource).
    
    2. Go to each directory (e.g., **fig3-a/**) and run **run.sh** in  each of its subdirectories to start the client.
    	- **ramp_f_original_latency_msg** and **ramp_s_latency_msg** refer to RAMP-F and RAMP-S, respectively.
    
    3. The statistical model checking results  will be stored in **result.out**.  The results may vary due to randomly chosen seeds. For reference, we also give our *normalized* results obtained on Emulab in the  **.dat** file.
    4. Always run **killserver.sh** to kill the remote server processes before any new experiment.
    
**Note**: Please change **PATH** in each script (**launch.sh**, **server.sh**, and **getpid.py**) accordingly for each set of experiments.
