label aqua_dialogue_night:
    show player 10 with dissolve
    player_name "Está ficando tarde..."
    player_name "Eu deveria encontrar o caminho para sair desta caverna subaquática antes que fique muito escuro."
    hide player with dissolve
    return

label aqua_dialogue_aqua_found:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    pause
    show player 16 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    show aqua 1
    aqua "(!!!)" with hpunch
    aqua "Você!!"
    show player 15
    show aqua 2
    player_name "Está certo! Eu!"
    player_name "Você disse que eu tinha que vir buscá-lo. Bem, aqui estou eu!"
    player_name "Agora me devolva o brilho!"
    show player 16
    show aqua 1
    aqua "Hahahaha! Seu humano engraçado!"
    aqua "Você percorre um longo caminho. Você deve ser um bom nadador, como Aqua!"
    show player 24
    show aqua 2
    player_name "*tosse * eu acho..."
    show player 30
    player_name "De qualquer forma, que lugar é esse?"
    show player 16
    show aqua 1
    aqua "Ninho deste Aqua!"
    show player 12
    show aqua 2
    player_name "Você vive aqui?"
    show player 11
    show aqua 1
    aqua "Sim."
    show player 10
    show aqua 2
    player_name "Por você mesmo?"
    show player 11
    show aqua 4
    aqua "Sim."
    show player 10
    show aqua 3
    player_name "Há mais de você?"
    show player 11
    show aqua 4
    aqua "Mais ... de mim?"
    show player 10
    show aqua 3
    player_name "Você sabe, outros ninhos com outros ... Hum, Aquas?"
    show player 11
    show aqua 4
    aqua "Oooh, não."
    show aqua 5
    aqua "Nenhum outross. Apenas Aqua. ultimo do tipo."
    show player 10
    show aqua 3
    player_name "Aww, bem, isso é meio triste. Soa solitário."
    show player 5
    show aqua 1
    aqua "Não sozinho. Tem peixe!"
    show aqua 2b
    aqua "Peixe que você rouba!"
    show player 15
    show aqua 1b
    player_name "Eu te disse que não era eu! Está {b}CAPTAIN Terry{/b}."
    show player 16
    show aqua 4
    aqua "Caplan Terry? Hmm..."
    show aqua 5
    pause
    show aqua 4
    aqua "Talvez você diga a verdade..."
    show player 12
    show aqua 3
    player_name "Estou falando a verdade, Aqua. eu prometo."
    show player 16
    show aqua 2b
    aqua "Bem, o que o Aqua faz então? Fishies continuam recebendo roubos de bola!"
    show aqua 4
    aqua "Se todos os peixes desaparecerem, com quem Aqua conversará?"
    show player 11
    show aqua 5
    aqua "Aqua enlouquece antes de encontrar companheiro."
    show player 10
    show aqua 3
    player_name "Companheira?"
    show player 11
    show aqua 4
    aqua "Sim, Aqua esperando por Mate. Faça Aquasss bebê."
    show player 10
    show aqua 5
    player_name "Realmente? Há quanto tempo você está esperando?"
    show aqua 4
    show player 11
    aqua "Aqua duno. Muito tempo. Ninguém vem. Ninguém encontra Aqua."
    show player 10
    show aqua 5
    player_name "Hmm ... Bem, eu te encontrei."
    show player 13
    show aqua 1
    aqua "Sim! Você encontra Aqua!"
    show aqua 2
    aqua "..."
    show aqua 9
    aqua "Se você fala a verdade e promete não rouba peixes. Me devolver brilhante."
    show player 14
    show aqua 8
    player_name "Sim! Obrigado Aqua."
    show player 13
    show aqua 9
    aqua "Você promete?"
    show player 14
    show aqua 8
    player_name "Eu prometo, não vou roubar peixes.'"
    show player 13
    show aqua 9
    aqua "Ookaay."
    show aqua 10
    pause
    show aqua 2
    show player 471
    show popup_lure zorder 3 at truecenter with dissolve
    pause
    hide popup_lure with dissolve
    player_name "Ufa ... Obrigado Aqua!"
    show player 470
    show aqua 1
    aqua "Lembre-se de não roubar os peixes do Aqua..."
    hide player
    hide aqua
    with dissolve
    return

label aqua_sex:
    $ game.timer.tick()
    if M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_pre_first")

    call expression game.dialog_select("aqua_sex_pre")
    if M_aqua.is_state(S_aqua_mate):
        label aqua_sex_replay:
            call expression game.dialog_select("aqua_sex_after_first")

    call expression game.dialog_select("aqua_sex_after")
    jump expression game.dialog_select("aqua_sex_loop")

