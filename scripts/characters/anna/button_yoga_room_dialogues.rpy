label anna_button_yoga_room_dialogue_pre:
    scene yoga_room_night
    show anna 2 at right
    show player 13 at left
    with dissolve
    anna "Oi, {b}[firstname]{/b}."
    show anna 1
    show player 14
    player_name "Oi, {b}Anna{/b}."
    show player 13
    show anna 2
    anna "E aí?"
    show anna 1
    return

label anna_button_yoga_room_dialogue_wheres_mrsj:
    show player 14
    player_name "Estou procurando por {b}Mrs. Johnson{/b}."
    show player 30
    player_name "Você sabe onde eu poderia encontrá-la?"
    show player 5
    show anna 2
    anna "Ela geralmente ensina durante o dia."
    anna "Ela deve estar em casa agora..."
    show anna 1
    show player 14
    player_name "Oh Eu vejo. obrigado!"
    show player 13
    show anna 3
    anna "Sem problema!"
    return

label anna_button_yoga_room_dialogue_yoga:
    show player 10
    player_name "Você quer praticar algumas poses de ioga comigo?"
    show player 5
    show anna 3
    anna "Claro!!"
    show anna 2
    anna "Eu gosto quando alguém pode me ajudar a alcançar essas ... posturas difíceis..."
    show anna 1
    show player 33
    player_name "Certo, você é bastante flexível, como me lembro."
    show player 13
    show anna 2
    anna "Tudo bem, vamos encontrar um tapete de ioga..."
    hide anna
    scene location_gym_yoga_front
    with fade
    show player 413 at left
    show anna 13
    with dissolve
    anna "Qual posição devemos praticar?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
