label button_ross_office_generic_pre_hscene:
    scene expression player.location.background_closeup
    show ross 11 at left
    show player 1f at right
    with dissolve
    ross "Bem Olá, {b}[firstname]{/b}."
    ross "Bom da sua parte me visitar! "
    show ross 10
    show player 2f
    player_name "Ei, {b}Miss Ross{/b}."
    show ross 11
    show player 1f
    ross "O que posso fazer para você?"
    return

label button_ross_office_generic_post_hscene:
    scene expression player.location.background_closeup
    show ross 10 at left
    show player 2f at right
    with dissolve
    player_name "Ei, {b}Miss Ross{/b}!"
    show player 1f
    show ross 27 with dissolve
    ross "{b}[firstname]{/b}! É tão bom ver você! "
    show ross 13 with dissolve
    ross "... Espero que você esteja aqui para outra aula particular? "
    return

label ross_dialogue_office_private_lessons:
    show ross 12
    show player 2f
    player_name "Sim, eu adoraria isso! "
    show ross 13
    show player 1f
    ross "Mmm, se apresse e tranque a porta! "
    show ross 12
    show player 2f
    player_name "O-ok..."
    return

label ross_dialogue_office_leave:
    scene expression player.location.background_closeup
    show ross 10 at left
    show player 2f at right
    player_name "Oh, eu não preciso de nada. "
    player_name "Desculpe incomodá-la."
    show ross 11
    show player 1f
    ross "Não incomoda, {b}[firstname]{/b}!"
    ross "Afinal, ajudar jovens artistas talentosos é minha especialidade! "
    show ross 10
    show player 2f
    player_name "Heh, ok. "
    player_name "Eu devo ir ..."
    show ross 11
    show player 1f
    ross "Aww, tudo bem. "
    tchau "tchau, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
