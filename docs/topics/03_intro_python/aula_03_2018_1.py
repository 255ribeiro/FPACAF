#! python2


from __future__ import division
import math as m

# definicao da funcao blondel
def blondel(h):
    # formula de blodel
    p = .63 - (2 * h)
    #retorna o piso
    return p

# entrada de dados
# desnivel da escada
des = input('entre com desnivel ')
#numero maxino de espelhos
espM = input('entre com o espelho maximo ')

# calcula numero de espelhos
nEsp = m.ceil(des/espM)


print "Numero de espelhos = ", nEsp

# espelho real 3 casas decimais
espR = round(des/nEsp , 3)

print 'espelho real ', espR

# chamada da funcao blondel
piso = blondel(espR)

print "piso = ", piso
