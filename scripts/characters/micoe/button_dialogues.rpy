label micoe_dialogue_blowjob:
    scene expression "backgrounds/location_hospital_room_blur.jpg"
    show player 10 at left
    show micoe at flip
    with dissolve
    player_name "Lembra quando você me ajudou ... Umm, extraia minha amostra para testar. "
    show player 5
    show micoe f_sexy_talk
    micoe "Quer dizer, quando eu chupei seu pau no banheiro? "
    show micoe f_sexy
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "S-sim. "
    show player 3
    show micoe f_laugh
    micoe "Hehehe, acho que já passamos de tímido, {b}[firstname]{/b}."
    show micoe f_sexy_talk
    micoe "Você está aqui para me deixar ter outro gosto? "
    show micoe f_sexy
    show player 17 with dissolve
    player_name "Uh huh."
    hide player
    show micoe b_pulling f_empty a_empty
    with dissolve
    micoe "Vamos, gracinha. "
    scene expression "backgrounds/location_hospital_bathroom.jpg"
    show player 13f at right
    show micoe f_sexy_talk
    with dissolve
    micoe "O que você está esperando?"
    micoe "Tire esse pau daqui!"
    show micoe f_sexy
    show player 14f
    player_name "O-okay."
    show player 261b with dissolve
    pause
    show player 263b at Position (xoffset=-150)
    show micoe knees
    with dissolve
    pause
    show micoe knees_talk
    micoe "Mmm, eu vou chupar esse pau lindo quando quiser, {b}[firstname]{/b}!"
    $ M_micoe.set('sex speed', .12)
    $ anim_toggle = True
    $ animated = True
    scene expression "backgrounds/location_hospital_bathroom_closeup.jpg"
    show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    micoe "{b}*Slurp*{/b}"
    player_name "Oh Deus..."
    player_name "Isso é incrível, {b}Micoe{/b}."
    micoe "Mmhmm!"
    return

label micoe_dialogue_goodbye:
    show player 14 at left
    show micoe f_normal at flip
    player_name "Apenas dizendo olá."
    show player 13
    show micoe f_sad_talk
    micoe "Oh, bem, isso é decepcionante ... "
    show micoe f_sexy_talk
    micoe "Eu pensei que talvez você estivesse aqui para se divertir um pouco. "
    show micoe f_sexy
    show player 14
    player_name "Desculpa."
    show player 13
    pause
    show player 14
    player_name "Vejo você por aí, ok? "
    show player 13
    show micoe f_normal_talk
    micoe "Tudo bem, gracinha. "
    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show micoe f_normal_talk at flip
    micoe "Olá, gracinha. "
    micoe "O que faz você voltar para me ver? "
    show micoe f_normal
    return

