label button_grace_mia_get_tattoo:
    scene tattoo_indoor_c
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    show tattoo_desk at right
    with dissolve
    grace "Hey lá!"
    grace "Você está aqui para uma consulta?"
    return

label button_grace_generic:
    show player 13 at left
    show grace f_normal_talk at right
    show tattoo_desk at right
    with dissolve
    grace "Hey lá!"
    grace "Você está aqui para uma consulta?"
    return

label button_grace_tattoo:
    show mia 10f
    mia "Eu gostaria de obter uma tatuagem ... Agora."
    show mia 7f
    show grace f_normal_talk
    grace "Agora ? Eu ver ..."
    show grace f_suspicious
    grace "Faça você tem um projeto em mente?"
    show grace f_normal
    show mia 30f at Position (xoffset=64) with dissolve
    mia "Meu amigo aqui desenhou isso para mim e eu gostaria que fosse feito hoje!"
    show mia 7f
    show grace f_normal_down_talk a_dressed_hip_paper
    with dissolve
    grace "Hmm..."
    show grace f_normal_talk
    grace "Tem você certeza que você quer este feito?"
    grace "As tatuagens são permanentes , de modo que eu tenho para fazer certeza meus clientes sabem o que eles estão ficando!"
    show grace f_normal
    show mia 10f
    mia "Eu tenho pensando sobre isso por um longo tempo e ... Sim, eu quero isso."
    show mia 7f
    show grace f_normal_talk
    grace "Tudo bem , querida . Mas , não é barato!"
    show grace f_normal
    show player 14
    player_name "Como muito é isso?"
    show player 13
    show grace f_normal_down_talk
    grace "Para esse tamanho ... com cores ... Em torno de {b}$400{/b}."
    show grace f_normal
    show player 22
    show mia 12f
    mia "!!!"
    mia "Droga ... acho que só tenho {b}$200{/b}..."
    show mia 8f
    show player 11
    player_name "..."
    show player 10
    player_name "Você não tem o suficiente?"
    show player 5
    show mia 12 with dissolve
    mia "Não, isso é tudo o que eu era capaz de salvar -se."
    mia "O que você acha que eu deveria fazer?"
    show mia 8
    return

