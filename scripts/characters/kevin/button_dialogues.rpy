label button_kevin_shift_cover_has_favor:
    show kevin 2
    kev "Você {b}já falou com Erik sobre me cobrir{/b}?"
    show kevin 1
    show player 17
    player_name "Eu falei".
    player_name "Ele vai fazer isso."
    show player 13
    show kevin 2b with dissolve
    kev "INFERNO!"
    kev "Sim!"
    kev "BRO!"
    show kevin 2c with dissolve
    kev "Você é o homem doido!"
    show kevin 6 with dissolve
    kev "Finalmente posso voltar aos meus dois por dia!"
    show kevin 5
    show player 14
    player_name "Heh, então acho que vou vê-lo na academia {b}de manhã{/b}?"
    show player 13
    show kevin 9b with dissolve
    kev "Você sabe, mano!"
    hide kevin
    hide player
    with dissolve
    return

label button_kevin_shift_cover_no_favor:
    show kevin 2
    kev "Você {b}já falou com Erik sobre me cobrir{/b}?"
    show kevin 1
    show player 29 with dissolve
    player_name "Não, ainda não."
    show player 3
    show kevin 2
    kev "Ugh, você tem que se apressar, mano!"
    show kevin 2b with dissolve
    kev "Meus músculos estão perdendo força aqui!"
    show kevin 1 with dissolve
    show player 14 with dissolve
    player_name "Heh, apenas relaxe."
    player_name "Eu vou falar com ele."
    show player 13
    return

label button_kevin_cafeteria_duty_repeat:
    show player 14
    player_name "Você está mais perto de sair daqui?"
    show player 13
    show kevin 2
    kev "Inferno não".
    kev "Eu vou ficar preso aqui o semestre inteiro, eu apenas sei disso!"
    show kevin 1
    return

label button_kevin_cafeteria_duty_first:
    show player 14
    player_name "Há quanto tempo você fica preso fazendo isso?"
    show player 13
    show kevin 2d with dissolve
    kev "{b}*Suspiro*{/b} Até eu conseguir minha nota de ciências, mano ..."
    kev "Honestamente, pode demorar todo o semestre."
    show kevin 2e
    show player 14
    player_name "Sério?"
    show player 13
    show kevin 2d
    kev "Sim".
    show kevin 2e
    show player 14
    player_name "Isso é péssimo para o homem."
    player_name "Eu preciso de você na academia para me encontrar."
    show player 13
    show kevin 2 with dissolve
    kev "Ah, não me deixe deprimido ..."
    kev "Você sabe que eu quero estar lá ajudando meu irmão a ser rasgado!"
    show kevin 1
    pause
    show kevin 4
    kev "Tsk, você sabe o que ..."
    show kevin 2
    kev "Será que eu poderia sair daqui?"
    show kevin 1
    show player 5
    player_name "Hmm?"
    show kevin 2
    kev "Quero dizer, se pudéssemos {b}encontrar alguém para me cobrir{/b}..."
    kev "... Como de manhã."
    kev "Poderia funcionar totalmente, mano!"
    show kevin 1
    show player 10
    player_name "Como assim?"
    show player 5
    show kevin 2
    kev "Bem, {b}Mrs. Smith{/b} nunca vem aqui de manhã."
    kev "Desde que o trabalho seja feito, não importa realmente quem o está fazendo."
    show kevin 1
    show player 14
    player_name "Então, precisamos apenas {b}encontrar alguém para cobrir você{/b}?"
    show player 13
    show kevin 2
    kev "Sim, você tem alguma idéia?"
    show kevin 1
    show player 4
    pause
    show player 14
    player_name "Hmm, talvez eu consiga convencer {b}Erik{/b} a fazer isso."
    show player 13
    show kevin 2
    kev "Oh, isso seria demais, mano!"
    show kevin 1
    show player 14
    player_name "Vou {b}perguntar a ele{/b} sobre isso."
    show player 13
    show kevin 2
    kev "Inferno, sim!"
    show kevin 1
    return

label button_kevin_intro_pre_favor:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 2 at right
    with dissolve
    kev "mano?!"
    show kevin 1
    show player 14
    player_name "Ei {b}Kevin{/b}."
    show player 13
    show kevin 2
    kev "Você está aqui para esfregar alguns potes?"
    show kevin 1
    show player 17
    player_name "Heh, de jeito nenhum cara!"
    show player 13
    show kevin 2
    kev "Ugh, esse serviço de cafeteria é péssimo, mano!"
    show kevin 1
    pause
    show kevin 2
    kev "... E não do tipo legal, também."
    show kevin 1
    show player 29 with dissolve
    player_name "Eh, certo ..."
    show player 5 with dissolve
    return

