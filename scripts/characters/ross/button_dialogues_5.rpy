label button_ross_paint_with_body:
    scene location_school_art_closeup
    show ross 1 at left
    show player 2f at right
    with dissolve
    player_name "Você disse que tinha uma técnica final para me ensinar? "
    show ross 2
    show player 1f
    ross "Ai sim! É uma boa também! "
    ross "Eu não posso te ensinar aqui. Você terá que vir me ver aqui. No {b}meu escritório{/b} esta {b}tarde{/b}." 
    show ross 1
    show player 2f
    player_name "Parece realmente incrível! "
    player_name "eu te vejo lá, {b}Miss Ross{/b}."
    return

label button_ross_end_intro:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "Aqui está meu pequeno herói!"
    show player 2f
    show ross 1
    player_name "Heh, ei {b}Miss Ross{/b}."
    show player 1f
    show ross 13 with dissolve
    ross "Você está ocupado {b}esta noite{/b}?"
    ross "Eu esperava que você estivesse interessado em mais... \"Aulas particulares\"?"
    ross "Estou ansiosa para te ensinar mais ... "
    show ross 12
    return

label button_ross_end_yes:
    show player 2f
    player_name "Claro, isso parece incrível! "
    show player 1f
    show ross 11
    ross "Maravilhoso!"
    Ross "Apenas venha {b}visite-me no meu escritório{/b} hoje mais tarde."
    show ross 10
    show player 2f
    player_name "Mal posso esperar! "
    show player 1f
    show ross 11
    ross "Agora, há mais alguma coisa em que eu possa ajudá-lo? "
    show ross 10
    return

label button_ross_end_no:
    show player 10f
    player_name "Oh, eu não posso hoje à noite, {b}Miss Ross{/b}..."
    player_name "... Eu tenho outros planos."
    show player 11f
    show ross 25
    ross "Aww, isso é muito ruim. "
    ross "... Deixe-me saber se algo mudar."
    show ross 11
    ross "Eu sempre arranjarei tempo para você, {b}[firstname]{/b}"
    show player 1f
    ross "Agora, há mais alguma coisa em que eu possa ajudá-lo? "
    show ross 10
    return

label button_ross_get_paint_grace_reminder:
    scene location_school_art_closeup
    show player 2f at right
    show ross 10 at left
    player_name "... Quem eu deveria {b}perguntar sobre a tinta{/b} novamente?"
    show player 1f
    show ross 11
    ross "Começar com {b}Eve{/b}."
    ross "Se tivermos sorte, ela pode ter uma tinta extra em casa que possamos usar. "
    show player 2f
    show ross 10
    player_name "Tudo bem, eu vou perguntar a ela. "
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
