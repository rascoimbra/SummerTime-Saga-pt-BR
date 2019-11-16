label erik_dialogue_intro:
    scene location_school_computer_day_blur
    show player 2 at left
    show erik 1 at right
    with dissolve
    return

label erik_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Estou ajudando Okita com um projeto."
    show player 1
    show erik 4
    eri "Realmente fantástico!"
    eri "Que tipo de projeto é esse?"
    show player 2
    show erik 1
    player_name "Uhh, acho que não devo dizer ..."
    show player 1
    show erik 4
    eri "Oh, pesquisa secreta?"
    eri "Legal, posso ajudar?"
    show player 2
    show erik 1
    player_name "Na verdade sim!"
    player_name "Eu preciso encontrar um par de {b}lenses{/b}."
    player_name "Você não teria um par extra de óculos, teria?"
    show player 1
    show erik 4
    eri "Está brincando?"
    eri "Você sabe quantas vezes {b}Dexter{/b} quebrou esse par? "
    eri "Eu sempre mantenho um conjunto sobressalente por perto."
    show player 2
    show erik 1
    player_name "Ótimo!!"
    player_name "Você me deixaria tê-los?"
    show player 1
    show erik 4
    eri "Sure!"
    show player 2
    show erik 1
    player_name "Obrigado, cara!"
    show player 1
    show erik 4
    eri "Não tem problema, {b}[firstname]{/b}! Para que São os amigos?"
    show player 10
    show erik 1
    player_name "... Oh, espera!"
    show player 29 with dissolve
    player_name "Eu esqueci, eles precisam ser {b}Varifocal lenses{/b}..."
    show player 3
    show erik 5
    eri "o que?"
    show player 10 with dissolve
    show erik 1
    player_name "Você é míope ou hipermetropico?"
    show player 11
    show erik 5
    eri "Míope. Por quê?"
    show player 10
    show erik 1
    player_name "Merda! Eu preciso de lentes de alguém que é ambos."
    show player 11
    show erik 5
    eri "Oh."
    show player 24
    show erik 1
    player_name "*suspiro*"
    show player 10
    player_name "Acho que vou ter que continuar procurando."
    show player 11
    show erik 5
    eri "Desculpa, {b}[firstname]{/b}."
    show player 2
    show erik 1
    player_name "Está tudo bem, {b}Erik{/b}. Obrigado de qualquer forma."
    show player 1
    show erik 4
    eri "A qualquer momento, cara."
    return

label erik_dialogue_leave:
    show player 14
    player_name "Oh nada!"
    player_name "Só dizendo Oi."
    show player 1
    show erik 4
    june "Oh, ok então ..."
    show erik 1
    show player 29 at Position(xoffset=8)
    player_name "Err ... te vejo mais tarde!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
