# ACSMPred-MVF
We designed a novel algorithmic framework named "ACSMPred-MVF" for solving the ACSM problem.

ACSMPred-MVF has Raw Data, Feature Descriptor,  Feature Representation and Classifier

In short, ACSMPred-MVF can be easily reproduced by using curated data within the Classifier folder	
- PCA42-D training set
- PCA42-D test set

The command to reproduce ACSMPred-MVF on Linux:

git clone https://github.com/lawankorn-m/ACSMPred-MVF.git

docker build -t ACSMPred-MVF_image

docker run -it --name ACSMPred-MVF_container ACSMPred-MVF_image

