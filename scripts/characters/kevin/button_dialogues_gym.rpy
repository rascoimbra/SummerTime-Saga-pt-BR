label kevin_gym_take_it_easy:
    show player 14
    player_name "Eu vou sair daqui, cara. "
    show player 13
    show kevin 11b with dissolve
    kev " Já , mano ?"
    show kevin 11c
    show player 14
    player_name " Sim , eu tenho algumas outras coisas que eu preciso para fazer."
    show player 13
    show kevin 9 with dissolve
    kev "Ah, tudo bem ."
    show kevin 8
    show player 14
    player_name " Até mais, {b}Kevin{/b}."
    hide kevin
    hide player
    with dissolve
    return

label kevin_gym_lets_lift:
    show player 14
    player_name " Vamos apenas levantar ."
    show player 13
    show kevin 9
    kev "Oh, você está pronto para levantar um pouco de ferro ?"
    show kevin 10 with dissolve
    kev " Direito em , bro ."
    kev " Vamos fazer isso !"
    hide kevin
    hide player
    with dissolve
    return

label kevin_gym_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 9 at right
    with dissolve
    kev " Ei , mano !"
    show kevin 8
    show player 14
    player_name " O que é para cima, {b}Kevin{/b}?"
    show player 13
    show kevin 9
    kev " Eu venho trabalhando em meus glúteos toda manhã !"
    show kevin 13b with dissolve
    kev " Sinta o quão apertados esses meninos maus são!"
    show player 10b with dissolve
    player_name " Eh , não, obrigado ..."
    show player 5b
    kev " Você tem certeza , mano ?"
    kev " Você não sabe o que está perdendo !"
    show kevin 8 with dissolve
    show player 29 with dissolve
    player_name "Heh."
    show player 5 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
