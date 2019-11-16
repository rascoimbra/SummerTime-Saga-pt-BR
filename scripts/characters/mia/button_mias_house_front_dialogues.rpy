label mia_dialogue_mias_house_front_intro:
    scene location_mia_closeup
    show player 14 at left
    show mia 1 at right
    with dissolve
    player_name "Ei {b}Mia{/b}!"
    show mia 4
    show player 1
    mia "Ei {b}[firstname]{/b}!"
    mia "O que você está fazendo aqui? "
    show mia 1
    show player 29
    player_name "Umm ... eu queria te perguntar uma coisa! "
    return

label mia_dialogue_mias_house_front_homework:
    show player 21
    player_name "Você ainda precisa de ajuda para estudar para os exames? "
    show mia 3
    show player 13
    mia "Claro! Eu estive procurando {b}alguém para estudar{/b}..."
    show mia 6
    show player 11
    mia "...Mas você já alcançou a aula? "
    show mia 2
    show player 10
    player_name "Oh! Direito! Eu provavelmente deveria ter aulas particulares de {b}Miss Bissette{/b} para recuperar o atraso ... "
    show mia 6
    show player 13
    mia "Sim, você provavelmente deveria fazer isso primeiro! "
    show mia 4
    mia "Então você pode vir à minha casa ... e estudaremos no meu quarto! "
    show mia 1
    show player 14
    player_name "Sim ... sim? "
    show mia 3
    show player 1
    mia "Certo! Vai ser divertido!"
    show mia 1
    show player 17
    player_name "Tudo bem ... eu vou deixar você saber quando eu terminar com eles! "
    show mia 4
    show player 1
    mia "Te vejo em breve!"
    hide mia with dissolve
    show player 5 with dissolve
    player_name "( Eu deveria tentar terminar meu {b}lição de casa francesa{/b}, para que eu possa estudar com {b}Mia{/b}. )"
    show player 4
    pause
    
Eu me pergunto por que ela me escolheu para ajudá-la a estudar. ) "
    player_name "(ela geralmente estuda com {b}Judith{/b} e é muito boa em francês ...)"
    player_name "(... não sei como poderia ajudá-la.)"
    show player 13
    player_name "( Pelo menos nós vamos sair, e ela é muito fofa ...) "
    hide player with dissolve
    return

label mia_dialogue_mias_house_front_leave:
    show player 4
    player_name "Hmm ... Sim, mas eu esqueci! "
    show mia 3
    show player 11
    mia "Haha! Você é engraçado ~ "
    show mia 1
    show player 17
    player_name "Desculpa! Não me lembro do que queria dizer! "
    show player 14
    player_name "Eu deveria ir. "
    show mia 4
    show player 1
    mia "Tenha uma boa noite!"
    hide player
    hide mia
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
