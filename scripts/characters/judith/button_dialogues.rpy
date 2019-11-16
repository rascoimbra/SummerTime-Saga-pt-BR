label judith_dialogue_start:
    scene lefthall_c
    show player 1 at left
    show judith 5 at right
    with dissolve
    jud "Ei {b}[firstname]{/b}!"
    show player 2 at left
    show judith 4 at right
    player_name "Ei {b}Judith{/b}, como está indo?"
    show player 1 at left
    show judith 5 at right
    jud "Oh, eu estou ótima!"
    show judith 2 at right
    jud "Eu ... eu só queria te agradecer."
    show judith 4 at right
    show player 21 at left
    player_name "Oh. Por quê?"
    show judith 3 at right
    show player 13 at left
    jud "No {bVestiario dos meninos{/b}... Você me fez sentir ... segura."
    show judith 4 at right
    show player 11 at left
    player_name "Oh..."
    show judith 5 at right
     jud "E, você sabe ... você enfrentou Annie. Acho que isso foi muito corajoso."
    show judith 4 at right
    show player 29 at left
    player_name "Está tudo bem, {b}Judith{/b}. Eu estava apenas tentando fazer a coisa certa."
    player_name "Eu deveria me desculpar ... por mostrar minha ... você sabe ..."
    show judith 5 at right
    show player 11 at left
    jud "Oh, tudo bem! Eu gostei-"
    show judith 3 at right
    jud "Quero dizer ... eu não me importei."
    show judith 5 at right
   jud "Nós apenas ... nos conhecemos um pouco melhor!"
    show judith 4 at right
    show player 21 at left
    player_name "Haha. Sim. Suponho que sim ..."
    show judith 5 at right
    show player 1 at left
    jud "Eu tenho que ir! Vejo você na aula então!"
    show player 14 at left
    show judith 4 at right
    player_name "Até mais!"
    return

label judith_dialogue_left_hallway_intro:
    scene lefthall_c
    show judith 1 at right
    show player 14 at left
    with dissolve
    player_name "Ei, {b}Judith{/b}!"
    show player 13
    show judith 5
    jud "Oh, Ei, {b}[firstname]{/b}."
    jud "Como você está?"
    show judith 4
    show player 14
    player_name "Muito bom. E como vai você?"
    show player 13
    show judith 6
    jud "..."
    show judith 2
    jud "Tudo bem, eu acho."
    show judith 1
    return

label judith_dialogue_art_classroom_intro:
    scene art_classroom_c
    show judith 1 at right
    show player 14 at left
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    player_name "Apreciando arte, {b}Judith{/b}?"
    show player 13
    show judith 5
    jud "Sim!"
    jud "É um dos meus assuntos favoritos."
    show judith 4
    show player 14
    player_name "Sim, o meu também!"
    show player 13
    show judith 5
    jud "Gosto porque, por mais ruins que sejam meus desenhos, ainda é considerado arte!"
    show judith 4
    show player 17
    player_name "Heh, bom."
    show judith 1
    return

label judith_dialogue_bathroom_fun:
    show player 2
    player_name "Diga, você gostaria de entrar no {b}vestiario dass meninas{/b} por um tempo ... Você sabe?"
    show player 1
    show judith 5
    jud "... Você realmente quer ..."
    jud "... comigo?"
    show player 2
    show judith 4
    player_name "Quero dizer, sim!"
    player_name "Se estiver tudo bem?"
    show player 1
    show judith 5
    jud "Oh, definitivamente!"
    jud "Vamos lá!"
    return

label judith_dialogue_dictionary_return:
    show player 14
    player_name "Ei, {b}Judith{/b}! Aqui está seu livro de volta."
    show player 239_240 with dissolve
    pause
    show player 522 with dissolve
    player_name "Obrigado novamente!"
    show player 13
    show judith 43
    with dissolve
    jud "Oh, bom, eu estava começando a me preocupar ..."
    show judith 4 with dissolve
    show player 14
    player_name "Não precisa se preocupar. Está na melhor forma ... Veja."
    show player 13
    show judith 5
    jud "Obrigado por ter cuidado com isso, {b}[firstname]{/b}."
    jud "Não sei por que me preocupo tanto ..."
    show judith 4
    show player 14
    player_name "Obrigado por me emprestar!"
    show player 13
    show judith 5
    jud "Qualquer coisa para você-"
    show judith 3
    jud "Quero dizer ... a qualquer momento!"
    show judith 1
    show player 10
    player_name "Ok, bem, eu vou te ver por aí."
    show player 5
    show judith 3
    jud "Tchau, {b}[firstname]{/b}."
    return

