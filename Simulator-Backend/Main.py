from CU import CU

def main():
    ram = [1] * 16
    cu = CU("intel", "2019-08-16", "manage everything", ram, 1.2, True)

    code = open("../.code", "r")
    codelines = code.readlines()

    cu.startInstructions(codelines)

if __name__== "__main__":
  main()