label button_crystal_preamble:
    show player 5 at left
    show crystal 3 at right
    with dissolve
    crys "É o namorado da minha garotinha de novo."
    show crystal 1 with dissolve
    show player 10
    player_name "Eu te disse que não estamos-"
    show player 5
    show crystal 2
    crys "Tudo o que você diz, jovem."
    show crystal 4 with dissolve
    crys "*Gulp*"
    show crystal 2 with dissolve
    crys "Então o que você quer?"
    return

label button_crystal_roxxys_dad:
    show player 10
    player_name "Onde está {b}O pai de Roxxy{/b}?"
    show player 11
    show crystal 2
    crys "Hah! Ela não tem pai!"
    crys "Eu a criei."
    show crystal 1
    show player 10
    player_name "Entendo."
    show player 11
    show crystal 2
    crys "Para dizer a verdade, não me lembro qual era..."
    show crystal 4 with dissolve
    crys "*Gulp*"
    show crystal 2 with dissolve
    crys "...Então o pai dela poderia ser qualquer um, pelo que sei."
    show crystal 1
    show player 22
    player_name "!!!"
    show crystal 2
    crys "Qualquer outra coisa sobre a qual você gostaria de falar?"
    show player 5
    show crystal 1
    return

label button_crystal_roxxy:
    show player 10
    player_name "Você sabe onde eu poderia encontrar {b}Roxxy{/b}?"
    show player 5
    show crystal 3 with dissolve
    crys "Hah! Você acha que eu babá minha filha?"
    show crystal 1 with dissolve
    show player 10
    player_name "Hmm..."
    show player 5
    show crystal 2
    crys "Ela está sempre fora fazendo coisas..."
    crys "...Mas, geralmente ela está {b}school{/b} ou em {b}the beach{/b}."
    show crystal 1
    show player 14
    player_name "Oh Eu vejo. obrigado!"
    show player 13
    show crystal 2
    crys "Algo mais?"
    show crystal 1
    return

label button_crystal_nothing:
    show player 10
    player_name "Oh nada."
    player_name "Eu só estava passando..."
    show player 11
    show crystal 2
    crys "Bem, eu tenho um visitante em breve, então por que você não se move."
    show crystal 1
    show player 10
    player_name "Eu sinto Muito. Eu vou indo então."
    player_name "Tchau!"
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_go_to_picnic:
    scene expression "backgrounds/location_trailer_night_closeup.jpg"
    show player 5 at left
    show player_wet at left
    show crystal 3 at right
    with dissolve
    crys "Mmm, você sabe que eu posso ajudá-lo com essas roupas molhadas, se você quiser?"
    show crystal 1 with dissolve
    show player 10
    player_name "Uhh ... eu..."
    show player 5
    player_name "..."
    show crystal 2
    crys "Não seja tímido agora."
    crys "Homem bonito, como você. Você merece atenção especial, não é??"
    show crystal 1
    show player 3 with dissolve
    player_name "..."
    rox "{b}Mamãe{/b}, sair {b}[firstname]{/b} sozinho!"
    show crystal 2
    crys "Hehehe, só estou provocando um pouco o garoto."
    show crystal 1
    rox "Bem, pare!"
    show crystal 4 with dissolve
    rox "{b}[firstname]{/b}, entre aqui!"
    show crystal 1
    player_name "..."
    hide crystal
    hide player
    hide player_wet
    with dissolve
    return

label button_crystal_rox8_11_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 5 at left
    show crystal 6 at right
    with dissolve
    crys "Você perdeu bonito?"
    show crystal 5
    show player 10
    player_name "Hã?!"
    show player 5
    show crystal 6
    crys "Ah sim {b}Roxxy's{/b} novo homem."
    show crystal 5
    show player 12
    player_name "não sou"
    show player 5
    show crystal 6
    crys "Ela está dentro."
    show crystal 5
    return

label button_crystal_rox8_11_day:
    scene trailer_interior_c
    show player 5 at left
    show crystal 2 at right
    with dissolve
    crys "Você perdeu bonito?"
    show crystal 1
    show player 10
    player_name "Hã?!"
    show player 5
    show crystal 2
    crys "Ah sim {b}Roxxy's{/b} novo homem."
    show crystal 1
    show player 10
    player_name "não sou-"
    show player 5
    show crystal 2
    crys "Ela não está aqui."
    show crystal 4 with dissolve
    return

