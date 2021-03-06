#!/bin/bash
conda create --yes -n chessvision python=3.5
source activate chessvision
while read requirement; do conda install --yes $requirement; done < requirements.txt 2>error.log
conda install --yes --channel https://conda.anaconda.org/menpo opencv3

# these need to be installed with pip
pip install python-chess
pip install stockfishpy

# To use with the Intel Math Kernel Library
#export MKL_THREADING_LAYER=GNU