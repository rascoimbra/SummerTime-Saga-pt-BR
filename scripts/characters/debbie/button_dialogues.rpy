label debbie_dialogue_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show player f_normal
    show debbie f_normal_talk
    deb "Então, o que ela disse?"
    show debbie f_normal
    show player f_worried
    player_name "Hmm?"
    show player f_worried_talk
    player_name "Oh, eu ainda não perguntei a ela ..."
    show player f_normal
    show debbie f_normal_talk
    deb "Heh, o que você está esperando, bobo?"
    show debbie f_normal
    show player f_normal_talk
    player_name "Eu vou agora."
    show player f_normal
    show debbie f_normal_talk
    deb "Obrigado querido."
    show debbie f_normal
    show player f_normal_talk
    player_name "Sem problema."
    hide debbie
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Hmm, acho que {b} [jen_name] {/b} está {b} descansando à beira da piscina ...{/b} )"
    hide player with dissolve
    return

label debbie_dialogue_mom_relaxing:
    scene expression player.location.background_closeup
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Olá docinho! Você não deveria ir?"
    show player 2 at left
    show debbie 1 at right
    player_name "Sim. Eu estava no meu caminho."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_not_revealing_kitchen:
    scene expression player.location.background_closeup with None
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 48 at Position(xpos=660,ypos=768) with dissolve
    deb "( !!! )"
    show debbie 48c
    deb "Querido, o que você está fazendo aí atrás?"
    show debbie 50j
    player_name "Nnnnn naaaaaada..."
    show debbie 50k
    deb "Querido!"
    deb "E se  {b}[jen_name]{/b} aparecer?"
    deb "Ela teria uma vaca!"
    show debbie 50j
    player_name "Heh, não se preocupe, ela está no quarto dela."
    player_name "... E além do mais..."
    player_name "... Isso vai ser rapidinho."
    show debbie 50k
    deb "Você é tão mau..."
    deb "Ahh!"
    deb "... Tudo bem! Seja rápido!"
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 48c with dissolve
    deb "Está bem, está bem! Temos que parar!"
    show debbie 50k
    deb "Mais e eu vou ter que mudar minha calcinha!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Em que mais posso ajudá-lo?"
    show debbie 1
    return

label debbie_dialogue_mom_fetch_lotion:
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Você encontrou minha {b}loção{/b} no {b}armário do meu quarto{/b}?"
    show debbie 1
    show player 10
    player_name "Não, ainda não."
    show player 5
    show debbie 2
    deb "Bem, o que você está esperando?"
    return

label debbie_dialogue_mom_car_condition:
    show player 10 at left
    show debbie 61 at right
    with dissolve
    player_name "Eu descobri por que o carro não liga ..."
    show player 5
    show debbie 63
    deb "Oh ?! Você já consertou?"
    show debbie 61
    pause
    show player 25
    player_name "Está muito ruim, {b}[deb_name]{/b}... Eu não acho que posso consertar."
    show player 5
    show debbie 39
    deb "Oh."
    show debbie 38
    show player 10
    player_name "Na verdade, acho que teremos que substituir todo o motor. Está realmente muito ruim!"
    player_name "Vai ser caro ..."
    show player 5
    pause
    show debbie 60
    deb "E o seguro? Devemos ir e ver o que a {b}loja de carros{/b} pode fazer por nós."
    deb "Espero que eles cubram os reparos, caso contrário ..."
    show debbie 39
    deb "...Podemos ficar sem carro por um tempo."
    show debbie 38
    pause
    show player 10
    player_name "Tenho certeza que vai ficar tudo bem, {b}[deb_name]{/b}. Vou conversar com a {b} concessionária {/b}."
    show player 5
    pause
    show player 14
    player_name "Vou consertar."
    player_name "De uma forma ou de outra."
    show debbie 61
    show player 13
    pause
    show debbie 62
    deb "Estou tão feliz por ter você por perto, querido!"
    deb "Obrigado!"
    return

