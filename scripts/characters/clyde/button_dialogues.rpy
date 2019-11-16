label button_clyde_pink_beaver:
    scene expression player.location.background_blur with None
    show player 14f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Ei, sobre o castor que você queria."
    show player 13f
    show clyde 2
    clyde "Yah?"
    show clyde 1
    show player 239_240f
    pause
    show player 709f
    player_name "É isso?"
    show player 708f
    show clyde 30
    clyde "!!!"
    show clyde 4 with dissolve
    clyde "Bem, bata manteiga na minha bunda e me chame de biscoito, você realmente conseguiu!"
    show clyde 3
    show player 709f
    player_name "Eu pensei que poderia ser isso."
    show clyde 34
    show player 13f
    with dissolve
    pause
    show clyde 35
    clyde "Como diabos você ganhou essa coisa?!"
    show clyde 33 with dissolve
    clyde "A feira nem vai ficar aqui por mais 2 meses!"
    show clyde 32
    show player 12f
    player_name "Eu comprei no shopping, {b}Clyde{/b}."
    show player 5f
    show clyde 2 with dissolve
    clyde "O Shopping?"
    clyde "Ah, atire."
    clyde "Eu nunca estive aqui antes."
    clyde "Para onde esse cachorro fugiu agora?"
    clyde "Vamos garota!"
    show clyde 1
    pause
    show player 10f
    player_name "Esperar. Você nunca esteve no shopping?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Não senhor."
    show clyde 3
    show player 10f
    player_name "Onde você compra suas compras então?"
    show player 5f
    show clyde 4
    clyde "Pfft, seu povo da cidade e suas compras..."
    clyde "Eu não estou pagando ninguém por essas coisas que são gratuitas aqui na floresta!"
    show clyde 3
    show player 10f
    player_name "... Huh?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Eu caço comida, amigo."
    show clyde 4 with dissolve
    clyde "Falando nisso, eu tenho um belo pote de guisado de esquilo lá em mah shack."
    clyde "Você deveria vir para o jantar!"
    show clyde 3
    show player 12f
    player_name "Eugh, não, obrigado."
    show player 5f
    pig "{b}*Squeeeeee*{/b}"
    show clyde 4
    clyde "Aí está você!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Onde você esteve garota?!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 38
    with dissolve
    pig "*{b}Oink{/b}*"
    show clyde 37
    clyde "Olha o que {b}[firstname]{/b} trouxe!"
    show clyde 38
    pig "{b}*SQUEE SQUEE*{/b}"
    show clyde 37
    clyde "Hehehe, olha como ela está feliz!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Você vai se divertir agora!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 3
    with dissolve
    pig "{b}*Snort*{/b}"
    pause
    show clyde 4
    clyde "Agora esse é um cão feliz."
    clyde "Tudo bem feller..."
    show clyde 9 with dissolve
    clyde "Eu tenho que pagar você de alguma forma."
    show clyde 3 with dissolve
    show player 12f
    player_name "Não se preocupe com isso."
    player_name "Apenas considere um presente."
    show player 5f
    show clyde 4
    clyde "Agora espere, só um segundo."
    show clyde 1 with dissolve
    pause
    show clyde 9 with dissolve
    clyde "Oh!"
    clyde "Eu tenho exatamente o que!"
    hide clyde
    hide clyde_hat
    with dissolve
    show player 10f
    player_name "Onde você vai?!"
    show player 5f
    clyde "Espere aí!"
    pause
    clyde "Não mexa um músculo!"
    show player 25f
    player_name "Oh, cara."
    player_name "R-realmente, está tudo bem..."
    player_name "Eu não preciso-"
    show player 11f
    show clyde 40 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    with dissolve
    clyde "Confira!"
    show clyde 39
    if player.has_item("mysterious_statue_1"):
        show player 23f
        player_name "!!!"
        show player 30f
        if M_clyde.get("cletus"):
            player_name "{b}Clyde{/b}, Eu pensei que você disse que não sabia nada sobre a estátua do seu avô!"
        else:
            player_name "{b}Cletus{/b}, Eu pensei que você disse que não sabia nada sobre a estátua do seu avô!"
        show player 90f
        show clyde 40
        clyde "Oh, certo."
        clyde "Eu disse isso, não disse?"
        show clyde 39
        pause
        show clyde 11 with dissolve
        clyde "Bem, eu estava mentindo'."
        show clyde 12
        show player 12f
        player_name "Por quê?!"
        show player 90f
    else:

        player_name "!!!"
        show player 30f
        player_name "Que raio é aquilo?"
        show player 5f
        show clyde 40
        clyde "Bem, costumava pertencer ao meu avô."
        show clyde 39
        show player 10f
        player_name "Seu avô?!"
        show player 5f
        show clyde 9 with dissolve
        clyde "Está certo!"
        clyde "Ole' {b}Jebediah Delmont{/b} ele mesmo!"
        show clyde 3
        pause
        player_name "..."
        show clyde 2 with dissolve
        clyde "Você nunca ouviu falar de {b}Jebadiah Delmont{/b}?"
        show clyde 1
        show player 10f
        player_name "Não?"
        show player 5f
        show clyde 2
        clyde "{b}*Sigh*{/b} Minha nossa."
        show clyde 4 with dissolve
        clyde "Ele costumava ser famoso em todas essas partes por suas vacas e seu delicioso leite!"
        clyde "Ele ganhou todos os tipos de concursos."
        show clyde 3
        show player 10f
        player_name "Ele era um fazendeiro?"
        show player 5f
        show clyde 4
        clyde "Bem, ele não fez apenas fazendas de laticínios'."
        clyde "Ele tinha todos os tipos de animais."
        show clyde 9 with dissolve
        clyde "Você deveria ter visto os ovos de galinha que ele traria para a feira."
        clyde "Eles eram do tamanho de uma bola de futebol!"
        show clyde 3 with dissolve
        show player 10f
        player_name "Sério?"
        show player 5f
        show clyde 4
        clyde "Heh, sim amigo!"
        show clyde 3
        pause
        show player 17f
        player_name "Isso parece incrível!"
        show player 14f
        player_name "Me diga mais."
        show player 13f
        show clyde 11 with dissolve
        clyde "Ah não. Eu-"
        clyde "{b}*Ahem*{/b} Eu realmente não quero entrar nisso tudo..."
        show clyde 12
        show player 10f
        player_name "Huh, porque não?"
        show player 5f
    show clyde 11
    clyde "Olha amigo, meu avô não é exatamente o orgulho do {b}Delmont family{/b}..."
    clyde "Nós não gostamos de falar sobre isso!"
    show clyde 12
    show player 10f
    player_name "Por quê?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Sigh*{/b} Vamos apenas dizer' {b}Jebediah{/b} foi um pouco, tocou na cabeça, tudo bem?"
    show clyde 1
    show player 10f
    player_name "Tocada na cabeça?"
    show player 5f
    show clyde 2
    clyde "Você sabe."
    clyde "Ele tinha alguns parafusos soltos."
    show clyde 1
    show player 10f
    player_name "Uhh..."
    show player 5f
    show clyde 9 with dissolve
    clyde "Sua roda estava girando, mas o hamster estava morto."
    show clyde 3 with dissolve
    show player 10f
    player_name "Eu não..."
    show player 5f
    show clyde 4
    clyde "Ele tinha poucas cartas abaixo do baralho completo."
    show clyde 3
    show player 12f
    player_name "Do que você está falando?!"
    show player 5f
    show clyde 26 with dissolve
    clyde "Tch, ele era mais maluco do que um potty de porta em um festival de amendoim, tudo bem?!"
    show clyde 25
    show player 12f
    player_name "Você quer dizer que ele era louco?"
    show player 5f
    show clyde 26
    clyde "Isso é o que eu tenho tentado lhe dizer..."
    show clyde 25
    show player 10f
    player_name "Oh."
    show player 5f
    show clyde 2
    clyde "Sim."
    clyde "Mamãe diz que ele sempre foi um pouco excêntrico."
    clyde "O pessoal do gritador costumava chamá-lo de mago caipira."
    show clyde 1
    show player 10f
    player_name "Ele era um mago?"
    show player 5f
    show clyde 2
    clyde "Sim, mas ele não era muito bom."
    clyde "Eu lembro, ele tentou me transformar em sapo uma vez, porque eu tinha ido e fiquei com a cabeça presa nas escadas."
    show clyde 1
    show player 10f
    player_name "Você ficou com a cabeça presa nas escadas?!"
    show player 5f
    show clyde 2
    clyde "Meu irmão me disse que havia um duende morando embaixo da escada e eu queria vê-lo."
    show clyde 1
    show player 17f
    player_name "Pfft, hahaha!"
    show player 13f
    show clyde 2
    clyde "De qualquer forma, seu feitiço não funcionou."
    show clyde 11 with dissolve
    clyde "Então mamãe teve que me untar com gordura de bacon e me tirar."
    show clyde 12
    show player 17f
    player_name "Haha!"
    show player 13f
    show clyde 4
    clyde "Então houve uma vez, eu estava reprovando na segunda série..."
    clyde "... E avô, ele disse: "Não se preocupe {b}Clyde{/b}. O avô vai consertar isso para você.\""
    show clyde 3
    pause
    show player 14f
    player_name "Ok, então o que aconteceu?"
    show player 13f
    show clyde 2 with dissolve
    clyde "Bem, eu não sei com razão. Eles o encontraram na casa da escola, no meio da noite, nu e coberto de sangue de galinha."
    show clyde 1
    show player 23f
    player_name "Sangue de galinha?!"
    show player 11f
    show clyde 2
    clyde "Sim, ele disse que estava realizando uma espécie de ritual para me ajudar com minha escola'."
    clyde "Aparentemente, ele estava piando e gritando e carregando."
    show clyde 1
    show player 10f
    player_name "Sim, ele parece um pouco louco, {b}Clyde{/b}."
    show player 12f
    show clyde 2
    clyde "Sim, eu acho que ele era."
    clyde "Ele era um homem doce e velho."
    clyde "É uma pena que todos os espíritos malignos ficaram bravos com ele."
    show clyde 1
    show player 10f
    player_name "Espiritos malignos?"
    show player 11f
    show clyde 2
    clyde "Sim, ele me contou tudo logo depois que ele quebrou esta estátua aqui e escondeu os pedaços."
    clyde "Disse que eles estavam vindo atrás dele e ele queria que ela estivesse segura."
    show clyde 1
    show player 10f
    player_name "Dela?"
    show player 5f
    show clyde 40 with dissolve
    clyde "A senhora da estátua, é claro!"
    clyde "Ele estava realmente chateado por escondê-la."
    clyde "Ela era seu amuleto de boa sorte, afinal."
    show clyde 39
    show player 12f
    player_name "Esquisita."
    show player 5f
    show clyde 9 with dissolve
    clyde "Então nós o pegamos fornicando com o gado e mamãe o mandou para a casa de nozes."
    show clyde 3 with dissolve
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Você quer dizer que ele-"
    player_name "com animais?!"
    show player 37f
    show clyde 11
    with dissolve
    clyde "{b}*Sigh*{/b} Sim, chorando como um bebê também."
    clyde "Aqueles espíritos devem realmente ter um número com ele, pobre companheiro."
    show clyde 12
    show player 10f with dissolve
    player_name "Então uhh..."
    player_name "... Seu avô ainda está morando na casa da castanha?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ah não."
    clyde "Cerca de duas semanas depois que a mãe o mandou para lá, seu quarto pegou fogo e ele ardeu nele.."
    show clyde 1
    show player 24f
    player_name "Jesus..."
    show clyde 2
    clyde "Eles não sabem como o fogo começou, mas eu acho que os espíritos finalmente o pegaram."
    show clyde 1
    player_name "Eu nem..."
    player_name "..."
    show clyde 30
    clyde "Sim, foi muito triste..."
    show clyde 29
    pause
    show player 11f
    show clyde 2
    clyde "Enfim!"
    show player 5f
    show clyde 40 with dissolve
    clyde "Eu acho que ele não se importaria de eu lhe dar este pedaço da estátua."
    clyde "Vendo como você me ajudou e tudo."
    clyde "Quem sabe, talvez isso lhe traga sorte também."
    show clyde 39
    show player 10f
    player_name "direita."
    player_name "Obrigado eu acho..."
    show player 715f
    show clyde 9
    with dissolve
    clyde "Não mencione, amigo!"
    show player 5f with dissolve
    clyde "Agora, se você me der licença."
    clyde "Eu quero ver meu cachorro dar a esse velho castor o que!"
    hide clyde
    hide clyde_hat
    with dissolve
    clyde "Hehehe."
    show player 239_240f with dissolve
    pause
    show player 715f with dissolve
    player_name "( Você sabe, isso realmente explica bastante sobre {b}Clyde{/b} e por que ele é do jeito que é... )"
    pause
    player_name "( Eu acho que eu deveria ficar de olho nas outras peças desta estátua. )"
    hide player with dissolve
    return

