#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo de malha regular de pontos

#importando modulos
import rhinoscriptsyntax as rs
import GhPython as gh

#--- Entradas:
#Dx distância em x dos prontos da malha -- (item, float)
#Nx número de pontos da manha na direção x -- (item, int)
#Dy distância em y dos prontos da malha -- (item, float)
#Ny número de pontos da manha na direção y -- (item, int)

if  O is None:
    O = rs.AddPoint(0,0,0)


#--- Saidas:
# P - lista com os pontos da malha
P = []
Leixos =[]
#--- Função principal:

for i in range(Nx):
    PAux = []
    for j in range(Ny):
        pt = rs.PointAdd( [i*Dx, j*Dy,0], O)
        PAux.append(pt)
    eixo = rs.AddLine(PAux[0],PAux[-1])
    Leixos.append(eixo)
    P = P + PAux

       