label debbie_dialogue_mom_revealing_kitchen_pre:
    scene expression player.location.background_blur
    show debbieobj 2 at Position(xpos=590,ypos=768)
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_pre:
    scene expression player.location.background_closeup with None
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 48 at Position(xpos=660,ypos=768) with dissolve
    deb "( !!! )"
    show debbie 48c
    deb "Querido?"
    deb "O que você está fazendo aí atrás?"
    show debbie 50j
    player_name "Nnnnn Naaada..."
    show debbie 50k
    deb "Ahh..."
    deb "E se  {b}[jen_name]{/b} aparecer por aqui?"
    deb "Ela seria uma vaca!"
    show debbie 50j
    player_name "Heh, não se preocupe. Ela está no quarto dela."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    pause
    show debbie 50j with dissolve
    player_name "Isso é bom?"
    show debbie 50k
    deb "Claro que sim..."
    deb "Mmm, você está me deixando tão molhada!"
    deb "Ahh!"
    show debbie 50j
    player_name "E se eu puxasse essa calcinha e te comesse aqui agora?"
    show debbie 50k
    deb "Oh Deus..."
    deb "Ok, faça! Mas seja rápido, querido!"
    show debbie 50j
    player_name "Mmm, é melhor você segurar firme naquele armário!"
    show debbie 50c with dissolve
    pause
    show debbie 50d with dissolve
    pause
    hide debbie
    show debbie 50e at right
    with dissolve
    pause
    show debbie 50g with dissolve
    deb "Que tesão!."
    hide debbie
    show debbies 164 at right
    with dissolve
    deb "Ahhh!"
    player_name "Uau, você está pingando ..."
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_after:
    show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies at right with dissolve
    deb "Vai, fode com vontade!"
    return

label mom_kitchen_fuck_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [164,165,166,167,168]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
        $ animcounter += 1
    call screen mom_kitchen_fuck_options

label debbie_kitchen_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            deb "Oh!!!{p=1}{nw}"
        else:
            deb "AHHH!!!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            deb "Você já gozou?{p=2}{nw}"
            player_name "Ainda não...{p=2}{nw}"
            deb "Depressa, gostoso ... Acho que não posso aguentar ... mais tempo!{p=3}{nw}"
    return

