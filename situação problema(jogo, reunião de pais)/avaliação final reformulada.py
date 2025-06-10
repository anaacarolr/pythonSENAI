#--------DICIONARIOS-------
import inputs

lista_alunos = []

def cadastrar_aluno():
        print("")
        print("Agora vamos cadastrar o aluno com as suas informações")
        nome = input("Digite o nome do aluno : ")
        n1 = input("Digite a nota 1 do aluno: ")
        n2 = input("Digite a nota 2 do aluno: ")
        n3 = input("Digite a nota 3 do aluno: ")
        
        #CRIAR
        cadastro = {
        "Nome do aluno": nome,
        "Nota 1": n1,
        "Nota 2" : n2,
        "Nota 3" : n3,
        }
        
        lista_alunos.append(cadastro)
    
def verificar_situacao(media):
    if media >= 7:
        print("APROVADO")
        print("Parabéns")
    elif media <= 5:
        print("REPROVADO")
    elif media >= 5.1:
        print("RECUPERAÇÃO")
        print("estude um pouco mais!!")
    else:
        return 


def calcular_media(n1, n2, n3):
    media = n1 + n2 + n3
    resultado = media / 3
    print(resultado)

while True:
    print("MENU")
    print("[ 1 ] cadastrar aluno")
    print("[ 2 ] exibir quantidade de alunos cadastrados")
    print("[ 3 ] exibir alunos cadastrados")
    print("[ 4 ] exibir média")
    print("[ 5 ] exibir se está reprovado ou não")
    print("[ 6 ] sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        cadastrar_aluno()
   
    elif opcao == 2:
        #exibindo todos
        print("o total de alunos cadastrados foram ", len(lista_alunos))  
    elif opcao == 3:
        #EXIBIR
        for cadastro in lista_alunos:
            for chave, valor in cadastro.items():
                print(f"{chave} - {valor}")
            print("")
              
    elif opcao == 4:
        n1 = inputs.input_float( " Digite a nota 1 número: ")
        n2 = inputs.input_float(" Digite a nota 2 número: ")
        n3 = inputs.input_float(" Digite nota 3 número: ")
        calcular_media(n1, n2, n3)
        
    elif opcao == 5:
        media = float(input( " Digite a média de seu aluno: "))
        print("para saber a média você precisa verifcar na opção 3")
        verificar_situacao(media)
 
    elif opcao == 6:
        print("você saiu")
        break
    else:
        print("essa opção não existe")