label button_kevin_used_panties_repeat:
    show player 10
    player_name "Não acredito que esse cara me roubou uma {b}calcinha usada{/b}..."
    show player 5
    show kevin magic 2
    kev "Não é grande coisa, mano!"
    kev "Basta deslizar um par de casa."
    show kevin magic 1
    show player 37 with dissolve
    player_name "Yeah, yeah."
    player_name "Vou {b}verificar a minha casa{/b} e ver se consigo encontrar um par de {b}[deb_name]'s{/b} ou {b}[jen_name]'s{/b}."
    show player 13 with dissolve
    return

label button_kevin_used_panties_first:
    show player 10 at left
    show kevin magic 1 at right
    player_name "Então eu conheci o novo treinador de {b}Muay Thai{/b} sobre o qual você estava falando."
    show player 5
    show kevin magic 2
    kev "Certo, mano!"
    kev "Ele é bem legal, né ?!"
    show kevin magic 1
    show player 12
    player_name "Ele é um total louco!"
    show player 5
    show kevin magic 2
    kev "Huh?"
    show kevin magic 1
    show player 12
    player_name "Sim, ele disse que não vai me ensinar, a menos que eu traga uma {b}calcinha usada{/b}!"
    show player 5
    show kevin magic 2
    kev "Oh, isso ..."
    show kevin magic 3 with dissolve
    kev "Umm."
    show kevin magic 4
    show player 10
    player_name "Espere um segundo ..."
    show player 14
    player_name "Você trouxe um par para ele, não foi ?!"
    show player 13
    show kevin magic 3
    kev "Eh, sim."
    show kevin magic 4
    show player 14
    player_name "Cara, sério?"
    show player 13
    show kevin magic 2 with dissolve
    kev "Bem, eu ouvi todas essas coisas incríveis sobre ele e fiquei curioso ..."
    kev "Depois que você passa pela coisa da calcinha, ele é totalmente legítimo!"
    show kevin magic 1
    show player 11
    player_name "..."
    show kevin magic 2
    kev "Estou falando sério!"
    kev "Ele realmente conhece suas coisas, mano."
    show kevin magic 1
    show player 14
    player_name "Onde você conseguiu um par de {b}calcinha usada{/b}?"
    show player 13
    show kevin magic 3 with dissolve
    kev "Ah, eh ... eu meio que ... Arranquei um par de {b}minha mãe{/b}, do cesto de roupas sujas."
    show kevin magic 4
    show player 12
    player_name "Cara ..."
    show player 5
    show kevin magic 2 with dissolve
    kev "O que ?!"
    kev "Não é tão estranho assim."
    kev "Acabei de pegar um par e não é como se estivesse pegando para mim."
    kev "Eu os entreguei ao {b}Master Somrak{/b}."
    show kevin magic 1
    show player 14
    player_name "É muito estranho {b}Kevin{/b}."
    show player 13
    show kevin magic 2
    kev "Nah, mano."
    kev "Você está ficando preso em coisas triviais ..."
    kev "Você tem duas garotas em sua casa, não é?"
    show kevin magic 1
    show player 10
    player_name "Sim, mas-"
    show player 11
    show kevin magic 2
    kev "Bem, aí está! Apenas pegue um par e você estará dentro!"
    kev "Realmente não é grande coisa, mano."
    show kevin magic 1
    show player 35
    player_name "Hmm, eu não sei ..."
    show player 34
    show kevin magic 2
     kev "Apenas faça, {b}[firstname]{/b}."
    kev "Os ensinamentos do{b}Master Somrak's{/b} mudarão sua vida, estou lhe dizendo!"
    show kevin magic 1
    show player 33
    player_name "Acho que eu poderia pegar um par ..."
    show player 13
    show kevin magic 2
    kev "Veja, lá vai você!"
    show kevin magic 1
    show player 14
    player_name "Eu vou {b}verificar a minha casa{/b} e ver se consigo encontrar um par de {b}[deb_name]'s{/b} ou {b}[jen_name]'s{/b} calcinha."
    show player 13
    return

