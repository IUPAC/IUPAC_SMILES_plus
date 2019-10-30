#!/usr/bin/env python
# coding: utf-8

# # Open Babel SMILES to InChI Calculation

# Load Open Babel Modules
# Open Babel 2.4.1
import pybel


# Calculate InChI from SMILES
# SMILES → Open Babel Molecular Object → InChI

# Set up conversion to InChI
conv = pybel.ob.OBConversion()
conv.SetOutFormat("inchi")
# conv.SetOptions("K", conv.OUTOPTIONS)  # use this for IK

# loop through SMILES and calculate InChI
with open("input_smiles.smi") as inp:
    with open("output_inchi.inchi", 'w') as out:
        for line in inp:
            try:
                mol = pybel.readstring("smi",line)
            except IOError:
                out.write("Open_Babel_SMILES_parse_error\n")
                continue
            # N.B. No InChI Options
            inchi = conv.WriteString(mol.OBMol)
            
            if not inchi:
                out.write("InChI_calculation_empty\n".format(inchi))
                continue
            out.write("{}".format(inchi))
out.close()