# IDAM2V for inferring disease-associated miRNAs
The microRNAs (miRNAs) play crucial roles in many biological processes involved in diseases and miRNAs function with protein coding genes (PCGs). In this study, we present a semi-supervised multi-label framework to integrate PCG-PCG interactions, PCG-miRNA interactions, PCG-disease associations using graph convolutional network (GCN). IDAM2V is then trained on a graph, which is further used to score associations between diseases and miRNAs.

# Development Environment
OS: Windows 10 Pro
RAM:8GB
CPU:Intel® Core™ i7-4790
GPU:GT720

## Packages dependencies
  * Python 3.7
  * sklearn 0.22
  * torch  1.3.1+cpu
  

# Demo
1. To run the demo code, some big file needs be downloaded from other website: <br>
   - PCG-PCG interaction file "9606.protein.links.v10.txt.gz" can be downloaded from <a href="https://string-db.org/">STRING</a> v10 database. <br>
   - Disease-PCG assications file "human_disease_integrated_full.tsv" can be downloaded from <a href="https://diseases.jensenlab.org/Downloads">DISEASES </a> database. We also upload the file human_disease_integrated_full.zip in this repository, please decompress it at directory data/.  <br>
   - PCG-miRNA interaction file "9606.v1.combined.tsv.gz" can be downloaded from <a href="https://rth.dk/resources/rain/">RAIN</a> v1.0 database. <br>
   - The above three files need be saved at dir "data/". <br> 

2. You can directly  get the prediction and give the ROC curve by running: <br>
``` python IDAM2V.py``` <br>

It will output training and validaiton loss. In total, It takes < 10 minutes to run.
