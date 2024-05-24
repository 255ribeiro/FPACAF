#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.1
#Coordenador: Arivaldo Leão de Amorim
#Professor: Fernando Ferraz Ribeiro
#Exemplo: perfis da treliça pelos euxos dos banzos

#Importando Módulos
import rhinoscriptsyntax as rs

#--- Entradas:
#Eixo -- (item, ghdoc)
#Ex Curva do banzo inferior -- (item, float)
#Ey -- (item, float)


#saidas

# Lista com as barras quadradas
Barras = []

# Versor Z auxiliar
vrZ= rs.VectorCreate([0,0,0],[0,0,1])
# Normal da curva
normal = rs.CurveTangent(Eixo, 0,)
# Vetor perpendicular ao conjunto
vecBase = rs.VectorCrossProduct(vrZ, normal)
# Se veBacbase é um vetor nulo
if vecBase == rs.VectorCreate([0,0,0],[0,0,0]):
    # plano auxiliar caso perpendicular
    plAux = rs.PlaneFromNormal(rs.CurveStartPoint(Eixo), normal)
else:
    # Plano Auxiliar caso geral
    plAux = rs.PlaneFromNormal(rs.CurveStartPoint(Eixo), normal, vecBase)
# Decompondo o plano
o1, x1, y1, z1 = plAux
# vetor para mover o plano
vAux = rs.VectorAdd((-Ex/2)*x1,(-Ey/2)*y1)
# Nova origem para o sistema
pOrig = rs.PointAdd( o1, vAux)
# novo plano de desennho
plAux = rs.MovePlane( plAux, pOrig)
# Perfil de tubo quadrado
perfil = rs.AddRectangle(plAux, Ex, Ey)
# criando a peça
Diag = rs.AddSweep1(Eixo, [perfil])
