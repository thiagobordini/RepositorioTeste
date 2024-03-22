#Sistema de calculadora com valores digitados pelo usuário
print("MENU CALCULADORA")
print("")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 -")
print("")

tipo_conta = input("Digite a opção desejável de cálculo: ")
print("")

if tipo_conta == "1":
    print("Cálculo de soma selecionado!")
    print("")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    soma = num1 + num2
    print("")
    print("A soma dos valores digitados é: {}".format(soma))

elif tipo_conta == "2":
    print("Cálculo de subtração selecionado!")
    print("")
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    sub = num1 - num2
    print("")
    print("A subtração dos valores digitados é: {}".format(sub))

elif tipo_conta == "3":
    print("Cálculo de Multiplicação selecionado!")
    print("")
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    multi = num1 * num2
    print("")
    print("A multiplicação dos valores digitados é: {}".format(multi))

elif tipo_conta == "4":
    print("Cálculo de Divisão selecionado!")
    print("")
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    div = num1 / num2
    print("")
    print("A divisão dos valores digitados é: {}".format(div))

else :
    print("Opção selecionada indisponível! Reinicie o script")
    exit()
