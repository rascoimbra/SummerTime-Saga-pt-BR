label dewitt_dialogue_lounge_intro:
    scene location_school_lounge_couch
    show player 10 at left
    show dewittl 5 at right
    with dissolve
    pause
    show dewittl 1 with dissolve
    player_name "Oh, oi, {b}Miss DeWitt.{/b}"
    show player 11
    show dewittl 3 with dissolve
    dewitt "{b}[firstname]{/b}? Você não deveria estar aqui ... "
    show player 10
    show dewittl 2
    player_name "Sim, desculpe-me."
    show player 2
    player_name "{b}Miss Ross{/b} me faz procurar revistas antigas ".
    player_name "Estamos fazendo uma colagem!"
    show player 1
    show dewittl 3
    dewitt "Colagem, hein?"
    dewitt "Eu costumava fazer isso o tempo todo quando era mais jovem!"
    show player 2
    show dewittl 2
    player_name "O que você está comendo?"
    show player 1
    show dewittl 3b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Oh isso?"
    show dewittl 3 at right with dissolve
    dewitt "É um dos {b}Brownies especiais de Barbara{/b}."
    show player 2
    show dewittl 2
    player_name "Eu não sabia {b}Miss Ross{/b} poderia assar? "
    show player 1
    show dewittl 3
    dewitt "Ela faz os melhores brownies!"
    dewitt "Eu simplesmente não consigo o suficiente!"
    show player 2
    show dewittl 2
    player_name "... Arrumada!"
    player_name "Então, você acha que eu poderia ter algumas daquelas revistas sobre a mesa?"
    show player 1
    show dewittl 3
    dewitt "Não vejo por que não."
    show player 2
    show dewittl 2
    player_name "Awes-"
    show player 11
    show dewittl 6 with dissolve
    dewitt "Se você puder responder uma pergunta do meu próximo teste!"
    show player 10
    show dewittl 2 with dissolve
    player_name "Realmente?"
    show player 11
    show dewittl 3
    dewitt "Nada é de graça na vida, {b}[firstname]{/b}."
    dewitt "Agora vamos ver ..."
    dewitt "A flauta é um membro de qual família instrumental?"
    return

label dewitt_dialogue_lounge_stat_pass:
    show player 2 at left
    show dewittl 2 at right
    player_name "That's easy! Woodwind."
    show player 1
    show dewittl 3
    dewitt "Muito bom, {b}[firstname]{/b}!"
    dewitt "Acho que você está prestando atenção na aula, afinal."
    show dewittl 4 with dissolve
    dewitt "Vá em frente e pegue quantas revistas precisar."
    show player 595 with dissolve
    show dewittl 2
    player_name "Impressionante!"

    player_name "Obrigado, {b}Miss Dewitt{/b}! Aproveite o seu brownie! "
    show player 594
    show dewittl 1b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Ohm, que bom! Mmm ..."
    return

label dewitt_dialogue_lounge_stat_fail:
    show player 10
    show dewittl 2
    player_name "[int_warn]Err ... O instrumento tem famílias? "
    show player 11
    show dewittl 3
    dewitt "[int_warn]Heh, bem, isso é algo que você deve descobrir se quiser essas revistas. "
    dewitt "[int_warn]Volte quando souber a resposta. "
    show dewittl 2
    show player 10
    player_name "[int_warn]Ah cara ... "
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
