#Importando bibliotecas
import json
import os

class Itens:
    def __init__(self, nome, altura, largura, comprimento, valor):
        self.nome = nome
        self.altura = altura
        self.largura = largura 
        self.comprimento = comprimento 
        self.valor = valor

    def salvarItem(self):
            itensDict[self.nome] = {
                'altura' : self.altura,
                'largura' : self.largura,
                'comprimento' : self.comprimento,
                'valor' : self.valor
            }

class Cidades:
    def __init__(self, nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []

    def adcionarAdjacente(self,adjacente):
        self.adjacentes.append(adjacente)

    def imprimirAdjacentes(self):
        for i in self.adjacentes:
            print(i.Cidades.nome, i.custo)
    
    def salvarCidade(self):
        cidadesDict[self.nome] = {
            'visitado': False,
            'adjacentes': [
                {'nome' : adj.nome,'custo' : adj.custo}
                for adj in self.adjacentes
            ]
        }

class Adjacentes:
    def __init__(self,nome, custo):
        self.nome = nome
        self.custo = custo

def cadastrarCidade():
    nomeCid = input("Digite o nome da cidade a ser cadastrada: ")
    cidade = Cidades(nomeCid.capitalize())
    os.system('cls')
    print("CADASTRE AS CIDADES VIZINHAS DE {}".format(nomeCid))
    
    while(True):
        controle = input("Existe uma cidade vizinha para cadastrar? S = Sim/ N = Não\n:").strip().upper()
        if controle != 'S':
            break
        else:
            nomeAdj = input("Digite o nome da cidade a ser adicionada como vizinha: ")
            custoAdj = int(input("Digite a distância da cidade em KM: "))
        
            cidade.adcionarAdjacente(Adjacentes(nomeAdj,custoAdj))
            print("CIDADE CADASTRADA COM SUCESSO")
            os.system('cls')

    cidade.salvarCidade()

def apagarCidade(cidade): 
    if len(cidadesDict) == 0:
        print("Sua lista de destinos está vazia!")
    else:
        cidade = cidade.capitalize() 
        valorRemovido = cidadesDict.pop(cidade, None)
        if valorRemovido == None:
            print('Destino não encontrado, por favor tente novamente!')
        else:
            print('{} removido com sucesso!'.format(cidade))

def imprimirCidades():
    if len(cidadesDict) == 0:
        print("Sua lista de destinos está vázia!")
    else:
        for i in cidadesDict:
            print("Cidade: {}".format(i))
            for adj in cidadesDict[i]["adjacentes"]:
                print("Conexão: {} á {} Km de distância.".format(adj["nome"], adj["custo"]))
            print("=-="*20)

def manutencaoDestinos():
    controlador = True
    while controlador == True:
        print("=-="*20)
        print("1. Cadastrar Destino")
        print("2. Apagar Destino") 
        print("3. Imprimir Destinos") 
        print("4. Voltar para o menu anterior")
        print("=-="*20)
        opcao = int(input("Escolha uma opção: "))
        os.system('cls')

        if opcao == 1:
            cadastrarCidade()
        elif opcao == 2:
            apagar = input("Digite a cidade a ser apagada: ")
            apagarCidade(apagar)
        elif opcao == 3:
            imprimirCidades()
        elif opcao == 4:
            controlador = False
        
    with open(nomeArquivoCidades, 'w') as f:
        json.dump(cidadesDict, f, indent=4)

def manutencaoItens():
    controlador = True
    while controlador == True:
        print("=-="*20)
        print("1. Cadastrar Itens")
        print("2. Apagar Itens")
        print("3. Imprimir Itens")
        print("4. Voltar para o menu anterior")
        print("=-="*20)
        opcao = int(input("Escolha uma opção: "))
        os.system('cls')

        if opcao == 1:
            print("EM CONSTRUÇÃO")
        elif opcao == 2:
            print("EM CONSTRUÇÃO")
        elif opcao == 3:
            print("EM CONSTRUÇÃO")
        elif opcao == 4:
            controlador = False
    
    with open(nomeArquivoItens, 'w') as f:
        json.dump(itensDict, f, indent=4)

def main():
    controlador = True
    while controlador == True:
        print("=-="*20)
        print("1. Manutenção de Destinos")
        print("2. Manutenção de Itens")
        print("3. Otimização de Entregas")
        print("4. Sair")
        print("=-="*20)
        opcao = int(input("Escolha uma opção: "))
        os.system('cls')

        if opcao == 1:
            manutencaoDestinos()
        elif opcao == 2:
            manutencaoItens()
        elif opcao == 3:
            print("EM CONSTRUÇÃO")
        elif opcao == 4:
            controlador = False

nomeArquivoItens = 'itens.json'
nomeArquivoCidades = 'cidades.json'

if os.path.exists(nomeArquivoCidades):
    with open(nomeArquivoCidades, 'r') as f:
        cidadesDict = json.load(f)
else:
    cidadesDict= {}

if os.path.exists(nomeArquivoItens):
    with open(nomeArquivoItens, 'r') as f:
        itensDict = json.load(f)
else: 
    itensDict = {}

main()

with open(nomeArquivoCidades, 'w') as f:
    json.dump(cidadesDict, f, indent=4)

with open(nomeArquivoItens, 'w') as f:
    json.dump(itensDict, f, indent=4)