label kevin_dialogue_ross_find_magazines:
    show player 2 at left
    show kevin 29b at right
    with dissolve
    player_name "Ei, {b}Kevin{/b}!"
    show player 1
    show kevin 30
    kev "O que há, {b}[firstname]{/b}?"
    show player 2
    show kevin 29b
    player_name "Não muito. O que você está lendo?"
    show player 1
    show kevin 30b
    kev "Oh, apenas algumas revistas de exercícios que recebi da academia."
    show player 2
    show kevin 29b
    player_name "Legal, você está tentando fazer um novo exercício ou algo assim?"
    show player 1
    show kevin 30
    kev "Não, por quê?"
    show player 11
    show kevin 29
    player_name "..."
    show kevin 31 with dissolve
    kev "Venha conferir este bolo, {b}[firstname]{/b}!"
    show player 10
    show kevin 31b
    player_name "... bolo de carne?"
    show player 11
    player_name "..."
    show player 10
    player_name "Uh, certo ... Você acha que eu poderia pegar algumas dessas revistas?"
    show player 11
    show kevin 30 with dissolve
    kev "Heh, eu não sabia que você era um conhecedor da forma masculina ..."
    show player 10
    show kevin 29
    player_name "Na verdade, estou fazendo uma colagem."
    show player 11
    show kevin 30b
    kev "Oh, certo. Colagem."
    show kevin 31 with dissolve
    kev "Eu peguei você, irmão! Não diga mais nada!"
    kev "Pegue tudo que você precisa! Este aqui vai me manter ocupado por um tempo."
    show player 2
    show kevin 31b
    player_name "Incrível! Obrigado, irmão ..."
    show player 1
    show kevin 31c
    kev "Daaaamn, ele está brilhando ..."
    show player 10
    player_name "..."
    return

label kevin_dialogue_ross_ask_model:
    show player 2 at left
    show kevin 1 at right
    player_name "Estou trabalhando em um projeto para a {b}Miss Ross{/b} e isso requer um modelo ativo."
    player_name "Você estaria interessado?"
    show kevin 2
    show player 1
    kev "Modelagem. Como se eu apenas tivesse que ficar lá?"
    show player 2
    show kevin 1
    player_name "Sim, você só precisa ficar lá."
    show player 10
    player_name "Nu".
    show kevin 3
    show player 11
    kev "Nu !?"
    kev "Oh, cara. Eu não sei, irmão."
    kev "Será só você desenhando?"
    show player 10
    show kevin 1
     player_name "Bem, {b}Mia{/b} e eu estaremos desenhando."
    player_name "{b}Miss Ross{/b} também estará lá."
    show player 11
    show kevin 4
    kev "Ugh, passei ..."
    show kevin 3
    kev "Não quero que as garotas me vejam nu, irmão. Isso é meio nojento."
    show kevin 1
    player_name "..."
    show player 10
    player_name "Tudo bem."
    return

label kevin_dialogue_intro:
    show kevin 23 at right
    show player 14 at left
    with dissolve
    player_name "Ei, {b}Kevin{/b}!"
    show player 13
    show kevin 9b
    kev "Olá, {b}[firstname]{/b}."
    show kevin 23
    show player 14
    player_name "O que houve?"
    show player 13
    show kevin 9b
    kev "Não muito. Ontem foi dia de glúteos para mim."
    kev "Minha bunda está dolorida!"
    kev "Sinta como está apertado!"
    show kevin 23
    show player 10
    player_name "Uhhh ... Não, obrigado cara."
    show player 13
    show kevin 9b
    kev "Sua perda!"
    return

label kevin_dialogue_erik_favor_2_completed:
    kev "É melhor te ver na academia hoje mais tarde!"
    show kevin 23
    show player 14
    player_name "Talvez ..."
    show player 13
    show kevin 9b
    return

