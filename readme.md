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

## Generate_brk2_data.py
Script for generating SQL command for populating dbo.brk2 table.

### Running the Script
First, generate insert statements.
```
source venv/bin/activate
python generate_brk2_data.py --cusip_file data/input/cusips.csv --breakdown_file data/input/4p-industry-sectors.txt > brk2-insert-commands.sql
```
Second, use sqlcmd to push data into the database.
```
sqlcmd -S portrisk-synapse-workspace-name.database.windows.net -U sqladminuser -P '[redacted]' -I -d portrisk_synapse_workspace_sql_pool -e -i brk2-insert-commands.sql
```

# Work Planning
## Sprint of week 24-May-2021
- systematic exposure aggregation
  - aggregate total portfolio
  - aggregate one-level breakdown
  - aggregate multi-level breakdown
- measure performance of systematic exposure aggregation on four portfolio sizes (10, 100, 1000, 6000)
- learn idiosyncratic exposure aggregation
- document setup see [Learning Notes](https://webster.bfm.com/Wiki/display/apps/Azure+POC+Learning+Notes)