label mom_kitchen_fuck_cum:
    call expression game.dialog_select("mom_kitchen_fuck_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["09_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label mom_kitchen_fuck_cum_dialogue:
    player_name "( !!! )"
    player_name "Oh, {b}[deb_name]{/b}!"
    player_name "Eu estou-"
    deb "Shhhh!"
    show debbies 169 with flash
    player_name "UHH!!!"
    hide debbies
    show debbie 50h at right
    with dissolve
    pause
    deb "Ah, eu adoro quando você se encarrega!"
    player_name "Você gozou?"
    deb "Oh sim!"
    show debbie 50i at right
    show player 434 at left
    with dissolve
    deb "{b} * Ufa * {/b}, minhas pernas ainda estão tremendo ..."
    deb "... Uau, você gozou muito!"
    pause
    show debbie 61 with dissolve
    show player 10
    player_name "Desculpe."
    show player 13
    show debbie 62
    deb "Não, eu amo isso! É gostoso tudo isso dentro de mim."
    show debbie 61
    show player 14
    player_name "Heh, eu adoro quando você diz coisas assim"
    show player 13
    show debbie 62
    deb "Hehe, bem, é a verdade ..."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_revealing_feel_ass_no_sex:
    scene expression player.location.background_closeup with None
    hide debbieobj
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 50k at Position(xpos=660,ypos=768) with dissolve
    deb "Well hello to you to, sweetie..."
    show debbie 50j
    player_name "Hey, {b}[deb_name]{/b}..."
    show debbie 50k
    deb "Just be careful..."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 50k with dissolve
    deb "Okay, okay! We have to stop!"
    deb "Anymore and I'll have to go change my panties!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "What else can I help you with?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing_talk:
    scene expression player.location.background_closeup with None
    hide debbieobj
    show debbie 1 at right
    show player 2 at left
    with dissolve
    player_name "Hey {b}[deb_name]{/b}, got a minute?"
    show debbie 2
    show player 1
    deb "Need something, {b}[firstname]{/b}?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if randomizer() <= 10:
        deb "There's my big man..."
    elif randomizer() <= 20:
        deb "Hey there, sweetie."
        deb "What can I do for you?"
    elif randomizer() <= 30:
        deb "Awww..."
        deb "No hello squeeze?"
    elif randomizer() <= 70:
        deb "Procurando por mim, espero."
    elif randomizer() <= 80:
        deb "Precisa de algo?"
        deb "Ou posso fazer algo por você?"
    elif L_home_shower.is_here(M_jenny):
        deb "{b}[jen_name]{/b} está no chuveiro."
        deb "Caso você precise de mim por um segundo rápido."
    else:
        deb "Eu esperava ver você hoje."
    show debbie 1
    show player 14
    if randomizer() <= 50:
        player_name "Oi, {b}[deb_name]{/b}."
    else:
        player_name "Você está bem hoje."
    show player 13
    return

label debbie_dialogue_mom_not_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Olá meu bem!"
    deb "Está tudo bem na escola?"
    show player 14 at left
    show debbie 1 at right
    player_name "Sim..."
    show player 13 at left
    show debbie 13 at right
    deb "Espero que você não tenha ficado muito atrasado depois de tudo que aconteceu..."
    show debbie 14 at right
    show player 14 at left
    player_name "Não, eu vou me recuperar."
    show player 13 at left
    show debbie 13 at right
    deb "Deixe-me saber se há algo que eu possa fazer para ajudar?"
    show player 21 at left
    show debbie 14 at right
    player_name "OK, {b}[deb_name]{/b}..."
    player_name "Eu tenho que ir."
    show player 13 at left
    show debbie 3 at right
    deb "Não fique de fora até tarde!"
    show debbie 1
    return

label debbie_dialogue_ask_about_dad:
    show player 10 at left
    show debbie 1 at right
    player_name "{b}[deb_name]{/b}, você sabe o que aconteceu com o meu {b}Dad{/b}?"
    show player 11
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Oh... Querido, eu..."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Por favor, eu quero saber a verdade!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Sinto muito, querido. Não tenho respostas para você."
    deb "A investigação policial não resultou em nada..."
    deb "De fato, entendo que o caso está em espera devido à falta de evidências."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Sim, mas eles vão encontrar algo, certo? Quero dizer, é o trabalho deles!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Só podemos esperar."
    show debbie 59 at Position (xoffset=-28)
    pause
    show debbie 60 at Position (xoffset=-28)
    deb "Querido...
    deb "Eu quero fechar essa coisa toda também..."
    deb "... Mas o seu {b} Father {/ b} não gostaria que ficássemos obcecados com isso."
    show debbie 63 at Position (xoffset=-28)
    deb "Você é jovem e precisa se concentrar em viver sua vida"
    deb "Faça isso pelo seu {b}Dad{/b}."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Sim. Vou tentar."
    show player 14
    show debbie 61 at Position (xoffset=-28)
    player_name "Obrigado, {b}[deb_name]{/b}."
    show player 1
    show debbie 2 with dissolve
    deb "Qualquer outra coisa que você precisa?"
    show debbie 1
    show player 1
    return

label debbie_dialogue_ask_about_money_problems:
    show debbie 1
    show player 10
    player_name "{b}[deb_name]{/b}, sobre o que você disse no telefone..."
    show debbie 13
    show player 11
    deb "Eu disse para você não se preocupar com isso."
    deb "Tudo ficará bem!"
    show debbie 14
    show player 14
    player_name "Ok, mas e se eu quisesse ajudá-lo?"
    player_name "E se eu conseguisse um emprego real?"
    show player 10
    player_name "Eu me sinto um pouco responsável por todo esse estresse..."
    show debbie 52 at Position (xoffset=1)
    show player 11
    deb "Você pode me ajudar ficando na escola!"
    deb "Seu {b}Father{/b} rolaria em seu túmulo se eu deixasse você conseguir um emprego em tempo integral..."
    deb "Ele queria que você terminasse sua educação."
    show debbie 51 at Position (xoffset=1)
    show player 10
    player_name "... Mas eu posso trabalhar depois da escola e nos fins de semana?"
    show debbie 53 at Position (xoffset=-18) with dissolve
    show player 13
    deb "{b}*Suspiro * {/ b} Você é tão teimoso, assim como seu {b}Pai{/b}..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    deb "Hmm..."
    show debbie 63 at Position (xoffset=-28)
    deb "Por que você não verifica a {b} caixa de correio {/ b}?"
    deb "Acho que vi algumas ofertas de emprego lá."
    deb "Talvez um desses atinja seu interesse?"
    show debbie 61 at Position (xoffset=-28)
    show player 18
    player_name "Tudo bem, vou dar uma olhada."
    show debbie 62 at Position (xoffset=-28)
    show player 1
    deb "Mais alguma coisa sobre a qual você queria falar, querida?"
    show debbie 1 with dissolve
    return

label debbie_dialogue_ask_about_men_in_suits:
    show player 10
    player_name "{b}[deb_name]{/b}, eu queria falar sobre o que aquele cara de terno disse..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    player_name "Meu {b} pai {/ b} esteve envolvido com eles?"
    show player 11
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b} * Suspiro * {/ b} Suponho que não posso mantê-lo no escuro para sempre ..."
    deb "Seu {b} Pai {/ b} era um homem bom, {b} [primeiro nome] {/ b}."
    deb "... Mas ele tinha uma fraqueza por jogar."
    deb "Ele sempre me disse que não havia nada para me preocupar e que ele tinha tudo em mãos."
    deb "... Mas agora ele se foi e parece que ele não compartilhou muito comigo."
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Seu {b} Pai {/ b} devia muito dinheiro a esses homens e eles ainda estão tentando arrecadar."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Devemos contar à polícia sobre isso!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "NÃO! Eu tenho medo do que pode acontecer se envolver as autoridades nisso!"
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "E daí, você só vai pagar esses babacas?!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Eu fiz o meu melhor, mas tenho medo de não ter dinheiro para cobrir tudo, querida."
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b} * Suspiro * {/ b} Talvez você e eu devêssemos desaparecer e começar de novo em outro lugar."
    show player 1
    show debbie 63 at Position (xoffset=-28) with dissolve
    deb "Heh, that would be an adventure, wouldn't it?"
    show debbie 51 at Position (xoffset=1)
    show player 2
    player_name "Sim, suponho."
    show debbie 2 with dissolve
    show player 1
    deb "Há mais alguma coisa sobre a qual você gostaria de falar?"
    show debbie 1
    return

