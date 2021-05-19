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

# Activation
```
. venv/bin/activate
```

# Setting Synapse Password
After activation run once:
```
keyring set synapse sqladminuser
```
At the prompt enter the password.

# Running Script
```
python synconn.py
```

Running Tests
```
cd test
python -m unittest test_synapse_connection
```

# Deactivation
```
deactivate
```
