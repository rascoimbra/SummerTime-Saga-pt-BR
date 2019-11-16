label mrsj_button_yoga_room_dialogue_pre_first:
    show player 1 at left
    show mrsj 10 at right
    with dissolve
    player_name "Umm-"
    show player 11 at left
    window hide
    pause
    player_name "..."
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right with hpunch
    mrsjo "Oh!"
    show player 18 at left
    mrsjo "...{b}[firstname]{/b}?"
    show mrsj 14 at right
    show player 17 at left
    player_name "Oi, {b}Mrs. Johnson{/b}!"
    show mrsj 17 at right
    show player 1 at left
    mrsjo "O que você está fazendo aqui?"
    show mrsj 14 at right
    show player 29 at left
    player_name "Eu ... vi você do principal {b}Academia{/b}!"
    player_name "Eu só vim dizer oi! "
    show player 13 at left
    show mrsj 18 at right
    mrsjo "Isso é tão querido!"
    show mrsj 17 at right
    mrsjo "Então você está malhando agora, hein? "
    show mrsj 14 at right
    show player 21 at left
    player_name "Haha Sim..."
    player_name "...Apenas comecei a treinar para ficar em forma! "
    show mrsj 19 at right
    show player 11 at left
    mrsjo "E aposto que você vai ficar legal e {b}Difícil{/b}-"
    mrsjo "..."
    show player 13 at left
    show mrsj 18 at right
    mrsjo "Quero dizer, {b}Forte{/b}!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Acredito que sim..."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Enfim, há algo que você gostaria de conversar? "
    return

label mrsj_button_yoga_room_dialogue_pre_repeat:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Oi, {b}Mrs. Johnson{/b}!"
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Oi, {b}[firstname]{/b}!"
    show player 11 at left
    show mrsj 18 at right
    mrsjo "Você está começando a parecer em forma, jovem! "
    show player 29 at left
    show mrsj 14 at right
    player_name "Oh Obrigado..."
    player_name "Então você está ..."
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Você gostaria de falar sobre algo? "
    return

label mrsj_button_yoga_room_dialogue_hows_erik:
    show player 10 at left
    show mrsj 14 at right
    player_name "Como está o {b}Erik{/b} hoje em dia? "
    player_name "Eu quase não o vejo. "
    show mrsj 18 at right
    show player 5 at left
    mrsjo "Bem ... Você sabe como ele é! "
    mrsjo "Ele simplesmente ama seus videogames ..."
    show player 10 at left
    show mrsj 14 at right
    player_name "Sim, mas tem sido ainda pior ultimamente. "
    player_name "Eu nem recebo mensagens de texto dele ..."
    show mrsj 19 at right
    show player 5 at left
    mrsjo "..."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "Sabe, acho que ele está tendo problemas para se adaptar à vida sozinho. "
    mrsjo "Eu me preocupo com ele."
    show mrsj 19 at right
    show player 12 at left
    player_name "Eu não fazia ideia."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "Ele não está acostumado a ser o homem da casa. "
    mrsjo "... E ele tem muita dificuldade com garotas."
    show mrsj 19 at right
    mrsjo "O pobre coitado tem que estar sozinho. "
    show mrsj 14 at right
    show player 21 at left
    player_name "...Sim. Eu acho que entendi."
    show mrsj 18 at right
    show player 13 at left
    mrsjo "É bom que ele tenha um amigo leal como você, {b}[firstname]{/b}!"
    mrsjo "Ele precisa de você. "
    show mrsj 14 at right
    show player 17 at left
    player_name "Bem, sempre fomos amigos, então ... "
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Vou dizer a ele para mandar uma mensagem com mais frequência! "
    show mrsj 14 at right
    show player 14 at left
    player_name "Está tudo bem, eu só queria ter certeza de que ele está bem. "
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Você gostaria de falar sobre mais alguma coisa? "
    return

label mrsj_button_yoga_room_dialogue_what_was_that:
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_pre")
    if M_anna.is_state(S_anna_start):
        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_anna_intro")
        $ M_anna.trigger(T_anna_intro)
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_after")
    return

