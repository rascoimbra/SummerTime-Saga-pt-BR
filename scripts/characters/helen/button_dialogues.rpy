label helen_dialogue_mia_route:
    show helen 50 at right
    show player 14 at left
    with dissolve
    player_name "olá, {b}Helen{/b}."
    show player 13
    show helen 51
    helen "olá, {b}[firstname]{/b}."
    show helen 50
    show player 14
    player_name "Como estão indo as coisas ultimamente?"
    show player 13
    show helen 51
    Helen "Muito melhor."
    helen "É tão bom saber que fui purificado."
    helen "O sacramento da igreja realmente ajudou a melhorar meu relacionamento com {b}Harold{/b}."
    show helen 24
    helen "Mas ... ninguém mais precisa saber sobre isso."
    show helen 50
    show player 21
    player_name "Heh ... Sim, suponho."
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "É um pouco embaçado, para mim..."
    show player 13
    hide xtra 21
    with dissolve
    show helen 51
     helen "Obrigado por sua ajuda novamente. Nossa família aprecia o que você fez ... e não fez."
    helen "Eu deveria deixar você ir. Você provavelmente quer sair com {b}Mia{/b}."
    show helen 50
    show player 14
    player_name "Sim."
    show player 36 with dissolve
    player_name "Vejo você mais tarde!"
    return

label helen_dialogue_helen_end_intro:
    show player 13 at left
    show helen 63 at right
    with dissolve
    helen "Olá, {b}[firstname]{/b}."
    show helen 62
    show player 14
    player_name "Olá, {b}Helen{/b}."
    show player 13
    show helen 63
    helen "Você veio para purificar meu corpo pecador?"
    show helen 62
    return

label helen_dialogue_helen_end_leave:
    show player 10
    player_name "Obrigado {b}Helen{/b}..."
    player_name "Talvez outra hora."
    show player 12
    player_name "Eu tenho ... outras coisas para fazer."
    show player 5
    show helen 48
    helen "Oh..."
    helen "Eu estava realmente esperando para servi-lo ..."
    helen "Não hesite em vir me visitar com mais frequência."
    show helen 47
    show player 12
    player_name "Claro ... informarei, {b}Helen{/b}."
    return

label helen_dialogue_helen_end_sex:
    show player 26
    player_name "Sim."
    show player 13
    show helen 63
    helen "Agradeço ao {b}Lord{/b}!"
    helen "Estive ocupado rezando para que você voltasse em breve."
    Helen "Tire suas roupas e eu deixarei entrar alguma luz."
    helen "Agora deite-se de costas para que eu possa deixar a luz de {b}God{/b} shine on me."
    hide helen
    scene mia_house_helen_window1
    show player helen_sex 59
    with fade
    pause
    scene mia_house_helen_window2
    show player helen_sex 59
    pause
    scene mia_house_helen_window3
    show player helen_sex 59
    show helen 54 with dissolve
    return

label helen_dialogue_change_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Olá, {b}Helen{/b}!"
    show player 5
    helen "..."
    show helen 3
    helen "Olá, {b}[firstname]{/b}."
    show helen 1
    show player 12
    player_name "Você parece estar com um humor melhor do que o normal!"
    show player 5
    show helen 2
    helen "Estou tentando ser ... de mente aberta ... mesmo com pessoas como você."
    show helen 1
    show player 14
    player_name "Isso é legal."
    show player 13
    show helen 2
    helen "O que você quer?"
    show helen 1
    return

label helen_dialogue_change_harold:
    show player 10
    player_name "Você falou com {b}Harold{/b}?"
    show player 11
    show helen 4
    helen "Não..."
    show helen 3
    helen "...Tudo está nas mãos de {b}God{/b}."
    show helen 1
    show player 12
    player_name "Huh?"
    show player 5
    show helen 4
    helen "Você deve sair agora..."
    return

label helen_dialogue_change_mia_clues:
    show player 10
    player_name "Onde você disse que eu poderia encontrar pistas sobre o paradeiro de {b}Harold's{/b}?"
    show player 5
    show helen 24 with dissolve
    helen "Comece interrogando seus colegas de trabalho na {b}delegacia{/b}..."
    helen "...E procure {b}pistas{/b} em torno de seu local de trabalho."
    show helen 23
    show player 12
    player_name "Suponho que posso pedir para ver onde ele poderia estar..."
    show player 5
    show helen 24
    helen "Obrigado..."
    return

label helen_dialogue_change_corset:
    show player 10
    player_name "Que tipo de lingerie você estava procurando de novo?"
    show player 5
    show helen 28
    helen "Sempre quis usar um espartilho... e {b}Harold{/b} adora me ver de vermelho."
    show helen 23
    show player 12
    player_name "{b}espartilho vermelho{/b}, então?"
    show player 5
    show helen 24
    helen "Se você puder encontrar um, traga de volta para mim."
    show helen 23
    show player 10
    player_name "Vou tentar..."
    show player 5
    show helen 28
    helen "Obrigado, {b}[firstname]{/b}."
    return

label helen_dialogue_change_angelica:
    show player 10
    player_name "Como está indo o sacramento?"
    player_name "Você e a {b}Irmã Angelica{/b} estão fazendo algum progresso?"
    show player 5
    show helen 27
    helen "..."
    show helen 24
    helen "Eu ... acho que estamos indo bem..."
    show helen 28
    helen "...{b}Irmã Angelica{/b} é muito ... completa e mais experiente que eu."
    show helen 23
    show player 10
    player_name "Entendo..."
    player_name "Bem, deixe-me saber se vocês precisam da minha ajuda!"
    return

