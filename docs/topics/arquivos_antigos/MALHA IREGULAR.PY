#----MALHA DE PONTOS
#- o programa gera uma malha de pontos em x,y
# ssa 15 de jul de 2017

#--- Importando modulos
import rhinoscriptsyntax as rs
 
#--- Entradas:
#O origem da malha -- (item, ghdoc)
#Lx Listas de vãos no sentido x -- (list, float)
#Ly Listas de vãos no sentido y -- (list, float)

#-- Tratando entradas:
# caso a entrada O não seja alimentada...
if not O:
    #... é criado um ponto nas coordenas (0,0,0)
    #    para ser usado como a origem da malha
    O = rs.AddPoint([0, 0, 0])

#--- Saidas:
# P - lista com os pontos da malhaa
P = []



#--- Função principal:
#- Manipulando listas
# Acrescentando valor 0 no início da lista de vãos Lx
Lx.insert(0,0.0)
# Acrescentando valor 0 no início da lista de vãos Ly
Ly.insert(0,0.0)

print Lx
#- limpando variavel xAux para Loop x
xAux = 0.0
#- Loop x
for i in range(len(Lx)):
    xAux = xAux + Lx[i]
    #- limpando variavel yAux para Loop y
    yAux = 0.0
    #- Loop y
    for j in range(len(Ly)):
        yAux = yAux + Ly[j]
        #cria um ponto com as coordenadas xAux, yAux
        ptAux = rs.AddPoint(xAux,yAux,0)
        #cria o ponto da malha somando o ponto ptAux ao ponto O
        pt = rs.PointAdd(O,ptAux)
        #coloca o ponto na lista de saidas
        P.append(pt)
#--- FIM
