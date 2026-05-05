# importando biblioteca
import random

# SUGESTÕES DE COMO CONTINUAR O CÓDIGO:
'''
- todo: deixar o código colorido
- todo: criar função para a batalha
+ todo: criar tipos de monstros diferentes
    + podem incluir:
        - raças diferentes
        - danos diferentes
        - golpe especial
+ criar funções para o código
    + exemplo:
        + barra que mostra as seguintes informações
            - vida do monstro (com um emoji)
            - vida do jogador (com um emoji)
            - quantidade de recursos extras para a batalha (você pode incluir outros) — com emoji
'''

# Criando o personagem

print("Bem-vindo ao jogo!")
nome = input("Qual o seu nome? ")
idade = int( input("Qual a sua idade? ") )

# Escolha a classe
classe = int(input("""
ESCOLHA A SUA CLASSE!
1 - Cavaleiro
2 - Mago
Escolha [1/2]: """))

if classe == 1:
    classe = "Cavaleiro"
    vida = 150
elif classe == 2:
    classe = "Mago"
    vida = 80
else:
    classe = "Camponês"
    vida = 30

print(f"""
JOGADOR REGISTRADO
* Nome: {nome},
* Idade: {idade},
* Classe: {classe}
""")

# COMBATE

print("Um monstro apareceu. Você precisa derrotá-lo!")

vida_monstro = 50
pocoes_cura = 3
# enquanto o monstro estiver vivo e usuário estiver vivo, faça algo
while vida_monstro > 0 and vida > 0:

    # TODO: transformar o menu em uma função
    print(f" 👹 monstro: {vida_monstro} | 👨 jogador: {vida} | pocoes: {pocoes_cura}")
    input("Pressione ENTER para atacar!")

    # jogador ataca SE ele estiver vivo
    if vida > 0:
        dano_jogador = random.randint(0, 40)
        # se ele acertou o ataque, o monstro leva o dano
        if dano_jogador > 0:
            print("Jogador atacou!")
            print(f"   Causou {dano_jogador} de dano.")
            # golpe acerto, o valor da vida do monstro diminui na quantidade do dano
            #vida_monstro = vida_monstro - dano_jogador
            vida_monstro -= dano_jogador
        else:
            print("Jogador errou o ataque!")

    # monstro ataca SE estiver vivo
    if vida_monstro > 0:
        dano_monstro = random.randint(0, 80)
        # se ele acertou o ataque, o jogador leva o dano
        if dano_monstro > 0:
            print("Monstro atacou!")
            print(f"    Causou {dano_monstro} de dano.")
            vida -= dano_monstro
        else:
            print("Monstro tropecou e errou o ataque!")

    # jogador pode tomar a poção
    print(f" monstro: {vida_monstro} | jogador: {vida} | pocoes: {pocoes_cura}")
    deseja_tomar_pocao = input("Deseja tomar a opção [S/N]: ").upper()

    if deseja_tomar_pocao == "S":
        # pocoes_cura = pocoes_cura - 1
        pocoes_cura -= 1
        vida += 25
        if classe == 1 and vida > 150:
            vida = 150
        elif classe == 2 and vida > 80:
            vida = 80
        else:
            vida = 30
    else:
        print("Resposta errada! Já era.")

# Mostrar quem ganhou o combate

# jogador ganhou
if vida > 0:
    print("VITÓRIA! O monstro foi derrotado\n")
    print("         +35xp")
# monstro ganhou
else:
    print(f"DERROTA! {classe} {nome} foi derrotado. Descanse em paz. ")
    print("       -100xp")