.. code:: ipython3

    # Load RDKit modules
    from rdkit import Chem
    from rdkit.Chem.Draw import IPythonConsole
    from rdkit.Chem import Draw
    from rdkit.Chem import AllChem
    
    # For Error Logs
    from io import StringIO
    import sys
    Chem.WrapLogs()
    
    # for changing directories
    import os
    
    # For csv import
    import csv
    
    # RDKit Version
    from rdkit import rdBase
    print(rdBase.rdkitVersion)


.. parsed-literal::

    2020.03.3


.. code:: ipython3

    # Calculate InChI from SMILES
    # SMILES → RDKit Molecular Object → InChI v1.05
    # Adapted from https://iwatobipen.wordpress.com/2018/01/06/simple-way-for-making-smiles-file-rdkit/
    
    # Record errors
    # http://rdkit.blogspot.com/2016/03/capturing-error-information.html
    
    os.chdir('/home/mydata')
    sio = sys.stderr = StringIO()
    er = open("RDKit_2020.03.3_InChIs_inputSMILES_LOG.txt", "a")
    
    # Import SMILES file
    # Be careful here, some of the files are space delimited. 
    # A VERY large log error file will be created if delimiter is set incorrectly.
    inp = Chem.SmilesMolSupplier('inputSMILES.smi',titleLine=False, delimiter ='\t')
    
    # Loop through SMILES and calculate InChI
    with open('RDKit_2020.03.3_InChIs_inputSMILES.inchi', 'w') as out:
        for i, mol in enumerate(inp):
            if not mol: 
                out.write("ERROR" + "\t" + str(i) + "\n".format(inchi))
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
