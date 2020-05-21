# IDAM2V for inferring disease-associated miRNAs
The microRNAs (miRNAs) play crucial roles in many biological processes involved in diseases and miRNAs function with protein coding genes (PCGs). In this study, we present a semi-supervised multi-label framework to integrate PCG-PCG interactions, PCG-miRNA interactions, PCG-disease associations using graph convolutional network (GCN). IDAM2V is then trained on a graph, which is further used to score associations between diseases and miRNAs.

# System Requirements

## Hardware Requirements

The IDAM2V requires only a standard computer with enough RAM to support the operations. For minimal performance, this will be a computer with about 8 GB of RAM. For optimal performance, we recommend a computer with the following specs:

  * RAM: 4GB+ 
  * CPU: Intel® Core™ i7-4790

### OS Requirements

This package is tested in  Windows 10 Pro operating systems. The package has been tested on the following systems:



## Package dependencies
  * <a href='https://github.com/scikit-learn/scikit-learn' target='_blank'>sklearn 0.22</a> <br>
  * GCN
  * <a href=https://pytorch.org/>PyTorch  1.3.1+cpu</a> <br>
  * Python 3.7

## Installation of GCN
Here we modified the orginal GCN (https://github.com/tkipf/pygcn) to support multi-label learning. <br> 
```python setup.py install```

# Demo
1. To run the demo code, some big file needs be downloaded from other website: <br>
   - PCG-PCG interaction file "9606.protein.links.v10.txt.gz" can be downloaded from <a href="https://string-db.org/">STRING</a> v10 database. <br>
   - Disease-PCG assications file "human_disease_integrated_full.tsv" can be downloaded from <a href="https://diseases.jensenlab.org/Downloads">DISEASES </a> database. We also upload the file human_disease_integrated_full.zip in this repository, please decompress it at directory data/.  <br>
   - PCG-miRNA interaction file "9606.v1.combined.tsv.gz" can be downloaded from <a href="https://rth.dk/resources/rain/">RAIN</a> v1.0 database. <br>
   - The above three files need be saved at dir "data/". <br> 

2. You can directly  get the prediction and give the ROC curve by running: <br>
``` python IDAM2V.py``` <br>

It will output training and validaiton loss. In total, It takes < 10 minutes to run.
