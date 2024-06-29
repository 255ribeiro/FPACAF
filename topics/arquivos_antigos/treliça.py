#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.1
#Coordenador: Arivaldo Leão de Amorim
#Professor: Fernando Ferraz Ribeiro
#Exemplo treliça a partir dos eixos dos banzos

#Importando Módulos
import rhinoscriptsyntax as rs

#entradas

#--- Entradas:
#C1 Curva do banzo superior -- (item, ghdoc)
#C2 Curva do banzo inferior -- (item, ghdoc)
#N1 Número de subdivisões dos banzos -- (item, int)


#Saidas
Cordas =[]
Diag =[]
Bsup =[]
Binf = []




# -> funções
def EixosPerp(lp1, lp2):
    eP = []
    for i in range(len(lp1)):
        lAux = rs.AddLine(lp1[i],lp2[i])
        eP.append(lAux)
    return eP



# -> Função Principal

# Dividir as curvas em partes iguais a N1
pontosC1 = rs.DivideCurve(C1,N1)
pontosC2 = rs.DivideCurve(C2,N1)
#saida dos Banzos
Bsup = rs.AddPolyline(pontosC1)
Binf = rs.AddPolyline(pontosC2)
# lista de pontos para gerar diagonais
pontosDiag = []
#Loop que gera a lista de pontos das diagonais
for i in range(len(pontosC2)):
    # se i é par
    if i % 2 == 0:
        pontosDiag.append(pontosC2[i])
    
    else:
        pontosDiag.append(pontosC1[i])

Diag = rs.AddPolyline(pontosDiag)


Cordas = EixosPerp(pontosC1,pontosC2)