label button_eve_intro:
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 13 at left
    show eve 1 at right
    with dissolve
    return

label button_eve_talent_show_help:
    show player 10
    player_name "Do que você jogar quaisquer instrumentos?"
    show player 5
    show eve 2
    eve "Não, eu não jogar quaisquer instrumentos . Eu sempre quis para aprender , mas eu simplesmente não tinha o tempo, você sabe ?"
    show eve 1
    show player 10
    player_name "Ok, bem , e quanto a cantar ?"
    show player 5
    show eve 6
    eve "Oh, umm..."
    show eve 2b
    eve "Sim , eu gosto de cantar eu acho . Eu não sei se eu sou qualquer boa embora."
    show eve 1
    show player 14
    player_name "Eu aposto que você é! Você deve assinar -se para o talento show de com -me!"
    player_name " Estamos realmente sofrendo por mais voluntários ."
    show player 13
    show eve 2b
    eve "... Sim , eu não sei."
    eve " Você quer me para cantar na frente da toda a escola ? Isso soa muito embaraçoso ."
    eve "... E eu não cantava em algum tempo . Não desde o meu karaoke máquina quebrou ."
    eve " Estou completamente fora de prática ."
    show eve 1
    show player 4 with dissolve
    player_name "Hmm..."
    show player 14 with dissolve
    player_name " Você sabe , eu acho que o meu amigo {b}Erik{/b} tem um {b}karaoke máquina{/b} em seu porão ."
    show player 13
    show eve 2
    eve "Oh, sim ?"
    show eve 1
    show player 17
    player_name " Totalmente! Você deveria vir um dia e praticar!"
    show player 13
    show eve 6
    eve " Heh, você quer me para cantar para você e seu amigo?"
    show eve 5
    show player 14
    player_name " Nah, nós podemos todos cantar juntos! Vamos lá, vamos fazê-lo hoje à noite, ele vai ser divertido!"
    show player 13
    show eve 1
    eve "..."
    show eve 6b
    eve "Tudo bem , eu acho que eu posso parar por para um pouco enquanto."
    show eve 5
    show player 14
    player_name " impressionante ! {b}eu vou atender você no de Erik casa{/b} esta noite."
    return

label button_eve_ross_find_art_pad:
    show player 2
    player_name "Eu preciso de pedir-lhe um favor."
    show player 1
    show eve 2
    eve "Oh?"
    show player 2
    show eve 1
    player_name "Você vê, eu estou meio que ajudando {b}Miss Ross{/b} com algo e nós precisamos sua arte pad".
    show player 1
    show eve 2
    eve "Bem, isso não é problema."
    eve "Você apenas tem que {b}me ajudar a encontrar a minha mochila{/b} primeiro."
    show player 10
    show eve 1
    player_name "Você perdeu sua mochila?"
    show player 11
    show eve 2
    eve "Sim ..."
    eve "Meu bloco de arte deve estar dentro dele."
    show player 10
    show eve 1
    player_name "Onde foi o último lugar que você lembra de tê- lo?"
    show player 11
    show eve 2
    eve "Hmm , bem eu acho {b}Eu tinha que quando eu fui para pendurar fora com os caras no parque última noite{/b}."
    show player 2
    show eve 1
    player_name "Tudo bem , eu estou nele!"
    return

label button_eve_ross_find_eve_backpack_have_backpack:
    show player 610
    player_name "Olha o que eu encontrei!"
    show player 609
    show eve 2
    eve "agradável!"
    show player 1 with dissolve
    eve "Obrigado, {b}[firstname]{/b}!"
    show player 2
    show eve 1
    player_name "Não se preocupe. Eu não poderia encontrar o seu {b}Art Pad{/b} embora ."
    show player 1
    show eve 2
    eve "Não estava na minha bolsa?"
    show player 2
    show eve 1
    player_name " Não ".
    show player 1
    show eve 2
    eve "Estranho."
    show eve 6b
    eve "Eu me pergunto se {b}Chad{/b} arrebatou -lo novamente?"
    show player 10
    show eve 1
    player_name "Chad?"
    show player 11
    show eve 2
    eve "Sim , ele curte minha arte."
    show player 10
    show eve 1
    player_name "Interessante ..."
    show player 2
    player_name "Eu vou ir perguntar -lhe ."
    show player 1
    show eve 2
    eve "Legal. Ver você {b}[firstname]{/b}."
    show player 2
    show eve 1
    player_name " Veja, {b}Eve{/b}."
    return

