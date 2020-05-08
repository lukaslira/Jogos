#Autoria: Lucas Alves Da Cruz lira


from random import randint
import time

white = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
lightblue = '\033[1;36m'
gray = '\033[1;37m'
stopcolor = '\033[m'


print(f"{blue}=-={stopcolor}"*10)
print(f"{yellow}Vamos Jogar Ímpar ou Par{stopcolor}")
print(f"{purple}=-={stopcolor}"*10)

while True:
    jogador = int(input(f"{red}Diga um valor: {stopcolor}"))
    while jogador >10:
        print(f"{green}Não pode jogar valores acima de 10...¯\(°_o)/¯{stopcolor}")
        jogador = int(input(f"{blue}Diga um valor: {stopcolor}"))

    par = input(f"{red}Par ou Ímpar? [P]/[Í]: {stopcolor}").strip().upper()
    computador = randint(1, 10)
    soma = jogador+computador
    while par not in "PI":
        par = input(f"{yellow}Par ou Ímpar? [P]/[Í]: {stopcolor}").strip().upper()

    print(f"{white}O computador está se preparando...{stopcolor}")
    time.sleep(2)
    print(f"{blue}1...{stopcolor}")
    time.sleep(1)
    print(f"{red}2...{stopcolor}")
    time.sleep(1)
    print(f"{gray}3...{stopcolor}")
    time.sleep(1)
    print(f"{lightblue}Lá vai...{stopcolor}")
    time.sleep(0.5)

    if (soma % 2) == 0:
        if par == "P":
            print("-=" * 20)
            print("Jogador Venceu!!")
            print(f"Você jogou {jogador} e o computador jogou {computador}. Um total de {soma}")
            print("Deu Par!")
            print("(^_^)")
            print("-=" * 20)
        else:
            if par == "I":
                print("-=" * 20)
                print("Computador venceu!!")
                print(f"Você jogou {jogador} e computador jogou {computador}. Total de {soma}")
                print("Deu Ímpar!")
                print("( ͡° ͜ʖ ͡°)")
                print("-=" * 20)
    else:
        if par == "I":
            print("-=" * 20)
            print("Jogador Venceu")
            print(f"Você jogou {jogador} e computador jogou {computador}. Total de {soma}")
            print("Deu Ímpar")
            print("(^_^)")
            print("-=" * 20)
        else:
            if par == "P":
                print("-=" * 20)
                print("Computador VENCEU")
                print(f"Você jogou {jogador} e computador jogou {computador}. Total de {soma}")
                print("Deu Par!")
                print("( ͡° ͜ʖ ͡°)")
                print("-=" * 20)

    perg = input("Quer continuar jogando? [S/N]: ").strip().upper()
    if perg == "S":
        print("     Boa sorte!! ᕦ(ツ)ᕤ     ")
        print("-=" * 20)


    else:

        print("(ಥ﹏ಥ)")
        print("Volte sempre!! Sentiremos a sua falta...Nunca é um Adeus")
        time.sleep(2)
        print("Saindo do programa...")
        break










