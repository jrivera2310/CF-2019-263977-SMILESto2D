from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem import Descriptors
from PIL import Image

# Ask the user to input a SMILES string
smiles_string = input("Please enter a SMILES string: ")

# Convert the SMILES string into a molecule object
mol = Chem.MolFromSmiles(smiles_string)

if mol:
    print("SMILES string is valid. Displaying the molecule structure.")

    # Generate an image of the molecule
    img = Draw.MolToImage(mol)

    # Display the image
    img.show()

    # Save the molecule as a .mol file (which ChemDraw can open)
    mol_filename = "molecule.mol"
    Chem.MolToMolFile(mol, mol_filename)
    print(f"Molecule structure saved to {mol_filename}. You can open this file in ChemDraw.")

    # List of descriptors available in RDKit
    descriptor_names = [desc[0] for desc in Descriptors._descList]

    # Create a descriptor calculator object
    calculator = MoleculeDescriptors.MolecularDescriptorCalculator(descriptor_names)

    # Calculate descriptors for the molecule
    descriptor_values = calculator.CalcDescriptors(mol)

    # Prepare the output as name-value pairs
    descriptors_dict = dict(zip(descriptor_names, descriptor_values))

    # Save descriptors to a .txt file
    output_file = "molecular_descriptors.txt"
    with open(output_file, "w") as file:
        file.write(f"Descriptors for SMILES: {smiles_string}\n\n")
        for name, value in descriptors_dict.items():
            file.write(f"{name}: {value}\n")

    print(f"Molecular descriptors saved to {output_file}.")
else:
    print("Invalid SMILES string. Please try again.")







