label josephine_button_dealership_dialogue_pre:
    scene expression player.location.background_closeup with None
    show joe 1 at Position(xpos=0.5474,ypos=0.7630)
    show xtra3 at right
    show player 24 at left
    with dissolve
    return

label josephine_button_dealership_dialogue_intro:
    player_name "Bom Dia."
    show player 109f
    pause
    pause
    show player 108f
    player_name "Olá?"
    show player 109f
    pause
    Josephine "{b}*Suspiro*{/b}"
    pause
    show sato 2 behind xtra3 at Position(xpos=.7630,ypos=0.7299) with dissolve
    show player 11
    Mr. Sato "{b}Josephine{/b}!"
    show sato 1
    show joe 3 at Position(xpos=0.4976,ypos=1.0000) with fastdissolve
    Josephine "O que?!"
    show joe 2
    show sato 2
    Mr. Sato "Você registrou esses relatórios do TPS como eu pedi?"
    show sato 1
    show joe 3
    Josephine "Ugh, nâo..."
    show player 5
    Josephine "Você sabe que eu odeio fazer papelada!"
    show joe 2
    show sato 2
    Mr. Sato "Eu não lhe dei esse trabalho para você ficar sentado o dia inteiro mandando mensagens no telefone."
    show sato 1
    show joe 3
    Josephine "Primeiro de tudo".
    Josephine "Eu não estou mandando mensagens."
    Josephine "Estou comprando sapatos".
    show joe 2
    show sato 2
    Mr. Sato "... {b}Josephine{/b}, isso não é uma piada!"
    Mr. Sato "Você não tem orgulho?"
    Mr. Sato "Como você pode ficar sentado sem fazer nada com todos os outros funcionários trabalhando tanto?"
    show sato 1
    Josephine "..."
    show kim 2 behind xtra3 at Position (xpos=950) with dissolve
    kim "Você ligou, {b}Mr. Sato{/b}?"
    show kim 1
    show sato 2
    Mr. Sato "Hmm?"
    Mr. Sato "Oh, olá {b}Kim{/b}."
    show sato 1
    show joe 1 at Position(xpos=0.5474,ypos=0.7630) with dissolve
    show kim 2
    kim "Eu acompanhei meus números de vendas mais barulhentos em sua mesa."
    show kim 1
    show player 9 with dissolve
    show sato 2
    Mr. Sato "Ah, muito bem!"
    Mr. Sato "Veja lá, {b}Josephine{/b}..."
    Mr. Sato "Por que você não pode agir mais como {b}Kim{/b} aqui?"
    show sato 1
    show joe 3 at Position(xpos=0.4976,ypos=1.0000) with dissolve
    Josephine "Psh, nem todos podemos ter o nariz enterrado na sua bunda, {b}Pai{/b}."
    show joe 2
    show sato 2
    Mr. Sato "{b}Josephine{/b}!"
    show sato 1
    show kim 2
    kim "Você gostaria que eu pegasse seu café, {b}Mr. Sato{/b}?"
    show kim 1
    show sato 2
    Mr. Sato "Oh, isso seria adorável, {b}Kim{/b}."
    Mr. Sato "Apenas traga para o meu escritório, sim?"
    Mr. Sato "Faça sua parte, {b}Josephine{/b}!"
    show sato 1
    show kim 3
    show player 11
    show joe 2c
    with dissolve
    Josephine "... Você acha que eu poderia tirar esses sapatos?"
    show joe 2
    show sato 2
    Mr. Sato "Argh! Apenas, atenda ao seu cliente!"
    show sato 1
    player_name "..."
    hide sato with dissolve
    pause
    show kim 4f at right with dissolve
    pause
    show kim 5 with dissolve
    kim "Hue hue hue hue!"
    show joe 2b
    kim "Que idiota desonesto!"
    show kim 4
    show joe 3
    Josephine "O que há de tão engraçado, menino gordo?"
    show joe 2b
    show kim 2 with dissolve
    kim "MENINO GORDO?!"
    kim "Como você ousa falar comigo desse jeito!"
    show kim 1
    show player 9 with dissolve
    show joe 3
    Josephine "Você é tão nojento..."
    show joe 2
    show kim 2
    kim "Grr, seja assim enquanto você pode!"
    kim "Você acabou de fazer minha merda explodir!"
    show kim 6 with dissolve
   kim "Seu dia de acerto de contas está se aproximando rapidamente!"
    kim "Em breve usurparei esse seu pai incompetente ..."
    kim "... E então você vai limpar minhas unhas dos pés com a língua!"
    show kim 1 with dissolve
    show joe 5
    Josephine "{b}*Bufa*{/b} Hahahaha!"
    show joe 3
    Josephine "Sim, qualquer puta ..."
    Josephine "Você não tem um café para buscar?"
    show joe 2b
    show kim 2
    kim "Grr..."
    hide kim with dissolve
    player_name "..."
    show joe 7 at Position (yoffset=-20) with dissolve
    Josephine "..."
    show player 108f with dissolve
    player_name "{b}*Ahem*{/b}"
    show player 109f
    Josephine "Sim, sim! Eu ouvi você..."
    Josephine "{b}*Suspiro*{/b}"
    Josephine "O que você quer?"
    show player 108f
    player_name "Você trabalha para o seu {b}Pai{/b}?"
    show player 5
    show joe 5 at Position (xpos=0.8294,ypos=1.0000) with dissolve
    Josephine "Oh, ótimas habilidades de observação..."
    Josephine "O que você é, o o sobrinho retardado de Sherlock Holmes ou algo assim?"
    show joe 4
    player_name "..."
    show joe 5
    Josephine "Olha, eu não quero trabalhar aqui. Ele apenas me faz fazer isso para que ele possa ficar de olho em mim."
    show joe 4
    show player 10
    player_name "Isso é realmente péssimo."
    show player 5
    show joe 5
    Josephine "Certo ?!"
    Josephine "Ele é um maníaco por controle, é ridículo!"
    show joe 4
    pause
    show joe 5
    Josephine "De qualquer forma, com o que posso ajudá-lo?"
    show joe 4
    return