label judith_dialogue_bissette_find_full_dictionary:
    show player 14
    player_name "Olá, {b}Judith{/b}! Tem um minuto?"
    show player 13
    show judith 5
    jud "Claro, {b}[firstname]{/b}."
    show judith 4
    show player 14
    player_name "Eu esperava poder emprestar seu dicionário de francês."
    player_name "Preciso fazer uma cópia rápida de algumas páginas e vou devolvê-la."
    show player 13
    show judith 3
    jud "Meu dicionário de francês?"
    show judith 5
    jud "Absolutamente! Contanto que você prometa ter cuidado com isso?"
    show judith 4
    show player 11
    player_name "(O que há com as mulheres e seus dicionários franceses?)"
    show player 10
    player_name "Sim, vou tomar muito cuidado e você nem notará que ele se foi."
    show player 13
    show judith 5
    jud "Ok, eu confio em você, {b}[firstname]{/b}."
    pause
    show judith 43 with dissolve
    jud "Aqui está ..."
    show judith 4
    show player 522
    with dissolve
    player_name "Obrigado {b}Judith{/b}! Eu te devo uma!"
    hide judith with dissolve
    show player 13
    player_name "(Tudo bem, agora vá ao {b}laboratório de informática{/b} e copie essas páginas ausentes.)"
    return

label judith_dialogue_dewitt_find_flute:
    show player 10
    player_name "Você ainda tem a flauta da escola?"
    player_name "Eu preciso disso para o show de talentos."
    show player 5
    show judith 2
    jud "Oh, umm..."
    show judith 1
    show player 10
    player_name "A folha de assinatura do instrumento tinha seu nome ao lado da flauta."
    show player 5
    show judith 2
    jud "*Suspiro*"
    show judith 3
    jud "Eu tenho. Está no meu armário."
    show judith 1
    show player 12
    player_name "Tenho a sensação de que há um \" mas \ "vindo?"
    show player 5
    show judith 3
    jud "MAS, eu meio que quebrei ..."
    show judith 1
    show player 1
    player_name "Você quebrou !?"
    player_name "Como isso aconteceu ?!"
    show player 5
    show judith 5
    jud "Heh, bem, eu acidentalmente meio que ..."
    show judith 6
    show player 11
    player_name "..."
    show judith 2
    jud "... sentei nele."
    show judith 1
    show player 10
    player_name "Você sentou nele?"
    show player 11
    show judith 3
    jud "... sim."
    show judith 5
    jud "O que é péssimo, porque eu estava gostando muito!"
    show judith 4
    show player 10
    player_name "Eu não sabia que você podia tocar flauta?"
    show player 5
    show judith 5
    jud "Oh, eu não posso jogar."
    show judith 4
    show player 12
    player_name "Bem, então eu não entendo como você estava gostando?"
    show player 5
    jud "..."
    show judith 5
    jud "Heh, deixa pra lá."
    show judith 2
    jud "Eu esperava que ninguém perguntasse sobre isso ..."
    show judith 1
    show player 10
    player_name "Talvez eu conserte!"
    show player 5
    show judith 4
    jud "..."
    show judith 5
    jud "Você pode tentar."
    show judith 4
    show player 12
    player_name "Ainda está no seu armário?"
    show player 5
    show judith 5
    jud "Sim."
    show judith 4
    show player 10
    player_name "Tudo bem, obrigado, {b}Judith{/b}."
    return

label judith_dialogue_talent_show_help:
    show player 10
    player_name "Eu queria saber se você gostaria de participar do próximo show de talentos?"
    show player 5
    show judith 3
    jud "Não, obrigada, {b}[firstname]{/b}. Eu realmente não sei tocar um instrumento."
    show judith 2
    jud "... E eu tenho vergonha de subir no palco na frente de toda a escola."
    show judith 1
    show player 10
    player_name "Bem, e se tocássemos juntos?"
    show player 5
    show judith 5
    jud "Você e eu?"
    show judith 4
    show player 14
    player_name "Claro, por que não?"
    show player 13
    show judith 6
    jud "Hmm..."
    show judith 2
    jud "Não, desculpe, {b}[firstname]{/b}."
    show judith 3
    jud "Por mais que eu goste de brincar com você; apenas o pensamento de estar no centro das atenções assim ..."
    show judith 8f at Position (xoffset=2) with dissolve
    show player 11
    jud "..."
    show judith 9f at Position (xoffset=-4) with dissolve
    jud "Com licença, preciso ir ao banheiro!"
    hide judith with dissolve
    show player 12
    player_name "Porra, pensei por um segundo que ela concordaria."
    show player 10
    player_name "Acho que é melhor eu continuar procurando ..."
    return

