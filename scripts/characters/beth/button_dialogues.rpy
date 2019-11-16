label beth_dialogue_pre:
    scene donut_c
    show beth 2 zorder 1 at right
    show xtra 27 zorder 2 at center
    show player 1 zorder 3 at left
    with dissolve
    beth "Olá, senhor!"
    show player 14
    show beth 1
    player_name "Oi."
    show player 1
    show beth 2
    beth "Olhando para comprar alguns buracos doces, você está?"
    show beth 1
    return

label beth_dialogue_do_not_know:
    show player 14
    player_name "Hmm ... ainda não sei o que preciso comprar."
    show player 1
    show beth 2
    beth "Voce nao sabe?"
    show player 14
    show beth 1
    player_name "Bem, eu estou comprando isso para alguém como presente, mas não tenho certeza do que ele gosta."
    show player 1
    show beth 2
    beth "Eu não posso te ajudar se você não sabe o que gostaria!"
    show player 14
    show beth 1
    player_name "Volto mais tarde quando conhecer as coberturas."
    return

label beth_dialogue_want_donuts:
    show player 14
    player_name "Eu gostaria de comprar uma caixa pequena, por favor."
    show player 1
    show beth 2
    beth "Coisa certa!"
    beth "Que tipo de cobertura e cobertura você gostaria neles?"
    return

label beth_dialogue_leave:
    show player 14
    player_name "Eu estou bem, obrigado!"
    player_name "Talvez outra hora..."
    show player 1
    show beth 2
    beth "Claro, até mais!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
