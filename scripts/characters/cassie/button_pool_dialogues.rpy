label cassie_pool_dialogue_rules:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    cas "Eu posso te ajudar com alguma coisa?"
    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Umm ... Quais são os {b}rules{/b} novamente?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cas "Bem, você não pode nadar com suas roupas..."
    show cassie 3
    cas "Você precisa usar um dos {b}changing rooms{/b} colocar um {b}swimsuit{/b}!"
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    show cassie 4
    player_name "Oh Ótimo! obrigado!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
