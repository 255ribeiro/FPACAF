#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.1
#Coordenador: Arivaldo Leão de Amorim
#Professor: Fernando Ferraz Ribeiro
#Exemplo pavimentos multiplos


import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d

#--- Entradas:
#Po: ponto no terreo -- (item, Point3d)
#Contorno: contorno da laje -- (List, ghdoc)
#PD: distancia piso a piso-- (item, float)
#h_laje: altura da laje -- (item, float)
#N_andares: Numerod e andares y -- (item, int)


#Saidas
# lista de pavimentos
Pav = []
#lista para teste de codigo
Teste = []


#função principal

# cria face atrves das linhas de contorno
face = rs.AddPlanarSrf(Contorno)
#ponto auxiliar para linha de extrude da laje
P2 = rs.PointAdd(Po, [0,0,h_laje])
# linha de extrude da laje
lAux = rs.AddLine(Po,P2)
# extrusão da laje na altura h_laje
laje = rs.ExtrudeSurface(face,lAux)
Pc = rs.SurfaceAreaCentroid(face)

vecAux = rs.VectorCreate( Po, Pc[0])
Teste.append(vecAux)
rs.MoveObject(laje, vecAux)


#coloca a laje na lista de pavimentos de saida
Pav.append(laje)

# Loop de copia dos pavimentos
for i in range(N_andares):
    # 
    zAux = Po.Z + (i * PD) + h_laje
    pAux = Point3d(Po.X,Po.Y, zAux)
    vecAux = rs.VectorCreate(pAux, Po)
    ljAux = rs.CopyObject(laje, vecAux)
    Pav.append(ljAux)