# Brief
Python sandbox for PortRisk Azure POC

# Installation
```
git clone /git-projects/python-sanbox-1/.git
cd python-sanbox-1
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Activation
```
. venv/bin/activate
```
## Deactivation
```
deactivate
```

# Scripts
## Synconn.py
Illustrates connection to the Synapse database

### Setting Synapse Password
After activation run once:
```
keyring set synapse sqladminuser
```
At the prompt enter the password.

### Running the Script
```
python synconn.py
```

### Running Tests
```
cd test
python -m unittest test_synapse_connection
```

## Readport.py
Script for generating input files for population exposure database tables

### Running the Script
```
python readport.py -l --var_factor_file data/input/var_factor --out_dir data/output data/input/exposures-small-sample.txt
```