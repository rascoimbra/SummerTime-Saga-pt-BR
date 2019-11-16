label angelica_dialogue_ross_get_linens_pre:
    scene church_c
    show player 1 at left
    show ang 1 at right
    with dissolve
    return

label angelica_dialogue_ross_get_linens:
    show player 2
    player_name "Estou fazendo um projeto de arte para a escola e precisamos de roupas de cama brancas.Minha amiga"
    player_name "Minha amiga {b}Mia{/b} disse que você pode estar disposto a poupar."
    show player 1
    show ang 2
    ang "Hmm, {b}Mia{/b} enviei a você?"
    ang "Ela é uma jovem tão devota."
    ang "Suponho que poderia lhe dar algumas de nossas velhas vestes batismais. Eles estão se desgastando de qualquer maneira..."
    show player 2
    show ang 1
    player_name "Isso deve funcionar muito bem! Muito obrigada."
    show player 1
    show ang 2
    ang "Se você quiser me agradecer, comece a aparecer para o serviço aos domingos."
    show player 11
    show ang 1
    player_name "..."
    show ang 2
    ang "Agora espere aqui enquanto eu vou buscá-los."
    hide ang
    with dissolve
    show player 10
    player_name "Bem, isso foi fácil."
    show player 11
    player_name "..."
    show player 10
    player_name "Eu tinha certeza que ela iria querer algo em troca..."
    show player 11
    pause
    show ang 40 at right with dissolve
    pause
    show ang 41
    ang "Aqui está."
    show ang 2
    show player 592
    with dissolve
    ang "Contar {b}Mia{/b} Espero vê-la cedo para o próximo serviço! Ela está muito atrasada devido a confissão."
    show player 593
    show ang 1
    player_name "Tudo bem, eu vou informá-la."
    show player 592
    ang "Hmm!"
    hide ang
    hide player
    show player 591 at Position (xpos=0.25, ypos=1.0)
    with dissolve
    player_name "... {b}Mia{/b} pode acabar enfrentando a conta nesse caso."
    player_name "É melhor eu pegar esses {b}Lençóis{/b} de volta a {b}Miss Ross{/b}."
    return

label angelica_dialogue_change_pre:
    scene church_c with fade
    show player 10 at left
    show ang 1 at right
    with dissolve
    player_name "Oi, {b}Sister Angelica{/b}."
    show player 5
    show ang 2
    ang "Você novamente."
    ang "O que você quer?"
    show ang 1
    return

label angelica_dialogue_change_talk:
    show player 10
    player_name "Eu só quero conversar"
    show player 5
    show ang 2
    ang "Quieto."
    show ang 1
    show player 24
    player_name "Oh..."
    show ang 2
    ang "Se você quer conversar, venha me visitar à noite nos meus aposentos..."
    show ang 1
    show player 25
    player_name "Está bem então. Desculpa."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_change_graveyard:
    show player 10
    player_name "Como você acessa o cemitério?"
    show player 5
    show ang 2
    ang "Está fora dos limites."
    ang "Embora, ele esteja trancado e as crianças ainda chatas continuem encontrando maneiras de {b}esgueirar-se através da cerca{/b}."
    show ang 1
    show player 12
    player_name "Mas meu pai está enterrado lá."
    show player 5
    ang "..."
    show ang 2
    ang "Tenho certeza que ele é."
    show ang 1
    show player 12
    player_name "Mas-"
    show player 16
    show ang 2
    ang "Começa. Você está desperdiçando o meu tempo."
    hide ang
    hide player
    show player 16
    with dissolve
    player_name "..."
    show player 12
    player_name "Talvez eu possa encontrar {b}um caminho através da cerca{/b} também."
    hide player with dissolve
    return

label angelica_dialogue_change_leave:
    show player 10
    player_name "Deixa pra lá. Eu tenho que ir."
    show player 5
    ang "..."
    show ang 2
    ang "Não perca meu tempo assim novamente."
    show ang 1
    show player 25
    player_name "Você está certo, me desculpe..."
    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_pre:
    scene church_c
    show ang 2 at right
    show player 1 at left
    with dissolve
    ang "Você é desta paróquia, jovem?"
    show ang 1
    show player 14
    player_name "Olá, eu estava"
    show ang 2
    show player 11
    ang "Você é desta paróquia, jovem?"
    show ang 1
    show player 14
    player_name "Uhh ... Na verdade não."
    show ang 2
    show player 11
    ang "Você acredita em Deus?"
    show ang 1
    show player 10
    player_name "Bem..."
    show ang 2
    show player 11
    ang "Eu sinto Muito."
    ang "Só posso ajudar aqueles que compartilham a fé de nosso senhor!"
    hide player
    hide ang
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