label debbie_dialogue_paint:
    show player 10
    player_name "Não havia tinta na garagem?"
    show player 5
    show debbie 13
    deb "Pintar? O que você quer com tinta velha??"
    show debbie 1
    show player 10
    player_name "Eu tentaria fazer ... alguma coisa."
    show player 5
    show debbie 2
    deb "Ah, bem, {b}Diane{/b} disse que se livraria deles por mim."
    show debbie 1
    show player 12
    player_name "Sério?"
    player_name "Bem, é melhor eu ver se consigo pegá-los antes que ela os jogue fora!"
    player_name "Obrigado, {b} [deb_name] {/ b}! Tchau, {b} [deb_name] {/ b}!"
    hide player with dissolve
    show debbie 2
    deb "Tchau!"
    return

label debbie_dialogue_help_mow_lawn:
    show player 10
    player_name "Você precisou de ajuda com alguma coisa?"
    show player 5
    show debbie 2
    deb "Você terminou de cortar a grama no quintal?"
    show debbie 1
    show player 10
    player_name "Ah, certo!"
    player_name "Vou tratar disso."
    show player 13
    show debbie 2
    deb "Eu realmente aprecio isso, querida."
    show debbie 1
    show player 14
    player_name "Não tem problema!"
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_help_fix_broken_pipe:
    show player 4
    player_name "( eu tenho que consertar a {b} pia do banheiro {/ b} de alguma forma... )"
    return

label debbie_dialogue_help_chores_pre:
    show player 14
    player_name "Mais alguma coisa com a qual você precise de ajuda?"
    show player 13
    show debbie 2
    return

label debbie_dialogue_help_chores_later:
    deb "Não. Agora não, querida."
    deb "Talvez mais tarde, se você ainda estiver disponível."
    return

label debbie_dialogue_help_chores_tomorrow:
    deb "Não. Hoje não, querida."
    deb "Talvez amanhã, se você ainda estiver disponível."
    return

