label bubbles_button_intro:
    scene movie_lobby with None
    show bubbles f_normal_talk o_desk at flip
    show player at flip
    with dissolve
    bub "Bem-vindo ao {b}CineSaga Theater{/b}, Meu nome é {b}Bubbles{/b}."
    bub "Como posso ajudá-lo?"
    show bubbles f_normal
    return

label bubbles_movie_select_pre:
    show player f_normal_talk
    player_name "Eu gostaria de ver um filme."
    show player f_normal
    show bubbles f_normal_talk
    bub "Certo."
    bub "Os ingressos são {b}Fifty dollars{/b} e tudo o que você precisa fazer é selecionar o que deseja ver..."
    show bubbles f_normal
    show player f_normal_talk
    player_name "Legal!"
    show player f_normal
    return

label bubbles_button_nevermind:
    show player f_normal_talk
    player_name "Só estou olhando, obrigado."
    show player f_normal
    show bubbles f_normal_talk
    bub "Tudo bem."
    bub "Deixe-me saber se você quer assistir algo."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
