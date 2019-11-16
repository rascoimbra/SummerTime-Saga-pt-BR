label button_ross_grab_clay:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "Vá pegar um pouco de barro, {b}[firstname]{/b}, para que possamos começar."
    show player 2f
    show ross 1
    player_name "Sim, senhora."

    return

label button_ross_find_partner:
    scene location_school_art_closeup
    show player 2f at right
    show ross 1 at left
    with dissolve
    player_name "Ei, {b}Miss Ross{/b}. Você está pronto para começar?"
    show player 1f
    show ross 2
    ross "Olá, {b}[firstname]{/b}! Quase ..."
    show ross 11 with dissolve
    ross "Eu realmente queria discutir algo com você primeiro."
    show player 2f
    show ross 10
    player_name "Oh?"
    show ross 11
    show player 1f
    ross "Acho que devemos arranjar um parceiro para você nessas sessões, o que você acha?"
    show ross 10
    show player 10f
    player_name "Um parceiro?"
    show ross 11
    show player 11f
    ross "Sim, alguém para trabalhar ao seu lado e rejeitar a ideia de um lado para o outro!"
    show ross 10
    show player 2f
    player_name "Claro, tudo bem."
    player_name "Você tem alguém em mente?"
    show player 1f
    show ross 10b with dissolve
    ross "Hmm..."
    show ross 11 with dissolve
    ross "Bem, meu pensamento inicial era de {b}Eve{/b}. Ela é uma artista talentosa como você ..."
    ross "... Mas duvido que ela tenha tempo com todos os seus estudos musicais."
    show ross 10b with dissolve
    pause
    show ross 11 with dissolve
    ross "Você acha que {b}Mia{/b} estaria interessado?"
    ross "Ela é uma gracinha, não é !?"
    show ross 10
    show player 2f
    player_name "Err, sim. Suponho."
    show player 1f
    show ross 11
    ross "Ótimo! Bem, por que você não vai falar com ela?"
    ross "Diga a ela que eu disse para trazer sua bunda fofa aqui!"
    show player 11f
    show ross 10
    player_name "..."

    return

label button_ross_ask_mia_partner:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "{b}[firstname]{/b}, você voltou!"
    ross "Onde está {b}Mia{/b}?"
    show player 10f
    show ross 1
    player_name "Ah, uhh ... eu ainda não a convenci."
    show player 11f
    show ross 2
    ross "Bem, vamos lá, {b}[firstname]{/b}!"
    ross "Precisamos do entusiasmo dela para ganhar essa coisa!"
    return

label button_ross_mia_is_partner:
    scene location_school_art_closeup
    show player 1f zorder 1 at right
    show ross 2 at left
    show mia 7 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "Olá, torta fofa!"
    show ross 1
    show mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "... Oh, umm. Olá."
    show ross 2
    show mia 55
    ross "Estou tão feliz que {b}[firstname]{/b} o convenceu a se juntar a nós!"
    show ross 1
    show mia 56
    mia "Hehe, sim ... Ele disse que vocês realmente precisavam da minha ajuda?"
    show ross 2
    show mia 55
    ross "Nós certamente precisamos!"
    show ross 1
    show player 2f
    show mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    player_name "Então, estamos prontos para começar agora?"
    show player 1f
    show ross 11 with dissolve
    ross "Sim! Por que vocês não pegam suas almofadas de arte e se sentam um em frente ao outro."
    show player 2f
    show ross 10
    player_name "Ok."
    show mia 8
    show player 596f with dissolve
    mia "..."
    show mia 12
    mia "Umm, pergunta ..."
    show mia 8
    show ross 11
    ross "Sim, querida?"
    show mia 12
    show ross 10
    mia "E se eu não tiver um bloco de arte?"
    show mia 8
    show ross 25
    ross "Oh, certo."
    show ross 25b
    ross "Bem, normalmente eu daria a você um desses ..."
    show ross 25
    ross "... Mas receio que tenhamos esgotado nossas lojas."
    show ross 24
    show player 598f
    player_name "Isso é péssimo!"
    show player 596f
    show mia 12b
    mia "Oh, bem, não é grande coisa. Eu não sou muito boa em desenhar de qualquer maneira ..."
    show mia 10
    mia "Eu vou assistir."
    show mia 7
    show ross 11
    ross "Bobagem!"
    ross "Nós vamos pegar um para você!"
    show ross 27 with dissolve
    ross "{b}[firstname]{/b}, por que você não pergunta a {b}Eve{/b} se podemos pegar emprestado um dela."
    show ross 26
    show player 598f
    player_name "... S-sim, ok!"
    show ross 27
    show player 596f
    ross "Veja, {b}[firstname]{/b} para o resgate!"
    show player 1f
    show ross 11
    with dissolve
    ross "Nós vamos ficar aqui e conversar sobre garotas."
    show ross 13
    ross "Certo, torta fofa?"
    show ross 12
    show mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Heh, ok ..."
    show mia 55
    show player 2f
    player_name "Volto já."
    return