label button_clyde_mysterious_statue_1:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 688cf
    player_name "Você sabe alguma coisa sobre isso {b}Clyde{/b}?"
    show player 688bf
    show clyde 30
    clyde "{b}*Gasp*{/b} Onde no mundo você achou isso?!"
    show clyde 29
    show player 688cf
    player_name "Foi enterrado sob a casa dos meus amigos."
    show player 688bf
    pause
    show player 688cf
    player_name "O nome {b}Delmont{/b} está gravado no fundo."
    show player 688bf
    show clyde 2
    clyde "Sim."
    show clyde 4 with dissolve
    clyde "Faz parte do amuleto de boa sorte do meu avô."
    show clyde 3
    show player 688cf
    player_name "Avô?"
    player_name "Você quer dizer seu avô?"
    show player 13f with dissolve
    show clyde 4
    clyde "Uh huh, {b}Jebadiah Delmont{/b}."
    clyde "Ele era muito famoso nessas partes há muitos anos pelo leite produzido por suas vacas."
    show clyde 3
    show player 10f
    player_name "Leite de vaca?"
    show player 5f
    clyde "Mmhmm."
    show clyde 4
    clyde "Estava uma delícia!"
    clyde "Ganhou um monte de concursos com ele."
    show clyde 3
    show player 14f
    player_name "Isso é bem legal."
    show player 13f
    show clyde 4
    clyde "Ele também tinha ovos de galinha incríveis."
    clyde "Eles eram grandes como uma bola de futebol!"
    show clyde 3
    pause
    show player 12f
    player_name "Direita..."
    show player 5f
    pause
    show player 10f
    player_name "Tão uhh..."
    player_name "Você sabe onde o resto desta estátua pode estar?"
    show player 5f
    show clyde 11 with dissolve
    clyde "Não!"
    show clyde 12
    pause
    show player 10f
    player_name "Oh, porque eu apenas pensei-"
    show player 5f
    show clyde 9 with dissolve
    clyde "Desculpe companheiro, não posso ajudá-lo!"
    clyde "Eu sei agachamento!"
    show clyde 3 with dissolve
    show player 10f
    player_name "Tudo bem..."
    show player 24f
    player_name "Obrigado de qualquer maneira, eu acho."
    show player 5f
    show clyde 1 with dissolve
    return

