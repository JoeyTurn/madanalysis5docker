SIMPLIFIED MODEL LIBRARY INSTRUCTIONS
v1.0


NOTE: These models and instructions are meant to be of benefit to the community and have been tested in a limited fashion, but are not guaranteed to be free of bugs or that they will work with all systems/software versions. Please report all issues with MadGraph, Pythia, or other software to the respective developers. If you think there is an issue with the UFO files (i.e., not with MadGraph or Pythia but a genuine bug in the 
UFO), please contact Brian Shuve (bshuve@g.hmc.edu), James Beacham (j.beacham@cern.ch), or whomever is listed in the contact information for the Simplified Models library.


Your mileage may vary. 

  
When using the library, please cite the LHC-LLP white paper: arXiv:18??.abcdf


****** INTRODUCTION ******


Each simplified model in the library consists of at least 3 components:

a) A model file in UFO format;
b) Process card(s) for generating the simplified model signature using MG5_aMC@NLO
c) Sample parameter and run cards that allow for the generation of events in the Les Houches format (LHE)

Due to its popularity, we provide process cards for generating parton-level events in MG5_aMC@NLO. However, it should be fairly straightforward to adapt the instructions for use in other event generators. We also comment that LHE events can further be processed to particle-level events using event generators such as Pythia 8.

Below, we provide step-by-step instructions for a single simplified model production + decay. These are supplemented with more model-specific directions for individual models in the corresponding directory (when needed). Our specific example is DIRECT PAIR PRODUCTION - SCALAR.

Note that the purpose of simplified models is to place limits on the production cross section. Therefore, the mapping between input couplings of the simplified model and the output cross section from the MC generator is typically irrelevant. However, there may be instances where one is interested in the couplings of the UV model used to generate the simplified model signatures. In this case, please see the comment on cross sections at the end of this README.


****** GENERATING THE BASE PROCESS ****** 


1) Copy the UFO model folder in to the models/ directory of MadGraph. In the case of our example, this is the RPVMSSM model.

2) Execute the following command in the main MadGraph directory:

./bin/mg5_aMC simplifiedmodel_DPP_scalar_proc_card.dat

where simplifiedmodel_DPP_scalar_proc_card.dat is the name of the provided process card. This will create a folder called simplifiedmodel_DPP_scalar/ in the MadGraph base directory. The generated process is direct sneutrino pair production, p p > sve sve~.

3) Copy the parameter card provided with the model (for example, simplifiedmodel_DPP_scalar_param_card.dat) into the directory simplifiedmodel_DPP_scalar/Cards, and rename the file param_card.dat. This file sets the parameters of the model file. You can change the masses of particles (in the MASS block) and the widths (you can also change the couplings, but this is usually not important for simplified models). All masses and widths are in GeV.

Regarding the masses, typically all particle masses EXCEPT those in the simplified model spectrum have been decouples (with masses set to > 10 TeV). You can change the particle masses appearing onshell in the process to whatever you like. The instructions accompanying each model should give the PID number corresponding the particles whose masses you might want to change.

For the widths, the most important one to set is the LLP width. This is because this will determine the decay position of the LLP in each event. This will be set by default to correspond to a proper decay  length of 1 mm, or a width of 1.9746e-13 GeV. To get longer/shorter decay lengths, you can put in  smaller/larger widths scaled by an appropriate linear factor. MadGraph doesn't like extremely small widths, so if you find that the run time is very long or you hit any instabilities, try increasing the width and manually modifying the resulting lifetime in the output LHE events.   

4) Copy the run card provided with the model (for example, simplifiedmodel_DPP_scalar_run_card.dat) into the directory simplifiedmodel_DPP_scalar/Cards, and rename the file run_card.dat. The default run_card.dat typically has minimal cuts applied, which should be fine for most LLP signals (you may wish to modify this if you are doing jet matching, etc.). For our purposes, the most important  parameter to set is "time_of_flight", which specifies how far a particle should decay from the primary vertex to be assigned a lifetime in the LHE output. By default, we have set this to 0.01 mm but this can be changed. NOTE THAT THIS IS THE PROPER LIFETIME: a particle with a short proper lifetime but huge boost might still decay at a macroscopic displacement, so be sure to choose this parameter with care! 

5) LHE event generation is launched by executing:

./bin/mg5_aMC
launch simplifiedmodel_DPP_scalar

...but first you will want to choose one of the following two methods to decay the LLP!


****** METHOD 1: DECAYING THE LLP WITH MADSPIN  ******


So far, we haven't specified how to decay the LLP. This is a good thing, because it means that we can decay the LLP many different ways using only one MG process!

If the interactions giving rise to LLP decay are contained within the UFO model, the decay
can be implemented using MadSpin. MadSpin generates the matrix elements for the decay process and generates decay events in the LLP rest frame, then consistently inserts them into the previously generated events with LLP final states.

