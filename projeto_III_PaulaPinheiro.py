from copy import deepcopy
from collections import deque
import csv

class Rios:
    rios_temp = []

    def __init__(self, arquivo):
        self.matriz = arquivo 
        self.lista_coord = [] 
        self.coord = self.forma_coord() 
        self.queue_conf = deque() 
        self.lista_rios = [] 

        self.forma_rios(self.coord[0])
        self.__str__()

    @property
    def matriz(self):
        return self.__matriz
    @matriz.setter
    def matriz(self, arquivo):
        try:
            with open(arquivo, mode = 'r', encoding= 'utf-8') as arquivo_bruto:
                conteudo = csv.reader(arquivo_bruto, delimiter = ';')
                self.__matriz = list(conteudo)
        except: print('\nErro: Falha na leitura do arquivo.\n')

    def forma_coord(self):
        for y, linha in enumerate(self.matriz):
            for x, ponto in enumerate(linha):
                if ponto == '1':
                    self.lista_coord.append((y,x))
        self.coord = deepcopy(self.lista_coord)
        return self.coord

    def forma_rios(self, ponto):
        Rios.rios_temp.append(ponto)
        self.coord.remove(ponto)
        antes = (ponto[0], ponto[1] - 1)
        depois = (ponto[0], ponto[1] + 1)
        acima = (ponto[0] - 1, ponto[1])
        abaixo = (ponto[0]  + 1, ponto[1])

        if antes in self.coord and antes not in self.queue_conf:
            self.queue_conf.append(antes)
        if depois in self.coord and depois not in self.queue_conf:
            self.queue_conf.append(depois)
        if acima in self.coord and acima not in self.queue_conf:
            self.queue_conf.append(acima)
        if abaixo in self.coord and abaixo not in self.queue_conf:
            self.queue_conf.append(abaixo)
        while len(self.queue_conf) > 0:
            ponto = self.queue_conf.popleft()
            self.forma_rios(ponto)
        if Rios.rios_temp:
            self.lista_rios.append(len(Rios.rios_temp))
            Rios.rios_temp = []
        if not self.queue_conf and self.coord:
            ponto = self.coord[0]
            self.forma_rios(ponto)
        return self.lista_rios

    def __str__(self):
        string = '\n----------------------------\n'
        string += f"{'MATRIZ':^{28}}\n"
        for linha in self.matriz:
            string += f"{str(linha):^{28}}\n"
        string += '----------------------------\n\n'
        string += 'COORDENADAS - INDICES DOS RIOS\n'
        string += str(self.lista_coord) + '\n\n'
        string += 'RESPOSTA:' + str(sorted(self.lista_rios))
        return print(string)

rios = Rios('mapa_original_PaulaPinheiro.csv')

