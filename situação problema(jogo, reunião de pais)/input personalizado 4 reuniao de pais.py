import inputs

nomes = []
ausentes = []
presentes = []
while True:
    print("MENU")
    print("[ 1 ] cadastrar um nome")
    print("[ 2 ] exibir o total de pais")
    print("[ 3 ] exibir a lista de nomes em ordem alfabética")
    print("[ 4 ] permitir a consulta de um nome")
    print("[ 5 ] relatorio de pais presentes e ausentes")
    print("[ 6 ] sair")
    opção = inputs.input_int("escolha uma opção")
    
    if opção == 1:
        nome = inputs.input_str("digite o nome do pai que vc deseja cadastrar")
        if nome in nomes:
            print("esse nome já está na lista de pais") 
        else:
            nomes.append(nome)
            print("Nome cadastrado com sucesso")
    elif opção == 2:
        print("O total de pais inscritos foram: ", len(nomes))
    elif opção == 3:
        nomes.sort()
        for nome in nomes:
            print(nome)
    elif opção == 4:
        for nome in nomes:
            print(nome)
            nome = inputs.input_str('nome está na lista de ausentes? [s ou n]')
            if nome == 's':
                print("adicionado na lista de presentes")
                presentes.append(nome)
            else:
                print("adicionado na lista de ausentes")
                ausentes.append(nome)
    elif opção == 5:
        print("")
        print("relatorio de pais presentes: ")
        for nome in nomes:
            print(nome)
        print("")
        print("relatorio de pais ausentes: ")
        for ausente in ausentes:
            print(ausente)
        print("")
    elif opção == 6:
        print("você saiu")
        break
    else:
        print("essa opção não existe")