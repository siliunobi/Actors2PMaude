# Reproducing experimental results in Figure 3 (c)

## Overview

We reproduced on [CloudLab](https://www.cloudlab.us/) the original RAMP experimental results (RAMP-F vs RAMP-S) given in the SIGMOD'14 [paper](https://dl.acm.org/doi/10.1145/2588555.2588562). The following shows the instructions workable for CloudLab clusters. The RAMP source code, as well as the instructions to run it, is available at [here](https://github.com/pbailis/ramp-sigmod2014-code).


## Instructions

1.	In the Config.java file change the network interfact monitor:

    ```public String network_interface_monitor = "ens3"```

2. In CloudLab pick the OpenStack experiment with 10 nodes, preferibly xl170 from Utah or similar and 10Gbps link speed.

3. In the openstack create 10 xlarge instances and 1 medium (5 clients, 5 servers, and a machine from which you can run the experiment).

4. SSH to the medium and copy the codebase there in /home/ubuntu/kaiju.

5. Add a folder called hosts in /home/ubuntu with 3 files:
	- all_clients.txt 
    - all_servers.txt
    - all_hosts.txt
   
   Paste all 5 client ip addresses, 5 server ip addresses, and 10 host ip addresses in the respective files.

6. Compile and then copy it to all other 10 machines (use ssh-copy-id to avoid inserting the password all the time).

7. Substitute the existing **setup_hosts.py** with the one in this repo.

8. Paste client ips and server ips in the lists at the beginning of the file.

9. Substitute **experiment.py** with the one in this repo

10. Run this command on the medium machine:

	```python setup_hosts.py --color -c us-west-2 -nc 5 -ns 5 --experiment tsize_test --tag example```

**Note**: 

- one can paste the following in the configuration for the OpenStack instances to pre-install dependencies:

```
#!bin/bash
sudo apt update
sudo apt install -y default-jdk
sudo apt install -y pssh
sudo apt install -y maven
```

- Again,  in case a CloudLab cluster is needed, we have created an account (let us know via hotcrp so that we could share the username and pwd).