#!/bin/python3

SYMBOLS = set("""
    H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu
    Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs
    Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl
    Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh
    Hs Mt Ds Rg Nh Nh Fl Mc Lv Ts Og
""".split())

# Complete the function below.

def symbolize(name):
    """
    Returns a sorted list of all the ways (if any) in which the name can be
    written using chemical symbols. The name is case-insensitive, but the
    return values should respect the case of the chemical symbols.
    """
    
    # symbolize("ne") == ["Ne"]
    # symbolize("e") == [""]
    # symbolize("") == [""]
    
    output = []
    if name[0].upper() in SYMBOLS:
        if len(name) <= 1:
            output += [name[0].upper()]
        else:
            output += [name[0].upper() + i for i in symbolize(name[1:])]
    
    if len(name) > 1 and name[0].upper() + name[1].lower() in SYMBOLS:
        if len(name) <= 2:
            output += [name[0].upper() + name[1].lower()]
        else:
            output += [name[0].upper() + name[1].lower() + i for i in symbolize(name[2:])]
        
    return output

print(symbolize("Catherine"))
