a = input("Entre com o valor de a:\n")


if a%2 == 0:
    print a, " � par"

    if a%3 == 0:
        print a, " � divisivel por 2,3 e 6"
elif a%3 == 0:
    print a, " n�o � divisivel por 2 e 6, mas � divisivel por 3"

else:
    print a, " n�o � divisivel por 2 , 3 e 6"
    

print "fim do script"


