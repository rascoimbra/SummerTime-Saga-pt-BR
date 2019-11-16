label debbie_dialogue_master_room_pre:
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with dissolve
    deb "Oi docinho..."
    deb "Você estava me procurando?"
    show debbie 54
    show player 111
    player_name "Sim..."
    show player 110
    show debbie 55
    deb "Há algo que você queria de mim?"
    show debbie 54
    return

label debbie_dialogue_master_room_after_kiss_dialogue:
    deb "Agora, há mais alguma coisa que você queria?"
    show debbie 54
    return

label debbie_dialogue_master_room_kiss:
    show player 111 at right
    show debbie 54 at left
    player_name "Posso ter um beijo?"
    show player 110
    show debbie 55
    deb "Claro, querida! Venha aqui."
    scene debbie_bedroom
    show debbie 79
    with fade
    deb "Mmmm..."
    show debbie 80_79
    pause 3
    show debbie 75 at Position(xpos=750)
    show player 227 at Position(xpos=200)
    with fastdissolve
    deb "Você está ficando melhor nisso!"
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with fade
    return

label debbie_dialogue_master_room_shower:
    show player 111
    player_name "Ei, {b}[deb_name]{/b}!"
    player_name "Quer tomar um banho comigo?"
    show player 110
    show debbie 55
    deb "Está ficando muito quente em casa..."
    deb "Certo! Um chuveiro parece adorável agora."
    deb "Você vai em frente, querida. Eu estarei lá em um minuto."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Desculpe por esperar, querida..."
    return

label debbie_dialogue_master_room_sex_random_true:
    show debbie 54 at left
    show player 111 at right
    player_name "Eu sinto como ... Fazendo isso com você novamente."
    show player 110
    show debbie 55
    deb "Tudo bem!"
    deb "Eu estava esperando que você quisesse ..."
    show player 111
    show debbie 54
    player_name "Realmente?"
    show player 110
    show debbie 58 with dissolve
    deb "Claro! Você é meu homem, afinal. "
    show debbie 57
    player_name "!!!"
    show debbie 58
    deb "Tire a roupa, querida."
    show debbie 57
    show player 8f
    pause
    show player 261
    pause
    show player 263
    pause
    show debbie 103
    deb "Mmm, venha me pegar, querida! "
    show player 262 at right
    show debbie 102 at left
    player_name "Não precisa me dizer duas vezes ... "
    return

label debbie_dialogue_master_room_sex_random_false:
    show debbie 54 at left
    show player 111 at right
    player_name "{b}[deb_name]{/b}, quer se divertir um pouco?"
    show player 110
    show debbie 54
    deb "Oh?"
    show debbie 56 with dissolve
    deb "Tipo ... isso é divertido? "
    show debbie 57
    show player 111
    player_name "Claro..."
    show player 110
    show debbie 58
    deb "Deixe-me ver esse seu pau ... "
    show debbie 57
    show player 8f with dissolve
    pause
    show debbie 101
    show player 261 with dissolve
    pause
    show player 263 with dissolve
    pause
    show debbie 58
    deb "Parece que você está pronto! "
    show debbie 57
    show player 262
    player_name "Estou ansioso por isso desde que acordei esta manhã. "
    show player 263
    show debbie 58
    deb "Eu também."
    show debbie 102 with dissolve
    pause
    show debbie 103
    deb "Venha e pegue, querida. "
    return

label debbie_dialogue_master_room_sex_after:
    hide player
    show debbie 104 at left
    with dissolve
    pause
    hide debbie
    hide player
    with dissolve
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_master_room_laundry_sex:
    show debbie 54
    show player 111
    player_name "Eu queria saber se você queria alguma ajuda no porão."
    show player 110
    show debbie 55
    deb "No porão? Pelo que?"
    show player 111
    show debbie 54
    player_name "Talvez eu possa ajudá-lo com a roupa ... Como fizemos da última vez? "
    show player 110
    show debbie 55
    deb "Oh, entendo ... eu sei exatamente o que você quer!"
    deb "Me dê um minuto para me arrumar. "
    deb "Encontro você lá embaixo ... "
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_master_room_watch_movie:
    show player 111
    player_name "Eu estava pensando, deveríamos assistir outro filme hoje à noite. Interessado?"
    show player 110
    show debbie 55
    deb "Mmm, uma noite de cinema, hein? "
    deb "Parece uma ótima idéia, querida! "
    show player 111
    show debbie 54
    player_name "Impressionante!"
    player_name "Vejo você hoje à noite na sala, então? "
    show player 110
    show debbie 55
    deb "Mal posso esperar ... "
    return

label debbie_dialogue_master_room_leave:
    show debbie 54
    show player 111
    player_name "Nada, {b}[deb_name]{/b}."
    player_name "Só queria dizer oi."
    show player 110
    show debbie 55
    deb "Ah, tudo bem ... "
    deb "Bem, volte se quiser ... estou um pouco entediada ... "
    deb "Podemos nos divertir sempre que você quiser. "
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