1) Copy the madspin steering card provided with the model (for LLP decay into two jets, use the file simplifiedmodel_DPP_scalar.jj.dat) into the directory simplifiedmodel_DPP_scalar/Cards, and rename the file madspin_card.dat. Now, run MG as usual. MadSpin will automatically run and decay the LLP. Both the decayed and undecayed LHE events will be stored in the relevant Events/run_xy folder.

2) You can now do whatever you like with the output LHE files - pass them through your favourite  event generator to get particle-level final states, analyze them directly, etc. You should check that the decay position of the LLP matches what you specified for the width (remember that MG records the rest-frame decay TIME of the LLP; this is the VTIMUP parameter, see https://arxiv.org/pdf/hep-ph/0609017.pdf for more details).     


****** METHOD 2: DECAYING THE LLP WITH PYTHIA 8 ******


An alternate method to decay the LLP is to have Pythia 8 implement the decay. Pythia by default implements the decay using only a phase space weighting. This means that angular distributions may not be correct for the decay products. However, in many LLP scenarios this will have only a minimal impact on the acceptance of the signal. An additional advantage of implementing the  decays in Pythia is that it can implement the decay even if there is no coupling in the UFO model that would allow the decay to proceed in MG. 

1) Find the DECAY entry in param_card.dat corresponding to the LLP. In our example, the PID of the sneutrino is 1000012. In our example, it looks like

DECAY 1000012 1.974600e-13 # wsn1

2) In the line below the corresponding DECAY entry, add an indented set of 4+ entries for each desired LLP decay mode. The first entry is the branching fraction for that decay, the second entry should indicate the number of final states in the decay, while all subsequent entries list the particle ID for each final state. For example, if the sneutrino decays into d dbar, you would modify the DECAY entry to be

DECAY 1000012 1.974600e-13 # wsn1
   1.0000e-00   2    1  -1 

whereas if you wanted 50-50 branching fraction into mu+ e- and e+ mu- you would use

DECAY 1000012 1.974600e-13 # wsn1
   0.50000e-00   2    11  -13
   0.50000e-00   2    13  -11	

3) Generate events as usual with MG, and then pass to Pythia (either using the built-in functionality with MG5_aMC@NLO or using stand-alone Pythia). Pythia should automatically implement the specified decays. As always, make sure you check the Pythia output to see that the decays were implemented as you wanted. 


****** COMMENTS ON CROSS SECTIONS ******


For simplified models, the most important information to provide is the limit on or  sensitivity to the signal production cross section. By definition, simplified models are meant to stand in for many possible UV-complete models, and the cross section provides the easiest way of mapping sensitivities to other models. Limits on a cross section can be determined from signal efficiency and the dataset; therefore, the signal cross section for the simplified model event sample is not important for assessing experimental sensitivity.

If you are an experimentalist wish to determine the sensitivity to the couplings in a
particular model, you in principle need to use the UFO file for the FULL model, which
can account for multiple LLP production modes and the kinematics for the very specific
model under consideration. However, it is often the case that the simplified model is
found by taking a certain limit of the full model file, in which case these simplified
model UFO files can be used to determine the signal cross section for a particular choice
of couplings.

If you wish to use these model files to find cross sections as a function of coupling, the
simplest and most effective way of doing this is to exploit the narrow-width approximation. Suppose you are computing the signal cross section for a process:

p p ----->  h  -------> X + X, X -----> j j

If X is an LLP, it has a very tiny width. In this case, the cross section can be written in factorized form:

sigma(pp->(XX, X->jj)) = sigma(pp->XX) * BR( X-> j j )

The cross section for the process p p -> X X can be computed directly in MadGraph, as can
the branching fraction X -> j j for a particular choice of couplings if desired.  It is then fairly simple to constrain the model in terms of the coupling that makes X and
the branchingfraction to j j.

Alternatively, one can calculate the total X width using MadGraph, and put this width
into the param_card.dat. Then, simulate LLP production as outlined earlier in this document. The cross section output from MadGraph should give the correct value.

As a second alternative, one can set the X width to Auto in the param_card.dat and MadGraph will generate the X width automatically while generating the full process p p > X X, X > j j. However, this method has been known to cause problems (for example, when the X decay is  implemented by an EFT) and should be used with caution.

DISCLAIMER: The most trustworthy way to calculate cross sections is via the narrow-width
approximation, as numerical issues are sometimes known to occur when widths are very tiny 
(as they are for LLPs!). In all cases, the simplified model library as designed is meant
to be used for generating events to determine efficiencies, NOT to constrain full UV models. You are responsible for assessing whether your method for calculating cross sections using these model files is correct. Further questions can be directed to the authors of whatever Monte Carlo program you use to generate events.