label button_eve_ross_find_eve_backpack_no_backpack:
    show player 2
    player_name "Onde se você deixar sua mochila , mais uma vez?"
    show player 1
    show eve 2
    eve "Eu sou não inteiramente certo. Eu me lembro de ter -lo com me {b}pelo o parque{/b} noite passada."
    show player 2
    show eve 1
    player_name "Ok, vou verificar lá!"
    return

label button_eve_ross_get_eve_drawing:
    show player 10
    player_name "Onde foi que você disse que tem um {b}Art Pad{/b}?"
    show player 11
    show eve 6b
    eve "Oh, {b}Chad provavelmente tem{/b}."
    show eve 2
    eve "Ele cava minha arte."
    show player 2
    show eve 1
    player_name "Entendi , obrigado!"
    return

label button_eve_ask_model:
    show player 2
    show eve 1
    player_name "u estou trabalhando em um projeto para {b}Miss Ross{/b} e isso requer um vivo modelo."
    player_name "Será que você estar interessado?"
    show player 1
    show eve 2
    eve "Modelagem ? Isso pode ser divertido."
    show player 2
    show eve 1
    player_name " Realmente !? Incrível ! Eu estava esperando que você poderia dizer que!"
    show player 1
    show eve 2
    eve "Sim , eu não me importo. É uma coisa boa eu usar essa roupa fofa hoje."
    show player 10
    show eve 1
    player_name "... Oh, umm . Ele iria ser nu modelagem."
    show player 11
    show eve 2b
    eve "Nu?!"
    show eve 6
    eve "Oh, inferno , não!"
    show player 10
    show eve 5
    player_name "Então você não vai fazê-lo? Eu pensei que você fosse um artista?"
    show player 11
    show eve 6
    eve "Sim , mas que não significa que eu sou em público nudez!"
    show player 10
    show eve 5
    player_name "Bom argumento. Desculpe."
    show player 11
    show eve 2
    eve "Está tudo bem. Só não estou interessado."
    show player 2
    show eve 1
    player_name "Bem, de qualquer forma, obrigado ..."
    return

label button_eve_ross_get_paint:
    show player 2
    show eve 1
    player_name "Eu preciso de um pouco de tinta . Alguma idéia de onde eu poderia encontrar um pouco?"
    show player 1
    show eve 6b
    eve "Não sei , talvez tente uma loja?"
    show player 2
    show eve 1
    player_name "Bem , sim , eu sei ... Duh , certo?"
    player_name "... Mas a pintura é para {b}Miss Ross{/b} e ela não pode ter recursos para comprar isso."
    show player 1
    show eve 6
    eve "Oh, hehe."
    show eve 4 with dissolve
    eve "Hmm , livre de pintura . Isso é um resistente."
    show eve 3
    show player 2
    player_name "Conte- me sobre isso ..."
    show player 1
    show eve 2 with dissolve
    eve "Nós poderia tentar pedir {b}Minha irmã{/b}."
    show player 2
    show eve 5
    player_name "Ela é uma {b}Tattoo Artist{/b}, certo?"
    show player 1
    show eve 6
    eve "Ela é a melhor {b}Tattoo Artist{/b}!"
    eve "Você deve vir verificar para fora seu trabalho , que é incrível!"
    show player 2
    show eve 5
    player_name "Você acha que ela iria deixar -me ter alguma pintura?"
    show player 1
    show eve 2
    eve "Nós podemos ir perguntar a ela."
    show eve 5
    show player 10
    player_name "O salão dela não se chama {b}Sugar Tats{/b}?"
    show player 11
    show eve 6
    eve "Yuuuup . É sobre a {b}do Norte{/b} lado da cidade."
    show player 2
    show eve 5
    player_name "Tudo bem , eu vou encontrar você lá!"
    return

label button_eve_ross_get_paint_grace:
    show player 10
    show eve 5
    player_name "Qual é o nome do salão da sua irmã de novo?"
    show player 11
    show eve 2
    eve "{b}Tatuagens de açucar{/b}.É sobre o {b}lado norte{/b}da cidade."
    show player 2
    show eve 5
    player_name "Ok, {b}eu vou atender você lá{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