label button_ross_find_art_pad:
    scene location_school_art_closeup
    show ross 13 at left
    show mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 1f at right
    with dissolve
    ross "... Você sabe, {b}Mia{/b}. Eu costumava ser amiga de uma garota que se parecia com você!"
    show ross 12
    show mia 56
    mia "Sério?"
    show ross 13
    show mia 55
    ross "Serio! O nome dela era Starchild e nós seguíamos nossa banda favorita em todo o país."
    show ross 12
    show mia 12b at Position(xpos=0.45, ypos=1.0) with dissolve
    mia "Bem, isso parece bem legal!"
    show ross 13
    show mia 8b
    ross "Oh, foi!"
    ross "Essa garota sempre teve as melhores drogas!"
    show ross 11
    ross "... E que beijadora! Ela podia fazer coisas com a língua que iam-"
    show player 10f
    show ross 10
    show mia 55 at Position(xpos=0.435, ypos=1.0) with dissolve
    player_name "* Ahem * Estou interrompendo alguma coisa?"
    show player 11f
    show mia 12f with dissolve
    mia "{b}[firstname]{/b}, você voltou!"
    show mia 12bf
    mia "Graças a Deus!"
    show mia 8bf
    show ross 11
    ross "Você conseguiu o {b}artpad da Eve{/b}?"
    show player 10f
    show ross 10
    player_name "Não, desculpe. Ainda estou trabalhando nisso."
    show player 11f
    show ross 11
    ross "Tsk, bem, ai! Vamos conversar sobre garotas aqui ..."
    show ross 10
    show player 10f
    player_name "... tudo bem. Eu voltarei."
    hide player with dissolve
    show mia 12f at Position(xpos=0.55, ypos=1.0) with dissolve

    mia "Não! Espere! Espere!"
    show mia 8f
    pause
    show ross 13 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Agora, onde eu estava?"
    show ross 12
    show mia 8b with dissolve
    mia "..."
    show ross 13
    ross "Oh, certo! Ela poderia fazer coisas com a língua que fariam uma prostituta corar!"
    show ross 12
    show mia 56 at Position(xpos=0.535, ypos=1.0) with dissolve
    mia "... oh meu."
    return

