label kassy_first_visit:
    show player 1f at right
    show kassy f_normal_talk at flip
    with dissolve
    Kass "Bem-vindo ao {b}cupido{/b}. Meu nome é {b}Kassy{/b}, existe algo que eu possa ajudá-lo a encontrar hoje? "
    show player 2f
    show kassy f_normal
    player_name "Não, obrigado, estou apenas olhando em volta. "
    show player 1f
    show kassy f_normal_talk
    Kass "Tudo bem. Bem, deixe-me saber se você precisar de alguma ajuda. "
    show player 2f
    show kassy f_normal
    player_name "Vai fazer! Obrigado, {b}Kassy{/b}."
    show player 1f
    show kassy f_normal_talk
    Kass "O prazer é meu!"
    return

label kassy_repeat:
    show player 2f at right
    show kassy f_normal at flip
    with dissolve
    player_name "oi{b}Kassy{/b}!"
    show player 1f
    show kassy f_normal_talk
    Kass "Olá, com o que posso ajudá-lo?"
    show player 2f
    show kassy f_normal
    player_name "Nada agora, apenas dando uma olhada
    show player 1f
    show kassy f_normal_talk
    Kass "Tudo bem. Bem, me dê um grito se precisar de algo."
    show player 2f
    show kassy f_normal
    player_name "ode deixar, obrigado"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
