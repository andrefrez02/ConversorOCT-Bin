bin = ["000", "001", "010", "011", "100", "101", "110", "111"]

def inputValue(valueOct):
    global Oct 
    Oct = valueOct
    checkValue()

def checkValue():
    if len(Oct) > 4:
        print("O valor digitado é maior do que 4 digitos!\n")
        inputValue(valueOct = input("Digite um número de 04 digitos de base Octal,"
                " para ser convertido para binário: \n"))
    if len(Oct) < 4:
        print("O valor digitado é menor do que 4 digitos!\n")
        inputValue(valueOct = input("Digite um número de 04 digitos de base Octal,"
                " para ser convertido para binário: \n"))
    if len(Oct) == 4:
        doubleCheck()

def doubleCheck():
    strBin = ""
    for i in range(4):
        if Oct[i] == "8" or Oct[i] == "9":
            print("O valor digitado não pode conter 8 ou 9!")
            inputValue()
        else:
            valueB = Oct[i]
            valueB = int(valueB)
            strBin = strBin + bin[valueB]
    global result
    result = strBin

print("CONVERSOR DE OCTAL PARA BINÁRIO\n"
        "Não digite números maiores do que '7'!\n")
inputValue(valueOct = input("Digite um número de 04 digitos de base Octal,"
                " para ser convertido para binário: \n"))
print("O valor: " + str(Oct) + " (Octal) é igual a: " + str(result) + " (Binário)")
input()