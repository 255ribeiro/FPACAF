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



# versor Z auxiliar
vrZ= rs.VectorCreate([0,0,1],[0,0,0])

# -> Tratando variáveis
# Se o numero de divisões não foi lido...
if not N1:
    # ... considerar N1 = 10
    N1 = 10

# se a entrada C2 contem um valor numérico
if type(C2) == float:
    # criar um offset da curva C1 na distância C2
    # na direção oposta ao versor Z auxiliar
    C2 = rs.OffsetCurve(C1,vrZ,C2)

if OfSup:

    C1 = rs.OffsetCurve(C1,vrZ,OfSup)

if OfInf :

    C2 = rs.OffsetCurve(C2,vrZ,-OfInf)

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

        
        
    
    # lista dos pontos de indice par do banzo sup
    banSupPt = pointsC1[0::2]
    # lista dos pontos de indice impar do banzo inf
    banInfPt = pointsC2[1::2]
    
    # lista vazia com tamanho igula a banSupPt + banInfPt
    diagPt = [None]*(len(banSupPt)+len(banInfPt))
    
    # intercalando as listas
    diagPt[::2] = banSupPt
    diagPt[1::2] = banInfPt
    
    # desenha polyline entre os pontos intercalados
    eixoDiag = rs.AddPolyline(diagPt)
    # retorna os eixos
    return [eixoDiag] , cordas
# -> Fim do metodo

# --> Função Principal
Diag, Cordas = EixoCordas(C1, C2, N1)

Bsup = C1

Binf = C2

# --> Fim