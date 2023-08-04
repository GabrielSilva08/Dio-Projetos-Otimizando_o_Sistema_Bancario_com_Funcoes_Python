def main():
    saldo_total = 0 #Variável inteira que contém o total de saldo do cliente
    extrato = [] #Lista que fará um track das operações de saque, depósito e da variável saldo_total
    numero_de_saques = 0 #Variável inteira contadora do número de saques feito pelo cliente
    usuarios = {} #Dicionário com chave string (CPF) e valores em forma de listas de strings
    contas = {} #Dicionário com chave inteira (Nconta) e valores em forma de listas de string
    Nconta = 1 #Variável inteira que faz um tracked com relação ao número de contas dos usuários
    while True: #Inicio do menu
        print("""
========== Menu =========
[0] -> Depositar
[1] -> Sacar
[2] -> Visualizar extrato
[3] -> Criar novo usuário
[4] -> Criar nova conta
[5] -> Listar contas              
[6] -> Sair
=========================""") #Fim do menu
        operacao = int(input("Operação desejada: ")) #Solicitação de qual operação realizar
        if operacao == 0: #Operação de depósito
            saldo_total = deposito(saldo_total, extrato)
        elif operacao == 1: #Operação de saque
            saldo_total, numero_de_saques = saque(saldo = saldo_total, numero_de_saques = numero_de_saques, extrato = extrato)
        elif operacao == 2: #Operação de extrato
            exibirExtrato(extrato, saldo=saldo_total)
        elif operacao == 3: #Operação de criar novo usuário
            criarNovoUsuario(usuarios)
        elif operacao == 4: #Operação de criar nova conta
            Nconta = criarNovaConta(usuarios, contas, Nconta)     
        elif operacao == 5: #Operação de listar todas as contas criadas
             listarContas(contas)
        elif operacao == 6: #Operação de saída
            break
        else:
            print("Operação inválida! Tente novamente.")
    print("Sistema encerrado com sucesso!")

def deposito(saldo, extrato, /):
    """
    Realiza a operação de depósito na conta cliente. retorna o saldo atualizado.

    Parâmentros:
    - saldo -> float
    - extrato -> lista de tuplas (string, float)

    Retorno:
    - saldo -> float 
    """
    aux = float(input("Por favor, informe o quanto deseja depositar: R$"))
    if aux < 0:
        print("Operação inválida! Valor informado não positivo.")
    else:
        saldo += aux
        extrato.append(("Depósito", aux)) #Atualização do extrato
    return saldo
def saque(*, saldo, extrato, numero_de_saques):
    """
    Realiza a operação de saque na conta cliente, levando em conta o número de saques e o limite máximo de valor passado.
    retorna o saldo atualizado e o número de saques incrementado ou não.

    Parâmentros:
    - saldo -> float
    - extrato -> lista de tuplas (string, float)
    - numero_de_extrato -> int

    Retorno:
    - saldo -> float
    - numero_de_saques -> int
    """
    if numero_de_saques < 3:
                aux = float(input("Por favor, informe o quanto deseja sacar: R$"))
                if aux > 500:
                    print("Saque desejado ultrapassou o limite (R$500)!")
                elif aux < 0:
                    print("Operação inválida! Valor informado não positivo.")
                elif aux <= saldo:
                    saldo -= aux
                    extrato.append(("Saque", aux)) #Atualização do extrato
                    numero_de_saques += 1
                else:
                    print("Saldo insuficiente para saque! Por favor, deposite mais saldo.")
    else:
        print("Limite diário de saques atingido! Por favor, solicite outra operação.")
    return saldo, numero_de_saques

def exibirExtrato(extrato, /, *, saldo):
    """
    Realiza a operação de exibir o extrato na conta cliente, ou seja, o histórico de operações de saque
    e depósito. retorna nada.

    Parâmentros:
    - extrato -> lista de tuplas (string, float)
    - saldo -> float 
    """
    print("========== Extrato ==========")
    for i, op in enumerate(extrato):
            print(f"Operação de {op[0]} - {op[1]} ({i+1})")
    print("=============================")
    print("Saldo atual = R${:.2f}".format(saldo))

def criarNovoUsuario(usuarios):
    """
    Realiza a operação de criação de novo usuário, restrigindo aqueles com mesmo CPF. retorna nada.

    Parâmetros:
    - usuarios -> dicionário de chaves string e valores dicionário, sendo esse s
                  tanto as chaves e os valores do tipo string.
    """
    cpf = input("Por favor, informe o CPF do usuário (###########): ")
    if cpf in usuarios:
         print("CPF já cadastrado! Encerrando operação.")
         return
    nome = input("Nome completo do usuário: ")
    nascimento = input("Data de nascimento: ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.update({cpf: {"nome":nome, "nascimento":nascimento, "endereco":endereco}})
    print("Usuário criado!")
    return

def criarNovaConta(usuarios, contas, Nconta):
    """
    Realiza a operação de criação de nova conta. Retorna o número total de contas criadas menos 1.

    Parâmetros:
    - usuarios -> dicionário de chaves string e valores dicionários, sendo esses 
                  tanto as chaves e os valores do tipo string.
    - contas -> dicionário de chaves int e valores dicionários, sendo esses com dois pares de valores,
                na forma: {string:string, string:int} 
    - Nconta -> int

    Retorno:
    - Nconta -> int
    """
    cpf = input("Por favor, informe o CPF do usuário (###########): ")
    if cpf not in usuarios:
         print("Usuário não cadastrado! Por favor, cadastre um usuário.")
         return Nconta
    contas[Nconta] = {"cliente":usuarios[cpf]["nome"], "numero_da_conta":Nconta}
    Nconta += 1
    print("Conta criada!")
    return Nconta

def listarContas(contas):
    """
    Realiza a operação de listar todas as contas criadas. retorna nada.

    Parâmetros:
    - contas -> dicionário de chaves int e valores dicionários, sendo esses com dois pares de valores,
                na forma: {string:string, string:int}
    """
    c = 1
    print("===== Contas criadas =====")
    for conta in contas:
        print(f"-- Conta {c} --\nAgência: 0001\nConta: {contas[conta]['numero_da_conta']}\nCliente: {contas[conta]['cliente']}\n")
        c += 1
    print("==========================")

if __name__ == "__main__":
    main()