label button_ross_found_art_pad:
    scene location_school_art_closeup
    show ross 46 at left
    show mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 11f zorder 1 at right
    with dissolve
    ross "... Hmm, acho que o meu favorito é a {b}Praia do Abricó{/b}"
    show ross 11 with dissolve
    ross "Está de volta em casa no Rio de Janeiro."
    show ross 10
    show mia 56
    mia "Oh, eu não sei ..."
    mia "... eu não acho que sou corajosa o suficiente para ir em uma praia de nudismo."
    show ross 13
    show mia 55
    ross "Oh, com certeza, torta fofa!"
    ross "Ninguém deveria se envergonhar de seu corpo. Afinal, a forma humana é uma obra de arte ..."
    show ross 13
    ross "... Especialmente o seu."
    ross "Você é absolutamente linda, {b}Mia{/b}!"
    show ross 12
    show mia 56
    mia "Uau, eu ... Uhh ..."
    show player 10f

    player_name "{b}*Ahem*{/b}"
    show player 11f
    show mia 12bf with dissolve
    mia "Oh, {b}[firstname]{/b}, graças a Deus você voltou!"
    show mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    show player 2f
    player_name "Vocês estão se divertindo?"
    show player 1f
    show ross 11
    ross "Estamos nos divertindo!"
    ross "Presumo que você tenha o {b}Art Pad{/b}?"
    show ross 10
    show player 598f with dissolve
    player_name "Sim, está bem aqui."
    show player 596f
    show ross 11 with dissolve
    ross "Bom trabalho, {b}[firstname]{/b}!"
    ross "Nós devemos começar agora."
    ross "Quero que vocês dois se sentem um diante do outro."
    show ross 58 with dissolve
    ross "... Porque hoje vocês vão desenhar retratos um do outro usando lápis e papel."
    show player 598f
    show ross 10 with dissolve
    player_name "Então você quer que eu desenhe {b}Mia{/b}?"
    show player 596f
    show ross 11
    ross "Isso mesmo e {b}Mia{/b}, quero que você desenhe {b}[firstname]{/b}."
    show ross 10
    show mia 12b
    mia "Eu vou tentar ..."
    show ross 13
    show mia 8b
    ross "Você é adorável demais, não é?"
    show ross 12
    show mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    ross "Não se preocupe, não existe arte ruim!"
    show mia 56
    mia "... Se você diz."
    show mia 55
    show ross 11
    ross "Agora vamos começar."


    scene location_school_art_cutscene06
    with fade
    show text "Eu sempre gostei de arte, mas desenhar um modelo ao vivo foi uma experiência totalmente diferente ..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... fico feliz que a {b}Miss Ross{/b} tenha escolhido {b}Mia{/b} como minha parceira para isso." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Ela realmente era fofa!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show player 1 zorder 1 at left
    show mia 8b at right
    show ross 11f zorder 0 at Position(xpos=0.535, ypos=1.0)
    with dissolve
    ross "Muito bem, vocês dois!"
    ross "É um desenho tão bonito, {b}[firstname]{/b}!"

    show ross 28f at Position(xpos=0.435, ypos=1.0) with dissolve
    ross "Estou me sentindo muito bem com nossas chances neste concurso de arte ..."
    ross "Você deve mostrar {b}Mia{/b}."
    show ross 12 at Position(xpos=0.35, ypos=1.0)
    show player 560
    with dissolve

    pause
    show mia 69
    mia "* suspiro *"
    show mia 10
    mia "Uau! É tão bom!"
    show mia 7
    show ross 11
    ross "Não é !?"
    show ross 13
    ross "É quase tão bonito quanto a coisa real!"
    show ross 13c
    ross "Você não acha, {b}[firstname]{/b}?"
    show player 561
    show ross 12b
    player_name "S-sim, quase ..."

    show player 560
    show ross 12
    show mia 56 with dissolve
    mia "Aww, obrigado {b}[firstname]{/b}."
    show mia 55
    show ross 13
    ross "Tudo bem então, vamos ver como você fez {b}Mia{/b}?"
    show mia 59b with dissolve
    mia "Mmm, não. Tudo bem. Prefiro que não."
    show ross 11
    show mia 59d
    ross "Oh, pish chique! Não brinque tanto!"
    ross "Lembre-se, não existe arte ruim ..."
    show ross 10
    show mia 59e
    mia "... Ok."
    show mia 59c
    show ross 24

    ross "..."
    show mia 59
    mia "Eu te disse, eu não sou muito bom ..."
    show mia 59c
    show ross 25
    ross "Bem, não, é - Interessante ..."
    show ross 11
    ross "Definitivamente, há espaço para melhorias."
    show player 561
    show ross 10
    player_name "Gostei, {b}Mia{/b}!"
    show player 560
    show mia 57
    mia "Você gostou mesmo?"
    show player 561
    show mia 58
    player_name "Sim, é realmente fofo!"

    show player 560
    show ross 11
    ross "Aí, agora veja, {b}Mia{/b}. {b}[firstname]{/b} gostou!"
    show ross 10
    mia "..."
    show ross 11
    ross "Bem, acho que é melhor encerrarmos por hoje."
    ross "Nós fizemos um progresso muito bom, vocês dois!"
    show ross 58 at Position(xpos=0.41, ypos=1.0) with dissolve
    ross "Certifique-se de que vocês descansem bastante e não se esqueçam de fazer as meditações que eu te ensinei!"
    show ross 10 at Position(xpos=0.35, ypos=1.0) with dissolve
    show player 2
    with dissolve
    player_name "Tudo bem, vou tentar, {b}Miss ross{/b}."
    player_name "Até mais, {b}Mia{/b}!"
    show player 1
    show mia 56 with dissolve
    mia "Tchau, {b}[firstname]{/b}."
    return