label button_crystal_final_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show crystal 6 at right
    with dissolve
    crys "Mmm, agora há um bom homem capaz!"
    show crystal 5
    show player 14
    player_name "Oi {b}Crystal{/b}..."
    show player 13
    show crystal 6
    crys "Por que você não pega uma cerveja e vem sentar comigo?"
    crys "Você pode mostrar essa língua de prata um pouco mais..."
    show crystal 5
    show player 14
    player_name "Oh, eu não sei... {b}Roxxy{/b} não-"
    show player 5
    show crystal 6
    crys "Você está aqui para chamar {b}Roxxy{/b} então?"
    show crystal 5
    return

label button_crystal_final_day:
    scene trailer_interior_c
    show player 13 at left
    show crystal 2 at right
    with dissolve
    crys "Mmm, agora há um bom homem capaz!"
    show crystal 1
    show player 14
    player_name "Oi {b}Crystal{/b}..."
    show player 13
    show crystal 2
    crys "Por que você não pega uma cerveja e vem sentar comigo?"
    crys "Você pode mostrar essa língua de prata um pouco mais..."
    show crystal 1
    show player 14
    player_name "Oh, eu não sei... {b}Roxxy{/b} não-"
    show player 5
    show crystal 2
    crys "{b}Roxxy{/b} não está aqui."
    show crystal 1
    return

label button_crystal_sorry_to_bother:
    show player 10
    player_name "Desculpe incomodá-lo."
    show player 5
    show crystal 6
    crys "Psh, falando, não me incomode..."
    crys "De fato, por que você não corre para a loja e me compra um pacote de doze?"
    crys "Você faz isso e podemos conversar até que seus ouvidos caiam."
    show crystal 5
    show player 17
    player_name "Heh, nah tudo bem."
    player_name "Eu deveria entrar e ver {b}Roxxy{/b}."
    show player 13
    show crystal 6
    crys "Se adequar."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_rox8_rox11:
    show crystal 1 with dissolve
    show player 10
    player_name "Você sabe onde ela está?"
    show player 5
    show crystal 2
    crys "Psh, não tenho idéia..."
    crys "Eu nunca posso acompanhar essa garota."
    show crystal 1
    show player 10
    player_name "Realmente?"
    show player 5
    show crystal 2
    crys "Pirralho ingrato, não me diga nada."
    crys "Ela precisa de um whoopin '! O que ela precisa..."
    show crystal 1
    player_name "..."
    return

label button_crystal_roxxy_final:
    show crystal 4 with dissolve
    show player 12
    player_name "Onde ela está?"
    show player 5
    show crystal 2 with dissolve
    crys "Heck, se eu souber."
    crys "Se ela não é {b}at school{/b}, então eu acho que ela provavelmente {b}at the beach.{/b}"
    crys "Eu juro, essa menina é meia sereia!"
    show crystal 1
    show player 17
    player_name "Heh, sim, talvez..."
    show player 13
    return

label button_crystal_roxxys_mom:
    show crystal 1 with dissolve
    show player 10
    player_name "Então você é {b}Roxxy's mom{/b}?"
    show player 5
    show crystal 2
    crys "Está certo."
    crys "Você não pode ver a semelhança?"
    show crystal 1
    menu:
        "Sim, suponho.":
            show player 12
            player_name "Agora que você mencionou, vocês dois se parecem muito."
            show player 5
            show crystal 2
            crys "Sim, ela realmente teve sorte, tomando atrás de mim."
            crys "O pai dela era feio como o pecado!"
            show crystal 1
            player_name "..."
            show crystal 2b
            crys "Hahaha!"
            show crystal 1
            jump roxmom_dialogue_repeat
        "Você parece tão jovem!":
            show player 12
            player_name "Eu vejo a semelhança, mas você parece jovem demais para ser {b}Roxxy's{/b} mamãe."
            show player 10
            player_name "Tem certeza de que não é a irmã dela?"
            show player 5
            show crystal 2
            crys "Bem, agora, se você não tem uma língua de prata em você!"
            crys "Eu acho que foi assim que você chamou a atenção da minha filha, hein?"
            show crystal 1
            show player 10
            player_name "Bem eu-"
            show player 5
            show crystal 2
            crys "Odeio quebrá-lo para você lá, liso ... Mas vai demorar mais do que conversa chique para mantê-la."
            crys "Eu a criei certo, você vê?"
            crys "Mostrou a ela que o valor de um homem está em suas ações e não em suas palavras!"
            show crystal 1
            player_name "..."
            show crystal 2
            crys "Se você não pode cuidar bem da minha garota, é melhor seguir em frente, garoto."
            show crystal 1
            jump roxmom_dialogue_repeat
    return

