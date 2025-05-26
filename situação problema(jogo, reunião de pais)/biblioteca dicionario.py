#--------DICIONARIOS-------
lista_livros = []

while True:
    print("MENU")
    print("[ 1 ] cadastrar livro")
    print("[ 2 ] exibir quantidade livros cadastrados")
    print("[ 3 ] exibir livros cadastrados")
    #print("[ 4 ] lista de titulos")
    print("[ 4 ] pesquisar livro")
    print("[ 5 ] sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("")
        print("Agora vamos cadastrar os livros com as informações corretas")
        isbn = int(input("Digite o isbn(único): "))
        titulo = input("Digite o titulo do livro: ")
        autor = input("Digite o autor do livro: ")
        categoria = input("Digite a categoria do livro: ")
        ano = int(input("Digite o ano de publicação do livro: "))
        
        #CRIAR
        livro = {
        "ISBN": isbn,
        "titulo": titulo,
        "autor" : autor,
        "categoria" : categoria,
        "ano_publicacao" : ano
        }
        
        lista_livros.append(livro)
        
    elif opcao == 2:
        #exibindo todos
        print("o total de livros cadastrados foram ", len(lista_livros))
        
        #for livro in lista_livros:
          #  for chave, valor in livro.items():
           #     print(f"{chave} - {valor}")   
    elif opcao == 3:
        #EXIBIR
        for livro in lista_livros:
            for chave, valor in livro.items():
                print(f"{chave} - {valor}")
            print("")
        #print(livro)
        #for chave, valor in lista_livros():
           # print(f"{chave}: {valor}")
        
    elif opcao == 4:
        pesquisar_livro = int(input("Digite o ISBN do livro para pesquisar ele: "))
        for livro in lista_livros:
            if pesquisar_livro in lista_livros:
                print("Esse livro está na biblioteca")
            else:
                print("Esse livro não está cadastrado!")
    elif opcao == 5:
        print("você saiu")
        break
    else:
        print("essa opção não existe")