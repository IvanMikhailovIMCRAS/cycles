from gsdc import Box, Mol, Pot

if __name__ == "__main__":
    script = "(A)1[(B)2[(B)2](B)2]((A)1[(B)2[(B)2](B)2])198(A)1(B)2[(B)2](B)2"
    mol = Mol(script)
    num_last_A = "".join(mol.types).rindex("A")
    mol.bonds.append((0, num_last_A))
    pot = Pot(Box(60.0, 60.0, 60.0))
    pot.add(mol)
    pot.fuller("W")
    pot.brew()
