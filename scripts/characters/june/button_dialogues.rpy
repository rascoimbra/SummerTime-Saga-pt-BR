label june_dialogue_bissette_fix_printer_repeat:
    scene computer_room_printer_c
    show xtra 40
    show june 17 at right
    show player 10 at left
    with dissolve
    player_name "Oi {b}June{/b}! Você já consertou a copiadora?"
    show player 5
    show june 19
    june "Não, desculpe. Não tive tempo de mexer com isso."
    show june 17
    player_name "..."
    show player 12
    player_name "Tecnologia estúpida!"
    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_first:
    scene computer_room_c
    show player 10 at left
    show june 1 at right
    with dissolve
    player_name "Oi, {b}June{/b}?"
    show player 5
    show june 3
    june "Sim, {b}[firstname]{/b}?"
    show june 2
    show player 12
    player_name "Estou tendo problemas com a impressora. O que significa carta de carregamento do PC?"
    show player 5
    show june 4
    june "Ugh, está fazendo isso de novo ?! Que pedaço de lixo!"
    show june 2
    show player 10
    player_name "Eu só preciso digitalizar algumas páginas deste livro e imprimi-las."
    player_name "Você poderia me ajudar?"
    show player 5
    show june 3
    june "Sim, claro!"
    june "Não para me gabar nem nada, mas eu sou muito bom em eletrônica."
    show june 2
    show player 14
    player_name "Incrível!"
    show player 13
    scene black with fade

    scene computer_room_printer_c
    show xtra 40
    show player 13 at left
    show june 9f at right
    with dissolve
    june "Ah, às vezes você só precisa reiniciá-lo. Deixe-me apenas ligar e desligar a energia."
    show june 10f with dissolve
    show player 108f
    player_name "Sério?"
    show player 5
    show june 9f with dissolve
    june "Sim, a tecnologia é exigente assim."
    june "Apenas esperando a inicialização ..."
    show player 10
    player_name "Tudo bem."
    show player 5
    pause
    pause
    show june 10f with dissolve
    show player 434
    june "Eu acho que deveria dar certo"
    show june 9f with dissolve
    show player 5
    june "Grr ... Erro no carregamento do PC ?!"
    show june 15 with dissolve
    show player 110f
    june "Seu pedaço inútil de"
    show june 16 with vpunch
    pause
    show june 15 with dissolve
    june "Acho que vou ter que abrir e consertar novamente."
    show player 10
    player_name "Quanto tempo isso levará?"
    show player 5
    show june 19 with dissolve
    june "Vai demorar um pouco, não tenho tempo para lidar com isso hoje."
    show june 17
    show player 10
    player_name "Sério?"
    show player 5
    show june 19
    june "Sim, essa coisa realmente é uma dor na bunda ..."
    show june 17
    show player 12
    player_name "Tecnologia estúpida!"
    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_fail:
    show player 519 with vpunch
    player_name "..."
    show player 10 with dissolve
    player_name "[str_warn]*Suspiro*"
    player_name "[str_warn]Acho que voltarei com você amanhã, então ..."
    show player 5
    show june 19
    june "[str_warn]Desculpe, {b}[firstname]{/b}."
    hide player
    hide june
    with dissolve
    return

label june_dialogue_bissette_fix_printer_pass:
    show player 519 with vpunch
    pause
    show player 11 with dissolve
    player_name "!!!"
    show june 18
    june "... Ei! Está funcionando!"
    show june 17
    show player 10
    player_name "Sério?"
    show player 5
    show june 18
    une "Sim! Você deve ter o toque midas, {b}[firstname]{/b}!"
    show june 17
    show player 14
    player_name "Hah, sim. Acho que sim ..."
    show player 13
    show june 18
    june "Bem, você pode copiar suas páginas agora ..."
    show june 17
    show player 14
    layer_name "Graças a Deus! Eu realmente preciso levar este livro para {b}Judith{/b} antes que ela fique chateada."
    player_name "Obrigado por toda a sua ajuda, {b}June{/b}!"
    show player 13
    show june 18
    june "Não tem problema."
    hide june with dissolve
    show player 518 with dissolve
    player_name "Imprimir!"
    show player 519 with vpunch
    show xtra_paper 39 at Position (xoffset=100) with dissolve
    pause .25
    hide xtra_paper 39 with dissolve
    show player 184 with dissolve
    pause

    show player 510 with dissolve
    player_name "Tudo bem! Eu finalmente tenho um dicionário completo de francês."
    player_name "Agora só preciso receber o livro de {b}Judith's{/b} para ela e posso começar com as aulas particulares de {b}Miss Bissette's{/b}."
    hide player with dissolve
    return