label aqua_sex_pre_first:
    scene location_lair_mount
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, tenho boas notícias!"
    show player 1
    show aqua 1
    aqua "*Suspiro * Você aprende a respirar debaixo d'água, como o Aqua?!"
    show player 12
    show aqua 2
    player_name "O que? ... Não."
    show player 1
    show aqua 7
    aqua "Oh OK. Que notícias então?"
    show player 2
    show aqua 6
    player_name "eu convenci {b}Captain Terry{/b} parar de pescar!"
    show player 1
    show aqua 7
    aqua "Você quer dizer peixes seguros!?"
    aqua "Não mais {b}Captain Terry{/b}!?"
    show player 17
    show aqua 6
    player_name "Ei, você disse certo nessa hora!"
    show player 1
    show aqua 7
    aqua "Hã?"
    show player 2
    show aqua 6
    player_name "Você disse '{b}Captain Terry{/b}' corretamente esse tempo."
    show player 1
    show aqua 7
    aqua "Sim. Caplan Terry!"
    show player 90
    show aqua 6
    player_name "..."
    show aqua 6b
    aqua "..."

    show player 37
    player_name "... Apenas não importa."
    show player 2
    player_name "Seu peixe deve estar seguro agora."
    show player 1
    show aqua 7
    aqua "Oh obrigado! Obrigado! Obrigado!"
    show aqua 14
    aqua "Você é bom humano! Humano forte!"
    show player 29
    show aqua 13
    player_name "De nada, Aqua..."
    show player 1
    show aqua 11
    aqua "..."
    show aqua 12
    aqua "É ... humano pronto para acasalar com o Aqua?"
    show player 21
    show aqua 13
    player_name "Agora?"
    show player 297
    show aqua 14
    aqua "Sim. Aqua espere o suficiente. Companheiro levá-la fortemente na água!"
    show player 10
    show aqua 13
    player_name "Na água?"
    show player 11
    show aqua 14
    aqua "Sim. Venha!"
    return

label aqua_sex_pre:
    scene location_lair_cutscene
    with fade
    show text "O toque de Aqua foi suave e gentil quando ela pegou minha mão e se dirigiu para a piscina luminescente." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Eu lutei para manter o ritmo, mexendo nas minhas roupas." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Bmas ela não pareceu notar, sua excitação palpável enquanto guia seu companheiro na água." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label aqua_sex_after_first:
    scene location_lair_water with fade
    show aswim 1 at left
    show pswim 1 at right
    pause
    show aswim 2
    aqua "Ooh, companheiro tem bom corpo."
    show aswim 1
    show pswim 2
    player_name "Obrigado Aqua..."
    show aswim 3
    show pswim 1
    pause
    show aswim 2
    aqua "Sua enguia está dormindo."
    show aswim 1
    show pswim 2
    player_name "Hã?"
    show aswim 3
    pause
    show pswim 3
    pause
    show pswim 2
    player_name "Oh Sim..."
    show aswim 2
    show pswim 1
    aqua "O companheiro gosta do corpo de Aqua?"
    show aswim 1
    show pswim 2
    player_name "Sim ... Umm, 'companheiro' gosta muito do corpo de Aqua."
    show aswim 2
    show pswim 1
    aqua "Boa. O corpo de Aqua pertence a você agora."
    aqua "A enguia do companheiro pode jogar Aqua inssside sempre que quiser."
    show aswim 3
    pause
    show aswim 2
    aqua "É quente por dentro Aqua..."
    show aswim 3
    pause
    show aswim 2
    aqua "... e macio..."
    show aswim 3
    pause
    show aswim 2
    aqua "... e umida."
    show pswim 3
    pause
    show aswim 3
    show pswim 4
    pause
    show aswim 4
    show pswim 5
    pause
    show pswim 9
    pause
    show aswim 2
    show pswim 6
    aqua "Oh, enguia gosta disso, sim?!"
    show aswim 3
    show pswim 7
    player_name "S-sim..."
    show aswim 4
    aqua "MMM bom. Aqua quer."
    show aswim 3
    show pswim 8
    player_name "..."
    show aswim 4
    aqua "Aqua quer agora!"
    hide pswim
    show aswim 5 with dissolve
    pause
    show aswim 6 at right with dissolve
    player_name "*Gulp*"
    aqua "Aaah, sim. Venha enguia, você joga inssside Aqua."
    aqua "Dê a Aqua bebês fortes..."
    player_name "Oh uau!"
    aqua "Mmm..."
    return