label button_clyde_mysterious_statue_2:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 715bf with dissolve
    player_name "Alguma idéia de onde posso encontrar mais desta estátua?"
    show player 715cf
    show clyde 2
    clyde "Erm, na verdade não."
    clyde "Conhecendo o avô, essa última peça provavelmente {b}encontrar-te{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "O que você quer dizer?"
    show player 5f
    show clyde 2
    clyde "Sim, eu acho que prolly jus' {b}encontre um lugar agradável e confortável para relaxar{/b}..."
    clyde "... {b}sperto da praia, talvez{/b}."
    show clyde 1
    pause
    show clyde 2
    clyde "Eu aposto' {b}essa cabeça vai aparecer por si só{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "Ehh certo..."
    player_name "Bem, obrigado. eu acho..."
    show player 5f
    show clyde 9 with dissolve
    clyde "Não tem problema, amigo."
    show clyde 1 with dissolve
    return


label button_clyde_your_dog:
    scene expression player.location.background_blur with None
    show player 10f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Então, sobre o seu cachorro..."
    show player 5f
    show clyde 4 with dissolve
    clyde "Ah sim, ela é uma boa garota, não é??"
    show clyde 3
    show player 10f
    player_name "OK, claro."
    show player 12f
    player_name "Você percebe que ela não é um cachorro, certo?"
    show player 5f
    show clyde 4
    clyde "Melhor cachorro que já tive!"
    show clyde 3
    show player 24f
    player_name "{b}*Sigh*{/b}"
    show player 5f
    show clyde 4
    clyde "É por isso que estou praticando tanto, para conquistá-la como uma {b}castores recheados{/b} na feira."
    show clyde 3
    show player 12f
    player_name "Sim, você mencionou isso."
    show player 10f
    player_name "Por que você não compra um para ela?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Psh, agora você está falando louco..."
    clyde "O que você acha {b}Castores-de-rosa{/b} apenas crescer em árvores ou algo assim'?"
    show clyde 3 with dissolve
    show player 10f
    player_name "A cor realmente importa?"
    show player 5f
    show clyde 4
    clyde "Caramba, isso importa!"
    clyde "{b}Castores-de-rosa{/b} são os melhores castores."
    show clyde 9 with dissolve
    clyde "Todo mundo sabe disso!"
    show clyde 3 with dissolve
    show player 402f
    player_name "... Direito."
    show player 10f
    player_name "Ok, boa sorte com tudo o que eu acho..."
    show player 5f
    show clyde 4
    clyde "\"Sorte\" é meu nome do meio, irmão."
    show clyde 3
    pause
    show clyde 2 with dissolve
    clyde "Na verdade, é Cornelius."
    show clyde 1
    show player 12f
    player_name "Hã?"
    show player 5f
    show clyde 2
    if M_clyde.get("cletus"):
        clyde "{b}Cletus Cornelius Delmont{/b}."
    else:
        clyde "{b}Clyde Cornelius Delmont{/b}."
    show clyde 1
    show player 10f
    player_name "Você é o nome do meio é Cornelius?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Sim amigo."
    clyde "Como aquele prospector no show de renas voando."
    show clyde 4
    clyde "Você viu esse?!"
    show clyde 3
    show player 10f
    player_name "Acho que não..."
    show player 5f
    show clyde 4
    clyde "Maaan, das uma ótima!"
    show clyde 3
    show player 10f
    player_name "Você é um cara estranho, {b}Clyde{/b}."
    show player 5f
    show clyde 4
    clyde "Uh huh!"
    show clyde 1 with dissolve
    return