label june_dialogue_okita_faptic_engine:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "{b}Miss Okita{/b} quer que eu pegue algo chamado {b}Faptic Engine{/b} para ela. Ela me disse que você poderia ajudar?"
    show player 1
    show june 4
    june "O que diabos ela quer com um desses?"
    show player 2
    show june 2
    player_name "Ela diz que precisa dele para sua mais nova invenção."
    show player 1
    show june 4
    june "Hah. Que coisa maluca ela inventou dessa vez?"
    show player 2
    show june 2
    player_name "Parece muito legal, na verdade, é um"
    show player 1
    show june 3
    june "Não, não me diga! Eu tenho certeza, não quero saber."
    show player 11
    show june 2
    player_name "..."
    show player 10
    player_name "Você pode me ajudar ou não?"
    show player 11
    show june 4
    june "Duvido. Precisa ser autêntico?"
    show player 10
    show june 2
    player_name "Err, suponho que sim."
    show player 11
    show june 4
    june "Bem, isso vai ser difícil de encontrar."
    show player 10
    show june 2
    player_name "O que é um {b}Faptic Engine{/b} de qualquer maneira?"
    show player 11
    show june 3
    june "Oh, você não sabe?"
    june "É uma minúscula maquinaria que fornece sensações táteis. Eles começaram a colocá-los no topo dos smartphones inteligentes da linha".
    show player 10
    show june 2
    player_name "Sensações táteis?"
    show player 11
    show june 4
    june "Sensações que você sente com a pele. Nesse caso, vibrações."
    show player 2
    show june 2
    player_name "Oh, entendi agora."
    player_name "Então, por que é tão difícil conseguir?"
    show player 1
    show june 3
    june "Bem, deixando de lado o fato de que esses telefones são super caros ..."
    show player 11
    show june 4
    june "Atualmente, eles estão esgotados, como em qualquer lugar!"
    show player 10
    show june 2
    player_name "Quão caro estamos falando?"
    show player 11
    show june 4
    june "Cerca de $ 2000".
    show player 23
    show june 2
    player_name "( !!! )" with hpunch
    show player 10
    player_name "O quê !? Para um telefone !?"
    show player 11
    show june 4
    june "Eu disse que eles são os melhores da linha".
    show june 3
    june "Mas realmente não importa, você não me ouviu? Eles estão completamente esgotados."
    show player 10
    show june 2
    player_name "Bem, dispara! O que vou dizer à Okita?"
    show player 11
    show june 3
    june "É uma pena que ela queira ser autêntica. Há algumas versões de imitação de boa qualidade nas quais você pode conseguir."
    show player 10
    show june 2
    player_name "Hmm, funcionaria tão bem quanto os autênticos?"
    show player 11
    show june 4
    june "Bem, não, mas bem perto. Depende do que você está usando."
    show june 3
    june "Na maioria dos casos, eu diria que a imitação faria o truque."
    show june 2
    player_name "..."
    show player 10
    player_name "Tudo bem, onde eu pegaria a versão imitadora?"
    show player 11
    show june 3
    june "Bem, eles estavam colocando-os naqueles controladores {b}Master Blaster{/b} alguns anos atrás."
    show player 10
    show june 2
    player_name "{b}Master Blaster{/b}? Gosta do videogame?"
    show player 11
    show june 3b
    june "Sim! Eu sempre quis um, mas meus pais não podiam pagar."
    show player 2
    show june 2
    player_name "Você sabe o quê? Meu amigo {b}Erik{/b} costumava ter um desses!"
    show player 1
    show june 6
    june "Ele ainda o tem?"
    show player 2
    show june 5
    player_name "Não faço ideia."
    show player 1
    show june 6
    june "Bem, se você conseguir colocar uma mão em uma, eu posso levar o {b}Faptic Engine{/b} para você."
    show player 2
    show june 2
    player_name "Ótimo! Vou falar com {b}Erik{/b} e ver se ele ainda o possui."
    player_name "Obrigado pela informação, {b}June{/b}."
    show player 1
    show june 3
    june "Boa sorte!
    return

