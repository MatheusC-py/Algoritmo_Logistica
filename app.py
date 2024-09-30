#Importando bibliotecas
import json
import os

#Criando as cidades
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
#Criando as conexoes para fazer um grafo
class Adjacentes:
    def __init__(self,nome, custo):
        self.nome = nome
        self.custo = custo
#Cadastrando a cidade
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
#Apagar cidade
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
#Imprimir Cidade
def imprimirCidades():
    if len(cidadesDict) == 0:
        print("Sua lista de destinos está vázia!")
    else:
        for i in cidadesDict:
            print("Cidade: {}".format(i))
            for adj in cidadesDict[i]["adjacentes"]:
                print("Conexão: {} á {} Km de distância.".format(adj["nome"], adj["custo"]))
            print("=-="*20)


#Main para controlar o código
def main():
    controlador = True
    while controlador == True:
        print("=-="*20)
        print("1. Cadastrar Destino")
        print("2. Apagar Destino") 
        print("3. Imprimir Destinos") 
        print("4. Sair")
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
#Abrindo o arquivo Json para salvar o código
nomeArquivo = 'cidades.json'
if os.path.exists(nomeArquivo):
    with open(nomeArquivo, 'r') as f:
        cidadesDict = json.load(f)
else:
    cidadesDict= {}
#Chamando a main para iniciar a aplicacao
main()
#salvando as altercoes no dicionario
with open(nomeArquivo, 'w') as f:
    json.dump(cidadesDict, f, indent=4)
