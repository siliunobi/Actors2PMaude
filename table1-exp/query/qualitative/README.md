#  Instruction on running the qualitative analysis

1. We assume the following are installed:
	- Python 3.7 or above
    - [umaudemc](https://github.com/fadoss/umaudemc) (```pip install umaudemc```; its command should be in the path)
    - LTSmin (its commands should be in the path or LTSMIN_PATH be set appropriately)
    - the Maude plugin for LTSmin (whose path should be set with MAUDEMC_PATH)
    - [the Spot Python library](https://spot.lrde.epita.fr/install.html) 
    - psutil (```pip install psutil``` for memory measurement)
  
	More specifically, 
    - Maude is used through the maude Python library (as a side effect of pip install umaudemc), so the maude binary need not be in the path for this part.

	- LTSmin should be available in the PATH and the language plugin (libmaudemc.so, available [here](https://maude.ucm.es/strategies/#downloads)) should be downloaded and its location pointed with the environment variable MAUDEMC_PATH.

	- Spot should be installed with Python support. It is used through Python, so it does not matter whether the binaries are in the path. Installing Spot in Debian/Ubuntu is explained  [here](https://spot.lrde.epita.fr/install.html).
    
    - If you are using a Python's [virtual environment](https://docs.python.org/3/library/venv.html), ```pip install umaudemc``` will install the command ```umaudemc``` and make it available. Otherwise, if you install umaudemc system-wide with pip, the command will be inserted somewhere but the location will not probably be in the PATH (pip shows a warning about this). You can add that location to PATH or replace umaudemc by ```python -m umaudemc``` in the scripts. Finally, if you do not even install umaudemc with pip, you can simply download the umaudemc file [here](https://github.com/fadoss/umaudemc/releases/tag/latest) and add it to the path.
    
   **Note**:   the above are all third party tools which we have managed to run on our end. We are unable to predict any install or running errors on a different setup. 

  2. Run **qualitative.sh**.
  
  3. The model checking results, whether ***true*** or ***false*** (a counterexample returned), are expected to be consistent with Table 1, while the actual time and memory usage may differ.     For reference, the repo **results/** shows the results obtained on our end.
  
  

