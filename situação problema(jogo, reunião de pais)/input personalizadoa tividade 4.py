
import inputs

nomes = []
while True:
    print("MENU")
    print("[ 1 ] cadastrar um nome")
    print("[ 2 ] exibir o total de inscritos")
    print("[ 3 ]exibir a lista de nomes em ordem alfabética")
    print("[ 4 ] permitir a consulta de um nome")
    print("[ 5 ] sair")
    opção = inputs.input_int("escolha uma opção: ")
    if opção == 1:
        nome = inputs.input_str("digite o nome que você deseja cadastrar")
        if nome in nomes:
            print("Nome cadastrado com sucesso")
        else:
            nomes.append(nome)
            print("Nome cadastrado com sucesso")
    elif opção == 2:
        print("O total de inscritos foram: ", len(nomes))
    elif opção == 3:
        for nome in nomes:
            print(nome)
    elif opção == 4:
        nome = inputs.input_str("digite o nome que você deseja consultar:")
        if nome in nomes:
            print(nome, "está na lista")
            if variavel == "sim":
                nomes.remove(nome)
                print("nome removido")
            elif variavel == "não":
                print("o nome ainda permanece na lista")
        else:
            vari1 = inputs.input_str("nome não encontrado deseja adiciona-lo [sim ou não] ")
            if vari1 == "sim":
                nomes.append(nome)
                print("o nome foi adicionado à lista")
            elif  vari1 == "não":
                print("ok")
            else:
                print("essa opção não existe")
    elif opção == 5:
        print("você saiu")
        break
    else:
        print("essa opção não existe")