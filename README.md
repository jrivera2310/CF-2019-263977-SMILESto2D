# CF-2019-263977-SMILESto2D
SMILESto2D.py
By José Alberto Rivera Chávez
Molecule Structure and Descriptor Calculator

This Python script takes a SMILES string (Simplified Molecular Input Line Entry System) as input, visualizes the molecule structure, and calculates molecular descriptors using the RDKit library. It also saves the molecule structure as a .mol file, which can be opened in software like ChemDraw, and exports the molecular descriptors to a .txt file.
Features

    Converts a SMILES string into a molecule object.
    Generates and displays a 2D image of the molecule.
    Saves the molecule structure to a .mol file.
    Calculates a variety of molecular descriptors.
    Saves the calculated molecular descriptors to a .txt file.

Prerequisites

Before running the script, you need to install the following Python packages:

    RDKit: A collection of cheminformatics and machine learning tools.
    Pillow (PIL): Python Imaging Library for displaying and manipulating images.

Install RDKit

RDKit can be tricky to install, as it’s not available directly via pip. You can install it using conda:

bash

conda install -c conda-forge rdkit

Install Pillow (PIL)

You can install Pillow using pip:

bash

pip install Pillow

How to Use

    Run the script: Run the Python script in your terminal or command prompt:

    bash

python SMILESto2D.py

Enter a SMILES string: After running the script, you will be prompted to enter a SMILES string that represents the molecule you want to analyze. For example:

css

    Please enter a SMILES string: CC(=O)O

    Molecule Structure Display:
        The script converts the SMILES string into a molecule object and generates a 2D image of the molecule. The image will be displayed on your screen.

    Save Molecule Structure:
        The molecule structure will be saved to a file called molecule.mol. This file can be opened with software like ChemDraw.

    Calculate Molecular Descriptors:
        The script calculates a set of molecular descriptors (physicochemical properties such as molecular weight, logP, etc.) using RDKit.
        The descriptors are saved to a text file named molecular_descriptors.txt.

    Review the Results:
        You can open molecule.mol to view the structure in ChemDraw.
        You can open molecular_descriptors.txt to view the calculated molecular descriptors.

Output Files

    molecule.mol: Contains the molecule structure in MOL format.
    molecular_descriptors.txt: Contains a list of molecular descriptors and their values for the given molecule.

Example

For the SMILES string CC(=O)O (which represents acetic acid), the script will:

    Display the structure of acetic acid.
    Save the structure in molecule.mol.
    Generate a .txt file with molecular descriptors, like this:

yaml

Descriptors for SMILES: CC(=O)O

MaxAbsEStateIndex: 8.333333333333334
MaxEStateIndex: 8.333333333333334
MinAbsEStateIndex: 0.0
MinEStateIndex: 0.0
...

Error Handling

If you enter an invalid SMILES string, the script will notify you and ask you to try again.
Notes

    Make sure you run this script in an environment where RDKit is properly installed.
    This script is designed for educational purposes and works for small to medium-sized molecules.
    