label debbie_dialogue_help_chores_after:
    show debbie 3
    deb "Obrigado por perguntar!"
    show debbie 1
    show player 14
    player_name "De nada, {b}[deb_name]{/b}."
    return

label debbie_dialogue_help_check_car:
    show player 4
    player_name "( devo verificar o {b} carro {/ b} como {b}[deb_name]{/b} me pediu. )"
    return

label debbie_dialogue_help_fix_car:
    show player 4
    player_name "( tenho que visitar a {b} concessionária de carros {/ b}. Talvez eles possam consertar o carro de{b}[deb_name]'s{/b}... )"
    return

label debbie_dialogue_help_nothing:
    show player 2
    player_name "Ei, {b}[deb_name]{/b}, qualquer coisa que eu possa fazer para ajudar em casa?"
    show player 1
    deb "Hmm..."
    show debbie 2
    deb "Nada que eu possa pensar agora, não."
    show debbie 1
    show player 2
    player_name "Legal. Deixe-me saber se algo acontecer."
    return

label debbie_dialogue_lotion_fun_had_sex:
    show player 14
    player_name "Precisa que eu esfregue um pouco mais de loção nas suas pernas?"
    show player 13
    show debbie 2
    deb "Isso parece maravilhoso, querida."
    deb "Eu realmente poderia usar seu toque gentil agora."
    return

label debbie_dialogue_lotion_fun:
    show player 10
    player_name "Precisa que eu esfregue um pouco mais de loção nas suas pernas?"
    show player 5
    show debbie 13
    deb "Ah ... de novo? Bem, eu ..."
    show debbie 14
    show player 10
    player_name "Eu fiz um trabalho ruim?"
    show player 5
    show debbie 13
    deb "Oh, não, querida. Foi ... muito bom."
    show debbie 14
    pause
    show debbie 13
    deb "Claro, acho que poderia fazer uma pausa."
    show debbie 1
    show player 14
    player_name "Ótimo!"
    show player 13
    show debbie 2
    return

label debbie_dialogue_lotion_fun_after:
    deb "Vá e pegue a {b} loção da cômoda do meu quarto {/b}."
    show debbie 1
    show player 14
    player_name "Tudo bem!"
    return

label debbie_dialogue_shopping:
    scene location_home_kitchen_day_blur
    show player 2 at left
    show debbie 1 at right
    player_name "Lembra quando você me pediu para fazer compras com você?"
    show player 1
    show debbie 2
    deb "Yeah."
    show player 2
    show debbie 1
    player_name "Bem, eu estou livre agora. Você ainda quer ir?"
    show player 1
    show debbie 3
    deb "Really?! Ótimo!"
    show debbie 2
    deb "Deixe-me me arrumar e eu te encontro no carro, ok?!"
    show debbie 1
    show player 2
    player_name "Tudo bem."
    return

label debbie_dialogue_shower_basement:
    show player 2
    show debbie 1
    player_name "Então uhh .."
    player_name "Eu estava pensando que talvez pudéssemos ... Tomar banho juntos?"
    show player 13
    show debbie 2
    deb "Right now?"
    show debbie 1
    deb "Hmm..."
    show debbie 3
    deb "Suponho que eu poderia tomar um banho."
    show debbie 2
    deb "Deixe-me terminar de colocar essa carga de roupa e eu te encontro lá em cima."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Espero que você não esteja quase pronto ..."
    deb "Eu esperava que pudéssemos passar algum tempo aqui."
    return

label debbie_dialogue_shower_kitchen:
    show player 2
    show debbie 1
    player_name "Ei, {b}[deb_name]{/b}!"
    player_name "Eu estava pensando..."
    show player 21
    player_name "Gostaria de tomar um banho comigo?"
    show player 14
    show debbie 2
    deb "Está ficando muito quente em casa.."
    show debbie 3
    deb "SClaro! Um banho parece adorável no momento."
    show debbie 2
    deb "Me dê um minuto. Eu me juntarei a você depois que terminar aqui."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Desculpe te deixar esperando, querida..."
    return