label june_dialogue_okita_get_controller_info:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "Qual era o nome desse controlador novamente?"
    show player 1
    show june 4
    june "{b}The Master Blaster{/b}."
    show june 3
    june "Você não disse que seu amigo {b}Erik{/b} tinha um?"
    show player 2
    show june 2
    player_name "Sim, ele costumava ..."
    player_name "Vou perguntar a ele sobre isso."
    player_name "Obrigado, {b}June{/b}."
    show player 1
    show june 3
    june "Boa sorte!"
    return

label june_dialogue_okita_has_controller:
    scene location_school_computer_day_blur
    show player 502 at left
    show june 2 at right
    with dissolve
    player_name "É sobre isso que você estava falando?"

    show player 1
    show june 11
    with dissolve
    june "Ei, você realmente conseguiu um. Incrível!"
    show player 2
    show june 12
    player_name "Então você pode tirar o {b}Faptic Engine{/b} disso?"
    show player 1
    show june 11
    june "Absolutamente".
    june "Apenas me dê alguns minutos para desmontá-lo."
    show player 2
    show june 12
    player_name "Tudo bem."
    show player 1
    show june 11

    june "Isso é tão legal!"

    pause
    scene location_school_computer_day_blur
    show player 1 at left
    show june 13 at right
    with dissolve
    june "Lá vamos nós, uma batida no {b}Faptic Engine.{/b}"
    show player 2
    show june 14
    player_name "É isso? É tão pequeno ..."
    show player 505
    show june 18
    with dissolve
    june "Sim, é uma coisinha, mas é um soco."
    show player 506
    show june 17
    player_name "Tudo bem, é melhor eu levar isso para Okita."
    show player 505
    show june 19
    june "Diga, {b}[firstname]{/b}?"
    june "Você se importaria se eu mantivesse o controle?"
    show player 2 with dissolve
    show june 17
    player_name "Não, de jeito nenhum. Bata-se!"
    show player 1
    show june 18
    june "Doce! Obrigado, {b}[firstname]{/b}!"
    return

label june_dialogue_mc_intro:
    show player 14 at left
    show june 5 at right
    player_name "Oi, {b}June{/b}!"
    show player 1
    show june 6
    june "Oi, {b}[firstname]{/b}!"
    june "O que houve?"
    show june 5
    return

label june_dialogue_intro:
    if player.location.is_here(M_erik):
        show erik 1b at Position (xpos=700)
    show june 1 at right
    show player 14 at left
    with dissolve
    player_name "Olá!"
    show june 3
    show player 1
    june "Ah, oi?"
    june "O que houve?"
    show june 2
    return

label june_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Ei, então uhh ..."
    player_name "Estou meio que ajudando a {b}Miss Okita{/b} com um projeto."
    show player 1
    show june 4
    june "{b}Miss Okita{/b} pediu ajuda para seus desenhos?"
    show player 10
    show june 2
    player_name "Sim".
    player_name "... E precisamos de algumas {b}lentes{/b}; como de um par de óculos?"
    show player 11
    show june 4
     june "Você quer meus óculos?"
    show player 10
    show june 2
    player_name "Bem, eu esperava que você tivesse um conjunto de reposição?"
    show player 11
    show june 4
    june "Não, apenas esse."
    show player 10
    show june 2
    player_name "Talvez eu possa convencê-lo a me dar esse par?"
    show player 11
    show june 4
    june "Eu duvido."
    show player 10
    show june 2
    player_name "Hmm, você tem míopia ou astigmatismo?"
    show player 11
    show june 3
    june "Míope."
    show player 29 with dissolve
    show june 2
    player_name "Oh, deixa pra lá então."
    player_name "Eu preciso de um par de alguém que seja ambos."
    show player 3
    show june 4
    june "Não acredito que a {b}Miss Okita{/b} pediu que {b}você{/b} ajudasse em seus projetos ..."
    show player 29
    show june 2
    player_name "Bem, ela está meio que me forçando ..."
    show player 3
    show june 6
    june "Sim, isso parece mais com ela."
    show june 3
    june "Bem, boa sorte."
    show player 2 with dissolve
    show june 2
    player_name "Sim, obrigado."
    return

