label latinas_dialogue_shower:
    scene location_school_lockershowers_closeup
    show martinez b_towel a_towel_crossed f_angry zorder 1 at Position (xpos=250)
    show lopez b_towel a_towel_hips f_angry_talk zorder 2
    show player 57 zorder 0 at left
    with dissolve
    lopez "Ei! O que você está fazendo aqui?"
    show lopez f_angry
    show player 58
    player_name "Umm ... Só estou tentando tomar banho?"
    show lopez f_angry_talk
    show player 59
    lopez "Escute, garoto. Este é o nosso território, então vá dar um passeio em outro lugar!"
    show lopez f_angry
    show martinez f_normal_talk
    martinez "Espere, {b}Lopez{/b}!"
    martinez "Ei, acho que esse é o cara sobre o qual as pessoas estão falando!"
    show lopez f_angry_left_talk
    show martinez f_normal
    lopez "O quê ?! De jeito nenhum ..."
    lopez "Você está me dizendo que esse cara tem um {b}pau enorme{/b}?"
    show lopez f_angry
    show martinez f_angry_talk
    martinez "Tudo bem garoto! Mostre-nos o que você tem aí em baixo, e você pode entrar!"
    show martinez f_angry
    show player 60
    player_name "Uhh ... acho que vou passar. Vou tomar banho em casa então-"
    show martinez b_towelgrab f_empty a_empty
    pause
    show player 61
    show lopez f_surprised_down
    show martinez b_towel a_towel_hold_towel f_smirk_down
    with hpunch
    pause
    player_name "..."
    show player 62
    show martinez f_normal_talk_right
    martinez "Lá vai você!"
    show martinez f_smirk_down
    show lopez f_normal_down_talk
    lopez "... É isso que você chama de {b}grande{/b}?"
    show lopez f_normal_down
    show martinez f_surprised_right
    martinez "O que-"
    show player 63
    show martinez f_suspicious
    martinez "ele é mole...!"
    martinez "... Ele precisa de um pouco de emoção ..."
    show martinez f_eyeroll
    martinez "...Hmm..."
    show martinez f_normal_talk_right
    martinez "... Isso deve funcionar!"
    show lopez f_normal with None
    show martinez f_normal_talk_right b_towel a_empty
    show martinez_body_parts a_towel_hold_towel_pull1 zorder 3
    with dissolve
    pause
    show player 64
    show lopez f_surprised_down_down b_toweldown a_towel_surprised
    show martinez f_smirk_down
    show martinez_body_parts a_towel_hold_towel_pull2
    with hpunch
    pause
    show lopez f_angry_left_talk a_toweldown_cover1
    show martinez a_towel_crossed
    hide martinez_body_parts
    with dissolve
    lopez "Oh meu Deus, puta!"
    show lopez f_angry
    show martinez f_normal_talk_right
    martinez "Calma, todos já o viram na escola!"
    show martinez f_laugh
    martinez "Haha!"
    show martinez f_smirk_down
    show lopez f_surprised_down
    lopez "Ei, não está fazendo nada!"
    show lopez f_normal_down
    show martinez f_eyeroll
    martinez "Talvez ele goste de caras?"
    show martinez f_angry
    show lopez f_normal_down_talk a_toweldown_pull1 with dissolve
    lopez "Aqui, eu sei o que vai funcionar!"
    show martinez b_empty
    show martinez_body_parts b_towelup zorder 0
    show lopez f_normal_down a_toweldown_pull2
    with dissolve
    pause
    show martinez f_smirk_down2
    show lopez f_surprised_down
    with hpunch
    pause
    show player 65
    show martinez f_smirk_down
    player_name "... Oh ... Não ..."
    pause
    show player 66 with hpunch
    show martinez f_surprised_down
    pause
    hide martinez_body_parts
    show martinez b_towel
    show lopez f_surprised_right a_toweldown_cover2
    with dissolve
    show player 67
    lopez "Oh, merda!"
    lopez "{b}Annie{/b} está chegando !!"
    show lopez f_sorry
    show martinez f_sad_down a_towel_cover b_towel with dissolve
    show player 68
    show annie 1 zorder 3 at Position (xpos=400)
    ann "..."
    show annie 3
    ann "O que está acontecendo aqui?"
    show player 69
    show annie 1
    player_name "Eu estava apenas tentando-"
    show player 68
    show annie 3
    ann "Expor-se inadequadamente?"
    show annie 4
    ann "{b}NOVAMENTE{/b}!?"
    show player 69
    show annie 6
    player_name "Não, não é-"
    show player 68
    show annie 5
    ann "Eu não quero ouvir suas desculpas patéticas!"
    ann "Minhas ordens são para levar criminosos repetidos ao {b}Escritório{/b}!"
    show annie 7
    ann "Venha comigo, {b}AGORA{/b}!!!"
    show annie 8f
    ann "... e vocês dois, saiam daqui antes de eu mandar vocês dois para detenção !!!"
    hide lopez
    hide martinez
    hide player
    hide annie
    with dissolve
    $ renpy.end_replay()
    return

label latinas_dialogue_leave:
    show player 57 at left
    show martinez b_towel a_towel_crossed f_angry zorder 1 at Position (xpos=250)
    show lopez b_towel a_towel_hips f_angry_talk zorder 2
    with dissolve
    lopez "Ei! Você está aqui para nos meter em problemas de novo?"
    show player 58 at left
    show lopez f_angry
    player_name "Umm ... Só estou tentando tomar banho?"
    show player 59 at left
    show martinez f_angry_talk
    martinez "Saia daqui!"
    show martinez f_angry
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