label debbie_dialogue_sex_in_debbies_room_basement:
    show player 14
    player_name "Gostaria de se juntar a mim no seu quarto?"
    show player 13
    show debbie 3
    deb "Agora?"
    show debbie 1
    show player 10
    player_name "Absolutamente!"
    show player 5
    show debbie 2
    deb "Heh, tudo bem..."
    show player 13
    deb "... Apenas verifique se, {b}[jen_name]{/b} não está nos vendo."
    show debbie 1
    show player 14
    player_name "Eu irei."
    show player 13
    show debbie 2
    deb "Hehehe..."
    deb "Você vai me desgastar!"
    show debbie 1
    show player 14
    player_name "Estou apenas garantindo que você faça bastante exercício!"
    show player 13
    show debbie 3
    deb "Ha Ha Ha."
    show debbie 2
    deb "Suba sua bunda e tire essas roupas!"
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_1:
        show debbie 86 at left
        show player 434f at right
        with dissolve
        deb "TOs lençóis são tão agradáveis ​​e macios ... Por que você não vem deitar comigo..."
        show debbie 84
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show debbie 85
        show player 263 with dissolve
        deb "Garoto travesso."
        show debbie 84
        show player 262
        player_name "O quê?"
        show player 263
        show debbie 85
        deb "Você realmente é insaciável."
        show debbie 84
        show player 262
        player_name "Você pode apenas ficar deitado de costas e eu posso fazer o resto."
        show player 263
        show debbie 86
        deb "Bem, onde está a graça nisso?"
        show debbie 84
        show player 262
        player_name "Heh, não se preocupe. Vou torná-lo divertido!"
        show player 263
        show debbie 84
        deb "Mmm, não tenho dúvidas sobre isso!"
        show debbie 89 with dissolve
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_kitchen:
    show player 14
    player_name "Gostaria de se juntar a mim no seu quarto?"
    show player 13
    show debbie 2
    deb "Agora?"
    deb "Absolutamente!"
    deb "Vamos apenas garantir que, {b}[jen_name]{/b} não nos veja."
    show debbie 1
    show player 14
    player_name "Sim."
    show player 13
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_2:
        show player 434f at right
        show debbie 86 at left
        with dissolve
        deb "Eu esperava que você me trouxesse aqui hoje hoje!"
        show debbie 84
        show player 435f
        player_name "Você estava realmente pensando nisso?"
        show player 434f
        show debbie 86
        deb "Isso realmente surpreende você?"
        deb "Estou sempre pensando naquele seu grande pau ..."
        show debbie 84
        show player 435f
        player_name "Heh, eu penso muito sobre isso ... Especialmente quando você está usando esse roupão."
        show player 434f
        show debbie 89 with dissolve
        deb "Você quer dizer essa coisa velha?"
        show debbie 90
        show player 435f
        player_name "... Ah, sim."
        show player 434f
        show debbie 89
        deb "Hehe, por que você não tira essas roupas e vem brincar comigo?"
        show debbie 90
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show player 263
        show debbie 102
        with dissolve
        deb "Mmmm..."
        show debbie 103
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_after:
    deb "Venha me pegar, garotão!"
    hide player
    show debbie 104 at left
    with dissolve
    pause
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_sex_in_my_room:
    show player 2
    player_name "Você quer dormir no meu quarto hoje à noite?"
    show player 1
    show debbie 2
    deb "Mmm, eu adoraria isso, querida."
    show player 2
    show debbie 1
    player_name "Ótimo! Vou esperar por você então."
    show player 1
    show debbie 2
    deb "Mal posso esperar!"
    return

label debbie_dialogue_sex_in_car:
    show player 14
    player_name "{b}[deb_name]{/b}, você poderia vir comigo por um segundo?"
    show player 13
    show debbie 2
    deb "Hmm?"
    show debbie 1
    show player 14
    player_name "Apenas me siga."
    show player 13
    show debbie 2
    deb "Hehe, o que você está fazendo?"
    show debbie 2
    deb "..."
    show debbie 3
    deb "Você está planejando algo!"
    show debbie 2
    deb "Hehe!"
    deb "É uma surpresa?"
    deb "... eu amo surpresas!"
    show debbie 1
    show player 14
    player_name "eh, eu sei que você faz."
    player_name "Eu realmente não chamaria isso de surpresa ..."
    show player 13
    show debbie 3
    deb "Hehe!"
    show debbie 2
    deb "Bem, como você chamaria então?"
    show debbie 1
    deb "..."
    show debbie 2
    deb "Isso é algo impertinente?"
    deb "..."
    show debbie 1
    show player 14
    player_name "Talvez."
    show debbie 2
    deb "Hehe, tudo bem. Vamos rapidamente enquanto {b} [jen_name] {/b} está lá em cima."
    hide player
    hide debbie
    scene black
    with fade
    return

