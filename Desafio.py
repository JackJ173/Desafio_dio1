menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair

Digite uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()
    #Então se a opção for Depósito, faça:
    if opcao == "d":
        quantia_deposito = float(input("Digite o valor do depósito: ")) #Aqui o usuario coloca o valor da quantia desejada em sua conta

        if quantia_deposito > 0: #Aqui garante que o valor é maior que 0
            saldo = saldo + quantia_deposito #Preciso que a variavél "saldo" receba quantas quantias eu desejar
            extrato = extrato + f"O Deposito foi de R$: {quantia_deposito:.2f}\n" #Aqui estou contatenando a string, adicionando um texto ao final da variável extrato, isso garante que eu armezene diversos extratos
        else:
            print("Digite um valor válido")
    #Então se a opção for saque, faça:
    elif opcao == "s": 
        quantia_saque = float(input("Digite um valor para sacar: ")) #Recebe o valor de saque o usuário
        quantia_maior_Que_saldo = quantia_saque > saldo #Aqui compara se o valor que o usuário quer sacar é maior que o saldo
        quantia_limite =  quantia_saque > limite # Verifica se o valor do saque ultrapassa o limite (500 reais) permitido por saque
        quantia_numero_saques = numero_saques >= LIMITE_SAQUES #Aqui serve para controlar quantas vezes o usuário sacou o dinheiro, antes de permitir um novo saque, você verifica
        if quantia_maior_Que_saldo:
            print("Saldo indisponível!")
        elif quantia_limite:
            print("O Máximo que você pode sacar hoje é de até [R$ 500,00].")
        elif quantia_numero_saques:
            print("Você atingiu a quantidade de saques diarios [3]!")
        elif quantia_saque > 0: #Aqui garante que o valor de saque seja maior que 0
            saldo = saldo - quantia_saque #Saldo recebe o saldo - qunatia de saque, aqui faz com que o saldo diminua com os saques do usuário
            extrato = extrato + f"Saque realizado no valor de R$ {quantia_saque:.2f}\n"
            numero_saques = numero_saques + 1 #Aqui estou atribuindo mais "1" a numero_saques para salve e vá até o limite de saques qe é 3 
        else:
            print("Digite um valor válido")
        #Enquanto a opção for Extrato, faça:
    elif opcao == "e":
        print("\n======== EXTRATO ======")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("==========================")
        #Enquanto a opção for Sair, faça:
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")