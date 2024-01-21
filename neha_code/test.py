from pymatgen.io.cif import CifWriter
from pymatgen.io.cif import CifParser


def abc():
    # Read the Cif file
    cif_file = "P3-Na0.6Li0.2Mn0.8O2_coloredExp.cif"
    parser = CifParser(cif_file)
    structure = parser.get_structures()[0]
    new_structure = structure.copy()
    for i in structure.sites:
        if structure.sites[i] == "Rb":
            structure.sites.remove[i]

    structure.sites.remove("Rb")
    print(structure)

    # Define the chemical formulas of atoms to be deleted
    # atoms_to_delete = ["Rb5", "Rb6", "Rb11", "Rb12", "Rb17", "Rb18"]
    #
    # create a new structure without the atoms to be deleted
    # new_structure = structure.copy()

    # for site in structure:
    #    if site.species_string not in atoms_to_delete:
    #       new_structure.remove(site) #Append non-deleted atoms to the new structure

    # Write the modified structure to a new cif file
    # new_cif_file = "no_Rb.cif"
    # CifWriter(new_structure).write_file(new_cif_file)
    #
    # print(f"{len(structure) - len(new_structure)} atom(s) deleted successfully.")


def neha():
    from pymatgen.io.cif import CifWriter
    from pymatgen.io.cif import CifParser

    # Read the Cif file
    cif_file = "P3-Na0.6Li0.2Mn0.8O2_coloredExp.cif"
    parser = CifParser(cif_file)
    structure = parser.get_structures()[0]

    # Define the chemical formulas of atoms to be deleted
    atoms_to_delete = ["Rb5", "Rb6", "Rb11", "Rb12", "Rb17", "Rb18"]

    # create a new structure without the atoms to be deleted
    new_structure = structure.copy()

    for site in structure:
        if site.species_string not in atoms_to_delete:
            new_structure.append(site)  # Append non-deleted atoms to the new structure

    # Write the modified structure to a new cif file
    new_cif_file = "no_Rb.cif"
    CifWriter(new_structure).write_file(new_cif_file)

    print(f"{len(structure) - len(new_structure)} atom(s) deleted successfully.")


if __name__ == '__main__':
    abc()
    # neha()
