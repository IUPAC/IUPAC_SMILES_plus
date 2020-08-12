# ChemDraw ChemScript 19 SMILES to InChi
# 19.0.1.28
from ChemScript19 import *
from io import StringIO
import sys

Environment.SetVerbosity(True)
# Calculate InChI from SMILES
# SMILES -> ChemDraw Molecular Object ->  InChI

# Add option to perform dekekulization, this 
# is necassary to calculate some of the InChIs
# Adapted from:
# https://github.com/nextmovesoftware/smilesreading/blob/master/scripts/ChemDraw.py

op = NormOptions()

op.AnonList = False
op.Azide = False
op.CleaveIntoSalts = False
op.CreatedDelRep_1 = False
op.CreatedDelRep_2 = False
op.CollapseZwitterion = False
op.Dative = False
op.DativeToDouble = False
op.Dekekulize = True
op.Delrep = False
op.Diazo_a = False
op.Diazo_b = False
op.FeaturelessHydrogens = False
op.Isonitrile_fg = False
op.MergeCharges = False
op.MergeMetalSalts = False
op.MoveChargeFromCarbon = False
op.NeutralDiazo_fg = False
op.RemoveIsotopy = False
op.RemoveLabel = False
op.RemoveNonGraphStereo = False
op.RemoveRTable = False
op.RemoveRxnCenters = False
op.RemoveTextAtoms = False
op.RemoveValence = False
op.RemoveWedge = False
op.StripEitherDoubleBond = False
op.StripEitherSingleBond = False
op.R3NO_b = False
op.ProvideMissingCoords = False
op.Thiazole = False
op.XMinusToX_fg = False
op.ExpandStoichiometry = False
op.ConsolidateStoichiometry = False

sio = sys.stdout = StringIO()
mol = StructureData()

with open("input_smiles.smi") as input:
	with open("output_inchi.inchi", 'w') as out:
		for line in input:
			mol.ReadData(line,'smiles')
			mol.NormalizeStructure(op)
					
			x = mol.Inchi
			
			# capture "Bad mimetype:chemical/x-inchi" and "Unknown data format!"
			# when a "Unknown data format!" error occurs, an extra InChI (from previous line) is written to that line
			# I would like to improve this in the future, but everything I tried did not work. 
			out.write(str(sio.getvalue().rstrip()).format(x))
			out.write("{}\n".format(x))
			sio = sys.stdout = StringIO() #reset log
out.close()
