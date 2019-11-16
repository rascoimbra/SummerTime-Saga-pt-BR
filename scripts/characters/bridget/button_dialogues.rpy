label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show player 11 at left
    show bridget f_angry_talk at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "O que você esta fazendo aqui?"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Desculpe, senhora!!!"
    player_name "Eu só tinha algumas perguntas!"
    show player 31
    show bridget f_angry_talk
    bri "Questões?!"
    bri "Como o quê?"
    show bridget a_dressed_crossed f_angry
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show player 11 at left
    show bridget f_angry_talk at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "É melhor você estar treinando sua bunda na {b}Gym{/b}, ou vou enfiar meu pé na sua bunda!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Sim, senhora!!!"
    show player 31
    show bridget f_angry_talk
    bri "Tem alguma dúvida?!"
    show bridget a_dressed_crossed f_angry
    return

label coach_bridget_dialogue_training_advice:
    show player 10
    show bridget a_dressed_crossed f_normal
    player_name "Eu ... Bem, onde devo treinar?"
    show bridget a_dressed_crossed f_angry
    show player 5
    bri "..."
    show player 22
    show bridget f_angry_talk
    bri "eu acabei de te dizer!"
    show bridget a_dressed_crossed f_angry_yell
    bri "No {b}GYM{/b}!!!"
    show player 10
    show bridget a_dressed_crossed f_angry
    player_name "Mas ... O que devo treinar?"
    show player 11
    show bridget f_angry_talk
    bri "Você tem que trabalhar no seu {b}strength{/b} e {b}dexterity{/b} se você quiser fazer!"
    bri "Você estará competindo no {b}110m com obstáculo{/b} corrida para qualificar isso {b}school{/b} e sua equipe no {b}state championship{/b}!"
    show player 10
    show bridget a_dressed_crossed f_angry
    player_name "Isso é ... Muita pressão."
    show player 23
    show bridget f_angry_talk
    bri "...E é melhor você não me deixar!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Sim, senhora!!!"
    hide bridget
    hide player
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show player 10
    show bridget a_dressed_crossed f_normal
    player_name "Eu esqueci."
    show player 11
    show bridget f_angry_talk
    bri "Esqueceu? Garoto, você é o pedaço de carne mais triste que eu já vi!"
    show player 22
    show bridget a_dressed_crossed f_angry_yell
    bri "Agora saia daqui e vá para {b}WORK{/b}!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Sim, senhora!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
