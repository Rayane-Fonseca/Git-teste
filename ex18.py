                  #Correção

#validação do nome
while True:
    nome = input("Digite o seu nome: ")
    if len(nome) >= 3:
        break
    else:
        print("Erro: o nome deve conter pelo menos 3 caracteres")
   
#validação da idade     
while True:
    idade = int(input("Digite a sua idade: "))
    if 0 <= idade <= 150:
        break
    else:
        print("Erro: a idade deve ser entre 0 e 150")
        
#validação do salário
while True:
    salario = float(input("Digite o seu salário: "))
    if salario > 0:
        break
    else:
        print("Erro: o salário deve ser maior que zero")
        
#validação de gênero
while True:
    genero = input("Digite seu gênero (F para Feminino, M para Masculino, O para Outros)").upper()
    if genero in ["F", "M", "O"]:
        break
    else:
        print("Erro: Gênero Inválido")
        
#validção estado civil
while True:
    estado_civil = input("Digite seu estado civil (S para Solteiro, C para Casado, V para Viúvo, D para Divorciado)").upper()
    if estado_civil in ["S", "C", "V", "D"]:
        break
    else:
        print("Erro: Estado civil inválido")
        
#exibir informações
print("\n Informações validadas com sucesso")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")

if genero == "F":
    print("Gênero: Feminino")
elif genero == "M":
    print("Gênero: Masculino")
else:
    print("Gênero: Outros")
    
if estado_civil == "S":
    print("Estado Civil: Solteiro")
elif estado_civil == "C":
    print("Estado Civil: Casado")
elif estado_civil == "V":
    print("Estado Civil: Viúvo")
else:
    print("Estado Civil: Divorciado") 