label debbie_dialogue_watch_movie:
    show player 2
    player_name "Eu estava pensando, talvez devêssemos assistir outro filme hoje à noite. Interessado?"
    show player 1
    show debbie 2
    deb "Mmm, uma noite de cinema, hein?"
    deb "Parece uma ótima idéia, querida!"
    show player 2
    show debbie 1
    player_name "Incrível!"
    player_name "Vejo você {b} hoje à noite {/b} na {b} sala de estar {/b}, então?"
    show player 1
    show debbie 2
    deb "Mal posso esperar..."
    return

label debbie_dialogue_laundry_sex_basement:
    scene home_basement
    show debbie 122 at right
    show player 14 at left
    player_name "Você está quase acabando com a roupa?"
    show player 13
    show debbie 123
    deb "Quase. Eu só tenho que mover essa carga para a secadora."
    deb "Por que, querida?"
    show player 14
    show debbie 122
    player_name "Eu apenas pensei que você gostaria de dar uma volta?"
    show player 13
    show debbie 123
    deb "Oh, estamos nos sentindo um pouco malcriados?"
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show debbie 123
    deb "Hehe, vou aceitar isso como um sim!"
    show player 263f with dissolve
    deb "..."
    show debbie 121
    show player 432
    player_name "Absolutamente!"
    show player 431
    pause
    show debbie 123
    deb "Tire essas roupas e entre na lavadora!"
    scene home_basement_sex_01
    show player 271 at Position(xpos=655,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with dissolve
    pause
    show debbie 108
    deb "Minha vez ..."
    deb "Mmm, eu estive esperando a manhã toda por isso!"
    show debbie 109
    pause
    show debbie 110
    pause
    show debbie 111
    pause
    show debbie 112
    pause
    show debbie 113
    pause
    show debbie 114
    pause
    player_name "Você está linda, {b}[deb_name]{/b}."
    show debbie 115
    deb "Sente-se e relaxe, querida."
    deb "Eu vou cuidar de tudo ..."
    deb "... Apenas certifique-se de me segurar."
    hide player
    hide debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655)
    pause
    show debbies 126f with dissolve
    deb "Oh!"
    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    return

label debbie_dialogue_laundry_sex_basement_random_true:
    deb "Mmmm..."
    deb "Eu mal consigo encaixar todos vocês."
    return

label debbie_dialogue_laundry_sex_basement_random_false:
    deb "Ahh..."
    player_name "( !!! )"
    player_name "Você é tão quente..."
    return

label debbie_dialogue_laundry_sex_kitchen:
    show player 14
    player_name "Ei, {b}[deb_name]{/b}... Deseja ficar no porão para se divertir rapidamente?"
    show player 13
    show debbie 2
    deb "Oh?"
    show debbie 1
    show player 14
    player_name "Imaginei que poderíamos ligar a máquina de secar e você poderia estar tão alto quanto quisesse..."
    show player 13
    show debbie 3
    deb "Ha Ha."
    show debbie 2
    deb "Isso é muito travesso, querida."
    show debbie 1
    pause
    show debbie 2
    deb "Hmm ... tudo bem!"
    deb "Eu tenho um tempo livre e posso usar um pouco de atenção."
    show debbie 1
    show player 14
    player_name "Sério?"
    show player 13
    show debbie 2
    deb "Claro!"
    deb "Apenas me encontre lá em um minuto ..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_kiss:
    show player 10 at left
    show debbie 1 at right
    player_name "Ei ... Umm, {b}[deb_name]{/b}?"
    show player 5
    show debbie 2
    deb "Sim, querido?"
    show player 10
    show debbie 1
    player_name "Posso lhe perguntar uma coisa?"
    show player 5
    show debbie 3
    deb "Claro! Você pode me perguntar qualquer coisa."
    show player 10
    show debbie 1
    player_name "em, é meio ... embaraçoso."
    show player 5
    show debbie 13
    deb "Oh? Bem, tudo bem, {b}[firstname]{/b}."
    deb "Não há necessidade de se sentir envergonhado."
    deb "Não comigo ..."
    show debbie 14
    show player 10
    player_name "Ok."
    return

