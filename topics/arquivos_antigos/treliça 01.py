#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.1
#Coordenador: Arivaldo Leão de Amorim
#Professor: Fernando Ferraz Ribeiro
#Exemplo treliça a partir do(s) eixos dos banzos

#Importando Módulos
import rhinoscriptsyntax as rs

#entradas


#Saidas
Cordas =[]
Diag =[]
Bsup =[]
Binf = []





# --> Métodos

# -> Método que desenha as cordas verticais
def EixosPerp(lp1, lp2): #recebe duas listas de pontos
    eP = []
    # Cria lista de pontos entre as lista de pontos
    for i in range(len(lp1)):
        lAux = rs.AddLine(lp1[i],lp2[i])
        eP.append(lAux)
    return eP
    
# -> Fim do metodo
    

# -> metodo que desenha o eixo das diagonais
def EixoCordas(banSup, banInf, num):
    # lista de pontos que dividem o banzo superior
    # em num segmentos
    pointsC1 = rs.DivideCurve(banSup,num)
    # lista de pontos que dividem o banzo inferior
    # em num segmentos
    pointsC2 = rs.DivideCurve(banInf,num)
  
    cordas = EixosPerp(pointsC1, pointsC2 )

    diagPt =[]    
    for i in range(N1+1):
        if i % 2 == 0:
            diagPt.append(pointsC1[i])   
        else:
            diagPt.append(pointsC2[i]) 
    
    # desenha polyline entre os pontos intercalados
    eixoDiag = rs.AddPolyline(diagPt)
    
    return eixoDiag , cordas
# -> Fim do metodo

# --> Função Principal
Diag, Cordas = EixoCordas(C1, C2, N1)

Bsup = C1

Binf = C2

# --> Fim