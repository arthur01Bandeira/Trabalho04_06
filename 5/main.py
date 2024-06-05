from funcao import *
while True:
    categoria = int(input('''
    1 - entrar no sistema
    2 - sair do sistema
    >:'''))

    if categoria != 1 or 2:
        print('Digite uma opção válida:')

    if categoria == 2:
        print('Tchau tchau! :]')
        break

    if categoria == 1:
        idiomas = int(input('Quantas horas foram cursadas em idiomas?'))


        print(contar_horas_idiomas(idiomas))

        eventos = int(input('Quantas horas foram cursadas em eventos?'))


        print(contar_horas_eventos(eventos))

        tecnicas = int(input('Quantas horas foram cumpridas em visitas técnica?'))

        print(contar_horas_tecnicas(tecnicas))

        extensao = int(input('Quantas horas foram cumpridas em visitas técnica?'))

        print(contar_horas_extensao(extensao))


        soma = contar_categorias()

        if soma >= 100:
            print(f"a soma da suas horas é {soma}")
            print('Vocẽ alcançou a quantidade necessaŕia de horas!')

        elif soma < 100:

            print(f"a soma da suas horas é {soma}")
            print('Vocẽ não alcançou quantidade mínima necessaŕia de horas!')

