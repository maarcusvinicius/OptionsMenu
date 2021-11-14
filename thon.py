from time import sleep
r1 = 0
r2 = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        r1 = v1 + v2
        print('A soma entre {} e {} é {}'.format(v1, v2, r1))
        print('=-' * 12)
        sleep(1)
    if opcao == 2:
        r2 = (v1 * v2)
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, r2))
        print('-=' * 12)
        sleep(1)
    if opcao == 3:
        if v1 > v2:
            print('O maior valor é {}'.format(v1))
            print('-=' * 12)
        else:
            print('O maior valor é {}'.format(v2))
            print('-=' * 12)
        sleep(1)
    if opcao == 4:
        print('Informe os números novamente')
        v1 = int(input('\033[0;32mPrimeiro valor:\033[m '))
        v2 = int(input('\033[0;32mSegundo valor:\033[m '))
        print('-=' * 12)
        sleep(1)
print('\033[0;31mFinalizando...\033[m')
sleep(2)
print('\033[0;32;1mObrigado por utilizar nosso programa!!!\033[m')