label judith_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Judith, você tem míopia ou astigmatismo?"
    show player 1
    show judith 2
    jud "Uhh, bem."
    show judith 3
    jud "Ambos ..."
    show player 2
    show judith 1
    player_name "Sério ?!"
    show player 1
    show judith 2
    jud "Sim. Eu sou cega sem meus óculos ..."
    show judith 3
    jud "Muito idiota. Eu sei ..."
    show player 2
    show judith 1
    player_name "Não, é ótimo!"
    show player 1
    show judith 3
    jud "É?"
    show player 29 with dissolve
    show judith 1
    player_name "Bem, quero dizer, não. É péssimo que você não possa ver sem eles."
    show player 2 with dissolve
    player_name "... Mas também é uma coisa boa, porque estou procurando um par de lentes Varifocal."
    show player 1
    show judith 5
    jud "Oh. Bem, você encontrou alguns."
    show player 2
    show judith 4
    player_name "Você não teria um conjunto sobressalente, teria?"
    show player 1
    show judith 5
    jud "Claro".
    show player 2
    show judith 4
    player_name "Incrível! poderia me dar?"
    show player 1
    show judith 2
    jud "Hmm, você quer que eu te dê meu conjunto de reposição?"
    show player 10
    show judith 1
    player_name "... Sim?"
    show player 11
    show judith 3
    jud "Que tal uma troca?"
    show player 2
    show judith 1
    player_name "Sim, tudo bem. O que você quer?"
    show player 1
    show judith 2
    jud "Umm, é meio embaraçoso ..."
    show judith 1
    player_name "..."
    show judith 2
    jud "Bem, veja bem, algumas das outras garotas estão me incomodando ..."
    show judith 3
    jud "... porque eu nunca tive namorado."
    show player 10
    show judith 1
    player_name "Isso é péssimo."
    show player 11
    show judith 2
    jud "Sim".
    jud "Eu estava pensando ..."
    show judith 3
    jud "... Bem, eu esperava que você fingisse ser meu namorado."
    show player 23
    show judith 1
    player_name "( !!! )" with hpunch
    show player 10
    player_name "Você quer que eu finja ser seu namorado?"
    show player 11
    show judith 3
    jud "Apenas o tempo suficiente para tirar algumas fotos!"
    show player 10
    show judith 1
    player_name "fotos?!"
    show player 11
    show judith 2
    jud "Sim".
    show judith 3
    jud "Você me encontra no parque, tiramos algumas fotos como se fossem namorado e namorada, e depois eu darei a você o meu conjunto de reposição."
    jud "Fechado?"
    show player 10
    show judith 1
    player_name "Eu uhh ..."
    show player 11
    show judith 3
    jud "Por favor? Seria uma ajuda enorme!"
    show player 2
    show judith 1
    player_name "Sim, tudo bem, acho que posso fazer isso."
    show player 1
    show judith 5
    jud "Você vai ?!"
    jud "Ok, encontre-me no parque! Estarei lá nas {b}tardes{/b}."
    show player 2
    show judith 4
    player_name "{b}O parque, à tarde.{/b} Entendi!"
    show player 1
    show judith 5
    jud "Ótimo! Vejo você lá!"
    return

label judith_dialogue_okita_take_picture_judith:
    show player 2
    player_name "Onde você quer tirar essa foto novamente?"
    show player 1
    show judith 3
    jud "Oh hum, no parque."
    show player 2
    show judith 1
    player_name "Tudo bem."
    show player 1
    show judith 3
    jud "Você não está tendo dúvidas, está?"
    show judith 2
    jud "Porque está tudo bem, não temos-"
    show player 2
    show judith 1
    player_name "Não, {b}Judith{/b}. Está tudo bem, sério!"
    show judith 4
    player_name "Encontro você lá!"
    show player 1
    show judith 5
    jud "... Obrigado, {b}[firstname]{/b}."
    return

label judith_dialogue_ross_ask_model:
    show player 2
    player_name "Estou trabalhando em um projeto para a {b}Miss Ross{/b} e isso requer um modelo ativo."
    player_name "Você estaria interessada?"
    show player 1
    show judith 5
    jud "Você quer que eu seja modelo para você?"
    show player 2
    show judith 4
    player_name "Sim, isso seria incrível!"
    show player 10
    player_name "É modelagem nua embora ..."
    show player 11
    show judith 3
    jud "... Oh."
    show judith 1
    jud "..."
    show judith 3
    jud "... Você realmente quer que eu faça?"
    show player 10
    show judith 1
    player_name "Claro!"
    show player 11
    show judith 5
    jud "Então eu farei isso! Para você, {b}[firstname]{/b}!"
    show player 2
    show judith 4
    player_name "Obrigado {b}Judith{/b}! Isso é realmente incrível da sua parte!"
    player_name "Apenas me encontre na sala de arte."
    show player 1
    show judith 5
    jud "Tudo bem."
    return

label judith_dialogue_left_hallway_leave:
    show player 5
    player_name "..."
    show judith 6
    jud "..."
    show player 29 with dissolve
    player_name "Bem ... é melhor eu ir em frente!"
    show player 3
    show judith 5
    jud "Até mais, {b}[firstname]{/b}."
    return

label judith_dialogue_art_classroom_leave:
    show player 14
    player_name "Até mais, {b}Judith{/b}."
    show player 13
    show judith 5
    jud "Tchau, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
