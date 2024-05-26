@echo off
title ACCELERATORE_ECONOMETRICO

call conda env create -f requirements/acceleratore_eco.yaml
call conda activate acceleratore_eco

python -m ipykernel install --user --name=acceleratore_eco

jupyter notebook
