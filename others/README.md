#  Instruction on testing other case studies

This repo contains three case studies, i.e., token ring, fbar, and aodv, that we have also considered in the paper (see the beginning of Section 9.1). This set of experiments is focused on testing the executability of transformed models, and thus no statistical model checking analysis is involved.

For all three case studies, we follow the same steps to run test cases:

1. Go to each repo and run ***test.sh***.


2. Check **output.txt** for the testing results (currently three test cases for each case study).

## Example Output

Let's take token-ring for example. If all three test cases pass, the output file would show the following results with no error popping up:

```
==========================================
rewrite in TEST : initState .
rewrites: 280 in 10ms cpu (12ms real) (27168 rewrites/second)
result Config: 
{
< n1 : Node | state: waitForCS,next: n2 > 
< n2 : Node | state: outsideCS,next: n3 > 
< n3 : Node | state: outsideCS,next: n4 > 
< n4 : Node | state: outsideCS,next: n5 > 
< n5 : Node | state: waitForCS,next: n6 > 
< n6 : Node | state: outsideCS,next: n7 > 
< n7 : Node | state: outsideCS,next: n8 > 
< n8 : Node | state: outsideCS,next: n9 > 
< n9 : Node | state: waitForCS,next: n10 > 
< n10 : Node | state: outsideCS,next: n1 > |
5.9999659954903679}
==========================================
rewrite in TEST : initState .
rewrites: 280 in 10ms cpu (11ms real) (26843 rewrites/second)
result Config: 
{
< n1 : Node | state: waitForCS,next: n2 > 
< n2 : Node | state: outsideCS,next: n3 > 
< n3 : Node | state: outsideCS,next: n4 > 
< n4 : Node | state: outsideCS,next: n5 > 
< n5 : Node | state: waitForCS,next: n6 > 
< n6 : Node | state: outsideCS,next: n7 > 
< n7 : Node | state: outsideCS,next: n8 > 
< n8 : Node | state: outsideCS,next: n9 > 
< n9 : Node | state: waitForCS,next: n10 > 
< n10 : Node | state: outsideCS,next: n1 > |
5.0623057987249114}
==========================================
rewrite in TEST : initState .
rewrites: 279 in 8ms cpu (11ms real) (31411 rewrites/second)
result Config: 
{
< n1 : Node | state: waitForCS,next: n2 > 
< n2 : Node | state: outsideCS,next: n3 > 
< n3 : Node | state: outsideCS,next: n4 > 
< n4 : Node | state: outsideCS,next: n5 > 
< n5 : Node | state: waitForCS,next: n6 > 
< n6 : Node | state: outsideCS,next: n7 > 
< n7 : Node | state: outsideCS,next: n8 > 
< n8 : Node | state: outsideCS,next: n9 > 
< n9 : Node | state: waitForCS,next: n10 > 
< n10 : Node | state: outsideCS,next: n1 > |
8.588363138749866}
Bye.
```
**Note**: 

- The actual logical time units in the final ```Config```, e.g., ```8.588363138749866```, might be different due to the randomly chosen seed.

- The actual statistics of running Maude, e.g., ```rewrites: 279 in 8ms cpu (11ms real) (31411 rewrites/second)```, may vary depending on the machine. 
