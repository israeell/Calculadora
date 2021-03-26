import os
import time
import math

#cabeçalho
def cabecalho():
    linha = '-_'
    msg = 'bem vindo(a) à calculadora de python'

    print(linha*30)
    print(msg.capitalize().center(55))
    print(linha*30)

#seleção de opções
def selecao():
    global sel
    cabecalho()
    print("Selecione uma opção\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[5]Raiz Quadrada\n[6]Expoente\n[7]Raiz Cúbica\n[8]Seno\n[9]Cosseno\n[10]Tangente\n[0]Sair")
    sel = int(input())

def opcoes(sel):
    print("\n" * os.get_terminal_size().lines)
    cabecalho()
    print("Digite os números que você deseja fazer a operação \nSegue o exemplo: 1 2 3 4 ")
    nums = []
    if sel == 0:
        print("\n" * os.get_terminal_size().lines)
        cabecalho()
        print("Obrigado por usar a calculadora!")
        time.sleep(2)
    
    
    # soma
    elif sel == 1:
        n = input().split()
        for i in n:
            i = int(i)
            nums.append(i)
        print(f'Sua soma deu: {sum(nums)}')
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    #subtração
    elif sel == 2:
        n = input().split()
        for i in n:
            i = int(i)
            nums.append(i)
        sub = nums[0]
        for c in range(len(nums)-1):
            sub -= nums[c+1]
        print(f'Sua subtração deu: {sub}')
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    #multiplicação
    elif sel == 3:
        n = input().split()
 
        for i in n:
            i = int(i)
            nums.append(i)
        mul = nums[0]
        for c in range(len(n)-1):
            mul *= nums[c+1]
        
        print(f'Sua multiplicação deu: {mul}')
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    #divisão
    elif sel == 4:
        n = input().split()
        for i in n:
            i = int(i)
            nums.append(i)
        div = nums[0]
        for c in range(len(n)-1):
            div /= nums[c+1]
        print(f'Sua divisão deu: {div}')
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    # Raíz Quadrada
    elif sel == 5:
        n = float(input())
        print('A raiz quadrada de {} é: {:.2f}'.format(n, n**0.5))
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)

    # Expoente
    elif sel == 6:
        n = input().split()
        for i in n:
            i = float(i)
            nums.append(i)
        resul = nums[0] ** nums[1]
        print('O número {} elevado à {} é: {}'.format(nums[0], nums[1], resul))
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    # Raíz cúbica
    elif sel == 7:
        n = float(input())
        print('A raíz cúbica de {} é: {:.2f}'.format(n, n**(1/3)))
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    # Seno
    elif sel == 8:
        n = float(input())
        print('O seno de {} é: {:.2f}'.format(n, math.sin(n)))
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)

    # Cosseno
    elif sel == 9:
        n = float(input())
        print('O cosseno de {} é: {:.2f}'.format(n, math.cos(n)))
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
    # Tangente
    elif sel == 10:
        n = float(input())
        print('A tangente de {} é {:.2f}'.format(n, math.tan(n)))
        time.sleep(2)
        print("\n" * os.get_terminal_size().lines)
    
print("\n" * os.get_terminal_size().lines)
selecao()
opcoes(sel)
while sel != 0:
    selecao()
    opcoes(sel)
