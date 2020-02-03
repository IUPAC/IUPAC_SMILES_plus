#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Open Babel SMILES to InChI Calculation
# Load Open Babel Modules

# For Open Babel 2.4.1
# import pybel

# Open Babel 3.0.0

from openbabel import openbabel as ob
from openbabel import pybel


# In[14]:


# Calculate InChI from SMILES
# SMILES → Open Babel Molecular Object → InChI

# Set up conversion to InChI
conv = pybel.ob.OBConversion()
conv.SetOutFormat("inchi")
# conv.SetOptions("K", conv.OUTOPTIONS)  # use this for IK

# loop through SMILES and calculate InChI
with open("input_file.smi") as inp:
    with open("OpenBabel_3.0.0_InChIs_output_file.inchi", 'w') as out:
        for i, line in enumerate(inp):
            try:
                mol = pybel.readstring("smi",line)
            except IOError:
                out.write("SMILES_parse_error" + "\t" + str(i) + "\n".format(inchi))
                continue
            # N.B. No InChI Options
            inchi = conv.WriteString(mol.OBMol)
            
            if not inchi: # captures an empty string return on inchi calc
                out.write("InChI_calculation_empty"  + "\t" + str(i) + "\n".format(inchi))
                continue
            out.write(inchi.rstrip() + "\t" + str(i) + "\n".format(inchi))
out.close()


# In[ ]:




