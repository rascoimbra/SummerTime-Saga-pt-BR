label annie_dialogue_music_classroom_intro:
    show player 2
    player_name "Oi, {b}Annie{/b}."
    show player 1
    show annie 3
    ann "Estou tentando me concentrar."
    show annie 1
    show player 3
    player_name "..."
    show player 29 with dissolve
    player_name "Sorr-"
    show player 3 with dissolve
    show annie 7
    ann "ESTOU CONCENTRANDO!"
    show annie 6
    show player 2f
    player_name "E eu vou embora!"
    player_name "Nossa..."
    hide player
    hide annie
    with dissolve
    return

label annie_dialogue_ross_ask_model:
    show player 2 at left
    show annie 1 at right
    player_name "Estou trabalhando em um projeto para {b}Miss Ross{/b} and it requires a live model."
    player_name "Você estaria interessado?"
    show player 1
    show annie 3
    ann "Não pode fazer isso. Eu tenho rodadas!"
    show player 10
    show annie 1
    player_name "Hã?"
    show player 11
    show annie 4
    ann "Eu tenho que patrulhar os malvados!"
    ann "Saia do meu caminho!"
    hide annie
    hide player
    show player 12f
    with dissolve

    player_name "Tudo bem, sheesh!"
    player_name "Esquisita..."
    return

label annie_dialogue_leave:
    show player 14
    player_name "Oi {b}Annie{/b}!"
    show annie 5
    show player 1
    ann "Faça isso rápido!"
    show annie 6
    show player 17
    player_name "Oh, nada ... eu só estava dizendo oi!"
    show annie 4
    show player 18
    ann "Estou no serviço de monitoramento do salão ... E você está perdendo meu tempo."
    show annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "Tudo certo. Desculpe incomodá-lo. Sheesh!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