label mrsj_button_yoga_room_dialogue_what_was_that_pre:
    show mrsj 14 at right
    show player 14 at left
    player_name "O que foi essa {b}pose de ioga{/b} que você estava fazendo antes? "
    show mrsj 13 at right
    show player 13 at left
    show player 1 at left
    mrsjo "Oh, eu vou te mostrar! "
    show mrsj 12 at right
    show player 11 at left
    mrsjo "Você começa assim! "
    show mrsj 11 at right
    window hide
    pause
    show player 21 at left
    show mrsj 10 at right
    window hide
    pause
    mrsjo "De joelhos! "
    window hide
    pause
    show player 21 at left
    player_name "Uhhh..."
    player_name "...Sim..."
    show player 11 at left
    mrsjo "É chamado de {b}Vaca de gato{/b}!"
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right
    show player 18 at left
    mrsjo "Não é ruim, certo? "
    return

label mrsj_button_yoga_room_dialogue_what_was_that_anna_intro:
    show anna 12f at Position (xpos=600)
    show mrsj 13 at right
    show player 13
    with dissolve
    anna "Olá, {b}Tammy{/b}."
    show anna 5f
    anna "Não me diga que você começou sem mim. "
    show anna 4f
    show mrsj 18
    mrsjo "Claro que não! Estou apenas conversando com um amigo do meu inquilino, {b}Erik{/b}!"
    show anna 11 at Position (xpos=700) with dissolve
    show mrsj 17b
    mrsjo "{b}Anna{/b}, isto é {b}[firstname]{/b}. {b}[firstname]{/b}, este é o meu amigo, {b}Anna{/b}."
    show mrsj 14
    show player 36 with dissolve
    player_name "Oi!"
    show player 13 with dissolve
    show mrsj 14b
    show anna 12
    anna "Você é amigo do {b}Erik{/b}?"
    show anna 11
    show player 14
    show mrsj 14
    player_name "Sim. Somos amigos há muito tempo. "
    show player 12
    player_name "Você também é treinador aqui? "
    show player 5
    show anna 2 with dissolve
    show mrsj 14b
    anna "Ah não. Eu sou apenas um estudante. "
    show anna 1
    show player 13
    show mrsj 17
    mrsjo "{b}Anna{/b} é um dos meus melhores. Ela poderia ensinar aqui se quisesse! "
    show mrsj 14b
    show anna 3
    anna "Acho que não! Ha ha! "
    show anna 2
    anna "Ela é uma ótima professora e eu sou apenas uma novata. "
    show anna 1
    show mrsj 17
    mrsjo "{b}Anna{/b}, é apenas ser humilde ".
    show mrsj 17b
    mrsjo "Ela pode ser iniciante, mas é muito talentosa ... e extremamente flexível. "
    show mrsj 14b
    show anna 3
    anna "Ha ha."
    show anna 2
    anna "Eu tenho que ir agora e me preparar para a minha próxima lição. "
    show anna 3
    anna "Adeus, {b}Tammy{/b}!"
    show anna 1
    show mrsj 17b
    mrsjo "Te vejo em breve."
    show mrsj 14b
    show anna 2
    anna "Foi um prazer conhece-lo, {b}[firstname]{/b}."
    show anna 1
    show player 14
    show mrsj 14
    player_name "Tchau!"
    hide anna with dissolve
    return

label mrsj_button_yoga_room_dialogue_what_was_that_after:
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Você gostaria de falar sobre mais alguma coisa? "
    return

label mrsj_button_yoga_room_dialogue_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Eu tenho que dizer, {b}Mrs. Johnson{/b}, você está realmente em forma! "
    player_name "Você se exercita muito? "
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Ah ... você é tão legal! "
    show mrsj 17 at right
    mrsjo "Bem, eu venho aqui sempre que posso e tento usar a academia ... "
    mrsjo "... eu também vou correr! E eu faço yoga no meu quarto à noite também ..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Bem, está funcionando! "
    show player 13 at left
    mrsjo "Você pensa?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "Minha {b}bunda{/b} ainda é um pouco grande ... "
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...E meus {b}peitos{/b} não são como costumavam ser ... "
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*gole*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Você gostaria de falar sobre mais alguma coisa? "
    return

label mrsj_button_yoga_room_dialogue_have_to_train:
    show mrsj 14 at right
    show player 14 at left
    player_name "Eu deveria voltar ao meu treinamento! "
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Está bem então!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Tchau, {b}Mrs. Johnson{/b}!"
    hide player 17 at left with dissolve
    hide mrsj 14 at right with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