label june_dialogue_ross_ask_model:
    show player 2
    player_name "Estou trabalhando em um projeto para a {b}Miss Ross{/b} e isso requer um modelo ativo."
    player_name "Você estaria interessada?"
    show player 1
    show june 3
    june "Modelagem?"
    show june 3b
    june "Eu pareço modelo para você?"
    show player 10
    show june 5
    player_name "Claro, por que não?"
    show player 11
    show june 3b
    june "Pfft, boa tentativa."
    show june 3
    june "Tenho outras coisas planejadas de qualquer maneira ..."
    show player 10
    show june 5
    player_name "Você sabe?"
    show june 3
    show player 11
    june "Sim, o pacote de expansão para o Orcette's Dungeon foi lançado hoje."
    june "É melhor você acreditar que estou recebendo uma cópia!"
    show player 10
    show june 5
    player_name "Tudo bem, divirta-se, eu acho."
    show player 11
    show june 3b
    june "Oh, eu irei!"
    return

label june_dialogue_hang_out:
    show player 14
    player_name "Eu queria saber se você gostaria de ir na minha casa?"
    show player 1
    show june 6
    june "Claro!"
    june "Depois da escola?"
    show player 14
    show june 5
    player_name "Sim".
    show player 1
    show june 6
    june "Então, seu quarto é então?"
    show player 10
    show june 5
    player_name "Meu quarto?"
    show player 11
    show june 6
    june "Sim! Precisamos de um lugar calmo e tranquilo para relaxar e jogar."
    show player 14
    show june 5
    player_name "Heh, okay!"
    show player 1
    show june 6
    june "Impressionante!"
    june "Eu tenho aulas chegando, eu devo ir."
    june "Vejo você depois da escola, {b}[firstname]{/b}!"
    return

label june_dialogue_cosplay_no_costume:
    show player 14
    player_name "Que cosplay você estava tentando fazer de novo?"
    show player 1
    show june 3
    june "Oh, é uma fantasia de orcette."
    june "Deveria ter dentes, colar e cinto!"
    show player 14
    show june 2
    player_name "Ah, certo!"
    player_name "Acho que conheço um lugar no {b}shopping{/b} que tem roupas ..."
    show player 1
    show june 6
    june "Ah, é?"
    show player 14
    show june 5
    player_name "Eu posso ir até lá e conferir!"
    show player 1
    show june 6
    june "Legal! Até mais."
    return

label june_dialogue_cosplay_has_costume:
    show player 17
    player_name "Acho que encontrei algo que você pode gostar!"
    show player 1
    show june 3
    june "Huh?"
    show june 6
    june "O que é isso?"
    show june 5
    show player 423 with fastdissolve
    player_name "É uma fantasia de orcette !!"
    show player 422
    show june 6
    june "Para o meu cosplay ?!"
    show player 1
    show june 7
    with fastdissolve
    pause
    show player 13
    show june 8
    june "Oh meu Deus !!"
    june "Tem todas as peças que faltava!"
    june "Aqueles até parecem dentes de verdade!"
    show player 17
    show june 5 with fastdissolve
    player_name "Estou feliz que você gostou."
    show player 14
    player_name "Vai ficar ótimo em você!"
    show player 1
    show june 6
    june "Muito obrigado, {b}[firstname]{/b}."
    show player 14
    show june 5
    player_name "Estou feliz que você tenha um ótimo cosplay na Comic Con."
    show player 11
    show june 6
    june "Eu provavelmente vou chamar muita atenção da multidão, tenho certeza!"
    show player 10
    show june 5
    player_name "Você quer dizer, pessoal?"
    show player 11
    show june 6
    june "Bem, eu acho, sim ..."
    show june 5
    player_name "..."
    show june 6
    june "Mas você sabe o que?"
    june "Acho que devo testar o cosplay antes de ir!"
    june "Talvez colocá-lo ... na frente de um amigo?"
    show june 5
    show player 10
    player_name "Como quem?"
    show player 11
    show june 6
    june "Você !! Parvo ..."
    show player 17
    show june 5
    player_name "Oh, ha ha!"
    show player 14
    player_name "Claro, eu poderia emm ... dar um feedback!"
    show player 1
    show june 6
    june "Ótimo! Que tal nos encontrarmos em sua casa ... Como da última vez?"
    show player 14
    show june 5
    player_name "Ok, vejo você depois da escola!"
    show player 1
    show june 6
    june "Até mais!"
    return