label button_ross_collage:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show mia 2f zorder 0 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "Você está pronto para outra sessão com {b}Miss Ross{/b}"
    show player 1f
    show mia 6f
    mia "Sim, eu acho ..."
    show player 10f
    show mia 2f
    player_name "Você não parece muito animada com isso."
    player_name "Eu pensei que você amava arte?"
    show player 11f
    show mia 6f
    mia "Eu amo arte."
    mia "... E eu realmente gosto de assistir você e a {b}Miss Ross{/b} trabalharem."
    show mia 6bf
    mia "É só que ..."
    show mia 6f
    mia "{b}Miss Ross{/b} me faz sentir um pouco constrangida."
    show player 10f
    show mia 2f
    player_name "Ela faz?"
    show player 11f
    show mia 6f
    mia "Ela está sendo muito sincera comigo, não acha?"
    show player 2f
    show mia 2f
    player_name "Sim, mas ela é assim com todos."
    show player 1f
    show mia 6f
    mia "Ela é?"
    mia "Não sei, ela viveu uma vida tão aventureira e é tão cheia de experiência ..."
    show mia 6bf
    mia "Ela me faz sentir tão chata."
    show player 2f
    show mia 2f
    player_name "Eu não acho você chata, {b}Mia{/b}."
    show player 1f
    show mia 4f
    mia "Você não?"
    show mia 1f
    show player 2f
    player_name "Nem um pouco."
    player_name "Eu acho que você só precisa relaxar e manter a mente aberta."
    player_name "Aposto que a {b}Miss Ross{/b} pode nos ensinar muitas coisas legais!"
    show mia 5f
    show player 1f
    mia "..."
    show mia 3f
    mia "Sim, talvez você esteja certo, {b}[firstname]{/b}!"
    show mia 4f
    mia "Eu poderia-"
    show mia 1f
    show player 11f
    show ross 11 at left with dissolve

    ross "Aqui estão meus alunos favoritos!"
    show mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "Do que vocês dois estão falando?
    show mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    show player 10f
    player_name "Pássaros do amor?"
    show mia 56
    show player 11f
    mia "Estávamos imaginando o que seria a sessão de hoje."
    show mia 55
    show ross 13
    ross "Direto aos negócios, hein?"
    ross "Seu pequeno foguete, eu adoro!"
    show ross 12
    mia "..."
    show ross 58 with dissolve
    ross "Hoje você vai fazer uma colagem!"
    show ross 10 with dissolve
    show mia 12b at Position(xpos=0.65, ypos=1.0) with dissolve
    mia "Colagem? Eu nem sei o que isso significa ..."
    show mia 8b
    show ross 27 with dissolve
    ross "Oh, elas são tão divertidas! Você vai amá-las {b}Mia{/b}!"
    ross "Vamos cortar fotos de revistas e colá-las para fazer arte."
    show ross 26
    show player 2f
    show mia 7
    player_name "Parece divertido para mim."
    show player 1f
    show mia 10
    mia "Sim, é verdade."
    show mia 7
    show ross 11 with dissolve
    ross "Tudo bem, eu tenho tudo o que precisamos aqui. {b}cola{/b} e {b}uma grande pilha de revistas.{/b}"
    ross "Por que vocês dois não vão nos encontrar?"
    show ross 10
    show player 2f
    player_name "Podemos fazer isso, certo {b}Mia{/b}?"
    show player 1f
    show mia 10b
    mia "Absolutamente. De fato, acho que meu {b}pai{/b} tem alguma cola em casa."
    show mia 10
    mia "Eu vou buscá-la!"
    hide mia with dissolve

    show ross 11
    ross "... E lá vai ela!"
    ross "Acho que isso significa que você é responsável por encontrar as {b}revistas, [primeiro nome]{/b}."
    ross "Se você encontrar {b}três GRANDES pilhas de revistas{/b}, acho que isso deve ser suficiente."
    show player 2f
    show ross 10
    player_name "Alguma idéia de onde eu poderia encontrar alguma?"
    show player 1f
    show ross 10b with dissolve
    ross "Hmm..."
    show ross 11
    ross "... eu começaria na {b}Biblioteca{/b}. Eles deveriam ter uma grande variedade para escolher!"
    show player 2f
    show ross 10
    player_name "Tudo bem, eu vou dar uma olhada."
    return

label button_ross_find_magazines:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show ross 10 at left
    with dissolve
    player_name "Onde você disse que eu deveria procurar de novo?"
    show player 1f
    show ross 11
    ross "Para as {b}revistas{/b}?"
    ross "Experimente a {b}Biblioteca{/b}."
    ross "E veja se você consegue encontrar {b}três GRANDES pilhas de revistas{/b}, está bem?"
    if M_ross.get("falei com Jane"):
        hide ross with dissolve
        show player 10 with dissolve
        player_name "{b}*Suspiro*{/b}"
        player_name "A biblioteca ainda não possui revistas."
        if M_ross.get("revistas restantes") == 3:
            player_name "E ainda preciso encontrar mais 3 revistas."
        elif M_ross.get("revistas restantes") == 2:
            player_name "E ainda preciso encontrar mais 2 revistas."
        elif M_ross.get("revistas restantes") == 1:
            player_name "E ainda preciso encontrar mais 1 revista."
        player_name "Acho que devo {b}procurar por aqui na escola.{/b}"
    else:
        show ross 10
        show player 2f
        player_name "{b}Biblioteca{/b}, entendeu!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
