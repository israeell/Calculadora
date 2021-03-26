import os
import time

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
    print("Selecione uma opção\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[0]Sair")
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

print("\n" * os.get_terminal_size().lines)
selecao()
opcoes(sel)
while sel != 0:
    selecao()
    opcoes(sel)