label june_dialogue_ask_about_class:
    show player 14
    player_name "Ei, em que classe você está?"
    player_name "Não vejo você na escola com frequência."
    show player 1
    show june 3
    june "Ah, eu não pratico esportes."
    june "Eu prefiro ficar por aqui ..."
    show player 14
    show june 2
    player_name "O que você faz na sala de computadores?"
    show player 1
    show june 3
    june "Você sabe, apenas coisas ... como navegar na internet ..."
    june "... participando de fóruns, assistindo a transmissões e jogando."
    show june 2
    show player 14
    player_name "Jogos, hein?"
    show player 1
    show june 3
    june "Sim".
    show june 1
    show player 14
    player_name "Como o que você está segurando?"
    show player 1
    show june 3
    june "Oh, essa coisa? É apenas um jogo bobo ..."
    show player 14
    show june 2
    player_name "Como se chama?"
    show player 1
    show june 3
    june "Chama-se Orc Bork."
    show player 14
    show june 2
    player_name "Um jogo sobre orcs?"
    show player 1
    show june 3
    june "Sim".
    show june 4
    june "É bem difícil."
    show player 11
    june "Estou tentando vencê-lo há meses ..."
    show player 14
    show june 2
    player_name "É realmente tão difícil?"
    show player 1
    show june 3
    june "Bem, é mais fácil quando você joga com dois jogadores."
    show june 4
    june "Eu não encontrei ninguém que jogue esse tipo de jogo na escola ..."
    show june 3
    june "A menos que você conheça alguém?"
    show june 1
    return

label june_dialogue_erik_help:
    show player 14
    player_name "Na verdade, sim!"
    player_name "Meu bom amigo {b}Erik{/b} ADORA jogos com orcs neles!"
    player_name "Especialmente ... os orcetes."
    player_name "Acho que vocês dois deveriam jogar juntos!"
    show player 1
    show june 3
    june "{b}Erik{/b}?"
    show player 11
    june "Acho que não o conheço ..."
    show player 10
    show june 1
    player_name "Ele disse que você pegou emprestado um de seus lápis uma vez."
    show player 1
    show june 4
    june "Huh..."
    show player 14
    show june 5
   player_name "Bem, ele passa muito tempo em seu quarto ... jogando jogos ..."
    show player 1
    show june 6
    june "Sério?"
    show player 14
    show june 5
    player_name "Acho que ele poderia ajudá-lo a vencer esse jogo."
    show player 1
    show june 6
    june "Isso seria incrível."
    june "Deixe-me saber se ele está pronto para isso!"
    show player 17
    show june 5
    player_name "Doce !!"
    show player 14
    player_name "Definitivamente vou avisá-lo."
    return

label june_dialogue_mc_help:
    show player 14
    player_name "Eu não sou muito bom nesses jogos ... Mas vou tentar!"
    show player 1
    show june 4
    june "Você ... quer brincar comigo?"
    june "Tem certeza de que gostaria disso?"
    show player 14
    show june 2
    player_name "Claro, por que não?"
    show player 11
    show june 3
    june "Bem, é só que ninguém nunca perguntou antes ..."
    show player 17
    show june 2
    player_name "Eu ficaria feliz em ser o seu primeiro!"
    show player 21
    show june 5
    player_name "Err ... quero dizer ... não gosto-"
    show player 11
    show june 6
    june "Ha ha, você é engraçado."
    show june 5
    player_name "..."
    show player 14
    player_name "Então ... você quer jogar agora?"
    show player 11
    show june 6
    june "Umm ... Que tal tocar em outro lugar?"
    june "Estou um pouco cansado de passar todo o meu tempo nesta sala de computadores ..."
    show player 14
    show june 5
    player_name "Ok, onde então?"
    show player 10
    player_name "Se jogarmos no corredor, {b}Annie{/b} nos dará detenção ..."
    show player 11
    show june 6
    june "Hmm ... Que tal brincar na sua casa?"
    show player 12
    show june 5
    player_name "Minha ... minha casa ?!"
    show player 11
    show june 6
    june "Sim!"
    june "Depois da escola?"
    show player 10
    show june 5
    player_name "Uhh ... acho que poderíamos?"
    show player 11
    show june 6
    june "Impressionante!"
    june "Obrigado por querer brincar comigo ..."
    show player 13
    june "É ... muito gentil da sua parte!"
    show player 14
    show june 5
    player_name "Oh, ha ha. Não é nada ..."
    show player 1
    show june 6
    june "Venha me perguntar quando estiver pronto para sair!"
    june "Estarei esperando aqui."
    show player 17
    show june 5
    player_name "Claro!"
    return

label june_dialogue_leave:
    show june 2 at right
    show player 14
    player_name "Oh, nada!"
    player_name "Apenas dizendo oi."
    show player 1
    show june 4
    june "Oh, tudo bem então ..."
    show june 1
    show player 29 at Position(xoffset=8)
    player_name "Err ... vejo você mais tarde!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
