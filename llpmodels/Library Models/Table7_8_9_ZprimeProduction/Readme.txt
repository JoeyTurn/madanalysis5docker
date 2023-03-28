*************************************************
*** SOME NOTES ABOUT LLP&MET SIMPLIFIED MODEL ***
*************************************************

We provide two sets of model files for the Z'-mediated processes:


-the simple set uses a separate UFO for each of the three Z' production topologies (LLP+MET,
LLP+LLP, LLP+LLP+MET) and is relatively straightforward, with flavour-blind quark couplings and lepton couplings.

-the advanced model file is more adaptable but also more complicated, with a large number of couplings 
and parameters. 
The advanced version differs from the simple version in the following respects:
1) it incorporates all three production topologies in a single model file;
2) it allows for an independent coupling to each generation of quarks;
3) it includes independent vector and axial-vector couplings of the quarks and dark particles to the Z’.

Even though the roles of the couplings should be clear from their names and descriptions in the .fr file, it may be difficult to navigate all of them. 
For this reason, two python scripts (called "Script.py" and "Cards.py") are provided to guide the implementation of the processes.

They should be put in the main MadGraph folder and "Script.py" should be executed with Python2.7; 
the user is then guided into the generation of the process and should
choose the production topology, the initial states and the final states. 

MadGraph notation should be used to type initial/final states, (e.g. for s2 s2~ in the final states, type "s2 s2~").

The script creates a folder called "LLP_cards" in the main MadGraph folder, and puts the three relevant cards (parameter, madspin and process) in it.

The user is then asked if he wants the script to automatically generate the folder corresponding to the process: if the answer is yes, then the scripts copies the three cards from "LLP_cards" into the process folder.

In the parameter card, all unused couplings are set to 0 (or very large in the case of effective energy scales). 
Masses and other couplings can be edited as desired.

The script is designed as an aid but is not required; The user can simply run the process card with MadGraph as usual,  and checking the generated diagrams to ensure that only the process of interest has been generated. Generally s2, x2 and j should be excluded from the intermediate states of the production mode

 (i.e. something like p p > <intermediate_states> / s2 x2 j, <intermediate_states> > <fin_states>) 

to avoid inclusion of processes other than the process of interest, and for the LLP+MET topology, an explicit zp in s-channel should be included between the initial and decaying states.
In addition, we also suggest to exclude zp in the decay process (e.g. x2 > x1 j j /zp).
Note that the decay mode s2 > s1 SM SM exists as a consequence of the production mode, and can affect the normalisation of the cross-section and s2 total width.