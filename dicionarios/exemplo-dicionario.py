
#--------DICIONARIOS-------

#CRIAR
aluno = {
    "nome": "carol",
    "idade": 16,
    "altura" : 1.62,
    "matricula" : True 
}

materia = {
    "professor": "DAILSON",
    "matéria": "história",
    "assunto": "guerras, revoluções etc"
}

materia2 = {
    "professor": "GABI",
    "matéria": "geografia",
    "assunto": "países, ONU, localização etc"
}

materia3 = {
    "professor": "LUCIANO",
    "matéria": "biologia",
    "assunto": "corpo humano, plantas, universo etc"
}

print(materia)
#ADICIONAR CAMPO
aluno["peso"] = 62

#ALTERAR CAMPO
aluno["idade"] = 17

#DELETAR CAMPO
del  aluno["altura"]


#VERIFICAR
if "altura" in aluno:
    print("altura existente")
else :
    print("altura inexistente")
    
#EXIBIR
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
    
#exibir uma lista de dicionarios
lista_materia = [materia, materia2, materia3]
    #escolhendo os campos
for materia in lista_materia:
    print(f"{materia['matéria']}")
    
    #exibindo todos
for materia in lista_materia:
    for chave, valor in materia.items():
        print(f"{chave} - {valor}")
    print()