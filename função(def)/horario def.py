import datetime

def hora_atual():
    horario = datetime.datetime.now().hour
    return horario

def mostrar_nome(nome) :
    if hora_atual() <= 5 : 
        print("BOA MADRUGADA", nome)
        
    elif hora_atual() <= 12 :
        print("BOM DIA", nome)
        
    elif hora_atual() <= 19 :
        print("BOA TARDE", nome)
        
    elif  hora_atual() <= 19 :
        print("BOA NOITE", nome)
    
nome = input("QUAL É O SEU NOME? ")

mostrar_nome(nome)