label button_grace_tattoo_help:
    show player 14
    player_name "Eu vou cobrir o resto."
    show player 13
    show mia 12
    mia "Sério?!"
    show mia 7
    show player 14
    player_name "Por que não."
    player_name "Eu tenho sido trabalhando ultimamente assim que eu tiver algum dinheiro para gastar..."
    show player 17
    player_name "...E é por uma boa causa!"
    show player 13
    show mia 10
    mia "Isso é muito gentil da sua parte..."
    mia "...E eu vou fazer certo a pagar -lhe de volta!"
    show mia 7
    show player 17
    player_name "Está tudo bem , ha ha."
    show player 13
    show grace f_normal_talk
    grace "Então?"
    show mia 7f with dissolve
    grace "Pronto para começar?"
    show grace f_normal
    show mia 10f
    mia "Estou pronto!"
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve

    scene tattoo_cs01
    show text "Ele levou um enquanto {b}Grace{/b} ia para terminar o trabalho.\foi realmente nervoso para {b}Mia{/b}...\n...Mas , ela parecia a ser bem o tempo todo!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide tattoo_cs01
    with dissolve

    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    with dissolve
    grace "Tudo pronto!"
    grace "Espero que vocês gostem."
    show grace f_normal
    show mia 10f
    mia "É ótimo ! E ele não machucar como muito como eu pensava..."
    show mia 7f
    show grace f_normal_talk
    grace "certeza você deixar o curativo por pelo menos por alguns poucos dias."
    show grace f_normal
    show mia 10f
    mia "Ok, graças a você!"
    show mia 7f
    show grace f_normal_talk
    grace "Tchau, pessoal."
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 7 at right
    with dissolve
    show player 14
    player_name "Como se sente?"
    show player 13
    show mia 12
    mia "A tatuagem?"
    show mia 7
    show player 14
    player_name "Sim."
    show player 13
    show mia 12
    mia "Está tudo bem ... Só tem essa sensação de formigamento."
    show mia 10
    mia "E eu estou feliz que eu fiz isso ... Eu posso finalmente dizer que eu fiz algo que eu queria."
    show mia 7
    show player 10
    player_name "Tem você assustou sua mãe pode encontrar fora?"
    show player 5
    show mia 9
    mia "Espero que não , mas está em um local bem escondido , ha ha."
    show mia 7
    show player 17
    player_name "Eu acho que é legal que você fez isso."
    show player 18
    show mia 10
    mia "Graças, {b}[firstname]{/b}. Estou feliz que você veio com me."
    show player 13
    mia "Eu deveria ficar indo , embora . Antes de minha mãe começa a ficar desconfiado..."
    show mia 7
    show player 14
    player_name "Ok, vejo você na escola!"
    show player 13
    show mia 10
    mia "Tchau."
    hide player
    hide mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    show player 10
    player_name "Talvez nós deve vir de volta mais tarde?"
    show player 5
    mia "..."
    show mia 12
    mia "Suponho que deveríamos."
    show mia 8
    show player 10
    player_name "É tudo bem. Nós podemos sempre vir para trás outra vez."
    show player 5
    show mia 12
    mia "Você está certo."
    show mia 8
    show player 10
    player_name "Desculpe, você não conseguiu fazer sua tatuagem hoje..."
    show player 5
    show mia 12
    mia "Está tudo bem. Eu deveria chegar em casa agora."
    show mia 8
    show player 10
    player_name "Tudo bem , vejo você mais tarde."
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene location_tattoo_indoor_closeup
    show player 10 zorder 3 at left
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace f_normal zorder 0 at right
    player_name "Posso perguntar uma coisa?"
    show player 11
    show grace f_normal_talk
    grace "Claro!"
    show player 10
    show grace f_normal
    player_name "Bem , você vê..."
    show player 11
    pause
    show player 10
    player_name "A coisa é..."
    show player 11
    grace "..."
    show player 10
    player_name "... Aqui está a coisa..."
    show player 11
    show eve 2f zorder 2 at Position(xpos=0.35, ypos=1.0) with dissolve
    eve "Nossa , cuspir -lo já, {b}[firstname]{/b}!"
    show eve 1bf with dissolve
    eve "O que se, Raggedy Ann?"
    show eve 5f with dissolve
    show grace f_laugh
    grace "Heh , não muito."
    show grace f_normal_talk
    grace "Você está ficando sem problemas , punk?"
    show eve 6bf
    show grace f_normal
    eve "Claro que não."
    show player 1
    show eve 5f
    show grace f_laugh
    grace "Hehe."
    show eve 2f
    show grace f_normal
    eve "Veja, {b}[firstname]{/b} aqui precisa de um pouco de tinta."
    show eve 5f
    show grace f_normal_talk
    grace "Oh, você está pensando em fazer uma tatuagem?"
    show player 11
    show grace f_normal
    player_name "..."
    show eve 1bf with dissolve
    eve "Não, não, não. Ele precisa real de tinta ! Como em garrafas!"
    show eve 6bf
    eve "Desculpe , ela pode ser um pouco lenta."
    show eve 5f
    show grace f_suspicious
    grace "Ei ! Eu ouvi isso!"
    show eve 6f
    show grace f_normal
    eve "Sim , eu disse isso alto..."
    show eve 5f
    show grace f_laugh
    grace "Haha, pequena bunda."
    show eve 6f
    show grace f_normal
    eve "te amo!"
    show eve 5f
    show grace f_normal_talk
    grace "Sim , sim . Você é sortudo você é bonito."
    show player 1
    show grace f_normal
    show eve 1bf with dissolve
    eve "Eu sou , não sou?"
    show grace f_normal_talk
    show eve 5f with dissolve
    grace "Então, como muita tinta que você precisa, {b}[firstname]{/b}?"
    show player 2
    show grace f_normal
    player_name "Umm, eu sou não tenho certeza ."
    player_name "Apenas o suficiente para fazer uma pintura ."
    show player 1
    show grace f_normal_talk
    grace "Ahhh , um artista , hein ?"
    show grace f_laugh
    grace "Números, o primeiro cara que {b}Eve{/b} traz para casa é um artista."
    show player 11
    show grace f_normal
    show eve 6bf
    eve "Tch , melhor do que o que biker assustar você tinha pendurado em torno de aqui em alta escola."
    show eve 1f
    show grace f_laugh
    grace "Heh , você não terá argumentos lá..."
    show grace f_normal_talk
    grace "Será uma garrafa de cada primário cor ser o suficiente?"
    show grace f_suspicious
    grace "Eu suponho que você sabe como para misturar?"
    show player 10
    show grace f_normal
    player_name "Misturar?"
    show player 11
    show eve 2f
    eve "Sim , você sabe ? Azul e vermelho ficam roxos."
    eve "Amarelo e azul tornam verde."
    show player 2
    show eve 1f
    player_name "Ah , sim , como coisas sobre rodas coloridas , certo?"
    show player 1
    show grace f_normal_talk
    grace "Sim , exatamente."
    show grace f_suspicious
    grace "Eu acho que a única questão agora , é o que são você vai fazer por mim?"
    show grace f_normal
    show player 10
    player_name "Oh, uhh . Eu não sei ? O que é que você quer me a fazer?"
    show grace f_suspicious
    show player 11
    grace "Hmm , se você acontecer para perceber o grafite sobre o lado do edifício quando você chegou?"
    show player 10
    show grace f_normal
    player_name "... Sim , é muito difícil de perder."
    show player 11
    show grace f_normal_talk
    grace "Eu vou dar -lhe as tintas se você pode lavar -lo para mim."
    show grace f_normal
    show eve 2f
    eve "De verdade?"
    show player 2
    show eve 1f
    player_name "Eu posso fazer isso!"
    show player 1
    show eve 6bf
    grace "Pfft , o que um desperdício de tempo!"
    show eve 1f
    show player 11
    player_name "..."
    show eve 1bf with dissolve
    eve "É apenas vai ficar marcado de novo..."
    show eve 1f
    show grace f_angry_talk a_dressed_hips_mad
    with dissolve
    grace "Bem , ele é seus idiotas do caralho amigos que mantêm fazendo isso!"
    grace "Você precisa de dizer essas pequenas cadelas , eu vou gritar seus malditos jumentos se isso acontece de novo!"
    show grace f_angry
    show player 10
    player_name "Daaang , eu não sei a sua {b}irmã{/b} tem uma bunda pequena!"
    show eve 6f
    show player 11
    eve "Heh , você tem nenhuma idéia."
    show eve 5f
    show grace f_angry_talk
    grace "Eu não sei por que você pendurar para fora com essas douchebags de qualquer maneira..."
    show eve 2f
    show grace f_angry
    eve "... Se você está indo para chantagear {b}[firstname]{/b} para fazer as tarefas. Você podia pelo menos ter -lhe fazer algo útil."
    eve "Como se estivesse movendo toda aquela merda pesada que você pediu para a sala dos fundos?"
    show eve 6bf
    show grace f_normal a_dressed_hip with dissolve
    eve "Eu não quero quebrar minha vagina carregando essa merda!"
    show eve 5f
    show grace f_suspicious
    grace "Hum , acho que não é uma má idéia."
    show grace f_laugh
    grace "... Especialmente se ele recebe -lo a fechar -se sobre a sua vagina,! Ugh!"
    show grace f_normal
    show eve 6bf
    eve "... Vadia."
    show eve 5f
    show grace f_laugh
    grace "Hahaha , não fingir como você não ama o abuso."
    show grace f_normal
    show eve 6bf
    eve "Sim , sim..."
    show eve 2f
    eve "Se você me der licença, {b}[firstname]{/b}."
    show player 1
    eve "Eu melhor ir avisar os caras que {b}Grace{/b} é sobre a guerra caminho novamente."
    show eve 1f
    show grace f_laugh
    grace "Muito certo!"
    show grace f_normal
    show eve 6f
    eve "Veja!"
    hide eve
    with dissolve
    show grace f_normal_talk
    grace "Os {b}caixas estão direita na frente do balcão{/b}. Apenas {b} mover -los{/b} para a volta para mim e a pintura é sua."
    show grace f_normal
    show player 2
    player_name "Parece bom!"
    return

