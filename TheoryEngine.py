# An application to make doing language operations easier for Computation Theory

def main():

    A = set(["a, aa"])
    B = set(["b, e"])
    C = set(["c, bb"])
    
    AB = squash(A, B)
    BC = squash(B, C)

    A_BC = squash(A, BC)
    AB_C = squash(AB, C)
    print(A_BC.issubset(AB_C))
    print(A_BC, AB_C, sep="\n")


def squash(setA, setB):
    squashed = set()
    for a in setA:
        for b in setB:
            squashed.add(str(a) + str(b))
    return squashed

if __name__ == "__main__":
    main()