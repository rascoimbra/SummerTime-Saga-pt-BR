label dewitt_dialogue_dewitt_eve_meet_up:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Eu deveria dar a ela algum espaço por enquanto. "
    player_name "E eu também deveria visitar {b}Eve{/b} no {b}park at night{/b}."
    return

label dewitt_dialogue_dewitt_science_adhesive:
    scene music_classroom_c
    show player 17 with dissolve
    player_name "{b}Kevin{/b} ia fazer algum adesivo em {b}Miss Okita's{/b} Sala de aula."
    player_name "Eu deveria ver o que ele está fazendo. "
    return

label dewitt_dialogue_dewitt_school_sneak_mission_help:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Talvez {b}Erik{/b} Me ajudará {b}esgueirar-se para a escola hoje à noite{/b}."
    return

label dewitt_dialogue_dewitt_office_night_visit_delay:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Lembre-se, tenho mais uma surpresa para você. "
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Você terá que vir ao meu escritório {b}amanhã{/b} depois da escola, se você quiser ... "
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "Ok..."
    player_name "I'll be there."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Mmm, eu mal posso esperar!"
    dewitt "Vejo você então, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_office_night_visit:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Lembre-se, eu tenho mais uma surpresa para você."
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Você terá que vir ao meu escritório depois da escola, se quiser ..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "Ok..."
    player_name "eu estarei lá."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Mmm, eu mal posso esperar!"
    dewitt "Vejo você então, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_end:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Mais uma vez obrigado por tudo, querida! "
    show dewitt 1
    show player 14f
    player_name "O prazer é meu, {b}Miss Dewitt{/b}."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Lembre-se, minha porta está sempre aberta para você. "
    show dewitt 18
    show player 17f
    player_name "Sim, senhora."
    return

label dewitt_dialogue_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 2f at right
    player_name "Oi, {b}Miss Dewitt{/b}."
    show dewitt 2
    show player 1f
    dewitt "Olá, {b}[firstname]{/b}!"
    dewitt "Pronto para curtir conosco hoje? "
    show dewitt 1
    show player 33f
    player_name "É claro!"
    show dewitt 2
    show player 13f
    dewitt "Quer falar sobre algo? "
    show dewitt 1
    show player 34f
    return

label dewitt_dialogue_dewitt_find_flute:
    show player 10f
    player_name "Onde devo começar a procurar a flauta?"
    show player 5f
    show dewitt 2
    dewitt "Você {b} verificou a folha de pagamento do instrumento no armário da sala de aula {/b}?"
    show dewitt 1
    show player 14f
    player_name "Oh sim!"
    player_name "Vou procurar lá uma pista!"
    show player 13f
    show dewitt 2
    dewitt "Tchau, docinho!"
    return

label dewitt_dialogue_dewitt_make_new_flute:
    show player 10f
    player_name "Sobre a flauta-"
    show player 11f
    show dewitt 2
    dewitt "Você já encontrou a flauta?"
    show dewitt 1
    show player 3f at Position (xoffset=-8) with dissolve
    player_name "..."
    show player 10f with dissolve
    player_name "Ainda não."
    show player 5f
    show dewitt 2
    dewitt "Espero que não esteja perdido."
    show dewitt 1
    show player 14f
    player_name "Não se preocupe! Estou nisso!"
    show player 13f
    show dewitt 2
    dewitt "Obrigado, {b}[firstname]{/b}!"
    hide dewitt with dissolve
    show player 4f with dissolve
    player_name "( {b}Erik{/b} disse que eu deveria ser capaz de fazer um. )"
    return

label dewitt_dialogue_talent_show_help:
    show player 10f
    player_name "Quantas pessoas você precisa para o show de talentos de novo?"
    show player 5f
    show dewitt 5
    dewitt "Eu esperava pelo menos {b}mais dois{/b}."
    dewitt "Menos e tenho medo de cancelar."
    show dewitt 4
    show player 14f
    player_name "Tudo bem, não se preocupe, {b}Ms. Dewitt{/b}! Eu vou encontrar alguém!"
    show player 13f
    show dewitt 5
    dewitt "Aww obrigada, docinho!"
    return

label dewitt_dialogue_leave:
    show player 10f
    player_name "Na verdade não..."
    player_name "Só espero que eu possa me recuperar."
    show dewitt 2
    show player 5f
    dewitt "Oh, querida. Você vai ficar bem!"
    show player 13f
    dewitt "Escolha um instrumento e sente-se!"
    dewitt "Nós o colocaremos de volta ..."
    show dewitt 1
    show player 14f
    player_name "Obrigado, {b}Miss Dewitt{/b}..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