label micoe_dialogue_increase_chance_of_conception:
    show micoe at flip
    show player 10 at left
    with dissolve
    player_name "Há algo mais que eu possa estar fazendo para ajudar meus amigos "
    player_name "{b}*Ahem*{/b} Quero dizer, ajudar minha namorada a conceber um bebê? "
    show player 5
    show micoe f_normal_talk
    micoe "Hmm, ela está estressada com isso? "
    show micoe f_normal
    show player 10
    player_name "Ehh, na verdade não ... "
    player_name "Eu só quero ter certeza de que estou fazendo tudo o que posso para ajudá-la."
    show player 5
    show micoe f_laugh
    micoe "Você é tão doce!"
    show player 13
    show micoe f_normal_talk
    micoe "Bem, vocês dois estão fazendo muito sexo? "
    show micoe f_normal
    show player 29 with dissolve
    player_name "S-sim. "
    show player 13 with dissolve
    show micoe f_normal_talk
    micoe "... E qual posição você está usando? "
    show micoe f_normal
    show player 10
    player_name "... Posição?"
    show player 5
    show micoe f_sexy_talk
    micoe "Sim, em que posição você está transando? "
    show micoe f_sexy
    show player 10
    player_name "Err, eu não sei. "
    show player 14
    player_name "Eu acho que geralmente estou atrás dela ... "
    show player 13
    show micoe f_sexy_talk
    micoe "Estilo cachorrinho? "
    show micoe f_sexy
    show player 5
    player_name "..."
    show micoe f_laugh
    micoe "Hehe, você é tão fofa! "
    show micoe f_normal_talk
    micoe "O estilo cachorrinho deve funcionar bem para a concepção ".
    show player 13
    micoe "Muitos médicos recomendam, porque permite a penetração mais profunda ".
    show micoe f_wink
    pause
    show micoe f_sexy_talk
    micoe "No entanto, com o que você está embalando, a penetração profunda não será problema. "
    show micoe f_sexy
    show player 29 with dissolve
    player_name "Heh, sim-sim ... "
    show player 13 with dissolve
    show micoe f_normal_talk
    micoe "Você pode tentar a posição missionária. "
    show micoe f_normal
    show player 10
    player_name "O que é isso?"
    show player 13
    show micoe f_normal_talk
    micoe "É quando a mulher deita de costas e você está por cima. "
    micoe "Nessa posição, a gravidade ajudará a transportar seu sêmen para o colo do útero."
    show micoe f_normal
    show player 17
    player_name "Ohh, entendi! Estilo normal ".
    show player 18
    show micoe f_sad
    pause
    show player 14
    player_name "Isso faz sentido."
    show player 13
    pause
    show player 14
    player_name "Algo mais?"
    show player 13
    show micoe f_normal
    micoe "Hmm."
    show micoe f_normal_talk
    micoe "Na verdade não."
    micoe "Infelizmente, o maior obstáculo na sua situação é a idade da sua namorada."
    show micoe f_normal
    show player 10
    player_name "Sim."
    show player 5
    pause
    show player 10
    player_name "Tem certeza de que não posso fazer mais nada para ajudar? "
    show player 5
    show micoe f_normal_talk
    micoe "Bem..."
    show micoe f_look_back
    pause
    show micoe f_normal_talk
    micoe "Há uma coisa ... Mas eu realmente não devo falar sobre isso. "
    show micoe f_normal
    show player 12
    player_name "Hã?"
    player_name "Como é que é?"
    show player 5
    pause
    show player 14
    player_name "Se houver uma chance de ajudar, eu realmente preciso saber! "
    player_name "{b}Diane{/b} realmente tem o coração definido para engravidar. "
    show player 13
    pause
    show player 18
    player_name "Por favor?"
    show micoe f_laugh
    micoe "Ngh, você é tão doce! "
    show player 13
    show micoe f_normal_talk
    micoe "Tudo bem, eu vou te dizer ... Mas você não ouviu isso de mim! "
    micoe "Entendeu?"
    show micoe f_normal
    show player 14
    player_name "S-sim, eu entendo! "
    show player 13
    show micoe f_normal_talk
    micoe "Há uma nova droga que tem mostrado muitas promessas quando se trata de aumentar as taxas de concepção ".
    micoe "Eles estão chamando {b}Pregnax{/b}."
    show micoe f_normal
    show player 14
    player_name "Isso parece perfeito! "
    show player 12
    player_name "Qual é o problema? "
    show player 5
    show micoe f_normal_talk
    micoe "Bem, o problema é que eles ainda estão na fase de testes. "
    show micoe f_normal
    pause
    show player 14
    player_name "Tudo bem, não me importo de ajudá-lo a testá-lo. "
    show player 13
    show micoe f_laugh
    micoe "Hehe, você terá que conversar com {b}Dr. Singh{/b} sobre isso."
    show micoe f_normal
    show player 10
    player_name "{b}Dr. Singh{/b}?"
    show player 5
    show micoe f_normal_talk
    micoe "Sim, {b}Singh's{/b} esse novo médico de fantasia que eles enviaram de algum lugar no exterior ".
    micoe "Funciona no {b}terceiro andar{/b}."
    micoe "Desenvolvido {b}Pregnax{/b} há anos. "
    show micoe f_normal
    show player 14
    player_name "Ok, então eu vou falar com ele! "
    show player 13
    show micoe f_sad_talk
    micoe "Heh, eu gostaria que fosse assim tão fácil. "
    micoe "Infelizmente, o {b}terceiro andar{/b} é uma área restrita ".
    micoe "Mesmo eu não tenho acesso a isso. "
    show micoe f_normal
    show player 12
    player_name "Então, como obtenho acesso? "
    show player 5
    show micoe f_normal_talk
    micoe "Eu realmente não posso ajudá-lo lá, gracinha. "
    micoe "Muitas pessoas na clínica não têm credenciais para se levantar {b}terceiro andar{/b}."
    show micoe f_normal
    show player 24
    player_name "Porcaria."
    pause
    show player 10
    player_name "Tudo bem, obrigado pela informação {b}Micoe{/b}."
    show player 5
    show micoe f_laugh
    micoe "Não tem problema, gracinha! "
    show micoe f_sexy_talk
    micoe "Sinta-se livre para vir me ver se tiver mais perguntas ... "
    show player 13
    show micoe f_wink
    pause
    show micoe f_sexy_talk
    micoe "... Ou você sente vontade de se divertir um pouco!
    show micoe f_sexy
    show player 29 with dissolve
    player_name "S-sim, tudo bem."
    show player 3
    show micoe f_sexy_talk
    micoe "Mmm, tão adorável ... "
    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_pregnax:
    scene expression "backgrounds/location_hospital_room.jpg"
    show player 10 at left
    show micoe f_normal at flip
    with dissolve
    player_name "Onde posso encontrar esse medicamento para fertilidade novamente? "
    show player 5
    show micoe f_sad_talk a_dressed_shh at Position (xoffset=-175) with dissolve
    micoe "Shh!"
    micoe "Não tão alto!"
    show micoe f_normal a_dressed_front with dissolve
    show player 10
    player_name "Oh, desculpe."
    show player 5
    show micoe f_normal_talk
    micoe "Eles continuam no {b}terceiro andar{/b}."
    show micoe f_normal
    show player 14
    player_name "{b}Terceiro andar{/b}, Entendi!"
    show player 13
    show micoe f_normal_talk
    micoe "Espere, você não pode simplesmente valsar lá em cima. "
    micoe "Você terá que {b}encontre alguém com acesso{/b} Para levá-lo."
    show micoe f_normal
    show player 10
    player_name "Hmm, quem eu poderia perguntar? "
    show player 5
    show micoe f_normal_talk
    micoe "Desculpe gracinha, eu não posso te ajudar com isso. "
    micoe "Lembre-se, você não ouviu nada disso de mim!"
    show micoe f_normal
    show player 14
    player_name "Não se preocupe, não vou contar. "
    show player 18
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
