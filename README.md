# ACSMPred-MVF
We designed a novel algorithmic framework named "ACSMPred-MVF" for solving the ACSM problem.

ACSMPred-MVF could be categorized in 3 folders
- Stack Feature Train contained some stacking train features 
- Stack Feature Test contained some stacking test features 
- Code consisted of Train and Test sub-folders with ACMPred-MVF.ipynb (and Mol2Vec_Handcrafted Feature.ipynb  for feature extraction)

The command to reproduce ACSMPred-MVF on Linux:

git clone https://github.com/lawankorn-m/ACSMPred-MVF.git

docker build -t ACSMPred-MVF_image

docker run -it --name ACSMPred-MVF_container ACSMPred-MVF_image

