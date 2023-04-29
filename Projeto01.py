#Vamos começar
#criando a função que fará sucessivas divisões por 2, antes de utilizá-la
def myfunction (x):
    resultado = x // 2 
    return resultado
#Declarando a variável que vai receber o imput, já declarei como número
dec = float (input('escolha um decimal para transformar em binário'))
list_b = ()
myfunction(dec)
while (myfunction (dec) % 2 != 0):
    list_b.append((myfunction (dec) % 2))
    myfunction(dec)
#eu queria concatenar todos os elementos de lista para que eles aparecessem juntos no print
print(list_b)





