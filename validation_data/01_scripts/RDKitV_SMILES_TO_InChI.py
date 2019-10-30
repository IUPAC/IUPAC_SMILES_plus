#!/usr/bin/env python
# coding: utf-8

# # RDKit SMILES to InChI Calculation

# Load RDKit modules
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

# For Error Logs
from io import StringIO
import sys
Chem.WrapLogs()

# RDKit Version
from rdkit import rdBase
print(rdBase.rdkitVersion)

# Calculate InChI from SMILES
# SMILES → RDKit Molecular Object → InChI
# Adapted from https://iwatobipen.wordpress.com/2018/01/06/simple-way-for-making-smiles-file-rdkit/

# Record errors
# http://rdkit.blogspot.com/2016/03/capturing-error-information.html
sio = sys.stderr = StringIO()
er = open("LOG_file.txt", "a")

# Import SMILES File
inp = Chem.SmilesMolSupplier('input_smiles.smi',titleLine=False, delimiter ='\t')

# Loop through SMILES and calculate InChI
with open('output_smiles.inchi', 'w') as out:
    for mol in inp:
        if not mol: 
            out.write("RDKit_SMILES_parse_error\n".format(inchi))
            print(sio.getvalue(), file=er)         
            continue
        # N.B. No InChI options   
        inchi = Chem.MolToInchi(mol)
        
        if not inchi:
            out.write("InChI_calculation_empty\n".format(inchi))
            print(sio.getvalue(), file=er) 
            continue
        out.write("{}\n".format(inchi))
        # reset error log
        sio = sys.stderr = StringIO()
               
out.close()
er.close()