label button_grace_you_look_familiar:
    show player 10
    player_name "Você sabe ... eu acho..."
    show player 12
    player_name "Uhh."
    show player 34
    show grace f_suspicious
    grace "Está tudo bem?"
    show grace f_normal
    show player 30
    player_name "Desculpe , mas você parece ... familiar."
    show player 5
    show grace f_suspicious
    grace "Huh?"
    show grace f_normal_talk
    grace "Hmm ... Talvez você está pensando de minha irmã?"
    show grace f_normal
    show player 12
    player_name "Irmã?"
    show player 11
    show grace f_suspicious
    grace "Minha pequena irmã? {b}Eve{/b}?"
    show grace f_normal
    show player 38 with dissolve
    player_name "Oh! É claro!"
    show player 14 with dissolve
    player_name "Eu posso ver a conexão agora."
    show player 13
    show grace f_laugh
    grace "Ha ha."
    show grace f_normal_talk
    grace "De qualquer forma , é há nada que eu possa fazer por você?"
    return

label button_grace_nothing:
    show player 14
    player_name "Estou apenas olhando ao redor."
    show player 13
    show grace f_normal_talk
    grace "Legal! Dê uma olhada."
    grace "Eu faço todos os estilos e designs exibidos em minha loja!"
    grace "Apenas deixe -me saber se você nunca pensar sobre obter algo , e nós pode fazer uma nomeação!"
    show grace f_normal
    show player 14
    player_name "Ok, obrigado!"
    show player 13
    show grace f_normal_talk
    grace "Veja."
    hide grace
    hide mia
    hide player
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