label josephine_button_dealership_dialogue_after:
    Josephine "O que você quer de novo?"
    show joe 4 at Position(xpos=0.8294,ypos=1.0000)
    return

label josephine_button_dealership_dialogue_buy_vehicle:
    Josephine "Claro! Qual deles você gostaria de comprar?"
    return

label josephine_button_dealership_dialogue_buy_vehicle_no_money:
    show player 24
    pause
    show player 29
    player_name "Hmmm ... não tenho dinheiro suficiente no momento."
    return

label josephine_button_dealership_dialogue_insurance_claim_pre:
    show player 14
    player_name "Bem, preciso falar com alguém sobre uma reivindicação de seguro"
    show player 11
    show joe 5
    Josephine "Tudo bem. Qual é o número da placa do veículo?"
    show joe 4
    show player 4
    return

label josephine_button_dealership_dialogue_insurance_claim_plate_menu_dialogue:
    player_name "O que era o {b}[deb_name]'s{/b} novamente?"
    return

label josephine_button_dealership_dialogue_insurance_claim_right_plate:
    show player 11
    show joe 6
    Josephine "Sim, parece que temos isso em nosso sistema."
    show joe 5
    Josephine "Você ainda mora na 240 Cookie Street?"
    show joe 4
    show player 17
    player_name "Sim!"
    show player 11
    show joe 5
    Josephine "Ok. Qual é o problema com o veículo?"
    show joe 4
    show player 10
    player_name "O mecanismo está todo quebrado!"
    show player 11
    show joe 6
    Josephine "Um segundo ..."
    pause
    Josephine "..."
    pause
    show joe 5
    Josephine "Sinto muito. Parece que a apólice de seguro do veículo foi cancelada por falta de pagamento".
    show joe 4
    show player 23
    player_name "O que !?"
    show player 22
    show joe 6
    Josephine "Vejo um saldo pendente de {b}$4,000{/b}."
    Josephine "... E sua franquia é fixada em {b}$5,000{/b}."
    show joe 4
    show player 23
    player_name "( !!! )" with hpunch
    show joe 5
    Josephine "Então você ganha pelo menos US $ 9.000 antes de cobrirmos qualquer coisa ..."
    Josephine "Quão ruim é o dano?"
    show joe 4
    show player 22
    player_name "Uhh ... Sim. É bem extremo."
    show joe 5
    Josephine "Isso é uma pena. Parece que você está sem sorte, amigo."
    show joe 4
    pause
    show player 10
    player_name "Droga ..."
    show player 24
    player_name "O que devo fazer agora?"
    return

label josephine_button_dealership_dialogue_insurance_claim_stat_fail:
    show player 24
    player_name "[chr_warn]I... Eu ... Uhm ... você poderia?"
    show joe 5
    Josephine "Eu poderia ... O quê?"
    show joe 4
    show player 37
    player_name "[chr_warn]Hum ... deixa pra lá."
    pause
    show player 24
    player_name "[chr_warn]Desculpe por incomodá-lo."
    show joe 5
    Josephine "Bem, espero que você conserte seu carro."
    show joe 4
    show player 25
    player_name "Sim, obrigado ..."
    show player 24
    player_name "( Vamos lá {b}[firstname]{/b}! Tudo o que você precisava fazer era pedir ajuda. )"
    player_name "{b}*Suspiro*{/b}"
    player_name "( estou muito nervoso... )"
    return

