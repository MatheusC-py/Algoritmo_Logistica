#Importando bibliotecas
import json
import os

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
    cidade = Cidades(nomeCid)
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
    print(cidade) #EM CONSTRUÇAO

def main():
    controlador = True
    while controlador == True:
        print("=-="*10)
        print("1. Cadastrar cidade")
        print("2. Apagar cidade") #Em construção
        print("3. Imprimir cidades") #Em construção
        print("4. Sair")
        print("=-="*10)
        opcao = int(input("Escolha uma opção: "))
        os.system('cls')

        if opcao == 1:
            cadastrarCidade()
        elif opcao == 2:
            apagar = input("Digite a cidade a ser apagada: ")
            apagarCidade(apagar)
        elif opcao == 4:
            controlador = False

nomeArquivo = 'cidades.json'
if os.path.exists(nomeArquivo):
    with open(nomeArquivo, 'r') as f:
        cidadesDict = json.load(f)
else:
    cidadesDict= {}

main()

with open(nomeArquivo, 'w') as f:
    json.dump(cidadesDict, f, indent=4)
