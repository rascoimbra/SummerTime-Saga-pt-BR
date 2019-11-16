label button_lucy_how_are_the_little_ones:
    show player f_normal_talk
    player_name "Como estão os pequenos?"
    show player f_normal
    show lucy f_normal_talk
     lucy "Aww, é muito gentil da sua parte vir conferir eles!"
    lucy "Todo mundo está indo maravilhoso !!"
    lucy "De fato, estávamos prestes a nos sentar para contar histórias."
    lucy "Gostaria de se juntar a nós?"
    show lucy f_normal_talk
    show player f_normal_talk
    player_name "Oh, ehh ... N-não, obrigado."
    player_name "Eu provavelmente entraria atrapalhando...!"
    show player f_normal
    show lucy f_normal_talk
    lucy "Oh, bobagem!"
    show lucy f_normal
    return

label button_lucy_baby_dialogue:
    show player 14 at left
    show lucy
    player_name "Como está o meu pequeno?"
    show player 13
    show lucy f_laugh
    lucy "Oh, tudo bem!"
    show lucy f_normal_talk
    lucy "Todo mundo está se divertindo!"
    lucy "O pequeno {b}Jack{/b} está perseguindo todas as garotas hoje."
    lucy "Essa é uma criança que teremos que ficar de olho à medida que envelhece."
    show lucy f_normal
    show player 14
    player_name "Crianças bobas".
    player_name "Bem, todos parecem estar se divertindo!"
    show player 13
    show lucy f_laugh
    lucy "Oh, sim! Isso é tudo o que fazemos todos os dias é nos divertir, divertir, divertir!"
    show lucy f_normal
    show player 14
    player_name "Bom. Bem, eu apenas pensei em dar uma passada e ver que todo mundo estava."
    show player 13
    show lucy f_normal_talk
    lucy "Awwww."
    lucy "Devo dizer, é tão refrescante ver um pai parar e checar seu pequeno."
    show lucy f_normal
    return

label button_lucy_baby_dialogue_multiple:
    show player 14 at left
    show lucy
    player_name "Como estão meus filhos pequenos?"
    show player 13
    show lucy f_laugh
    lucy "Oh, tudo bem!"
    show lucy f_normal_talk
    lucy "Todo mundo está se divertindo!"
    if randomizer() > 50:
        lucy "Fique de olho em {b}Jacob{/b}."
        lucy "Ele encontrou alguns adesivos e os colocou em todos os lugares."
    elif randomizer() > 50:
        lucy "O pequeno {b}Jack{/b} está perseguindo todas as garotas hoje."
        lucy "Essa é uma criança que teremos que ficar de olho à medida que envelhece."
    else:
        lucy "Caso contrário, as crianças estão se comportado muito bem."
        lucy "Eu gostaria que todos os dias fossem assim."os
    show lucy f_normal
    show player 14
    player_name "Crianças bobas".
    player_name "Bem, todos parecem estar se divertindo!"
    show player 13
    show lucy f_laugh
    lucy "Oh, sim! Isso é tudo o que fazemos todos os dias é nos divertir, divertir, divertir!"
    show lucy f_normal
    show player 14
    player_name "Bom. Bem, eu apenas pensei em dar uma passada e ver que todo mundo estava."
    show player 13
    show lucy f_normal_talk
    lucy "Awwww."
    lucy "Devo dizer, é tão refrescante ver um pai parar e checar seus pequenos."
    show lucy f_normal
    return

label lucy_button_intro_day:
    show player 13 at left
    show lucy f_normal_talk
    with dissolve
    lucy "Olá, {b}[firstname]{/b}."
    lucy "O que traz você hoje?"
    show lucy f_normal
    show player 14
    player_name "Oh, eu estava no bairro e pensei em dizer olá."
    show player 13
    show lucy f_normal_talk
    lucy "Bem, isso é legal."
    show lucy f_normal
    return