label debbie_dialogue_kiss_teach:
    show player 10 at left
    show debbie 14 at right
    player_name "Eu queria saber se você poderia ..."
    player_name "Bem ..."
    show player 5
    show debbie 13
    deb "Se eu pudesse o quê, querida?"
    show player 10
    show debbie 14
    player_name "Err ... Lembra do outro dia no shopping?"
    show player 5
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "... Sim?"
    show player 10
    show debbie 14b
    player_name "Bem ... eu esperava que você pudesse me ensinar mais sobre beijos?"
    show player 5
    show debbie 13
    deb "O que?!"
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "Isso foi um erro, querida. Eu nunca deveria ter ..."
    deb "O que você está esperando que eu lhe ensine de qualquer maneira?"
    show player 10
    show debbie 14b
    player_name "Você sabe como fazê-lo."
    player_name "Pensei que talvez você pudesse me mostrar o que as mulheres gostam?"
    show player 5
    show debbie 13
    deb "Hmm, bem, eu certamente poderia dizer o que as mulheres gostam."
    deb "... Mas eu não acho que mostrar a você é uma boa idéia. Seria meio inapropriado ..."
    show debbie 14b
    return

label debbie_dialogue_kiss_teach_stat_fail:
    show player 10 at left
    show debbie 14b at right
    player_name "[chr_warn]Você tem certeza?"
    player_name "[chr_warn]Eu realmente gostaria de praticar com você."
    show player 5
    deb "..."
    show debbie 13
    deb "Não é uma boa ideia, querida."
    show player 10
    show debbie 14b
    player_name "[chr_warn]Oh ... tudo bem."
    show player 5
    show debbie 13
    deb "Desculpe, querida."
    show player 10
    show debbie 14b
    player_name "[chr_warn]Está tudo bem, {b}[deb_name]{/b}."
    return

label debbie_dialogue_kiss_leave:
    show player 10 at left
    show debbie 14 at right
    player_name "... Na verdade."
    player_name "Deixa pra lá."
    show debbie 13
    show player 5
    deb "Você tem certeza?"
    deb "Você sempre pode falar comigo, {b}[firstname]{/b}."
    show player 10
    show debbie 14
    player_name "Sim, não é nada."
    player_name "Desculpe incomodá-lo."
    show player 5
    show debbie 13
    deb "Você nunca me incomoda, querida."
    return

label debbie_dialogue_kiss_practice:
    show player 2 at left
    show debbie 1 at right
    player_name "Você acha que poderíamos praticar de novo?"
    player_name "Você sabe ... Beijando?"
    show player 1
    show debbie 13
    deb "Novamente?"
    show player 2
    show debbie 14b
    player_name "Sim. Acho que estou melhorando!"
    show player 1
    show debbie 13
    deb "... Tudo bem."
    deb "Mas só um pouco!"
    show player 2
    show debbie 14
    player_name "Ok, claro."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    deb "Mmm..."
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show debbie 77
    deb "Uau ... eu diria que você definitivamente está melhorando."
    deb "... e você já era tão bom para começar!"
    show player 232
    show debbie 76
    player_name "Obrigado {b}[deb_name]{/b}!"
    show player 231
    show debbie 74
    pause
    show player 230
    pause
    show player 232
    show debbie 76
    player_name "Desculpe pelo ... Você sabe."
    show player 231
    show debbie 75
    deb "Hehe, está tudo bem, querida."
    deb "Perfeitamente natural."
    deb "As garotas desta cidade estão com problemas."
    show player 232
    show debbie 72
    player_name "Hah, você apostou!"
    show player 231
    show debbie 73
    deb "Vá pegá-los, querida!"
    show player 232
    show debbie 72
    player_name "Sim, senhora!"
    return

label debbie_dialogue_leave:
    show player 2
    player_name "Actually, nevermind, see you later, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