label aqua_sex_after:
    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    aqua "{b}Aqua{/b} precisa dele por dentro dela!"
    aqua "Apresse meu companheiro!"
    player_name "..."
    show aquas 2
    aqua "Dele."
    aqua "Sua enguia tão grande!"
    aqua "Me leve forte!"
    $ M_aqua.set("sex speed", .175)
    show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
    with fade
    aqua "Ooohh!."
    pause
    aqua "Tão forte!"
    pause
    aqua "e profundo!"
    $ M_aqua.set("sex speed", .125)
    aqua "Aaahh!"
    pause
    aqua "Mmm, meu companheiro."
    aqua "Mais rápido!"
    $ M_aqua.set("sex speed", .075)
    pause
    return

label aqua_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
                $ animated = True
            pause 5
            call expression game.dialog_select("aqua_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "aquas {}".format(pose_list[pose_counter]) as aquas
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("aqua_hscene_dialog")
        $ animcounter += 1
    call screen aqua_sex_options

label aqua_hscene_dialog:
    if animcounter == 1:
        aqua "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 3:
        aqua "Leve-me!!!{p=1}{nw}"
        player_name "Uhhh...{p=1}{nw}"
    return

label aqua_sex_cum:
    call expression game.dialog_select("aqua_sex_cum_pre")
    if not store._in_replay == None or M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_cum_first")

    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["01_unlocked"] = True
    $ M_aqua.trigger(T_aqua_mated)
    hide player
    hide aqua
    with dissolve
    $ player.go_to(L_map)
    $ game.main()

label aqua_sex_cum_pre:
    player_name "Isto é inacreditável!"
    player_name "{b}Aqua{/b}, Eu vou..."
    aqua "Sim ... Sim, meu companheiro!"
    aqua "Dar {b}Aqua{/b} suas sementes!"
    aqua "DELE!!!"
    show aquas 8 with flash
    player_name "UHHH!!"
    aqua "AAAAHHH!!!!"
    pause
    show aquas 9
    player_name "Uau!"
    player_name "Isso foi incrível!"
    aqua "Sim..."
    aqua "... {b}Aqua{/b} pode sentir bebês fortes nadando por dentro dela!"
    pause
    scene black with fade
    return

label aqua_sex_cum_first:
    scene location_lair_mount
    show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Então você gostou disso?"
    show player 1
    show aqua 12
    aqua "Sim. Aqua aproveite muito! Ainda sinto formigamento dançando nas pernas!"
    show player 2
    show aqua 11
    player_name "Você foi incrível! Eu nunca senti nada assim antes."
    show player 1
    show aqua 14
    aqua "Sim, a primeira vez deste Aqua também."
    show aqua 12
    aqua "... Mas o Aqua quer mais."
    show aqua 14
    aqua "O companheiro volta, dá mais água ao Aqua. sim?"
    show player 2
    show aqua 13
    player_name "Absolutamente, voltarei muito em breve!"
    show player 1
    show aqua 14
    aqua "Promessa de companheiro?"
    show player 2
    show aqua 13
    player_name "Oh, eu prometo!"
    show player 1
    show aqua 12
    aqua "Boa. Aqua quer muito mais!"
    show aqua 14
    aqua "Volte em breve, Humano."
    show aqua 11
    aqua "Aqua, espere aqui, até formigar, parar de dançar..."
    return

label aqua_dialogue_pre:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    player_name "Hi, Aqua!"
    show player 1
    show aqua 1
    aqua "Sim..."
    show player 2
    show aqua 2
    player_name "Eu queria falar com voce."
    show player 1
    show aqua 4
    aqua "O que menino humano quer?"
    return

label aqua_dialogue_the_others:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, o que aconteceu com o resto da sua espécie?"
    show player 11
    show aqua 4
    aqua "Hmm, Aqua não é certo. Eles acabaram de sair um dia. Aqua."
    show aqua 5
    show player 10
    player_name "Aww, me desculpe Aqua."
    show player 11
    show aqua 1
    aqua "Você faz mais perguntas?"
    show aqua 2
    return

label aqua_dialogue_how_are_you:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, como você está?"
    show player 1
    show aqua 4
    aqua "Como eu estou?"
    show player 2
    show aqua 3
    player_name "Sim, como você está se sentindo??"
    show player 1
    show aqua 5
    aqua "Hmm, Aqua está bem. Solitário com tão poucos peixes..."
    show aqua 4
    aqua "... mas gosta daquele garoto humano vem visitar."
    show player 2
    show aqua 3
    player_name "Eu também gosto de conversar com você Aqua."
    show player 1
    show aqua 1
    aqua "Sim, como falar."
    aqua "Você faz mais perguntas?"
    show aqua 2
    return

label aqua_dialogue_mating_pre:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Aqua, que tipo de companheiro você está procurando?"
    show player 11
    show aqua 4
    aqua "Cara. homem forte. Faça bebês fortes do Aqua."
    show aqua 1
    aqua "você conhece homem assim?"
    show player 34
    show aqua 3
    player_name "Hmm."
    return

label aqua_dialogue_mating_stat_fail:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 29 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "[chr_warn]E quanto a mim?"
    show player 3
    show aqua 4
    aqua "[chr_warn]Seu homem forte?"
    show player 29
    show aqua 3
    player_name "[chr_warn]Sim?"
    show player 3
    show aqua 5
    aqua "..."
    aqua "Hmm..."
    pause
    show aqua 4
    aqua "[chr_warn]Aqua pensa ... Não. Má ideia."
    show player 24
    show aqua 3
    player_name "[chr_warn]Vadio..."
    return

label aqua_dialogue_mating_stat_pass:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Talvez eu possa ajudar?"
    show player 1
    show aqua 7
    aqua "Você?"
    show player 2
    show aqua 6
    player_name "Bem, quero dizer, eu nadei até aqui para encontrar você."
    show player 1
    show aqua 7
    aqua "Você fez."
    show player 2
    show aqua 6
    player_name "... E eu lutei com uma lula muito má ao longo do caminho."
    show player 1
    show aqua 7 with hpunch
    aqua "Você luta com tinta?!"
    show player 2
    show aqua 6
    player_name "Tinta? Sim. Eu luto com tinta."
    show aqua 7
    aqua "Oooh, tinta forte!"
    show aqua 12
    pause
    show aqua 11
    aqua "Talvez você dê a Aqua bebês fortes."
    show player 14
    show aqua 13
    player_name "Realmente?!"
    show player 1
    show aqua 14
    aqua "Sim. Mas sem companheiro ainda. Primeiro você prova a força."
    show player 10
    show aqua 13
    player_name "Prove minha força? Como eu devo fazer isso?"
    show player 1
    show aqua 7
    aqua "Você diz que Caplan Terry rouba peixinhos, sim?"
    show player 12
    show aqua 6
    player_name "{b}CAPTAIN Terry{/b}. Sim, ele é o cara que está pescando na doca."
    show player 11
    show aqua 7
    aqua "Hmm, você vai fazer Caplan Terry parar."
    show aqua 11
    aqua "Você faz isso e depois acasala com o Aqua."
    show player 10
    show aqua 13
    player_name "Bem, acho que posso tentar."
    show player 11
    show aqua 14
    aqua "Boa. Você vai então. salvar peixes!"
    return

label aqua_dialogue_mating_hint:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "O que preciso fazer de novo, Aqua? Para provar minha força?"
    show player 11
    show aqua 7
    aqua "Você salva peixes de Caplan Terry!"
    show player 10
    show aqua 6
    player_name "Oh, certo. {b}CAPTAIN Terry{/b}."
    show player 11
    show aqua 7
    aqua "É o que o Aqua diz! Caplan Terry!"
    show player 12
    show aqua 6
    player_name "CAPT- Deixa pra lá. Acho que devo tentar falar com ele."
    show player 5
    show aqua 7
    aqua "Sim. Você vai, salvar peixes!"
    return

label aqua_dialogue_mate:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Eu pensei que talvez você gostaria de ... Entre na água novamente?"
    show player 26
    show aqua 3
    aqua "..."
    show aqua 1
    aqua "Oh! Você quer fazer bebês?"
    show player 21
    show aqua 12
    player_name "Eu, err ... Claro?"
    show player 26
    show aqua 11
    aqua "Hahaha! Humano engraçado. Você companheiro do Aqua agora."
    show aqua 14
    aqua "Aqua sempre pronto para mais sementes! Companheiro levá-la fortemente na água sempre que ele quer."
    return

label aqua_dialogue_nothing:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Nada, eu só estava dizendo oi!"
    show player 1
    show aqua 4
    aqua "Menino humano é ... engraçado..."
    show aqua 1
    aqua "...Eu gosto de menino humano..."
    show player 21
    show aqua 2
    player_name "Eu errei ... como você também!"
    show player 13
    aqua "..."
    show player 29
    player_name "E sim, eu deveria ir."
    show player 3
    show aqua 1
    aqua "Você volta, vê Aqua em breve."
    show player 17
    show aqua 2
    player_name "Pode apostar!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
