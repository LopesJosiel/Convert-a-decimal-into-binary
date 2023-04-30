<<<<<<< HEAD
#Vamos começar
#criando a função que fará sucessivas divisões por 2, antes de utilizá-la
#def myfunction (x):
    #resultado = x // 2 
    #return resultado
#Declarando a variável que vai receber o imput, já declarei como número
#dec = input('escolha um decimal para transformar em binário' )
#ec = int (dec)

#myfunction(dec)
#while (myfunction (dec) % 2 != 0):
    #list_b = []
    #list_b.append((myfunction (dec) % 2))
    #myfunction(myfunction (dec)) #criando uma função autocorrelacionada
#eu queria concatenar todos os elementos de lista para que eles aparecessem juntos no print
#print(list_b)

#fazer com que a lista não apareça vazia, mas apresente todos os restos da divisão inteira por dois!





#=======
#criei um loop para a continuação das transformações ou encerramento, conforme necessidade.
while input ('tecle @ para sair ou enter para continuar') != '@':
    tupla1 = []
    numero1 = int (input ('escolha um decimal para transformar')) #criei a variável numero1 para receber a entrada do número a ser transformado e para aparecer na impressão.
    numero2=numero1
    while numero2 != 0 :
        resto  = numero2 % 2
        tupla1.append(str(resto))
        numero2 //= 2
    tupla2 = list (reversed (tupla1)) # método que inverte as posições dos elementos da lista, o que é necessário para essa transformação.
    tupla3 = "".join(tupla2)
    mensagem = "o decimal {} em binário é {}".format(numero1, tupla3) #aplicação do método format para aplicar variáveis dentro de strings.
    print (mensagem)


