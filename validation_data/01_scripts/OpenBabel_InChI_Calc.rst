.. code:: ipython3

    # Open Babel SMILES to InChI Calculation
    # Load Open Babel Modules
    
    # For Open Babel 2.4.1
    # import pybel
    
    # Open Babel 3.1.1
    
    from openbabel import openbabel as ob
    from openbabel import pybel
    
    # for changing directories
    import os

.. code:: ipython3

    # Calculate InChI from SMILES
    # SMILES → Open Babel Molecular Object → InChI
    
    os.chdir('/home/mydata')
    
    # Set up conversion to InChI
    conv = pybel.ob.OBConversion()
    conv.SetOutFormat("inchi")
    # conv.SetOptions("K", conv.OUTOPTIONS)  # use this for IK
    
    # loop through SMILES and calculate InChI
    with open("inputSMILES.smi") as inp:
        with open("OpenBabel_3.1.1_InChIs_inputSMILES.inchi", 'w') as out:
            for i, line in enumerate(inp):
                try:
                    mol = pybel.readstring("smi",line)
                except IOError:
                    out.write("ERROR" + "\t" + str(i) + "\n".format(inchi))
                    continue
                # N.B. No InChI Options
                inchi = conv.WriteString(mol.OBMol)
                
                if not inchi: # captures an empty string return on inchi calc
                    out.write("InChI_calculation_empty"  + "\t" + str(i) + "\n".format(inchi))
                    continue
                out.write(inchi.rstrip() + "\t" + str(i) + "\n".format(inchi))
    out.close()

