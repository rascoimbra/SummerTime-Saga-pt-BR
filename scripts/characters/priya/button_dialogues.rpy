label priya_button_intro:
    scene expression "backgrounds/location_hospital_lab_blur.jpg"
    show player 5 at left
    show priya f_angry a_dressed_point
    with dissolve
    priya "Você novamente?!"
    priya "O que você está fazendo aqui?!"
    show priya f_stern a_dressed_crossed with dissolve
    pause
    show priya f_angry
    priya "Você tem alguns resultados para relatar? "
    show priya f_stern
    return

label priya_button_menu_no:
    show priya f_stern a_dressed_crossed
    show player 24 at left
    player_name "Não, desculpe. "
    player_name "Eu só estava-"
    show player 5
    show priya f_angry a_dressed_point with dissolve
    priya "Esta é uma área restrita por um motivo! "
    priya "Você não pode simplesmente ir e vir quando quiser ..."
    show priya f_stern a_dressed_crossed with dissolve
    show player 10
    player_name "Eu sinto Muito, {b}Priya{/b}."
    show player 24
    player_name "EU-"
    player_name "Eu vou ..."
    show player 5
    show priya f_facepalm_talk a_dressed_facepalm with dissolve
    priya "{b}*Suspiro*{/b}"
    priya "Não, me desculpe ... me desculpe. "
    show priya f_hopeful_talk a_dressed_sides with dissolve
    priya "Não quero gritar com você. "
    show priya f_normal_talk
    priya "É só que ... é perigoso para você estar aqui em cima. "
    priya "Então, por favor, não volte a menos que você tenha algo a relatar."
    show priya f_normal
    show player 10
    player_name "Tudo bem. "
    hide player
    hide priya
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
