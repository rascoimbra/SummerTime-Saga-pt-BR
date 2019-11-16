label mom_cupid_outing_choose_gift:
    show player 5 at left with dissolve
    show debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    deb "Você encontrou algo, querido?"
    show player 10
    show debbie 164
    player_name "Eu ainda estou procurando."
    show player 5
    show debbie 166
    deb "Hehe, ok!"
    show debbie 165
    deb "Não pareça tão sério. É fácil! Basta encontrar algo que você acha que eu vou gostar..."
    show debbie 164
    pause
    hide debbie with dissolve
    show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "( ... )"
    player_name "( Alguma coisa {b}[deb_name]{/b} gostaria? )"
    player_name "( Um colar talvez? )"
    return

label mom_cupid_outing_show_necklace:
    show player 492 zorder 0 at left
    show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    show debbie 164 at Position(xpos=0.75, ypos=1.0) with dissolve
    player_name "Ok, {b}[deb_name]{/b}. Que tal agora?"
    hide xtra
    show player 1 with dissolve
    show debbie 170 at Position(xpos=0.7, ypos=1.0) with dissolve
    show debbie 172
    deb "Oh, {b}[firstname]{/b}... Que bonito {b}colar{/b}."
    show debbie 170
    show player 14
    player_name "Você gosta mesmo?"
    show player 13
    show debbie 171
    deb "Eu faço! Você tem muito bom gosto, querida."
    show debbie 170
    show player 14
    player_name "Heh, obrigado {b}[deb_name]{/b}!"
    show player 13
    show debbie 173 at Position(xpos=0.775, ypos=1.0)
    pause 1
    show debbie 174 at Position(xpos=0.7, ypos=1.0)
    pause 1
    show debbie 175
    pause 2
    show debbie 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
    pause
    show debbie 165
    deb "Bem?"
    show player 14
    show debbie 164
    player_name "... Hmm?"
    show player 13
    show debbie 166
    deb "Como estou?"
    show player 14
    show debbie 164
    player_name "Você está bonita, {b}[deb_name]{/b}!"
    show player 13
    show debbie 166
    deb "Aww... Obrigado, querido."
    show debbie 164
    deb "Hmm..."
    show debbie 165
    deb "Onde está um espelho quando você precisa de um?"
    show debbie 164
    player_name "..."
    show player 14
    player_name "Provavelmente há um no camarim..."
    show player 13
    show debbie 165
    deb "Bom pensamento, querido!"
    deb "eu volto já."
    hide debbie
    hide mneck
    with dissolve
    show player 14
    player_name "Ok."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