label kevin_dialogue_dewitt_kevin_give_guitar:
    show player 14
    player_name "Encontrei um violão para você!"
    show player 13
    show kevin 24
    kev "Sério?"
    show kevin 23
    show player 239_240 with dissolve
    pause
    show player 577 with dissolve
    player_name "O que você acha?"
    show player 13 with dissolve
    show kevin 16f with dissolve
    kev "Puta merda! Onde você conseguiu essa coisa?"
    kev "Essa coisa é realmente de ponta!"
    show kevin 14f
    show player 10
    player_name "É?"
    show player 5
    show kevin 15f
    kev "Uhh, sim, mano!"
    kev "Espero que você não tenha roubado ou algo assim."
    show kevin 14f
    show player 14
    player_name "Foi emprestado de verdade por um amigo meu. Portanto, tenha cuidado com isso, sim?"
    hide player
    show kevin 27 at left
    with dissolve
    kev "Não há problemas!"
    kev "Vou tratar essa beleza com o respeito que ela merece!"
    show kevin 28
    player_name "Legal, então você vai jogar no show de talentos."
    show kevin 27
    kev "Estou triste!"
    show kevin 28
    player_name "Incrível! Vejo você na aula da {b}Ms. Dewitt's{/b} em breve para o treino!"
    show kevin 27
    kev "Parece bom, mano!"
    show player 13 at left
    show kevin 16 at right
    with dissolve
    kev "Eu vou te ligar... Devin"
    ev "Você gostaria que bonito?"
    show player 11
    hide kevin with dissolve
    player_name "..."
    return

label kevin_dialogue_talent_show_help:
    show player 10
    player_name "Estou ajudando a {b}Ms. Dewitt{/b} a encontrar voluntários para o show de talentos."
    player_name "Você não tocava violão?"
    show player 5
    show kevin magic 2
    kev "Sim, eu costumava."
    show kevin magic 1
    show player 10
    player_name "O que aconteceu?"
    show player 5
    show kevin magic 2
    kev "Ah, meu ex meio que quebrou depois que eu terminei com ele."
    show kevin magic 1
    show player 12
    player_name "Ele?"
    show player 11
    show kevin magic 3 with dissolve
    kev "Eu disse a ele? Desculpe, eu quis dizer ela."
    kev "... Sim, ela quebrou em pedaços."
    show kevin magic 1 with dissolve
    show player 14
    player_name "Hein, você gosta de garotas malucas, não é?"
    show player 13
    show kevin magic 3 with dissolve
    kev "Heh, você sabe disso! Garotas loucas, estou apaixonada por elas! Totalmente ..."
    show kevin magic 1 with dissolve
    show player 14
    player_name "Então, se você tivesse um violão, tocaria no show de talentos?"
    show player 13
    show kevin magic 2
    kev "Sim, eu não me importaria."
    kev "Onde eu vou conseguir um violão? Eles são super caros!"
    show kevin magic 1
    show player 35
    player_name "Hmm, talvez eu encontre um para você ..."
    show player 34
    player_name "( {b}Erik{/b} em um monte no porão. Talvez eu possa pegar um emprestado?)"
    show player 14
    player_name "Já Volto!"
    show player 13
    show kevin magic 2
    kev "Tudo bem."
    return

label kevin_dialogue_talent_show_replace_guitar:
    show player 14
    player_name "Então, se você tivesse um violão, tocaria no show de talentos?"
    show player 13
    show kevin magic 2
    kev "Sim, eu não me importaria."
    kev "Onde eu vou conseguir um violão? Eles são super caros!"
    show kevin magic 1
    show player 34
    player_name "( preciso trocar meu violão personalizada por uma no {b}Erik's{/b} basement! )"
    show player 14
    player_name "Já Volto!"
    show player 13
    show kevin magic 2
    kev "Tudo bem."
    return

label kevin_dialogue_talent_show:
    show player 14
    player_name "Então, se você tivesse um violão, tocaria no show de talentos?"
    show player 13
    show kevin magic 2
    kev "Sim, eu não me importaria."
    kev "Onde eu vou conseguir um violão? Eles são super caros!"
    show kevin magic 1
    show player 35
    player_name "Hmm, talvez eu encontre um para você ..."
    show player 34
    player_name "( {b}Erik{/b} tem um monte no porão. Talvez eu possa pegar um emprestado?)"
    show player 14
    player_name "Já Volto!"
    show player 13
    show kevin magic 2
    kev "Tudo bem."
    return

label kevin_dialogue_dewitt_science_adhesive:
    show player 10
    player_name "O que precisamos para esse {b}adesivo{/b} novamente?"
    show player 13
    show kevin 2
    kev "Encontre-me no {b}laboratório de ciências depois da aula{/b}."
   kev "Eu vou cuidar do resto."
    show kevin 1
    show player 14
    player_name "Incrível! Obrigado, {b}Kevin{/b}!"
    return

label kevin_dialogue_leave:
    show player 14
    player_name "De qualquer forma, tenho que ir."
    player_name "Mantenha seu ânimo, cara."
    show player 13
    show kevin 2
    kev "Sim, tudo bem mano."
    kev "Vejo você por aí."
    hide kevin
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
