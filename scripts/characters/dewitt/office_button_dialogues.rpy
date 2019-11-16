label dewitt_dialogue_office_dewitt_eve_meet_up:
    scene expression game.timer.image("dewitt_office_c{}")
    show player 10 with dissolve
    player_name "Eu deveria dar a ela algum espaço por enquanto."
    player_name "E eu também deveria visitar {b} Eva {/b} no {b} parque à noite {/b}."
    return

label dewitt_dialogue_office_dewitt_end_intro:
    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 18 at left
    show player 14f at right
    with dissolve
    player_name "Olá, {b}Melody{/b}!"
    show player 13f
    show dewitt 19
    dewitt "Mmm, ei {b}[firstname]{/b}!"
    dewitt "Eu esperava que você viesse me visitar hoje à noite ..."
    show dewitt 18
    show player 14f
    player_name "Heh, você está com vontade de se divertir um pouco?"
    show player 13f
    show dewitt 19
    dewitt "Estou sempre de bom humor para você, {b}[firstname]{/b}."
    dewitt "Você quer ir direto ao assunto ou devo dançar primeiro para você?"
    show dewitt 18
    return

label dewitt_dialogue_office_dewitt_end_dance:
    show dewitt 19
    dewitt "Sente-se, querida."
    scene expression game.timer.image("dewitt_office_sex{}"):
    $ M_dewitt.set("sex speed", 0.125)
    show dewitts 1
    show dewitt cloths 1b
    show player dewitts 1 zorder 2 at left
    with dissolve
    pause
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", [1,2,3,4,5,6,7,8,9,10], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    dewitt "Mmm..."
    dewitt "Você gosta disso, bebê?"
    player_name "Oh sim!"
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Oh!"
    dewitt "Adoro quando você faz isso!"
    pause
    dewitt "Eu acho que deveria perder algumas dessas roupas!"
    dewitt "O que você acha, docinho?"
    player_name "Sim!"
    hide dewitts
    hide dewitt_twerk
    hide dewitt
    hide player
    with dissolve

    scene expression game.timer.image("dewitt_office_c{}")
    show dewitt 20 zorder 1 with dissolve
    pause
    show dewitt 31b with dissolve
    pause
    show dewitt 32b with dissolve
    pause
    show dewitt 29 with dissolve
    dewitt "Vamos mudar a música também!"
    show dewitt 35b at Position (xoffset=354) with dissolve
    pause

    show player 626 zorder 0 at Position (xpos=550) with dissolve
    pause
    show dewitt 36 at Position (xoffset=354)
    dewitt "E o que você está fazendo aí atrás?"
    dewitt "Você não ouviu que não deveria tocar nos dançarinos?"
    show dewitt 35 at Position (xoffset=354)

    show player 629
    show player_hand 629b_629c zorder 2 at Position (xpos=550)
    with dissolve
    player_name "Ops..."
    show player 628
    show dewitt 36 at Position (xoffset=354)
    dewitt "Menino travesso-"

    show player_hand 629d
    show dewitt 37 at Position (xoffset=290) with hpunch
    show player 626
    hide player_hand
    with dissolve
    dewitt "Olá!"
    show dewitt 38 at Position (xoffset=290)
    show player 627
    with dissolve
    dewitt "Volte para o sofá, travesso!"

    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show dewitt cloths 1c
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Mmm, como está agora?"
    hide dewitts
    hide dewitt
    show expression AnimatedImage("dewitt_twerk", ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    player_name "Você é tão sexy, {b}Melody{/b}!"
    dewitt "Heh, obrigada, docinho!"
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Mmm!"
    dewitt "Seu garoto travesso!"
    dewitt "Você está me deixando tão molhada!"
    pause
    dewitt "Você está pronta para o final?"
    player_name "Sim, senhora!"
    dewitt "Hehe, observe atentamente ..."
    scene black with fade
    pause 0.25
    $ M_dewitt.set("sex speed", 0.125)
    scene expression game.timer.image("dewitt_office_sex{}"):
    show dewitts 1
    show player dewitts 1 zorder 2 at left
    with dissolve
    dewitt "Mmm, observe-me trabalhar essa boceta, bebê!"
    hide dewitts
    show expression AnimatedImage("dewitt_twerk", ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"], M_dewitt) as dewitt_twerk at Position(xalign = 0.55, yalign = 0.0)
    with dissolve
    pause
    show player dewitts 1b with hpunch
    show player dewitts 1 with dissolve
    dewitt "Porra!"
    dewitt "Não aguento mais, docinho!"
    dewitt "Eu preciso desse pau grande!"
    pause
    return


label dewitt_dialogue_office_dewitt_end_bj:
    show player 14f
    player_name "Eu preciso desse pau grande!"
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Eu adoraria!"
    dewitt "Você sabe que eu toquei algumas flautas antes."
    dewitt "Mas sua flauta de pele é a melhor que já tive o prazer de envolver meus lábios."
    dewitt "Mas chega de conversa, deixe-me fazer outra apresentação particular."
    scene black with fade

    $ M_dewitt.set("sex speed", 0.175)
    scene expression game.timer.image("dewitt_office_bj{}")
    show dewitt bj 1 at left
    with dissolve
    pause
    show dewitt bj 2
    pause
    show dewitt bj 3
    pause
    show dewitt bj 4
    pause
    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    return

label dewitt_dialogue_office_dewitt_end_sex:
    show dewitt 19
    dewitt "Eu estava esperando que você quisesse pular direto!"
    dewitt "Vamos ver quem consegue tirar as roupas o mais rápido!"
    show dewitt 20 with dissolve
    show player 26f
    player_name "O que não conta?"
    show dewitt 31f with dissolve
    show player 8f with dissolve
    dewitt "Nope!""Não!"
    show dewitt 32f with dissolve
    show player 261 with dissolve
    pause
    show dewitt 18b with dissolve

    show player 263 with dissolve
    pause
    show dewitt 19b
    dewitt "Parece que eu ganhei!"
    dewitt "Agora me faça gozar!"
    show player 262
    player_name "Sim, senhora!"
    label dewitt_twerk_end:
        scene black with fade
        pause 0.25
        scene expression game.timer.image("dewitt_office_sex{}"):
        show dewitts 1
        show player dewitts 2 zorder 2 at left
        with dissolve
        dewitt "Me dê isto, {b}[firstname]{/b}!"
        hide player
        show dewitts 3 at left
        with dissolve
        dewitt "Pare de tocar lá! Mal posso esperar!"
        show dewitts 4
        dewitt "Bem aqui, docinho ..."
        show dewitts 5 with dissolve
        pause
        $ M_dewitt.set("sex speed", 0.125)
        show expression AnimatedImage("dewitts", [5,6,7,8,9,10,11,12,13,14], M_dewitt) as dewitts
        $ anim_toggle = True
    jump expression game.dialog_select("dewitt_sex_loop")

label dewitt_dialogue_office_intro:
    scene expression game.timer.image("dewitt_office_c{}"):
    show dewitt 1b at left
    show player 14f at right
    with dissolve
    player_name "Olá, {b}Miss Dewitt{/b}."
    show player 13f
    show dewitt 2b
    dewitt "Olá, {b}[firstname]{/b}!"
    dewitt "Você precisava de algo?"
    show dewitt 1b
    return

label dewitt_dialogue_office_flute_lessons:
    show player 26f
    player_name "Eu esperava que você pudesse me ajudar a me ensinar a dominar minha flauta."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Eu estava esperando que você fosse perguntar!"
    dewitt "Encontre-me aqui hoje à noite e podemos brincar juntos!"
    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "E não se atrase, ou terei que tocar sozinho."
    return

label dewitt_dialogue_office_leave:
    show player 14f
    player_name "Não no momento."
    show player 13f
    show dewitt 2b
    dewitt "Tudo bem. Bem, tenha um dia maravilhoso!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