label button_crystal_roxxy_busy:
    show player 29 with dissolve
    player_name "Is {b}Roxxy{/b} ocupada?"
    show player 3
    show crystal 6
    crys "Psh, duvido..."
    crys "Ela provavelmente está lá, gritando naquele maldito telefone dela."
    show crystal 5
    show player 12 with dissolve
    player_name "Então eu posso simplesmente ir vê-la?"
    show player 5
    show crystal 11
    crys "... Você espera que eu pare você ou algo assim?."
    show crystal 10
    show player 10
    player_name "Eu não-"
    show player 11
    show crystal 6
    crys "Bom sofrimento, garoto."
    crys "Crescer um par e chegar lá já!"
    hide crystal
    hide player
    with dissolve
    return

label button_crystal_happy_home:
    show player 10
    player_name "Você está feliz por estar em casa??"
    show player 5
    show crystal 2
    crys "Maldito tootin eu sou!"
    crys "Este lugar pode ser um buraco de merda, mas supera essa cela da prisão, eu vou te dizer isso de graça!"
    crys "Eu acho que tenho que agradecer por me tirar de lá, hein?"
    show crystal 4 with dissolve
    show player 14
    player_name "Oh, não, obrigado obrigado. Fiquei feliz em ajudar."
    show player 13
    show crystal 2 with dissolve
    crys "Heh, sim ... Ok."
    crys "Se você diz, liso."
    crys "A oferta permanece se você mudar de idéia..."
    crys "Eu posso ser realmente grato ... Saiba o que eu quero dizer?"
    show crystal 1
    show player 5
    player_name "... {b}*Gulp*{/b}"
    show crystal 2
    crys "Hehehe."
    return

label button_crystal_should_go_evening:
    show player 14
    player_name "Eu provavelmente deveria entrar lá..."
    show player 13
    show crystal 6
    crys "Sim, eu acho certo sobre isso."
    crys "Cuide bem da minha garota agora, você ouve?"
    show crystal 5
    show player 14
    player_name "Sim, senhora."
    hide player with dissolve
    pause
    show crystal 6
    crys "Hahaha, "senhora ...\""
    crys "Isso me mata toda vez!"
    hide crystal with dissolve
    return

label button_crystal_should_go_day:
    show player 14
    player_name "Eu provavelmente deveria ir e encontrar {b}Roxxy{/b}."
    show player 13
    show crystal 2
    crys "Bem, você não precisa sair correndo agora..."
    crys "Estou mais do que feliz em lhe fazer companhia até que ela chegue em casa."
    show crystal 1
    show player 14
    player_name "Heh, não, está tudo bem. Eu odiaria ser um incômodo."
    show player 13
    show crystal 2
    crys "Psh, não há problema."
    crys "Eu sei algumas maneiras pelas quais podemos passar o tempo..."
    show crystal 1
    show player 3 with dissolve
    player_name "{b}*Gulp*{/b}"
    show player 29
    player_name "Eu vou ... Até mais tarde, {b}Crystal{/b}."
    show player 3
    show crystal 2
    crys "Se adequar."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_she_here:
    show player 14
    player_name "Sim, ela está aqui?"
    show player 13
    show crystal 6
    crys "Oh, sim, ela está lá..."
    show crystal 11
    crys "Provavelmente yappin 'em seu telefone, como de costume."
    crys "Se eu não soubesse melhor, eu juraria que aquela coisa estava colada ao lado da cabeça daquela garota..."
    show crystal 5
    show player 17
    player_name "Heh, sim."
    show player 13
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
