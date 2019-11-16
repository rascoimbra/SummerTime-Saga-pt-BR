label button_consuela_intro:
    show player 10 at left
    show consuela
    with dissolve
    player_name "Olá, {b}Consuela{/b}."
    show player 5
    show consuela f_unsure
    consuela "Olá senhor {b}[firstname]{/b}."
    show consuela f_normal
    show player 12
    player_name "Você pode me ligar {b}[firstname]{/b}..."
    show player 5
    show consuela f_unsure
    consuela "O que?"
    consuela "Não falo ."ingles
    show consuela f_normal
    show player 10
    player_name "Oh, uhh..."
    show player 5
    pause
    consuela "..."
    show player 3 with dissolve
    player_name "..."
    show consuela f_unsure
    consuela "Ehh ... eu limpo agora."
    consuela "Sim?"
    show consuela f_normal
    show player 10 with dissolve
    player_name "Oh, sim."
    player_name "Err, quero dizer ... Sim!"
    show player 14
    player_name "Obrigado, {b}Consuela{/b}."
    show player 13
    show consuela f_normal_talk
    consuela "De nada, senhor {b}[firstname]{/b}."
    hide player
    hide consuela
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
