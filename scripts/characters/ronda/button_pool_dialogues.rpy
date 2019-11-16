label ronda_pool_dialogue_pre_cassie_fun:
    show ronda b_swim a_swim_sides f_normal at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "..."
    show ronda f_normal_talk
    ron "O que você está fazendo aqui? "
    show ronda f_normal
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Apenas fazendo exercício! "
    player_name "Achei que tinha que começar em algum lugar, e isso pode me ajudar a me preparar para as eliminatórias!"
    show ronda f_normal_talk
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Olha: eu não estou ajudando você, muito menos entrar na água ao mesmo tempo que você ... Então esqueça, ok? "
    show ronda f_normal
    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "Isso é bom!"
    player_name "Eu posso gerenciar sozinho ..."
    show ronda f_rolleyes
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Ugh ... tanto faz. "
    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda b_swim a_swim_sides f_upset_talk at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "Aqui para pagar {b}Cassie{/b} uma pequena visita? "
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh ... eu só estou aqui para nadar! "
    show ronda f_upset_talk
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Você pode parar de fingir ... "
    ron "... Você não está aqui para treinar, como eu."
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh ... ok?"
    show ronda f_upset_angry
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Ugh ... você é patético. "
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