label helen_dialogue_change_whipping:
    show player 10
    player_name "Você está bem? Ainda não acredito que vi {b}Irmã Angelica{/b} chicotear você."
    show player 5
    show helen 25
    helen "..."
    show helen 28
    helen "Estou um pouco dolorida, mas..."
    show helen 24
    helen "...eu sou um pecadora {b}[firstname]{/b}. Eu ... eu preciso disso."
    show helen 28
    helen "Se isso me ajudar a me livrar do meu pecado, devo fazê-lo."
    show helen 27
    show player 37 with dissolve
    player_name "..."
    show player 10 with dissolve
    player_name "Tudo bem, eu acho."
    player_name "Se você precisar de ajuda ou quiser sair, me avise."
    player_name "Farei tudo o que puder para ajudá-lo."
    show player 5
    show helen 24
    helen "Obrigado, {b}[firstname]{/b}. Você é muito útil."
    helen "{b}Irmã Angelica{/b} está me ajudando a ver que é a minha pecaminosidade que levou a todos os meus problemas na vida."
    helen "Eu preciso concluir este treinamento e talvez eu seja tão útil e gentil ... quanto você."
    show helen 27
    show player 37 with dissolve
    player_name "{b}Helen{/b}..."
    show helen 23
    show player 10 with dissolve
    player_name "Eu não acho que você é ruim."
    show player 5
    show helen 28
    helen "Obrigado, {b}[firstname]{/b}."
    return

label helen_dialogue_change_ritual:
    show player 10
    player_name "Você sabe ... tenho passado mais tempo na igreja ultimamente..."
    show player 5
    show helen 2
    helen "...Você tem?"
    show helen 1
    show player 14
    player_name "Sim!"
    show player 10
    player_name "Estou tentando aprender mais ... você sabe ... sobre {b}God{/b} e outras coisas!"
    show player 5
    show helen 2
    helen "Hmm... serio?"
    show helen 1
    show player 12
    player_name "Você sabia disso, err ... há um sacramento tarde da noite?"
    show player 5
    show helen 4
    helen "Serviços noturnos?"
    show helen 1
    show player 10
    player_name "Sim! Eles são como ... rituais?"
    show player 5
    show helen 4
    helen "Eu nunca tive consciência disso e frequento nossa igreja há mais de 20 anos."
    show helen 2
    helen "Como é que eu nunca ouvi falar de tal ... sacramento?"
    show helen 1
    return

label helen_dialogue_change_ritual_stat_fail:
    show player 10
    player_name "[chr_warn]Eu não tenho certeza se eu, emm ... eu realmente não posso explicar ..."
    show player 5
    show helen 4
    helen "[chr_warn]Parece que isso não é muito sério ..."
	show helen 1
    show player 24
    player_name "[chr_warn]..."
    show player 25
    player_name "[chr_warn]Bem, eu também não fui, então não sei muito sobre o que isso envolve."
    show player 24
    show helen 4
    helen "[chr_warn]Não sei se entendi bem o propósito disso tudo ..."
    show helen 2
    helen "[chr_warn]...Mas boa sorte com seu trabalho voluntário e me avise quando tiver mais detalhes."
    show helen 1
    show player 25
    player_name "[chr_warn]Oh... Ok."
    return

label helen_dialogue_change_ritual_stat_pass:
    show player 12
    player_name "{b}Irmã Angelica{/b} está no comando!"
    player_name "Ela disse que eu deveria espalhar a palavra e encontrar ... ehh ... seguidores fiéis para se juntar a nós!"
    show player 14
    player_name "u sei que você é extremamente devoto ..."..."
    show player 33
    player_name "layer_name "E com 20 anos na igreja, estou surpreso por você nunca ter freqüentado os sacramentos da noite. Talvez eu-"
    show helen 4
    helen "Espere."
    show helen 1
    show player 13
    player_name "..."
    show helen 4
    helen "Você está participando disso?"
    show helen 1
    show player 14
    player_name "Digamos que emm ... eu gosto de fazer trabalho voluntário para a igreja!"
    show player 13
    show helen 2
    helen "Eu tenho que dizer que estou agradavelmente surpreendido por sua devoção a nossa igreja..."
    show helen 4
    helen "...não sei se entendi bem o propósito de tudo isso."
    show helen 1
    show player 14
    player_name "{b}Irmã Angelica{/b} parece achar que essa é uma ótima maneira de absolver pecados e purificar a alma ..."..."
    show player 13
    show helen 3
    helen "Hmm..."
    show helen 2
    helen "É à noite, você diz?"
    show helen 1
    show player 14
    player_name "Sim, senhora! É ehh ... na câmara das freiras!"
    show player 13
    show helen 3
    Helen "Ok, você me convenceu."
    show helen 2
    helen "Vou com você visitar {b}Irmã Angelica{/b}  à noite e ver do que se trata..."
    show helen 1
    show player 14
    player_name "Isso parece ótimo!"
    return

label helen_dialogue_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Olá, {b}Helen{/b}!"
    show player 5
    show helen 4
    helen "Você de novo."
    helen "O que você quer ?!"
    show helen 1
    return

label helen_dialogue_harold:
    show player 10
    player_name "Você falou com {b}Harold{/b}?"
    show player 11
    show helen 5
    helen "Nossa situação não é da sua conta
    show helen 4
    Além disso, não há nada que possamos fazer no momento ..."
    show helen 3
    helen "...tudo está nas mãos de {b}God{/b}!"
    show helen 1
    show player 12
    player_name "Huh?"
    show player 5
    show helen 4
    helen "Você deve sair agora..."
    return

label helen_dialogue_leave:
    show player 5 at left
    show helen 2 at right
    with dissolve
    helen "!!!"
    show helen 4
    helen "O que você está fazendo aqui ?!
    show player 22
    helen Este é o meu quarto! Saia !"
    show helen 6
    show player 10
    player_name "Desculpe!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
