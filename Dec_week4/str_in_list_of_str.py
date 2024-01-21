def ispresent(str, exclude_elements):
    for i in range(0, len(exclude_elements)):
        if exclude_elements[i] in str:
            return True
    return False


if __name__ == '__main__':
    str = "MnCrO"
    exclude_elements = ["B", "C", "N", "P", "S", "Se", "F", "Cl", "Br", "I", "H", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd",
                        "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk",
                        "Cf", "Es", "Fm", "Md", "No", "Lr", "Li", "Na", "K", "Rb", "Cs", "Fr", "Be", "Mg", "Ca", "Sr",
                        "Ba", "Ra"]
    print(ispresent(str, exclude_elements))