label lucy_button_intro_night:
    show player 13 at left
    show lucy f_sad_talk b_messy a_dressed_cover
    with dissolve
    lucy "Oh, Deus."
    show lucy f_normal_talk a_dressed_sides with dissolve
    lucy "Eu não sabia que você estava passando, {b}[firstname]{/b}."
    show lucy f_normal_talk_down
    lucy "Eu imagino que pareço uma bagunça ..."
    show lucy f_normal
    show player 14
    player_name "Não, de jeito nenhum."
    player_name "Você está sempre bonita, {b}Lucy{/b}."
    show player 13
    show lucy f_normal_talk
    lucy "Bem, é legal da sua parte dizer isso."
    show lucy f_normal
    return

label button_lucy_how_are_you:
    show player 14 at left
    show lucy f_normal
    player_name "Você está bem?"
    show player 13
    lucy "Hmm?"
    show lucy f_normal_talk
    lucy "Oh, eu estou bem."
    show lucy f_laugh
    lucy "Essas crianças apenas iluminam meu dia."
    show lucy f_normal
    show player 12
    player_name "{b}Richard{/b}ta te tratando você bem?"
    show player 5
    show lucy f_normal_talk
    lucy "Ah, você conhece o {b}Richard{/b}."
    lucy "Ele está no seu caminho."
    show lucy f_normal
    show player 12
    player_name "Bem, deixe-me saber se você precisar de alguma ajuda, ok?"
    show player 5
    show lucy f_normal_talk
    lucy "Você é tão doce."
    lucy "Obrigado, {b}[firstname]{/b}."
    show lucy f_normal
    return

label button_lucy_hows_the_milk:
    show player 14 at left
    show lucy f_normal
    player_name "Satisfeita com seu último carregamento de leite?"
    show player 13
    show lucy f_laugh
    lucy "Ah, sim."
    show lucy f_normal_talk
    lucy "Os pequenos simplesmente não conseguem o suficiente."
    show lucy f_normal
    show player 10
    player_name "Você gosta mesmo de cuidar de todas essas crianças?"
    show player 5
    show lucy f_laugh
    lucy "Eu amo isso!"
    show lucy f_normal_talk
    lucy "Isso me mantém jovem, sabia?"
    show lucy f_normal
    show player 14
    player_name "Bem, você certamente parece jovem."
    show player 13
    show lucy f_smirk_talk
    lucy "Aww, você é um encantador, {b}[firstname]{/b}!"
    show lucy f_smirk
    return

label button_lucy_annie_around_day:
    show player 10 at left
    show lucy f_normal
    player_name "{b}Annie{/b} está por aí?"
    show player 5
    show lucy f_normal_talk
    lucy "Não, acho que ela está na escola, querido."
    lucy "Você quer que eu diga a ela que você parou aqui?"
    show lucy f_normal
    show player 10
    player_name "N-não, tudo bem."
    player_name "Eu só estava curioso."
    show player 5
    return

label button_lucy_annie_around_night:
    show player 10 at left
    show lucy f_normal
    player_name "Annie está por aí?"
    show player 5
    show lucy f_normal_talk
    lucy "Acho que ela mencionou que tinha algum dever de casa a fazer."
    lucy "Você a conhece, ela é muito particular em relação ao trabalho na escola."
    show lucy f_normal
    show player 10
    player_name "Ah, eu sei."
    show player 14
    player_name "Obrigado, {b}Lucy{/b}."
    show player 13
    lucy "Mmhmmm."
    return

label button_lucy_leave:
    show player 14 at left
    show lucy f_normal
    player_name "Eu devo ir."
    show player 13
    show lucy f_normal_talk
    lucy "Tudo bem, querido."
    show lucy f_normal
    show player 14
    player_name "Foi um prazer vê-la novamente."
    show player 13
    show lucy f_normal_talk
    lucy "Você também, querido."
    hide player
    hide lucy
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