label josephine_button_dealership_dialogue_insurance_claim_pay:
    show player 14
    player_name "Eu deveria ter o suficiente para cobrir o custo."
    show player 12
    player_name "Você aceita dinheiro?"
    show player 5
    show joe 5
    Josephine "Sim."
    show joe 4
    show player 14
    player_name "Aqui."
    show player 41 at Position (xoffset=38) with dissolve
    show joe 5
    Josephine "Obrigado."
    show player 5
    show joe 6
    Josephine "Você trouxe o carro hoje?"
    show joe 4
    show player 12
    player_name "Não ... está quebrado."
    player_name "Ainda está em nossa casa."
    show player 5
    show joe 6
    Josephine "Oh ... Bem, podemos enviar um mecânico."
    show joe 5
    Josephine "Quando você gostaria que consertássemos?"
    show joe 4
    show player 14
    player_name "Hoje seria o ideal."
    show player 12
    player_name "É o nosso único carro e demorei uma eternidade para chegar aqui."
    show player 5
    show joe 5
    Josephine "Umm ... Normalmente, estamos reservados por uma semana ..."
    show joe 6
    Josephine "Deixe-me olhar."
    Josephine "Você está com sorte."
    show joe 5
    Josephine "Eu devo mandar um mecânico esta tarde."
    show joe 4
    show player 14
    player_name "Ótimo!"
    player_name "Muito obrigado."
    show player 13
    show joe 5
    Josephine "De nada."
    show joe 4
    show player 10
    player_name "Mais alguma coisa?"
    show player 5
    show joe 5
    Josephine "Não, você deve estar pronto."
    show joe 4
    show player 14
    player_name "Obrigado novamente!"
    show player 106
    show joe 1 at Position(xpos=0.5474,ypos=0.7630) with dissolve
    Josephine "Uh huh."
    return

label josephine_button_dealership_dialogue_insurance_claim_pay_convince:
    show player 12
    player_name "Seria possível fazer os pagamentos posteriormente?"
    show player 10
    player_name "Estamos meio que passando por uma fase difícil no momento."
    player_name "A mulher com quem estou morando tem apenas um carro e é muito importante para nós ..."
    show player 11
    show joe 5
    Josephine "Eu acho que não posso-"
    show joe 4
    show player 24
    player_name "... E meu {b}pai{/b} acabou de falecer há pouco mais de um mês ..."
    show player 25
    player_name "Então, estamos lutando para sobreviver!"
    pause
    show joe 6
    Josephine "{b}*Suspiro*{/b} Ouça..."
    show joe 5
    Josephine "Eu vou ajudá-lo desta vez {b}um{/b} momento!"
    show joe 6
    Josephine "Meu {b}pai{/b} me mataria se descobrisse, então mantenha-o em baixo."
    show joe 4
    show player 14
    player_name "Isso seria maravilhoso! Muito obrigado!"
    show player 13
    show joe 5
    Josephine "Não mencione. Eu meio que gosto da idéia de estragar tudo com ele."
    show joe 6
    Josephine "Vou apenas fazer sua dívida desaparecer e reduzir sua franquia ao mesmo tempo."
    Josephine "Vou agendar um técnico em sua casa para consertar o veículo. Ele deve ser consertado até o final do dia."
    show joe 4
    show player 10
    player_name "Isso é incrível, muito obrigado!"
    Josephine "... Uh huh."
    show player 14
   player_name "Realmente, você é uma pessoa maravilhosa!"
    show player 13
    show joe 5
    Josephine "Pffft !!! Sim ... Ok. Você {b}me deve uma{/b}!"
    show joe 4
    show player 17
    player_name "... Ah, claro. O que você quiser!"
    return

label josephine_button_dealership_dialogue_insurance_claim_give_up:
    show player 10
     player_name "Eu provavelmente deveria conversar com {b}[deb_name]{/b} sobre isso."
    show player 2
    player_name "Obrigado!"
    show player 1
    show joe 5
    Josephine "Claro, tanto faz."
    return

label josephine_button_dealership_dialogue_insurance_claim_proctologist_plate:
    show player 11
    show joe 5
    Josephine "Você definitivamente não é o {b}homem bunda{/b}. O proctologista local tem essa licença."
    show joe 4
    show player 26
    player_name "Oh. Sim ..."
    show player 4
    return

label josephine_button_dealership_dialogue_insurance_claim_wrong_plate:
    show player 11
    show joe 6
    pause
    show joe 5
    if randomizer() < 50:
        Josephine "Josephine "Não estou vendo uma conta que corresponda àquela placa".."
    else:
        Josephine "Esse seria um prato bonito, mas infelizmente não está no sistema."
    Josephine "Alguma outra placa em que você pode pensar?"
    show joe 4
    show player 4
    return

label josephine_button_dealership_dialogue_kim:
    show player 10
    player_name "O que há com esse tubby?"
    show player 5
    show joe 5
    Josephine "Hmm?"
    Josephine "Oh, {b}Kim{/b}?"
    Josephine "... Sim, ele é um idiota."
    Josephine "Ele passa o dia inteiro castigando meu {b}Pai{/b} e depois tramando pelas costas."
    show joe 4
    show player 12
    player_name "Você não gostaria, avise seu {b}Pai{/b} ou algo assim?"
    show player 5
    show joe 5
    Josephine "Psh, inferno, não!"
    Josephine "Se ele é estúpido demais para ver o que esse munchkin malvado está fazendo, então ele merece perder o emprego."
    Josephine "Pelo menos então, eu poderia sair desse buraco de merda ..."
    show joe 4
    player_name "..."
    Josephine "..."
    show joe 3
    Josephine "oh meu Deus, isso é chato!"
    show joe 4
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
