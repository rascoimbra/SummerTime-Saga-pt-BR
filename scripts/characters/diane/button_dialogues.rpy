label dianes_dialogue_daisy:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Como está indo a {b}Daisy{/b}?"
    show player 13
    show diane f_normal_talk
    dia "Oh, ela está muito bem!"
    dia "Meio engraçado que um produtor de leite encontraria uma vaca mágica, não é?"
    dia "Ainda bem que construí aquele celeiro ..."
    show diane f_normal
    pause
    show diane f_laugh
    dia "Ela é uma garota doce."
    show diane f_normal
    show player 14
    player_name "Sim, ela é."
    show player 13
    show diane f_normal_talk
    dia "Estou tão feliz que a encontramos."
    show diane f_normal
    return

label dianes_dialogue_cow_girl:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides
    with dissolve
    player_name "Algum progresso com o nosso novo amigo?"
    show player 5
    show diane f_shamed_talk_smile
    dia "{b}*Suspiro*{/b} Coitadinho."
    dia "Ela ainda está meio convencida de que seu mestre vai aparecer e puni-la por nos deixar vê-la."
    dia "O que quer que aquele homem horrível tenha feito com ela, ela não está pronta para falar sobre isso."
    show diane f_shamed
    show player 10
    player_name "Ela pelo menos deu o nome dela?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Não, ainda não."
    dia "Ela está voltando embora."
    dia "Eu imagino que não vai demorar até que ela esteja pronta para falar com você."
    show diane f_shamed
    show player 10
    player_name "Okay."
    show player 5
    return

label dianes_dialogue_milk_sample:
    scene expression player.location.background_blur with None
    show diane b_naked a_naked_sides
    show player 14 at left
    player_name "Posso ter uma pequena amostra do seu leite?"
    show player 13
    show diane f_smirk_talk
    dia "Hehe, com sede, não é?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "N-não, eu realmente só preciso de uma amostra."
    show player 13 with dissolve
    show diane f_surprised
    pause
    show diane f_shamed_talk
    dia "Oh."
    dia "Uhh, claro. Apenas me dê um segundo."
    if M_diane.outfit.get == "shirtless":
        show diane b_topless
    show diane a_squeeze3 f_down_front
    with dissolve
    pause
    show diane f_normal_talk a_bottle1 with dissolve
    dia dia "Isso vai funcionar?"
    show diane b_naked f_normal a_naked_sides with dissolve
    show player 713
    with dissolve
   player_name "Sim, isso é perfeito!"
    player_name "Obrigado, {b}Diane{/b}!"
    show diane f_normal_talk
    hide player with dissolve
    dia "Sem problema"
    show diane f_surprised
    pause
    show diane f_shamed_front
     dia "(O que ele está fazendo?)"
    hide diane with dissolve

    return

label dianes_dialogue_hows_baby_doing_boy:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Como ele está?"
    show player 13
    show diane f_normal_talk
    dia "Oh, ele é simplesmente maravilhoso!"
    dia "Eu nunca quero derrubá-lo."
    show diane f_normal
    show player 14
    player_name "Bem, você terá que acabar com ele eventualmente ..."
    show player 13
    show diane f_laugh
    dia "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_twins:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Como eles estão?"
    show player 13
    show diane f_normal_talk
    dia "Oh, eles são simplesmente maravilhosos!"
    dia "Eu nunca quero colocá-los para baixo."
    show diane f_normal
    show player 14
    player_name "Bem, você terá que acabar com eles eventualmente ..."
    show player 13
    show diane f_laugh
    dia "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_girl:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Como ela está?"
    show player 13
    show diane f_normal_talk
    dia "Oh, ela é simplesmente maravilhosa!"
    dia "Eu nunca quero colocá-la no chão."
    show diane f_normal
    show player 14
    player_name "Bem, você terá que acabar com ela eventualmente ..."
    show player 13
    show diane f_laugh
    dia "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_get_anything_baby:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Posso pegar algo para você?"
    show player 13
    show diane f_normal_talk
    dia "Não, eu estou bem."
    dia "Obrigado, garanhão."
    show diane f_normal
    show player 14
    player_name "De nada."
    show player 13
    show diane f_shamed_talk_smile
    dia "Não, obrigado, {b}[firstname]{/b}."
    dia "Para tudo."
    show diane f_shamed
    show player 14
    player_name "É um prazer, {b}Diane{/b}."
    show player 13
    return

label dianes_dialogue_baby_leave:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Vou deixar vocês em paz."
    show player 13
    show diane f_normal_talk
    dia "Tudo bem."
    show diane f_laugh
    dia "Diga adeus, papai."
    show diane f_cheese
    show player 17
    player_name "Hehe."
    show player 36 with dissolve
    if M_diane.pregnancy.baby_gender == "twins":
        player_name "Adeus, pequeninos."
    else:
        player_name "Adeus, pequena."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_gave_birth_intro:
    show player 14 at left
    show diane b_casual a_casual_baby
    with dissolve
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Shh, ele está dormindo."
    elif M_diane.pregnancy.baby_gender == "twins":
        dia "Shh, eles estão dormindo."
    else:
        dia "Shh, ela está dormindo."
    show diane f_normal
    show player 14
    player_name "Oh, desculpe."
    show player 13
    return