label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "Precisamos conversar sobre essa situação com {b}Crystal{/b}."
    show player 5f
    show clyde 22
    clyde "eu prefiro que nao..."
    show clyde 21
    show player 10f
    player_name "{b}Clyde{/b}, eles vão mandá-la embora para a prisão e levar o trailer embora!"
    show player 5f
    show clyde 26
    clyde "Olha lá! Você acha que eu não sei disso!"
    clyde "Eu me sinto mal, mas não há nada que eu possa fazer para impedir isso!"
    show clyde 25
    show player 12f
    player_name "Você pode se entregar..."
    show player 5f
    show clyde 22
    clyde "Okay, certo..."
    clyde "Então nós dois acabamos atrás das grades!"
    show clyde 21
    show player 10f
    player_name "Não se você lhes disser que {b}Crystal{/b} não tinha ideia de que você escondeu as drogas lá."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "... E por que eu faria isso?"
    show clyde 1
    show player 12f
    player_name "... Porque é a coisa certa a fazer!"
    show player 90f
    show clyde 2
    clyde "Pfft."
    clyde "Eu não posso ir para a prisão!"
    clyde "Feller bonito como eu, esses animais vão me comer vivo aqui."
    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Olha cara. Ela levou a queda por você, porque ela é sua família."
    player_name "...Mas isso é muito pior do que ela pensa que é!"
    player_name "Ela vai embora por um longo tempo e {b}Roxxy{/b} vai perdê-la {b}Mom{/b} e a casa dela."
    show player 12f
    player_name "{b}Roxxy{/b} não fez nada para merecer isso!"
    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Aww, merda! Você está certo."
    clyde "{b}Roxanne{/b} não deveria ter que sofrer por minha conta..."
    clyde "... Mas eu não vou voltar para a prisão! ... Não senhor!"
    show clyde 21
    player_name "..."
    show player 14f
    player_name "E se você enviou sua confissão com uma carta?"
    player_name "Conte a eles sobre seu barraco e deixe-os encontrar as evidências."
    player_name "Se você fizer as coisas certas, poderá demorar muito antes que elas comecem a procurá-lo."
    show player 13f
    clyde "..."
    show clyde 22
    clyde "Suponho que poderia voltar ao gritador..."
    clyde "Eles nunca vão me encontrar lá."
    clyde "... Com certeza sentiria falta {b}Auntie Crystal{/b} Apesar..."
    show clyde 21
    show player 10f
    player_name "Você a salvaria da prisão, cara."
    show player 5f
    show clyde 22
    clyde "Hmm, eu acho que você tem um bom plano."
    show player 13f
    clyde "Então eu faço isso e ela sai livre?"
    show clyde 21
    show player 12f
    player_name "... Ainda teríamos que pagar uma fiança para ela, mas é um bom começo."
    show player 5f
    show clyde 22
    clyde "Quanto dinheiro você precisa?"
    show clyde 21
    show player 12f
    player_name "$50,000..."
    show player 5f
    show clyde 2
    clyde "... Huh."
    clyde "Bem, eu posso fazer isso!"
    show clyde 1
    show player 10f
    player_name "O que ?! "com soco."
    player_name "Você não pode estar falando sério..."
    player_name "Você tem $ 50.000 espalhados por algum lugar?"
    show player 11f
    show clyde 2
    clyde "Não exatamente."
    show clyde 4 with dissolve
    clyde "... Mas eu tenho uma bagunça toda essa metanfetamina."
    clyde "O suficiente para liberar US $ 100.000 para o comprador certo, imagino."
    show clyde 3
    show player 10f
    player_name "Isso é loucura!"
    player_name "Você pode realmente vendê-lo?"
    show player 5f
    show clyde 4
    clyde "Pfft! Vamos amigo..."
    clyde "Você não sabe com quem está falando?"
    clyde "Eu poderia vender um picolé de ketchup para uma garota usando luvas brancas!"
    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... Picolé de ketchup?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Sim amigo!"
    show clyde 3 with dissolve
    show player 14f
    player_name "...Quando você pode fazer isso?"
    show player 13f
    show clyde 4
    clyde "Hmm, eu vou ter que ligar para mah comprador."
    clyde "... Mas perty logo, eu acho'."
    show clyde 3
    show player 14f
    player_name "Eu vou contar {b}Roxxy{/b} as boas notícias!"
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "[chr_warn]Você é um covarde!"
    show player 90f
    show clyde 26
    clyde "[chr_warn]Ei agora, você não está ligando {b}ME{/b} sem covarde!"
    clyde "[chr_warn]Você não tem ideia de como é o que bate com violência para alguém como eu!"
    clyde "[chr_warn]Eu já estive lá uma vez e serei amaldiçoado se vou voltar!"
    show clyde 25
    show player 15f
    player_name "[chr_warn]Tanto faz... {b}COWARD{/b}!"
    show player 16f
    show clyde 26
    clyde "[chr_warn]Dane-se!"
    clyde "[chr_warn]Eu não tenho que tomar isso!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Ugh, esqueça!"
    show player 90f
    show clyde 22
    clyde "Sim, é exatamente isso que pretendo fazer'!"
    clyde "Eu acho que é uma bagunça toda esquecendo no fundo dessas latas de cerveja aqui!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "Quando você pode vender esse Meth?"
    show player 5f
    show clyde 2
    clyde "Segure seus cavalos, amigo!"
    clyde "Essas coisas levam tempo."
    show clyde 1
    player_name "..."
    show clyde 2
    clyde "Você apenas continua e diz ao meu doce {b}cousin{/b} naquele {b}Clyde{/b}vai cuidar do everthang!"
    show clyde 1
    show player 14f
    player_name "... Direito."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "Você já entrou em contato com seu comprador?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Sim amigo!"
    show player 13f
    clyde "Estou me preparando para matar um negócio aqui!"
    show clyde 3
    show player 12f
    player_name "{b}Roxxy{/b} diz que você nunca vendeu Meth antes!"
    show player 90f
    show clyde 26 with dissolve
    clyde "o que?!"
    clyde "Ela não sabe nada'!"
    clyde "Eu estive em muitas dessas ofertas aqui!"
    show clyde 25
    show player 12f
    player_name "Você já lidou com os compradores antes?"
    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Bem, eu assisti {b}Auntie Crystal{/b} faça isso um hundert vezes!"
    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{b}*Sigh*{/b} eu vou contigo."
    show player 90f with dissolve
    show clyde 2
    clyde "Hã?"
    clyde "O que você sabe sobre a venda de medicamentos?!"
    show clyde 1
    show player 12f
    player_name "Não é uma coisa maldita."
    player_name "... Mas eu conheço você e você definitivamente não é competente o suficiente para fazer isso sozinho."
    show player 90f
    show clyde 22
    clyde "Bem, isso não é ... Espere um segundo, o que significa campito?!"
    show clyde 1
    show player 12f
    player_name "... Exatamente."
    show player 90f
    show clyde 2
    clyde "Tch, tanto faz, amigo."
    clyde "Venha ou não venha. Não importa para mim!"
    show clyde 26
    clyde "... Mas se você está vindo, é melhor {b}encontre-me no trailer, hoje à noite{/b}."
    clyde "You got that?"
    show clyde 1
    show player 12f
    player_name "É, eu entendi."
    player_name "Eu vou te ver {b}tonight at Roxxy's trailer{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Ainda é bom vender esse Meth?"
    show player 90f
    show clyde 4 with dissolve
    clyde "Claro que nada."
    clyde "Apenas esteja aqui {b}esta noite{/b} Se o seu plano é definir junto."
    show clyde 3
    show player 12f
    player_name "É, eu entendi."
    player_name "Eu vou te ver {b}esta noite{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Você está pronto para ir?"
    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "Você está usando esse?"
    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "O que há de errado com o que estou vestindo?"
    show player 5f
    show clyde 2
    clyde "Eugh ... não sei, amigo. Você parece muito desconfiado..."
    clyde "Eu com certeza não compraria drogas de alguém parecendo você."
    show clyde 1
    show player 10f
    player_name "Bem, eu não trouxe nenhuma outra roupa..."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "Espere um segundo. Eu tenho algo para você vestir!"
    hide clyde with dissolve
    show player 12f
    player_name "... Isso deveria ser interessante."
    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "Vamos agora, amigo..."
    clyde "Você vai nos atrasar!"
    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "Não acredito que deixei você me convencer a usar isso..."
    player_name "Me sinto ridículo!"
    show player 90f
    show clyde 4
    clyde "Psh, não seja bobo."
    clyde "Você parece o verdadeiro negócio!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "O comprador deve estar aqui a qualquer momento."
    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Clyde{/b}?!"
    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "Quando você voltou para a cidade?!"
    show player 5f
    show clyde 2
    clyde "Ehh, desculpe amigo."
    clyde "Você entendeu errado..."
    show clyde 1
    show player 10f
    player_name "Hã?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Nome {b}Cletus{/b}!"
    clyde "Prazer em conhecê-lo!"
    show clyde 3
    player_name "..."
    show player 12f
    player_name "Do que você está falando, {b}Clyde{/b}?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Ahem*{/b} Novamente..."
    clyde "Os nomes não {b}Clyde{/b}... Está {b}Cletus{/b}."
    show clyde 1
    show player 12f
    player_name "... Mas você parece {b}Roxxy's{/b} prima {b}Clyde{/b}."
    show player 5f
    show clyde 2
    clyde "Hmm, desculpe. Eu não sei isso {b}Clyde{/b} pessoa."
    show clyde 9 with dissolve
    clyde "Ele com certeza soa como um belo filho da puta!"
    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Você está brincando comigo agora?!"
    show player 13f
    show clyde 4
    clyde "Deixe-me perguntar isso..."
    clyde "Fez isso {b}Clyde{/b} usar um chapéu?"
    show clyde 3
    show player 10f
    player_name "... Não."
    show player 5f
    show clyde 4
    clyde "Bem, então lá vai você!"
    clyde "Como você pode ver... {b}Cletus{/b} nunca vai a lugar nenhum, sem o chapéu de confiança!"
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Isso é estranho."
    show player 12f
    player_name "eu vou."
    show player 5f
    show clyde 4
    clyde "Tudo bem. Bem, foi um prazer conhecê-lo, {b}[firstname]{/b}!"
    show clyde 3
    player_name "..."
    show player 92f
    player_name "Eu não te disse meu nome!"
    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Oh, err..."
    clyde "... Bem eu..."
    show clyde 11 with dissolve
    clyde "Umm... Telepatia!"
    show clyde 12
    show player 10f
    player_name "Hã?!"
    show player 5f
    show clyde 11
    clyde "I, {b}Cletus{/b}... Sou um telepata."
    show clyde 4 with dissolve
    clyde "... E eu leio seus pensamentos com balas mentais!"
    show clyde 3
    show player 10f
    player_name "Balas mentais?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Dat está certo, amigo!"
    show clyde 4 with dissolve
    clyde "Então não diga às pessoas que estou aqui."
    clyde "Porque eu vou saber..."
    clyde "Especialmente, se essas pessoas são o fuzz."
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Eu..."
    player_name "... Somente..."
    player_name "... Tchau."
    hide player with dissolve
    pause
    show clyde 4
    clyde "Até mais, amigo!"
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Posso ajudá-lo com algo'?"
    show clyde 1
    show player 10f
    player_name "Uhh, não?"
    show player 5f
    show clyde 22
    clyde "Oh cara. Você é um dos dem porta a porta, jesus te ama, pessoas?"
    show clyde 21
    show player 12f
    player_name "O que?! Não!"
    show player 5f
    show clyde 26
    clyde "{b}*Gasp*{/b} Você é um policial?!"
    clyde "Você tem que me dizer agora, é a lei!"
    show clyde 25
    show player 12f
    player_name "Não, cara ... Nos conhecemos na outra noite!"
    show player 5f
    clyde "..."
    show player 10f
    player_name "Eu estava ajudando {b}Roxxy{/b} com a lição de casa?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Oh, merda, sim!"
    clyde "Yer {b}Roxanne's{/b} novo namorado!"
    show clyde 3
    show player 10f
    player_name "Não, nós somos apenas-"
    show player 5f
    show clyde 4
    clyde "Como vai, irmão?!"
    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "O que há, irmão?!"
    show clyde 3
    show player 14f
    player_name "Oh, ei {b}Clyde{/b}..."
    show player 5f
    show clyde 4
    clyde "O que você está fazendo aqui??!"
    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "assim {b}Cletus{/b}, direita?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Dat está certo, amigo!"
    show clyde 4 with dissolve
    clyde "O que posso fazer??!"
    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{b}*Sigh*{/b} Eu estou bem."
    player_name "Como vai você?"
    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "Mais como, quem não sou eu!"
    clyde "Hahah, sabe o que eu quero dizer, irmão?!"
    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "'Porque eu estou tendo todo o sexo ... Com as mulheres..."
    clyde "{b}*Ahem*{/b} Senhoras humanas."
    show clyde 12
    show player 12f
    player_name "Sim, entendi, {b}Clyde{/b}..."
    show clyde 9 with dissolve
    clyde "Heh, sim você faz!"
    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "Eu nunca ouvi alguém falar do jeito que você faz, {b}Clyde{/b}..."
    show player 12f
    player_name "De onde você é??"
    show player 5f
    show clyde 4
    clyde "Isso porque todos vocês da cidade estão falando esquisitos!"
    clyde "Lá no Holler, todos falamos como dis..."
    show clyde 3
    show player 10f
    player_name "... O Holler?"
    show player 5f
    show clyde 4
    clyde "Sim."
    show clyde 3
    show player 10f
    player_name "O que é isso?!"
    show player 5f
    show clyde 4
    clyde "Uhh, onde eu cresci!"
    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "São apenas alguns condados ao norte daqui."
    clyde "Nas colinas."
    show clyde 3
    show player 10f
    player_name "Eu pensei que era tudo bosques no norte?"
    show player 5f
    show clyde 4
    clyde "Sim, bastante..."
    show clyde 3
    show player 12f
    player_name "As pessoas moram lá em cima?"
    show player 5f
    show clyde 4
    clyde "Psh, a maioria da minha família ainda vive aqui."
    clyde "Eu pensei em subir aqui com {b}Auntie Crystal{/b} para um feitiço."
    clyde "Dê um toque justo à vida da cidade."
    show clyde 3
    show player 10f
    player_name "Como isso está funcionando?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ehh, tem seus altos e baixos."
    clyde "Eu sinto falta do luar de volta para casa e toda a erva."
    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... Mas eu estou fazendo uma cozinhando aqui!"
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "O que você está cozinhando?"
    show player 5f
    show clyde 22
    clyde "Ehh... "
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Frango!"
    show clyde 4 with dissolve
    clyde "Heh, sim! Estou cozinhando tiras de frango frito!"
    clyde "Vocês da cidade simplesmente não conseguem o suficiente..."
    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "Eu deveria ir..."
    show player 5f with dissolve
    show clyde 4
    clyde "Sim, ok."
    clyde "Continue balançando, irmão!"
    clyde "Wooo!!"
    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "O que você tem aí??"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ehh, desculpa irmão."
    clyde "O barraco está estritamente fora dos limites!"
    show clyde 9 with dissolve
    clyde "A menos que você tenha peças femininas?!"
    show clyde 3 with dissolve
    show player 30f
    player_name "... Não."
    show player 5f
    show clyde 4
    clyde "Heh, lembre-se disso ... Se o barraco estiver balançando, é melhor não estar batendo'!"
    show clyde 9 with dissolve
    clyde "Sabe o que eu quero dizer?!"
    show clyde 3
    show player 401f
    player_name "... Sim. Eu gostaria de não ter..."
    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Agradavel trator."
    show player 13f
    show clyde 4
    clyde "Oh, sim!"
    clyde "É você {b}Big Bertha{/b}!"
    clyde "Ela não é uma beleza?!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Eu a construí a partir de sucatas, eu mesma."
    clyde "31,2 cavalos de potência, 2500 rpm, tanque de 8,5 galões..."
    clyde "... E basta olhar para esse acabamento vermelho rubi!"
    clyde "Mmm! Ela é a coisa mais sexy de quatro rodas!"
    show clyde 9 with dissolve
    clyde "Sabe o que eu quero dizer?"
    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "Na verdade, deixa pra lá."
    player_name "... Talvez outra hora?"
    show player 5f
    show clyde 4
    clyde "Psh, inferno sim, irmão!"
    clyde "Você sabe onde me encontrar."
    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "Vamos lá, {b}Clyde{/b}! Eu sei que é você!"
    show player 16f
    show clyde 4
    clyde "Eu não sei o que você está falando..."
    show clyde 3
    show player 15f
    player_name "Isso é estúpido, não vou contar a ninguém que você voltou..."
    show player 16f
    show clyde 4
    clyde "O que você está fumando, amigo?"
    show player 428f
    clyde "Os nomes {b}Cletus{/b} e esta é minha primeira vez aqui."
    clyde "Sempre."
    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "Ainda diz {b}Clyde{/b} acima da sua caixa de texto!"
    show player 403f
    show clyde 2 with dissolve
    clyde "Ei agora!"
    clyde "Não vá quebrar a quarta parede!"
    clyde "Isso é trapaça'!"
    clyde "O nome é {b}Cletus{/b}!!!"
    show clyde 26
    clyde "Diz!"
    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "Vamos lá, você sabe que quer dizer..."
    show clyde 1
    show player 24f
    player_name "{b}*Sigh*{/b}"
    show player 25f
    player_name "{b}Cletus{/b}."
    show player 24f
    show clyde 4 with dissolve
    clyde "Lá vai você!"
    clyde "Isso não era tão difícil agora, era??!"
    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
