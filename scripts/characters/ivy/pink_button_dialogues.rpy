label button_ivy_start_intro:
    scene location_pink_closeup
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    ivy "Oi!"
    ivy "Eu posso te ajudar com alguma coisa?"
    show player 29
    show ivy 1
    player_name "É a minha primeira vez aqui. Eu ... Umm..."
    show player 13
    show ivy 3
    ivy "Está bem! Compreendo! Todo mundo é um pouco tímido quando eles vêm aqui..."
    show ivy 2
    ivy "Temos uma grande variedade de {b}brinqueos{/b} e {b}roupas sexy{/b} que você pode ver na nossa tela."
    show player 11
    ivy "Nós também podemos oferecer uma... {b}sessão de massagem de corpo inteiro{/b} em um de nossos ... quartos privativos."
    ivy "Nossa massagista utiliza uma variedade de técnicas naturais de relaxamento corporal ... Isso certamente satisfará suas necessidades..."
    show player 12
    show ivy 1
    player_name "Oh ... eu não sabia que você oferecia massagens aqui."
    show player 1
    show ivy 3
    ivy "É um dos nossos ... serviços ... menos anunciados."
    show ivy 2
    ivy "Deseja ver sua seleção de mensagens no {b}panfleto{/b}?"
    return


label button_ivy_end_intro:
    scene pink
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    ivy "Oi!"
    ivy "Eu posso te ajudar com alguma coisa?"
    return

label button_ivy_diane_outfit_package:
    show ivy 1
    show player 2
    player_name "Estou aqui para pegar um {b}pacote{/b}."
    show player 1
    show ivy 3
    ivy "Certo!"
    show ivy 2
    ivy "Em que nome está?"
    show ivy 1
    show player 12
    player_name "{b}Diane{/b}?"
    show player 1
    show ivy 11
    ivy "Deixe-me verificar ... Certo! Aqui está!"
    show ivy 1
    show player 170
    player_name "Obrigado!"
    show ivy 3
    show player 169
    ivy "Isso é para a sua {b}namorada{/b}?"
    show ivy 1
    show player 171
    player_name "!!!"
    show player 29
    player_name "Ah não! É para ... Ummm ... Alguém me pediu para pegar isso por ele!"
    show ivy 2
    show player 13
    ivy "Bem, é um item muito legal da nossa coleção..."
    show ivy 3
    ivy "Tenho certeza que você vai gostar!"
    show player 21
    show ivy 4
    player_name "Obrigado..."
    hide player 21
    hide ivy 4
    show unlock29 at truecenter
    with dissolve
    pause
    hide unlock29 with dissolve
    return

label button_ivy_massage:
    show ivy 5
    show player 21
    player_name "Eu posso ver ... seu panfleto de massagem?"
    show player 13
    show ivy 4
    ivy "Certo! aq está!"
    player_name "Obrigado..."
    hide ivy
    hide player
    with dissolve
    return

label button_ivy_just_shopping:
    show player 10
    show ivy 1
    player_name "Vou bem obrigado."
    player_name "Eu só estou aqui para fazer compras..."
    show player 13
    show ivy 3
    ivy "Tudo bem então! Se você precisar de mais alguma coisa é só me chamar."
    return

label button_ivy_massage_first:
    show ivy 5
    show player 21
    player_name "Eu acho que eu poderia dar uma olhada nisso..."
    show player 13
    show ivy 4
    ivy "Certo! aq está!"
    hide ivy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