label dianes_dialogue_intro_kitchen:
    scene expression player.location.background_blur
    show player 14 at left
    show diane b_nightgown a_nightgown_water
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ei, {b}[firstname]{/b}."
    show diane f_normal
    show player 10
    player_name "Você está bem?"
    show player 5
    dia "Hmm?"
    show diane f_normal_talk
    dia "Sim, eu estou bem."
    show player 13
    dia "Eu estava com sede, então eu vim aqui para um copo de água."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Agora só estou pensando ..."
    show diane f_normal
    show player 14
    player_name "Pensando em quê?"
    show player 13
    show diane f_laugh
    dia "Hehe, eu não sei, coisas de trabalho, eu acho ..."
    show diane f_normal
    show player 14
    player_name "Tudo bem."
    show player 13
    return

label dianes_dialogue_hows_business:
    show player 14 at left
    show diane b_naked a_naked_sides
    player_name "Você já teve mais facilidade em acompanhar todos os seus pedidos agora?"
    show player 13
    show diane f_laugh
    dia "Oh meu, sim!"
    show diane f_normal_talk
    dia "Acho que meu suprimento de leite mais que dobrou desde o nascimento!"
    dia "A produção está indo muito bem agora."
    if M_diane.pregnancy.number_of_babies == 1:
        dia "Eu só tenho que ter certeza de deixar um pouco de leite para o pequeno."
        show diane f_laugh
        dia "Esse nosso filho está com tanta fome!"
    else:
        dia "Eu só tenho que ter certeza de deixar um pouco de leite para os pequenos."
        show diane f_laugh
        dia "Esses nossos filhos estão com tanta fome!"
    show diane f_normal
    show player 17
    player_name "Haha."
    show player 14
    player_name "Bem, esse seu leite é tão delicioso ... não posso culpá-los!"
    show player 13
    return

label dianes_dialogue_goodnight_1:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Eu estava indo para a cama."
    player_name "Você precisa de alguma coisa?"
    show player 13
    dia "Hmm?"
    show diane f_normal_talk
    dia "Oh, eu estou bem, garanhão."
    dia "Obrigado por perguntar."
    show diane f_normal
    show player 14
    player_name "Tudo bem então, boa noite."
    show player 13
    show diane f_normal_talk
    dia "Boa noite."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_goodnight_2:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Sim, está tudo bem."
    player_name "Desculpe acordar você."
    show player 13
    show diane f_normal_talk
    dia "Tudo bem."
    show diane f_normal
    show player 14
    player_name "Boa noite".
    show player 13
    show diane f_normal_talk
    dia "Boa noite, garanhão."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_what_up_to:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "O que você está fazendo?"
    show player 13
    show diane f_normal_talk
    dia "Oh, eu só estou sentado aqui entediado."
    dia "TV tarde da noite é uma merda."
    show diane f_normal
    show player 14
    player_name "Heh, isso é verdade!"
    show player 13
    show diane f_smirk_talk
    dia "Você quer fazer algo divertido?"
    show diane f_smirk
    show player 10
    player_name "O que você tinha em mente?"
    show player 13
    show diane f_smirk_talk
    dia "Mmm, eu posso pensar em algumas coisas ..."
    show diane f_smirk
    return

