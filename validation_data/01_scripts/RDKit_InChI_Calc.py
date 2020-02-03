#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Load RDKit modules
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

# For Error Logs
from io import StringIO
import sys
Chem.WrapLogs()

# For csv import
import csv

# RDKit Version
from rdkit import rdBase
print(rdBase.rdkitVersion)


# In[4]:


# Calculate InChI from SMILES
# SMILES → RDKit Molecular Object → InChI v1.05
# Adapted from https://iwatobipen.wordpress.com/2018/01/06/simple-way-for-making-smiles-file-rdkit/

# Record errors
# http://rdkit.blogspot.com/2016/03/capturing-error-information.html
sio = sys.stderr = StringIO()
er = open("RDKit_2019.09.2_InChIs_input_file_LOG_file.txt", "a")

# Import SMILES file
inp = Chem.SmilesMolSupplier('input_file.smi',titleLine=False, delimiter ='\t')

# Loop through SMILES and calculate InChI
with open('RDKit_2019.09.2_InChIs_output_file.inchi', 'w') as out:
    for i, mol in enumerate(inp):
        if not mol: 
            out.write("SMILES_parse_error" + "\t" + str(i) + "\n".format(inchi))
            print(sio.getvalue(), file=er)         
            continue
        
        # No InChI options, calculates standard InChI   
        inchi = Chem.MolToInchi(mol)
        
        if not inchi:
            # This captures an empty string returned from the InChI calculation
            # Here is an example: [C@H]1([C@H](C1C2[C@@H]([C@@H]2C(=O)O)C(=O)O)C(=O)O)C(=O)O
            out.write("InChI_calculation_empty" + "\t" + str(i) + "\n".format(inchi))
            print(sio.getvalue(), file=er)
            continue
        out.write(inchi + "\t" + str(i) + "\n".format(inchi))
        # reset error log
        sio = sys.stderr = StringIO()
               
out.close()
er.close()


# In[ ]:




