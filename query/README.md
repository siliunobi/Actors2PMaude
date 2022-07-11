# Getting Started: reproducing experimental result for our running example 

The following shows steps to reproduce the statistical model checking result for Example 8.1 (Section 8).

1. Run ***test.sh*** under the current repo (which is expected to finish instantly on a local machine).

2. Check ***result.txt*** for the analysis result. Note that the actual SMC result may *differ* for each run due to the randomly chosen seed for probabilistic sampling. For reference, below shows the result on our end:

```
Confidence (alpha): 0.05
Threshold (delta): 0.01
Samples generated: 60
SMC result: 5.791871271488804
```

**Note**:  Do not forget to kill the "pvesta-server.jar" process before performing a new experiment.