label dianes_dialogue_on_my_way_debbie:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Eu estava a caminho de ver {b}[deb_name]{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ahh, tudo bem."
    dia "Ela está no quarto dela."
    show diane f_normal
    show player 14
    player_name "Falo com você mais tarde, ok?"
    show player 13
    show diane f_normal_talk
    dia "Tudo bem."
    show diane f_normal
    hide player with dissolve
    pause
    show diane f_smirk_talk
    dia "Vocês dois se divertem."
    show diane f_laugh
    dia "Hehehe."
    hide diane with dissolve
    return

label dianes_dialogue_leave_d19_d20_day:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Eu deveria checar o jardim."
    show player 13
    show diane f_normal_talk
    dia "Ok".
    dia "Só não esqueça que eu preciso da sua ajuda também!"
    show diane f_normal
    show player 14
    player_name "Não vou".
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_business:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Os negócios estão crescendo!"
    dia "Eu mal consigo acompanhar todos os pedidos!"
    show diane f_normal
    show player 14
    player_name "Isso é bom, certo?"
    show player 13
    show diane f_normal_talk
    dia "Está muito bom."
    show diane f_laugh
    dia "Vou ter que começar a contratar mais peitos em breve."
    show diane f_cheese
    return

label dianes_dialogue_call_veronica:
    show player 10 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Você já conversou com {b}Veronica{/b} yet?"
    show player 13
    show diane f_sad_talk
    dia "Não, ainda não."
    show diane f_normal_talk
    dia "Eu vou embora."
    show diane f_normal
    show player 14
    player_name "Ela realmente gostaria de trabalhar para você."
    show player 13
    show diane f_laugh
    dia "Sim, vamos ver."
    show diane f_cheese
    return

label dianes_dialogue_what_are_you_up_to:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "O que você está fazendo?"
    show player 13
    show diane f_normal_talk
    dia "Oh, apenas assistindo TV e bebendo um pouco do delicioso vinho de {b}[deb_name]'s{/b} delicious wine."
    dia "É tão bom ter colegas de quarto novamente."
    show diane f_normal
    show player 14
    player_name "É?"
    show player 13
    show diane f_normal_talk
    dia "Claro!"
    dia "Eu estava tão sozinha ali naquela casa grande sozinha."
    show diane f_normal
    show player 14
    player_name "Sim, eu posso imaginar."
    show player 13
    show diane f_normal_talk
    dia "Agora sinto que faço parte de uma família novamente."
    show diane f_normal
    show player 14
    player_name "Você faz parte da nossa família {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Aww, obrigado lindo."
    show diane f_normal
    return

label dianes_dialogue_wheres_debname:
    show player 10 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Ela não costuma sentar aqui com você?"
    show player 13
    show diane f_normal_talk
    dia "Ela foi dormir cedo esta noite ..."
    dia "... Disse que estava cansada."
    show diane f_normal
    show player 14
    player_name "Ah, entendi."
    show player 13
    show diane f_normal_talk
    dia "Você ainda pode ir vê-la se quiser, tenho certeza que ela não se importaria."
    show diane f_normal
    show player 14
    player_name "sim, talvez ..."
    show player 13
    return

label dianes_dialogue_love_that_nightgown:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Parece incrível para você!"
    show player 13
    show diane f_laugh a_nightgown_hip with dissolve
    dia "Hehe, obrigado!"
    show diane f_reading_intrigued
    dia "Eu estava preocupado que isso pudesse ser um pouco inadequado, mas, considerando o que {b}[deb_name]{/b} e {b}[jen_name]{/b} se destacam em ..."
    show diane f_normal
    show player 14
    player_name "Heh, sim."
    show player 426
    pause
    show diane f_smirk_talk
    dia "Hehe, você ainda está comigo bonito?"
    show diane f_smirk
    player_name "Hmm?"
    show player 29 with dissolve
    player_name "Oh, desculpe!"
    show player 3
    show diane f_smirk_talk
    dia "Haha, está tudo bem."
    dia "Você pode olhar."
    show diane f_smirk
    show player 426 with dissolve
    pause
    pause
    show player 403
    show diane a_nightgown_sides with dissolve
    return

label dianes_dialogue_goodnight:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Eu provavelmente deveria ir para a cama."
    show player 13
    show diane f_normal_talk
    dia "Sim, eu também."
    show diane f_normal
    show player 14
    player_name "Boa noite, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Boa noite, lindo."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_couch:
    show player 14 at left
    show diane f_normal b_shirtless a_shirtless_sides
    player_name "Você está dormindo bem?"
    show player 13
    show diane f_normal_talk
    dia "Oh, tudo bem."
    dia "Um pouco irregular, mas eu vou conseguir."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Você quer ouvir algo estranho?"
    show diane f_normal
    show player 14
    player_name "Claro".
    show player 13
    show diane f_normal_talk
    dia "{b}[jen_name]{/b} continua descendo no meio da noite e bufando quando ela me encontra deitada lá."
    dia "Então, quando pergunto o que ela precisa, ela revira os olhos e sai murmurando algo sobre desperdiçar dinheiro."
    dia "Alguma idéia do que se trata?"
    show diane f_normal
    show player 29 with dissolve
    player_name "Eu uhh-"
    show player 3
    show diane f_normal_talk
    dia "O que ela poderia querer na sala no meio da noite?"
    show diane f_normal
    pause
    show player 10 with dissolve
    player_name "Não faço ideia."
    show player 5
    show diane f_thinking
    dia "{b}*Sigh*{/b} Provavelmente apenas a maneira dela de tentar me irritar."
    show diane f_normal
    show player 14
    player_name "Heh sim, provavelmente ..."
    show player 13
    show diane f_annoyed_talk
    dia "Ela é uma vadia."
    show diane f_cheese
    return

label dianes_dialogue_feeling_better:
    show player 14 at left
    show diane f_normal
    player_name "Como você está se sentindo?"
    show player 13
    show diane f_laugh
    dia "Oh, muito melhor agora que você está me ajudando a bombear!"
    show diane f_smirk_talk
    dia "Obrigado por isso, {b}[firstname]{/b}."
    show diane f_smirk
    show player 14
     player_name "De nada."
    player_name "Apenas descanse bastante, ok?"
    show player 13
    show diane f_laugh
    dia "Haha, tudo bem, pai!"
    show diane f_cheese
    show player 17
    player_name "Haha!"
    show player 13
    show diane f_smirk
    return

label dianes_dialogue_like_working_for_you:
    show player 14 at left
    show diane f_normal
    player_name "Você sabe, eu realmente gosto deste trabalho {b}Diane{/b}."
    show player 13
    show diane f_laugh
    dia "Hah, aposto que sim!"
    if M_diane.outfit.get == "dressed":
        show diane f_smirk_talk a_dressed_finger with dissolve
    else:
        show diane f_smirk_talk
    dia "Que jovem não gostaria de lidar com os seios o dia todo?"
    if M_diane.outfit.get == "dressed":
        show diane f_smirk a_dressed_shovel with dissolve
    else:
        show diane f_smirk
    show player 14
    player_name "Não é isso que eu-"
    player_name "Heh, eu quero dizer ... Essa parte é incrível."
    show player 401
    player_name "Você tem ótimos peitos."
    show player 403
    show diane f_smirk_talk
    dia "Uh huh."
    show diane f_smirk
    show player 14
    player_name "... Mas não é só isso!"
    player_name "É bom cuidar de você."
    player_name "Eu gosto."
    show player 13
    if M_diane.outfit.get == "dressed":
        show diane f_smirk_talk a_dressed_blush with dissolve
    else:
        show diane f_smirk_talk
    dia "Aww."
    dia "Eu também gosto, {b}[firstname]{/b}."
    if M_diane.outfit.get == "dressed":
        show diane f_smirk a_dressed_shovel with dissolve
    else:
        show diane f_smirk
    pause
    show diane f_smirk_talk
    dia "Apenas não diga a {b}[deb_name]{/b}!"
    show diane f_smirk
    show player 14
    player_name "Não se preocupe, não vou."
    show player 403
    return

label dianes_dialogue_leave_d12b:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "É melhor eu voltar a isso."
    show player 13
    show diane f_normal_talk
    dia "Tudo bem."
    dia "Se você precisar de alguma coisa, sabe onde me encontrar."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_have_you_spoken_with_debname:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Você falou com {b}[deb_name]{/b} recentemente?"
    show player 13
    show diane f_tired_talk
    dia "Oh, o tempo todo!"
    dia "Estamos de volta aos telefonemas diários novamente."
    show diane f_tired
    show player 14
    player_name "Isso é legal."
    show player 13
    show diane f_tired_talk
    dia "Tem sido maravilhoso!"
    dia "Eu senti tanto a falta dela!"
    show diane f_tired
    show player 14
    player_name "Bem, ela também sentiu sua falta."
    player_name "Todos nós fizemos, realmente."
    show player 13
    show diane f_tired_talk
    dia "Aww."
    hide player
    if M_diane.outfit.get == "dressed":
        show diane kiss
    else:
        show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    return

label dianes_dialogue_about_veronica:
    show player 12 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Então, como você conheceu a garota {b}Veronica{/b}?"
    show player 13
    show diane f_tired_talk
    dia "Você quer dizer {b}Vee{/b}?"
    dia "Oh, eu amo essa garota!"
    dia "Nos conhecemos na seção de jardinagem de {b}Consum-R{/b}, alguns anos atrás."
    dia "Ela acabara de se mudar para cá do país e não conhecia ninguém."
    show diane f_tired
    show player 14
    player_name "Aposto que foi difícil."
    show player 13
    show diane f_tired_talk
    dia "Ah, com certeza foi."
    dia "Ela estava uma bagunça!"
    dia "Eu me ofereci para mostrar aos pobres queridos da cidade em troca de alguns conselhos de jardinagem e nós meio que nos damos bem".
    show diane f_tired
    show player 14
    player_name "Isso foi legal da sua parte."
    show player 13
    show diane f_tired_talk
    dia "Sim, eu acho."
    dia "Sinceramente, eu também precisava de um amigo."
    dia "O que comh {b}[deb_name]{/b} sendo tão envolvido com {b}seu pai{/b}  tudo mais."
    show diane f_tired
    show player 5
    player_name "..."
    pause
    show diane f_tired_talk
    dia "Oh, me desculpe, lindo!"
    dia "Eu não quis que isso soasse ruim."
    show diane f_tired
    show player 10
    player_name "Sim, eu sei que você não."
    show player 5
    show diane f_tired_talk
    dia "Seu {b}pai{/b} era um homem bom, eu sempre gostei dele."
    show diane f_tired
    show player 10
    player_name "Obrigado."
    show player 5
    return

label dianes_dialogue_hows_the_garden_2:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Então, eu estou realmente bem com o jardim?"
    show player 13
    show diane f_tired_talk
    dia "Você está indo melhor do que tudo bem!"
    dia "Eu nunca vi meu jardim tão bonito!"
    dia "Eu posso ter os melhores pepinos em toda a terra!"
    show diane f_tired
    show player 14
    player_name "Hah, eu não sei sobre isso ..."
    player_name "Estou feliz que tenha ficado tão bem."
    show player 13
    return

label dianes_dialogue_take_it_easy:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Tudo bem, acho que devo voltar ao trabalho."
    show player 10
    player_name "Vá com calma, ok?"
    player_name "Eu me preocupo com você se esforçando demais."
    show player 5
    show diane f_tired_talk
    dia "Psh, você soa como {b}[deb_name]{/b}..."
    dia "Eu vou ficar bem."
    show diane f_tired
    show player 10
    player_name "Okay..."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_about_debname:
    show player 14 at left
    show diane f_normal
    player_name "Estou feliz que você esteja passando um tempo com {b}[deb_name]{/b} novamente."
    player_name "Eu sei que ela está sentindo falta da sua empresa."
    show player 13
    show diane f_normal_talk a_dressed_blush with dissolve
    dia "Aww e eu senti falta dela!"
    show diane a_dressed_shovel with dissolve
    dia "Éramos inseparáveis ​​em nossa juventude, sabia?"
    show diane f_normal
    show player 14
    player_name "Sim, eu ouvi as histórias."
    show player 13
    show diane f_laugh
    dia "Hah!"
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Bem, espero que ela não tenha contado todas as histórias!"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 10
    player_name "Huh?"
    show player 13
    show diane f_laugh
    dia "Hehe, deixa pra lá."
    show diane f_normal
    show player 14
    player_name "Ainda não consigo superar o quanto vocês são parecidos ..."
    show player 13
    show diane f_normal_talk
    dia "Sim, costumávamos fazer isso o tempo todo."
    dia "Eles nos chamavam de gêmeos na faculdade."
    show diane f_normal
    show player 14
    player_name "Eu posso ver isso."
    show player 13
    show diane f_normal_talk
    dia "Eu era a selvagem e ela era a linda!"
    show diane f_normal
    show player 29 with dissolve
    player_name "Eu acho que vocês dois são bonitos, {b}Diane{/b}."
    show player 3
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "Aww, obrigado lindo."
    show diane f_normal a_dressed_shovel with dissolve
    show player 13 with dissolve
    return

label dianes_dialogue_hows_the_garden:
    show player 14 at left
    show diane f_normal
    player_name "Então, como está o seu jardim?"
    show player 13
    show diane f_sad_talk
    dia "Definitivamente já viu dias melhores ..."
    dia "Ultimamente tenho me preocupado tanto com o trabalho ao lado que temo que meu jardim não receba a atenção que merece."
    show diane f_normal_talk
    dia "É por isso que fiquei tão animado quando {b}[deb_name]{/b} disse que você poderia me ajudar neste verão."
    show diane f_normal
    show player 14
    player_name "Estou feliz em ajudar, {b}Diane{/b}!"
    show player 13
    return

label dianes_dialogue_what_have_you_been_up_to:
    show player 14 at left
    show diane f_normal
    player_name "Então, o que você tem feito consigo mesmo nos últimos anos?"
    show player 13
    show diane f_normal_talk
    dia "Ah, não muito mesmo ..."
    show diane f_normal
    show player 14
    player_name "Não muito ?!"
    player_name "Eu pensei que você estivesse lá fora festejando como um louco e sendo perseguido por homens ricos?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Haha, Deus não!"
    dia "O que lhe deu essa idéia?"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Bem, {b}[deb_name]{/b} sempre diz que você é louco."
    show player 13
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Bem, talvez na minha juventude ..."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "Honestamente, desde o divórcio, passo a maior parte do meu tempo aqui neste jardim."
    show diane f_normal
    show player 14
    p player_name "Você quer dizer que não sai mais?"
    show player 13
    show diane f_normal_talk
    dia "Ocasionalmente vou tomar um drinque com minha amiga {b}Veronica{/b}."
     dia "Nada muito emocionante."
    show diane f_normal
    show player 14
    player_name "Você não sente falta?"
    show player 13
    show diane f_normal_talk
    dia "Hmm, às vezes."
    dia "Estou velho demais para esse tipo de vida agora."
    show diane f_smirk_talk
    dia "Além disso, não há homens bons nesta cidade."
    show diane f_smirk
    show player 12
    player_name "Sério ?!"
    show player 13
    show diane f_laugh
    dia "Heh, confie em mim."
    show diane f_smirk_talk
    dia "Na minha idade, a única coisa que resta são os resíduos."
    show diane f_smirk
    show player 10
    player_name "Que chatice".
    show player 5
    return

label dianes_dialogue_intro_d1_d6:
    show player 13 at left
    show diane f_normal_talk
    with dissolve
    dia "Olá, {b}[firstname]{/b}!"
     dia "Estou tão feliz que você decidiu vir e me ajudar."
    show diane f_normal
    show player 14
    player_name "Sim, não há problema {b}Diane{/b}."
    player_name "Obrigado por me pagar!"
    show player 13
    show diane f_laugh
    dia "Hehe, meu prazer é lindo."
    show diane f_normal
    return

label dianes_dialogue_intro_d7_d12:
    show player 5 at left
    show diane f_tired_talk b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    dia "Ei, {b}[firstname]{/b}."
    dia "Meu jardim está realmente parecendo-"
    dia "* bocejo *"
     dia "... Muito bom."
    show diane f_tired
    show player 10
    player_name "Você está bem, {b}Diane{/b}?"
    show player 5
    show diane f_tired_talk
    dia "Sim, eu estou bem."
    dia "Apenas cansado."
    show diane f_tired
    return

label dianes_dialogue_intro_d12b_d15:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Olá, lindo!"
    show diane f_normal
    show player 14
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Você precisa de algo?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_barn:
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides
    with dissolve
    dia "Olá, garanhão!"
    show diane f_normal
    show player 14
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Você está pronto para trabalhar?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_couch:
    show player 13 at left
    show diane f_normal_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Olá, garanhão!"
    show diane f_normal
    show player 14
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Você está indo para a cama?"
    show diane f_normal
    show player 14
    player_name "Sim, em alguns minutos."
    show player 13
    return

label dianes_dialogue_intro_d19_d20_barn:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Olá, garanhão!"
    show diane f_normal
    show player 14
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Você está pronto para trabalhar?"
    show diane f_normal
    return

label dianes_dialogue_intro_d19_couch:
    show player 13 at left
    show diane f_smirk_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Olá, garanhão!"
    show diane f_smirk
    show player 14
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Você está procurando por mim ou {b}[deb_name]{/b}?"
    show diane f_normal
    return

label dianes_dialogue_intro_d20_couch:
    show player 13 at left
    show diane f_normal_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Hmm, {b}[firstname]{/b}?"
    show diane f_normal
    show player 14
    player_name "Ei, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Está tudo bem?"
    show diane f_normal
    return

label dianes_dialogue_ready_to_pump:
    show player 14 at left


    show diane f_normal b_naked a_naked_sides
    with dissolve
    player_name "Você está pronto para bombear?"
    show player 13
    show diane f_normal_talk
    dia "Absolutamente".
    dia "Apenas me dê um segundo para configurar."
    hide diane with dissolve
    show player 14
    player_name "Tudo bem."
    return

label dianes_dialogue_hows_the_baby_pregnancy_1:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Oh, ainda não há muito a relatar."
    dia "A menos que você esteja interessado em ouvir sobre minha doença da manhã?"
    show diane f_normal
    show player 10
    player_name "Bem, se você quiser falar sobre isso, nós podemos?"
    show player 13
    show diane f_laugh
    dia "Haha, oh Deus, não!"
    show diane f_normal_talk
    dia "Eu aprecio que você pergunte."
    dia "Obrigado, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_2:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Oh, ainda não há muito a relatar."
    dia "A menos que você esteja interessado em ouvir sobre minha doença da manhã?"
    show diane f_normal
    show player 10
    player_name "Bem, se você quiser falar sobre isso, podemos?"
    show player 13
    show diane f_laugh
    dia "Haha, oh Deus, não!"
    show diane f_normal_talk
    dia "Eu aprecio que você pergunte."
    dia "Obrigado, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_3:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Heh, meus peitos estão tão inchados!"
    dia "Eles parecem maiores para você?"
    show diane f_normal
    show player 26
    player_name "Não sei, eles eram muito grandes para começar ..."
    show player 18
    show diane f_normal_talk
    dia "Oh, vamos lá!"
    show player 13
    dia "Eles são definitivamente maiores!"
    show diane f_normal
    pause
    show player 14
    player_name "Eu simplesmente amo seu bebê!"
    show player 13
    show diane f_laugh a_touch_belly with dissolve
    dia "Hehe, eu sei!"
    show diane f_normal_talk
    dia "Não é adorável?"
    show diane f_normal
    pause
    show diane f_normal_talk a_naked_sides with dissolve
    dia "Obrigado por entrar em contato comigo, {b}[firstname]{/b}."
    show diane f_normal
    show player 14
    player_name "Claro."
    player_name "Mal posso esperar para conhecer nosso bebê, {b}Diane{/b}!"
    show player 13
    show diane f_normal_talk
    dia "Aww, você é o homem mais doce do mundo!"
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_4:
    show player 13 at left
    show diane f_tired_talk b_naked a_naked_sides
    with dissolve
    dia "Ugh, estou exausta ..."
    show player 5
    dia "Meus pés estão me matando, pareço uma baleia e meus seios nunca param de vazar!"
    show diane f_tired
    show player 10
    player_name "... Oh."
    show player 5
    show diane f_laugh
    dia "Hehe, mas está tudo bem."
    show diane f_normal_talk a_touch_belly with dissolve
    dia "Eu vou ser mamãe muito em breve!"
    show diane f_normal
    show player 14
    player_name "Está certo, você está!"
    show player 13
    show diane f_normal_talk
    dia "Estou tão empolgado, {b}[firstname]{/b}!"
    dia "Mal posso esperar para segurar nosso filho nos meus braços!"
    show diane f_normal
    show player 14
    player_name "Sim, eu também."
    show player 13
    show diane a_naked_sides
    with dissolve
    return

label dianes_dialogue_breeding_session:
    show player 13 at left
    show diane b_naked a_naked_sides f_smirk_talk
    with dissolve
    dia "Você está pronto para começar?"
    show diane f_smirk
    show player 14
    player_name "C-certa".
    show player 13
    show diane f_smirk_talk
    dia "Graças a Deus!"
    dia "Estou ficando tão molhada só de pensar em que você está colocando um bebê dentro de mim ..."
    show diane f_smirk
    show player 10
    player_name "Você é ?!"
    hide player
    show diane b_pull_mc_naked f_empty a_empty
    with dissolve
    dia "Mmm, eu preciso tanto disso, {b}[firstname]{/b}!"
    hide diane
    with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed_mc
    show diane_sex_breed pre_talk
    with dissolve
    dia "É isso aí, garanhão."
    dia "Dê para mim."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Ahh!!"
    return

label dianes_dialogue_cow_suit:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Eu queria falar com você sobre sua roupa de vaca ..."
    show player 13
    show diane f_normal_talk
    dia "Oh?"
    show diane f_normal
    menu:
        "Put it back on." if M_diane.outfit.get == "naked":
            show player 14 at left
            show diane f_normal
            player_name "Eu quero que você use enquanto eu procrio você."
            player_name "É tão sexy!"
            show player 13
            show diane f_laugh
            dia "Oh, eu estou tão feliz que você pensa assim!"
            show diane f_normal_talk
            dia "Eu também adoro!"
            show diane f_smirk_talk
            dia "Parece certo, sabia?"
            dia "Vestindo aqui."
            show diane f_smirk
            show player 14
            player_name "Sim, totalmente."
            hide diane
            with dissolve
            $ M_diane.outfit.is_naked = 0
            $ M_diane.outfit.set_default_outfit_schedule([["cow","cow","nightgown","nightgown"]])

        "Could you remove it?" if not M_diane.outfit.get == "naked":
            show player 14 at left
            show diane f_normal
            player_name "Prefiro deixá-lo completamente nu."
            show player 13
            show diane f_smirk_talk
            dia "Você faria ?!"
            dia "Mmm, seu menino travesso ..."
            show diane f_smirk
            pause
            show diane f_smirk_talk
            dia "Eu posso tirar, se é isso que você realmente quer."
            dia "O que quer que ajude você a colocar um bebê na minha barriga."
            hide diane
            with dissolve
            $ M_diane.outfit.set_default_outfit_schedule([["naked","naked","nightgown","nightgown"]])
    return

label dianes_dialogue_dump_pump:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_sides
    with dissolve
    player_name "O que eu preciso fazer de novo?"
    show player 13
    show diane f_normal_talk
    dia "Hmm?"
    dia dia "Oh, {b} apenas entre no galpão e jogue o que está na bomba em um jarro de armazenamento.{/b}"
    show diane f_normal
    show player 14
    player_name "Certo!"
    player_name "Estou nisso!"
    hide player
    hide diane with dissolve
    return

label dianes_dialogue_daylight_drinking:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "Como você está indo por aqui?"
    show player 426
    show diane f_laying_laugh
    dia "Mmm, fantástico!"
    show diane f_laying_smirk_up
    show player 429
    player_name "Posso pegar algo para você?"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Eu não diria não a uma bebida."
    show diane f_laying_smirk_up
    show player 429
    player_name "Seu desejo é meu comando!"
    player_name "Que tipo de bebida você quer?"
    show player 426
    $ randomdrink = M_diane.get("random drink")
    show diane f_laying_thinking
    dia "Que tal um {b}[randomdrink]{/b}?"
    show diane f_laying_smirk_up
    show player 427
    player_name "{b}[randomdrink]{/b}?!"
    player_name "Eu nunca fiz nada assim antes ..."
    show player 426
    show diane f_laying_laugh
    dia "Hehe, não se preocupe. Eu farei."
    show diane f_laying_smirk_up
    show player 429
    player_name "Não! Eu posso descobrir."
    player_name "Você relaxa no seu dia de folga!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Você tem certeza?"
    show diane f_laying_smirk_up
    show player 429
    player_name "Positivo!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Ok. Bem, {b}a receita está dentro de um bloco de notas ao lado do mixer.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "Entendi!"
    player_name "Um {b}[randomdrink]{/b}, chegando logo!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_make_drink:
    $ randomdrink = M_diane.get("random drink")
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 427 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "Que bebida você quer de novo?"
    show player 426
    show diane f_laying_thinking
    dia "Hmm, um {b}[randomdrink]{/b} seria legal."
    show diane f_laying_smirk_up_talk
    dia "{b} A receita está dentro de um bloco de notas ao lado do mixer.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "Uma {b}[randomdrink]{/b}, chegando logo!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_diane_fetch_pump:
    show player 10 at left
    show diane f_normal
    with dissolve
    player_name "O que você precisa que eu faça de novo?"
    show player 5
    show diane f_normal_talk
    dia "Apenas me traga {b}ferramenta{/b} que eu deixei no {b}kitchen counter.{/b}"
    show diane f_normal
    show player 14
    player_name "Ah, certo!"
    player_name "Eu já volto!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_diane_got_pump:
    scene garden
    show player 239_240 at left
    show diane at lright
    with dissolve
    pause
    show player 103 at Position (xoffset=38) with dissolve
    player_name "É disso que você precisa?"
    show player 13
    show diane a_dressed_pump f_normal_talk
    with dissolve
    dia "Sim!"
    show diane f_normal
    show player 10
    player_name "O que é isso de qualquer maneira?"
    show player 13
    show diane f_normal_talk
    dia "Você nunca viu uma bomba de mama antes?"
    show diane f_normal
    show player 10
    player_name "... Não?"
    show player 12
    player_name "É uma bomba?"
    show player 5
    dia "Mmmhmm."
    show player 10
    player_name "Como isso funciona?"
    show player 5
    show diane f_explain
    dia "Hehe, bem, você coloca essa ponta sobre o mamilo e, em seguida, pressiona a alavanca aqui e ela suga o leite dos dentes e para dentro deste recipiente."
    show diane f_normal
    show player 14
    player_name "Whoa!"
    show player 10
    player_name "... E não machuca a vaca?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Hahaha!"
    dia "Não, bonito."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "É muito bom!"
    show diane f_shamed_talk_smile
    dia "Você sabe, pela uhh ... vaca."
    show diane f_shamed
    show player 14
    player_name "Posso tentar ordenhar a vaca em algum momento?"
    show player 13
    show diane f_laugh
    dia "Haha, eu não acho que seja uma boa ideia, bonito."
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Por enquanto você apenas trabalha no jardim, ok?"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 14
    player_name "... Ok."
    show player 13
    show diane f_smirk_talk
    dia "Se você precisar de mim, eu estarei aqui."
    dia "Basta bater primeiro, entendeu?"
    show diane f_smirk
    show player 14
    player_name "Sim, entendi."
    show player 13
    show diane f_laugh
    dia "Hehe, obrigado garanhão."
    hide player
    hide diane
    with dissolve
    return


label dianes_dialogue_delivery_1_reminder:
    scene garden
    show player 10 at left
    show diane
    with dissolve
    player_name "Onde devo entregar esse leite novamente?"
    show player 5
    show diane f_normal_talk
    dia "Você precisa anotar esse pedido para {b}Tony{/b} na {b} Tony's Pizzeria{/b}."
    show diane f_normal
    show player 14
    player_name "Ah, sim, eu conheço esse lugar!"
    player_name "Tudo bem, voltarei em um instante."
    show player 13
    show diane f_normal_talk
    dia "Obrigado, {b}[firstname]{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_1_done:
    scene garden
    show diane f_normal
    show player 640e at left
    with dissolve
    player_name "Fiz sua entrega para você."
    show player 13
    show diane f_normal_talk a_dressed_money
    with dissolve
    dia "Oh, muito obrigado {b}[firstname]{/b}!"
    show diane a_dressed_shovel with dissolve
    dia "Did {b}Tony{/b} disse alguma coisa?"
    show diane f_normal
    show player 14
    player_name "Uh huh, ele disse que o leite realmente levou suas pizzas a um nível totalmente novo!"
    show player 13
    show diane f_normal_talk
    dia "{b}*Suspiro*{/b}"
    dia "Então ele gostou?!"
    show diane f_normal
    show player 14
    player_name "Heh, eu diria."
    show player 17
    player_name "Ele quer triplicar o seu próximo pedido!"
    show player 13
    show diane f_sad_talk
    dia "Triplo ?!"
    show diane f_surprised_front
    dia "Hmm..."
    show player 12
    player_name "Isso é um problema?"
    show player 5
    show diane f_shamed_front_talk
    dia "Hein? Oh ... Bem, eu não tenho certeza."
    dia "Não sei se consigo lidar com"
    show diane f_surprised
    pause
    show diane f_smirk_talk
    dia "Quero dizer, minha vaca ..."
    dia "... não sei se ela consegue lidar com tanta demanda."
    show diane f_smirk
    show player 12
    player_name "Parece que você pode precisar se expandir e conseguir mais gado."
    show player 13
    show diane f_thinking
    dia "..."
    show diane f_thinking_back
    dia "Eu definitivamente não estou pronto para isso ainda."
    dia "Vou ter que empurrá-la mais e começar a estocar ..."
    show diane f_normal
    show player 14
    player_name "Posso fazer algo para ajudar?"
    show player 13
    show diane f_normal_talk
    dia "Heh, não, está tudo bem."
    dia "Você já me ajudou bastante."
    show diane f_normal
    player_name "..."
    show diane f_normal_talk
    dia "Por que você não volta ao seu trabalho no jardim?"
    show diane f_normal
    show player 14
    player_name "Sim, tudo bem ..."
    show player 13f with dissolve
    show diane f_teasing
    dia "Oh!"
    show diane f_normal
    show player 13 with dissolve
    show diane f_normal_talk
    dia "... eu quase esqueci."
    show diane a_dressed_money with dissolve
    dia "Este é seu."
    show diane f_normal a_dressed_shovel
    show player 640c
    with dissolve
    player_name "Hein? Esse é o pagamento inteiro da entrega!"
    show player 640b
    show diane f_normal_talk
    dia "Hehe, eu te disse, {b}[firstname]{/b}. Este não é um esforço de ganhar dinheiro para mim."
    show diane f_smirk_talk
    dia "Pelo menos não no momento."
    show diane f_smirk
    player_name "..."
    show diane f_normal_talk
    dia "Você pega e coloca na sua aula."
    show diane f_normal
    show player 14 with dissolve
    player_name "Obrigado, {b}Diane{/b}!"
    show player 13
    show diane f_laugh
     dia "De nada, lindo!"
    hide player
    show diane kiss
    with dissolve
    pause
    hide diane with dissolve
    return

label dianes_dialogue_leave_d1:
    show player 14 at left
    show diane f_normal
    player_name "Eu provavelmente deveria começar no jardim."
    show player 13
    show diane f_normal_talk
    dia "Tudo bem."
    dia "Obrigado novamente por ajudar!"
    show diane f_normal
    show player 14
    player_name "Não tem problema."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_3_reminder:
    show player 10 at left
    show diane b_naked a_naked_sides at lright
    with dissolve
    player_name "O que eu deveria fazer de novo?"
    show player 13
    show diane f_normal_talk
    dia "{b}Pegue o pacote de leite do meu galpão e entregue no refeitório da sua escola.{/b}"
    show diane f_normal
    show player 14
    player_name "Ah, certo."
    player_name "Estou nisso!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_pre_fun_paint:
    show player 10
    player_name "{b}[deb_name]{/b} disse que deu a pintura velha na garagem."
    player_name "Você ainda está certo?"
    show player 5
    if L_diane_garden.is_here(M_diane):
        show diane f_laugh
    else:
        show diane b_naked a_naked_sides f_laugh
    dia "Bem, claro que sim!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 13
    if L_diane_garden.is_here(M_diane):
        show diane f_normal_talk
    else:
        show diane b_naked a_naked_sides f_normal_talk
    dia "Deve haver um pouco no galpão."
    dia "Sirva-se!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 14
    player_name "Obrigado!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
