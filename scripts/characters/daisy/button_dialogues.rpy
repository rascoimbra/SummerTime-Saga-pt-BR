label daisy_button_baby_leave:
    show player 14b
    player_name "Vou deixar vocês ficarem."
    show player 1b
    show daisy f_normal_talk
    daisy "Tudo bem."
    show daisy f_down_talk
    daisy "Diga, tchau tchau papai."
    show daisy f_down
    show player 17
    player_name "Hehe."
    show player 14b
    if M_daisy.pregnancy.baby_gender == "gêmeos":
        player_name "Adeus, pequeninos."
    else:
        player_name "Adeus, pequena."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_anything_baby:
    show player 14b
    player_name "Posso pegar algo para você?"
    show player 1b
    show daisy f_normal_talk
    daisy "Não estou bem."
    daisy "obrigado, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "De nada."
    show player 1b
    return

label daisy_button_hows_baby_doing_boy:
    show player 14b
    player_name "Como ele está?"
    show player 1b
    show daisy f_normal_talk
    daisy "Ele dorme muito..."
    daisy "... E quando ele não está dormindo, ele está comendo!"
    show daisy f_normal
    show player 14b
    player_name "Heh, então ele leva atrás de sua mãe então?"
    show player 1b
    show daisy f_laugh
    daisy "Nu uh!"
    show daisy f_normal
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_hows_baby_doing_twins:
    show player 14b
    player_name "Como eles estão?"
    show player 1b
    show daisy f_normal_talk
    daisy "Eles dormem muito..."
    daisy "... E quando não estão dormindo, estão comendo!"
    show daisy f_normal
    show player 14b
    player_name "Heh, então eles pegam a mãe deles então?"
    show player 1b
    show daisy f_laugh
    daisy "Nu uh!"
    show daisy f_normal
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_hows_baby_doing_girl:
    show player 14b
    player_name "Como ela está?"
    show player 1b
    show daisy f_normal_talk
    daisy "Ela dorme muito..."
    daisy "... E quando ela não está dormindo, ela está comendo!"
    show daisy f_normal
    show player 14b
    player_name "Heh, então ela leva atrás de sua mãe então?"
    show player 1b
    show daisy f_laugh
    daisy "Nu uh!"
    show daisy f_normal
    show player 17
    player_name "Hehehe."
    show player 1b
    return

label daisy_button_gave_birth_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_naked_baby f_down
    with dissolve
    player_name "Oi, {b}Daisy{/b}."
    show player 1b
    show daisy f_down_talk
    if M_daisy.pregnancy.baby_gender == "Garoto":
        daisy "Ele não é maravilhoso, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "Com certeza ele é!"
        show player 1b
        show daisy f_normal_talk
        daisy "Ele tem seus olhos."
    elif M_daisy.pregnancy.baby_gender == "gêmeos":
        daisy "Eles não são maravilhosos, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "Eles com certeza são!"
        show player 1b
        show daisy f_normal_talk
        daisy "Eles têm seus olhos."
    else:
        daisy "Ela não é maravilhosal, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "Ela tem certeza!"
        show player 1b
        show daisy f_normal_talk
        daisy "Ela tem seus olhos."
    show daisy f_normal
    pause
    show daisy f_down_talk
    daisy "E meus chifres!"
    show daisy f_laugh
    daisy "Hehehe!"
    show daisy f_normal
    return

label daisy_button_hows_the_baby_1:
    show player 14b at left
    show daisy
    player_name "Como está o bebê?"
    show player 1b
    show daisy f_normal_talk
    daisy "Umm, eu não sei."
    daisy "Isso me deixa doente de manhã, mas caso contrário, sinto o mesmo de sempre."
    show daisy f_normal
    show player 14b
    player_name "Bem, isso é bom."
    player_name "Você se certifica e diz {b}Diane{/b} ou eu, se você sentir que algo está errado, ok?"
    show player 1b
    show daisy f_normal_talk
    daisy "sim, ok {b}[firstname]{/b}."
    show daisy f_normal
    return

label daisy_button_hows_the_baby_2:
    show player 1b at left
    show daisy f_normal_talk
    daisy "Hehe, olha {b}[firstname]{/b}!"
    show daisy f_down_talk
    daisy "Meus peitos estão ficando maiores!"
    show daisy f_down
    show player 14b
    player_name "Sim, você está produzindo mais leite em preparação para o bebê."
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, isso fará {b}Diane{/b} feliz, não vai?"
    show daisy f_normal
    show player 14b
    player_name "Sim, com certeza vai."
    show player 1b
    pause
    show daisy f_down_talk a_naked_touch with dissolve
    daisy "Você viu minha barriga?"
    show daisy f_normal
    show player 14b
    player_name "Sim."
    show player 1b
    show daisy f_sad_talk
    daisy "Você acha feio?"
    show daisy f_sad
    show player 14b
    player_name "Não, de jeito nenhum!"
    player_name "Eu acho que é meio fofo, na verdade..."
    show player 1b
    show daisy f_laugh
    daisy "Serio?!"
    daisy "Hehe, você é estranho {b}[firstname]{/b}!"
    show daisy f_normal a_naked_sides with dissolve
    show player 17
    player_name "Hehe!"
    show player 1b
    return

label daisy_button_hows_the_baby_3:
    show player 1b at left
    show daisy a_naked_touch f_sad_talk
    daisy "{b}*Sigh*{/b}"
    daisy "Esse negócio de bebês é um verdadeiro aborrecimento, você sabe?!"
    show daisy f_sad
    show player 10b
    player_name "Oh?"
    show player 5b
    show daisy f_sad_talk
    daisy "Eu tenho que fazer xixi a cada cinco minutoss!"
    show daisy f_sad
    show player 14b
    player_name "Heh, sim, isso soa como um aborrecimento!"
    show player 1b
    show daisy f_down_talk
    daisy "... E o bebê está dançando o tempo todo!"
    show daisy f_down
    show player 14b
    player_name "Dançando?"
    show player 1b
    show daisy f_normal_talk
    daisy "Sim, {b}Diane{/b} diz que está chutando, mas eu não sei por que isso me chutaria..."
    daisy "Eu sou é mamãe afinal."
    show daisy f_normal
    show player 14b
    player_name "Heh, tenho certeza que você está certo."
    player_name "Provavelmente é apenas animado para sair."
    show player 1b
    show daisy f_laugh
    daisy "Sim!"
    daisy "Quero dizer, eu danço quando estou animado."
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Heh, você com certeza."
    show player 1b
    return

label daisy_button_intro_end:
    scene expression player.location.background_blur with None
    show daisy f_normal_talk
    show player 1b at left
    with dissolve
    daisy "{b}*Gasp* [firstname]{/b}!!!"
    show daisy f_normal
    show player 14b
    player_name "Oi {b}Daisy{/b}."
    hide player
    show daisy b_naked_hug f_empty a_empty
    with dissolve
    daisy "senti sua falta!"
    pause
    show daisy b_naked a_naked_sides f_normal
    show player 14b at left
    player_name "Sim, eu também senti sua falta."
    show player 1b
    return

label daisy_button_have_sex_first:
    show player 14b at left
    show daisy
    player_name "Você ainda quer fazer sexo?"
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, sim!"
    daisy "Quero muito!"
    show daisy f_normal
    pause
    show player 14b
    player_name "Tudo bem, vamos fazer isso."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} serio?!"
    show daisy f_laugh
    daisy "Sim!!!"
    show daisy f_normal
    show player 14b
    player_name "Vamos lá, vamos a uma das máquinas de ordenha."
    show player 1b
    show daisy f_laugh
    daisy "Ok!"
    hide player
    hide daisy
    with dissolve
    pause
    return

label daisy_button_have_sex_repeat:
    show player 10b at left
    show daisy
    player_name "Você quer ... Você sabe?"
    show player 5b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} Fazer sexo?!"
    show daisy f_normal
    show player 14b
    player_name "Sim."
    show player 1b
    show daisy f_normal_talk
    daisy "Claro!"
    daisy "Adoro quando fazemos sexo!"
    show daisy f_normal
    show player 14b
    player_name "Heh, vamos para as máquinas de ordenha então."
    show player 1b
    show daisy f_laugh
    daisy "Ok!"
    hide player
    hide daisy
    with dissolve
    pause
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed pre_talk
    show daisy_sex_breed_mc
    with dissolve
    daisy "Tudo bem, doninha ... Vamos lá!"
    daisy "Hehehe!"
    hide daisy_sex_breed_mc
    show daisy_sex_breed insert_and_pullout
    with dissolve
    pause
    show daisy_sex_breed creampie_pullout with dissolve
    pause 1
    show daisy_sex_breed creampie
    daisy "!!!" with hpunch
    $ animated = False
    return

label daisy_button_diane_breeding:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_naked a_naked_sides f_shamed_talk_smile
    with dissolve
    dia "Psst, {b}[firstname]{/b}."
    show diane f_shamed
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "{b}Diane{/b}, o que está acontecendo?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Você estava no seu caminho para ver {b}Daisy{/b}?"
    show diane f_shamed
    show player 14
    player_name "Sim, eu estava a caminho de ordenhá-la."
    show player 13
    show diane f_smirk_talk
    dia "Mmm, vendo você ordenhar ela me deixa tão-"
    show diane f_smirk
    pause
    hide player
    show diane b_pull_mc_naked f_empty a_empty at flip
    dia "Venha comigo! "Com soco"
    dia "{b}Daisy{/b} pode esperar um pouco mais."
    dia "Eu preciso de você dentro de mim, agora!"
    hide diane with dissolve
    player_name "Ok-"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    dia "Vamos garanhão, me dê!"
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Oh sim!!" with hpunch
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    pause
    dia "Ahh!"
    pause
    dia "Obrigado, {b}[firstname]{/b}."
    dia "É errado da minha parte roubar você de {b}Daisy{/b} enquanto ela ainda está se ajustando, mas..."
    dia "...Eu realmente preciso-"
    dia "Ah, merda!"
    dia "... Realmente precisava disso hoje!"
    pause
    player_name "Heh, não tem problema {b}Diane{/b}."
    pause
    scene location_diane_garden_cutscene12
    with fade
    player_name "eu acho que {b}Daisy's{/b} vem se ajustando muito bem."
    player_name "Ela parece muito feliz vivendo aqui."
    dia "eu também acho."
    dia "Nós realmente tivemos sorte em encontrá-la."
    dia "Ela é tão adorável!"
    player_name "Pela está ajudando você com seus negócios agora, certo?"
    dia "Definitivamente!"
    dia "Ela produz mais do que eu e nem sequer"
    scene location_diane_garden_cutscene12b with fade
    "{b}*Clink*{/b}{p=1}{nw}"
    "{b}*Smash*{/b} !!!" with hpunch
    player_name "O que-"
    pause
    dia "{b}Daisy{/b}?!"
    scene expression player.location.background_blur with None
    show player 368f at Position (xpos=650)
    show diane b_naked a_naked_sides f_smirk at Position (xpos=600)
    show daisy b_naked_shy a_naked_shy_front f_shy_sad_talk at flip
    with dissolve
    daisy "Eu não-"
    daisy "Eu não estava-"
    show daisy f_shy_sad
    show diane f_smirk_talk
    dia "Você estava nos assistindo?"
    show diane f_smirk
    pause
    show daisy f_shy_sad_talk
    daisy "Me desculpe, por favor, não fique bravo!"
    show daisy f_shy_sad
    show diane f_laugh
    dia "Hehe, está tudo bem, querida!"
    hide daisy
    show daisy b_naked_diane_comfort a_empty f_empty at Position (xpos=200)
    show diane b_empty a_empty f_smirk_talk_fardown zorder 1 at Position (xpos=200)
    with dissolve
    dia "Shh, não estamos bravos."
    show diane f_smirk_fardown
    show daisy b_naked_diane_comfort2
    daisy "{b}*Sniff*{/b} você não está bravo?"
    show daisy b_naked_diane_comfort
    show diane f_smirk_talk_fardown
    dia "Claro que não!"
    dia "Você estava apenas curioso, não estava??"
    show diane f_smirk_fardown
    show daisy b_naked_diane_comfort2
    daisy "sim..."
    show diane b_naked a_naked_sides f_smirk at Position (xpos=600)
    hide daisy
    show daisy b_naked a_naked_sides f_normal_talk at flip
    with dissolve
    daisy "Eu nunca vi mais ninguém jogar {b}esconder a doninha{/b} antes..."
    show daisy f_normal
    show player 367f
    player_name "{b}Esconder a doninha{/b}?"
    show player 368f
    show daisy f_normal_talk
    daisy "Mestre e eu também jogávamos!"
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "Sua doninha não era tão grande quanto {b}[firstname]'s{/b} Apesar..."
    show daisy f_normal
    show player 367f
    player_name "Você quer dizer, {b}Jebadiah{/b}estava fazendo sexo com você?!"
    show player 368f
    show diane f_shamed_talk_smile
    dia "{b}*Sigh*{/b} Claro que ele era..."
    dia "... O velho bastardo sujo."
    show diane f_shamed_talk
    show daisy f_normal_talk
    daisy "Não fique chateado {b}Diane{/b}..."
    show daisy f_laugh
    daisy "Mestre só precisava da minha ajuda!"
    daisy "Eu não queria que sua doninha ficasse doente e morresse!"
    show daisy f_normal
    show player 367f
    player_name "Ok, eu estou confuso."
    show player 368f
    show daisy f_normal_talk
    daisy "É por isso que você brinca com {b}[firstname]{/b}, direito?"
    show daisy f_normal
    pause
    show diane f_shamed_talk_smile
    dia "Querida, exatamente o que aquele velho disse a você?"
    show diane f_shamed
    show daisy f_normal_talk
    daisy "Umm, que às vezes a doninha de um homem fica doente e fica dura por todo o lado..."
    show daisy f_normal
    player_name "..."
    show daisy f_normal_talk
    daisy "... E quando isso acontece, ele precisa colocá-lo dentro do esconderijo de uma mulher."
    daisy "Otherwise it turns blue and falls off."
    show daisy f_normal
    pause
    show diane f_shamed_talk_smile
    dia "Bem, ele era um velho bastardo criativo ... eu vou dar isso a ele."
    show diane f_shamed
    show player 367f
    player_name "... Hidey-hole?"
    show player 368f
    show daisy f_normal_talk
    daisy "Sim!"
    hide daisy
    show daisy b_naked_behind f_empty a_empty at Position (xpos=100)
    with dissolve
    show diane f_surprised_front
    daisy "Mestre disse que sua doninha gostava mais do meu esconderijo!"
    show player 430f
    with hpunch
    pause
    show player 66f
    daisy "{b}*Gasp*{/b}"
    hide daisy
    show daisy b_naked a_naked_sides f_sad_talk at flip
    with dissolve
    show diane f_surprised
    daisy "Veja {b}Diane{/b}!"
    daisy "{b}[firstname]'s{/b} doninha está ficando doente novamente!"
    show diane f_surprised_front
    show daisy f_sad
    show player 67f
    pause
    hide daisy
    show daisy b_naked_behind f_empty a_empty at Position (xpos=100)
    with dissolve
    daisy "Você quer usar meu esconderijo desta vez?!"
    show player 430bf
    player_name "Uhh."
    show player 430f
    show diane f_shamed_talk_smile
    dia "Não, não, não..."
    dia "{b}[firstname]'s{/b} {b}*Ahem*{/b} doninha ... vai ficar bem."
    show diane f_shamed
    hide daisy
    show daisy b_naked a_naked_sides f_normal at flip
    with dissolve
    show diane f_shamed_talk_smile
    dia "Agora, acho que você e eu precisamos conversar."
    show diane f_shamed
    show daisy f_normal_talk
    daisy "Oh, okay."
    show daisy f_normal
    show diane f_smirk_talk
    dia "Tenho certeza {b}[firstname]{/b} pode cuidar disso sozinho, você não pode {b}[firstname]{/b}?"
    show diane f_smirk
    show player 432f
    player_name "Sim..."
    show player 431f
    show diane f_smirk_talk
    dia "Por que você não vai para casa durante o dia e nos dá um tempo para garotas."
    show diane f_smirk
    show player 432f
    player_name "Coisa certa."
    show player 431f
    show daisy f_laugh
    daisy "Tchau, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 432f
    player_name "Heh, tchau {b}Daisy{/b}."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_more_jebadiah_delmont_2:
    show player 10b
    player_name "Ainda há algo que eu não entendo, {b}Daisy{/b}."
    show player 5b
    show daisy f_normal
    daisy "Hmm?"
    show player 10b
    player_name "Por que você estava com tanto medo de mim quando apareceu pela primeira vez?"
    show player 5b
    show daisy f_sad_talk
    daisy "Oh."
    show daisy f_surprised_after_appear
    daisy "Umm..."
    pause
    show player 10b
    player_name "Você não precisa me dizer se não quer."
    show player 5b
    show daisy f_sad_talk
    daisy "Não eu-"
    daisy "eu quero."
    show daisy f_sad_talk_closed
    daisy "eu só..."
    pause
    show daisy a_naked_cover with dissolve
    daisy "Eu era uma garota má, {b}[firstname]{/b}!"
    show player 10b
    player_name "Hã?!"
    player_name "Acho difícil imaginar."
    show player 5b
    show daisy f_sad_talk
    daisy "Não, eu estava!"
    show daisy a_naked_sides
    daisy "Você vê, o mestre esqueceu de trancar a cabana uma noite e eu-"
    show daisy f_sad_talk_closed
    daisy "Eu-"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "Eu só queria dar um passeio!"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "Mas eu me perdi..."
    show daisy f_sad
    show player 10b
    player_name "Você fez?"
    show player 5b
    show daisy f_sad_talk
    daisy "Uh huh."
    daisy "Foi tão assustador!"
    daisy "Fiquei perdido por dias sem comida ou água..."
    daisy "... Fiquei perdido por dias sem comida ou água."
    show daisy f_sad
    show player 10b
    player_name "Quem te salvou?"
    show player 5b
    show daisy f_sad_talk
    daisy "Bernice and Jethro."
    daisy "Eles me trouxeram de volta para a casa deles e me deram comida."
    show daisy f_sad
    show player 10b
    player_name "Bem, isso teve sorte."
    show player 5b
    show daisy f_sad_talk
    daisy "isso foi... "
    show daisy a_naked_wiping_tears with dissolve
    daisy "{b}*Sniff*{/b}"
    show daisy a_naked_sides with dissolve
    daisy "Eles eram pessoas muito legais."
    daisy "Mestre achou que não..."
    show daisy f_sad
    player_name "Hmm?"
    show daisy f_sad_talk
    daisy "Ele estava tão bravo comigo!"
    daisy "Eu disse a ele que não queria, mas ele me agarrou pelo braço com muita força e me puxou para fora de casa."
    daisy "Jethro gritou para ele ir com calma e o Mestre bateu nele."
    daisy "De novo e de novo e de novo outra vez."
    daisy "Foi terrível!"
    show daisy f_sad
    show player 10b
    player_name "Que idiota..."
    player_name "Por que ele estava tão bravo?!"
    show player 5b
    show daisy f_sad_talk
    daisy "Ele disse que outras pessoas não eram confiáveis, especialmente homens."
    daisy "Que eles me entregariam ao Gophermant para dar um tapinha na cabeça."
    show daisy f_sad
    show player 10b
    player_name "Gophermant?!"
    show player 5b
    pause
    show player 10b
    player_name "Você quer dizer Government?"
    show player 5b
    show daisy f_sad_talk
    daisy "Sim, é esse."
    show daisy f_sad
    player_name "..."
    show player 10b
    player_name "Então o que aconteceu?"
    show player 5b
    show daisy f_sad_talk
    daisy "Depois disso, o mestre começou a me acorrentar na cabana à noite."
    show daisy f_sad
    show player 10b
    player_name "Ele acorrentou você?!"
    show player 5b
    show daisy f_sad_talk
    daisy "Sim, ele disse que era para o meu próprio bem..."
    daisy "... Que eu era uma garota má."
    show daisy f_sad
    show player 10b
    player_name "Você não é uma garota má, {b}Daisy{/b}."
    player_name "Parece-me que ele era um mau mestre."
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} realmente?"
    show daisy f_sad
    show player 10b
    player_name "Sim."
    player_name "Você definitivamente não merecia ser tratado assim!"
    show player 5b
    show daisy f_sad_talk_closed
    daisy "É difícil dormir quando você está acorrentado."
    show daisy f_sad
    show player 10b
    player_name "eu aposto."
    player_name "Eu gostaria de acorrentá-lo e mostrar como ele se sente!"
    show player 5b
    daisy "..."
    show player 10b
    player_name "É por isso que você estava com medo quando nos viu?"
    show player 5b
    show daisy f_sad_talk
    daisy "Uh huh."
    daisy "Eu estava preocupado mestre iria descobrir."
    show daisy f_sad
    show player 10b
    player_name "Bem, não há necessidade de se preocupar com isso."
    player_name "{b}Diane{/b} e eu não vou deixar ninguém te machucar, nunca mais."
    show player 5b
    return

label daisy_button_how_are_your_flowers_3:
    show player 14b
    player_name "Como estão suas flores?"
    show daisy f_normal_talk
    daisy "Oh, o {b}Sunflowers{/b} você me pegou é tão bonita!"
    daisy "Adoro eles!"
    show daisy f_normal
    show player 14b
    player_name "Isso é ótimo!"
    player_name "Eu tinha a sensação de que eles iriam te animar."
    show player 1b

    daisy "Mmhmm!"
    return

label daisy_button_you_seem_happy:
    show player 14b
    player_name "Você parece muito feliz hoje."
    show player 1b
    show daisy f_normal_talk
    daisy "eu sou!"
    daisy "Muito muito feliz!"
    daisy "Eu moro aqui no belo celeiro e {b}Diane{/b} cuida de mim e você me traz pizza deliciosa..."
    show daisy f_normal
    pause

    show daisy f_normal_talk
    daisy "Estou feliz que você foi quem me encontrou {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "Sim eu também."
    player_name "Eu gosto de te ver feliz, {b}Daisy{/b}!"
    show player 1b
    show daisy f_surprised_after_appear
    daisy "!!!"
    show daisy a_naked_touch with dissolve
    pause
    show player 10b
    player_name "Você está bem?"
    show player 5b
    show daisy f_normal_talk
    daisy "Sim."
    show daisy a_naked_sides with dissolve
    daisy "Às vezes, me sinto engraçado na minha barriga quando você está por perto..."
    show daisy f_normal
    player_name "Hmm?"
    show player 10b
    player_name "Isso doi?"
    show player 5b
    show daisy f_down_talk
    daisy "N-não, parece ... Tudo formigando."
    show daisy f_down
    show player 10b
    player_name "Estranho."
    show player 5b
    return

label daisy_button_want_me_to_milk_you:
    show daisy f_normal_talk
    show player 1b at left
    daisy "Umm, {b}[firstname]{/b}?"
    show daisy f_normal
    show player 14b
    player_name "Sim?"
    show player 1b
    show daisy f_normal_talk
    daisy "você poderia me ordenhar?"
    show daisy f_down_talk b_naked_boob a_empty with dissolve
    daisy "Porque meus peitos estão cheios de novo."
    show daisy f_down
    pause
    show player 14b
    player_name "{b}*Gulp*{/b} certo."
    hide player
    show daisy b_player_milking a_empty f_down
    with dissolve
    daisy "!!!"
    player_name "Isso parece bom?"
    show daisy f_down_talk
    daisy "Sim."
    show daisy f_down
    player_name "Apenas relaxe e aproveite, {b}Daisy{/b}."
    return

label daisy_button_finished_milking_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh a_naked_up
    with dissolve
    daisy "{b}*Gasp* [firstname]{/b}!!!"
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Oi, {b}Daisy{/b}."
    show player 1b
    show daisy f_normal_talk
    daisy "O que vamos fazer hoje?!"
    show daisy f_normal
    show player 14b
    player_name "Ainda não sei."
    show player 1b
    return

label daisy_button_daisy_need_milking:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Ok, eu estou pronto!"
    show daisy f_normal
    show player 10b
    player_name "posso te perguntar uma coisa?"
    show player 5b
    daisy "Hmm?"
    show player 10b
    player_name "Como você quer que eu-"
    player_name "{b}*Ahem*{/b} ordenhe você?"
    show player 5b
    show daisy f_normal_talk
    daisy "Bem, {b}Diane{/b} diz que você é melhor nisso do que ela e..."
    show daisy f_down_talk
    daisy "... E eu..."
    show daisy f_down
    pause

    show daisy f_down_talk
    daisy "... você me faz..."
    daisy "... Não sei."
    show daisy f_laugh
    show player 14b
    player_name "Umm, ok."
    show daisy f_normal
    player_name "Acho que devemos começar, hein?"
    show player 1b
    pause
    hide player
    show daisy b_player_milking a_empty f_down
    with dissolve
    daisy "!!!"
    player_name "Isso parece bom?"
    show daisy f_down_talk
    daisy "Sim."
    show daisy f_down
    player_name "Deixe-me saber se eu faço algo que não faz, ok?"
    show daisy f_normal_smelling
    daisy "Mmmhmm."
    pause
    show daisy f_down_talk
    daisy "{b}Diane{/b} estava certo, você é realmente bom nisso!"
    show daisy f_down
    player_name "Heh, obrigado."
    show daisy f_down_talk
    daisy "Ahh!"
    show daisy f_down
    player_name "Apenas relaxe e aproveite, {b}Daisy{/b}."
    return

label daisy_button_get_new_flowers_has_flowers:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_naked_shy_front b_naked_shy f_shy_sad at Position (yoffset=10)
    with dissolve
    player_name "Oi, {b}Daisy{/b}."
    show player 1b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Oi, {b}[firstname]{/b}."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 14b
    player_name "Eu tenho uma coisa para você."
    show player 1b
    daisy "Hmm?"
    show player 239_240 with dissolve
    pause
    show player 722 with dissolve
    pause
    show daisy f_normal_talk b_naked a_naked_cover with dissolve
    daisy "{b}*Gasp*{/b} Wowzers!!!"
    show player 1b
    show daisy a_naked_sunflower1 f_down_talk
    with dissolve
    daisy "Veja como são grandes e bonitas!"
    pause
    show daisy a_naked_sunflower2 f_normal_smelling with dissolve
    daisy "Mmm!"
    show daisy b_naked_hug f_empty a_empty
    hide player
    with dissolve
    daisy "Obrigado, obrigado, obrigado!!!"
    show player 14b at left
    show daisy a_naked_sunflower1 b_naked f_down zorder 1 at Position (xpos=300)
    with dissolve
    player_name "Heh, de nada."
    show player 1b
    show daisy f_down_talk
    daisy "Como são chamadas essas flores?"
    show daisy f_down
    show player 14b
    player_name "Aqueles são chamados {b}Sunflowers{/b}."
    show player 1b
    show daisy f_normal_talk
    daisy "Por que eles os chamam assim?"
    show daisy f_normal
    show player 14b
    player_name "Hmm, provavelmente por causa de sua cor amarela."
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, entendi."
    show daisy f_laugh
    daisy "Como o sol!"
    show daisy f_down
    show player 14b
    player_name "Heh, está certo."
    show player 1b
    show daisy f_laugh
    daisy "Hehe!"
    show daisy f_normal
    show diane b_shirtless a_shirtless_sides f_shamed_talk_fardown at Position (xpos=600) with dissolve
    show player 13
    dia "Oh, você recebeu novas flores?"
    show diane f_shamed_fardown with None
    show daisy f_laugh at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "{b}[firstname]{/b} me trouxe um pouco!"
    show daisy f_down
    show diane f_smirk_talk
    dia "Bem, não foi tão gentil da parte dele..."
    show diane f_smirk
    show daisy f_normal_talk
    daisy "Uh huh!"
    daisy "{b}[firstname]{/b} é o homem mais legal de todos os tempos!"
    show daisy f_down
    show diane f_smirk_talk
    dia "Ele certamente é."
    show diane f_smirk
    pause
    show diane f_shamed_talk_fardown
    dia "Tudo bem, devemos colocar essas flores em um pouco de água para que eu possa ordenha-lo, querida."
    dia "Muito trabalho a ser feito hoje."
    show diane f_shamed_fardown with None
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "eu quero {b}[firstname]{/b} fazer isso."
    show player 11
    player_name "!!!" with hpunch
    show player 10b
    player_name "o que?"
    show player 5b
    show daisy f_normal_talk
    daisy "Tudo bem se {b}[firstname]{/b} me ordenha, {b}Diane{/b}?"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "Está bem comigo."
    show diane f_shamed_fardown with None
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show diane f_smirk
    daisy "Você vai me ordenhar, {b}[firstname]{/b}?"
    show daisy f_normal
    show player 14b
    player_name "Uhh, claro ... Se é isso que você quer."
    show player 1b
    show daisy f_laugh
    daisy "Yay!!"
    show daisy f_normal
    show diane f_smirk_talk
    dia "Apenas tenha cuidado com ela, ok?"
    show diane f_smirk
    show player 14
    player_name "sim, eu irei."
    show player 13
    show diane f_shamed_talk_fardown
    dia "Tudo bem, vamos cuidar dessas flores."
    show diane f_shamed_fardown
    show daisy f_shy_talk_back
    daisy "Ok."
    show daisy f_normal_talk
    daisy "eu volto já, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "ok."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_get_new_flowers_no_flowers:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy a_naked_cover f_sad_talk_closed
    with dissolve
    player_name "Você está bem?"
    show player 5b
    show daisy a_naked_wiping_tears with dissolve
    daisy "Sim."
    show daisy a_naked_shy_front b_naked_shy f_shy_sad_talk at Position (yoffset=10) with dissolve
    daisy "Só sinto falta das minhas flores..."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Eu sinto Muito, {b}Daisy{/b}."
    player_name "Posso pegar algo para você?"
    player_name "Eu não gosto de ver você triste assim..."
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Não, está tudo bem."
    show daisy f_shy_sad at Position (yoffset=10)
    pause
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Obrigado, {b}[firstname]{/b}."
    hide daisy with dissolve
    show player 5
    player_name "( Hmm, eu deveria ir para {b}Cupid{/b} e {b}the Mall{/b} e {b}dê-lhe algumas flores novas{/b}. )"
    show player 13
    player_name "( Aposto que vai animá-la. )"
    pause
    player_name "( {b}Diane{/b} disse que eu deveria procurar {b}Girassóis{/b}. )"
    hide player with dissolve
    return

label daisy_button_sleeping:
    show player 434 with dissolve
    player_name "( Ah, olha como ela é fofa quando está dormindo! )"
    player_name "( Eu deveria deixá-la ser. )"
    hide player with dissolve
    return

label daisy_button_no_veggie_pizza:
    show player 1b
    show daisy f_normal_talk
    daisy "Você me trouxe outra {b}veggie pizza{/b}?"
    show daisy f_normal
    show player 10b
    player_name "Não, hoje não."
    show player 5b
    show daisy f_sad_talk
    daisy "Aww..."
    show daisy f_sad
    show player 10b
    player_name "Desculpa, {b}Daisy{/b}..."
    player_name "... Talvez amanhã, tudo bem?"
    show player 5b
    show daisy f_sad_talk
    daisy "Ok."
    show daisy f_sad
    return

label daisy_button_has_veggie_pizza:
    show player 14b
    player_name "Te trouxe uma coisa!"
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} Um presente?!"
    show daisy f_normal
    player_name "Mmmhmm."
    show player 239_240 with dissolve
    pause
    show player 719c with dissolve
    show daisy f_normal_talk
    daisy "{b}Veggie pizza{/b}?!"
    show daisy f_normal
    show player 719d
    player_name "Hehe, está certo!"
    show player 719c
    show daisy f_laugh
    daisy "Yay!!"
    show daisy f_normal
    show player 721 with dissolve
    pause
    show player 18
    show daisy a_naked_pizza_slice
    with dissolve
    pause
    show daisy f_laugh a_naked_up with dissolve
    daisy "Eu amo pizza!!"
    show player 17
    player_name "Eu também!"
    show player 1b
    show daisy a_naked_pizza_eat with dissolve
    pause
    daisy "Mmm!"
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_more_jebadiah_delmont:
    show player 10b
    player_name "Então, você acha que está pronto para me contar mais sobre seu antigo mestre?"
    show player 5b
    show daisy f_shy_sad_talk a_naked_shy_front b_naked_shy at Position (yoffset=10) with dissolve
    daisy "Mmm, talvez..."
    daisy "O que você quer saber?"
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Como ele era?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Hmm, Mestre era..."
    daisy "... Diferente do que você e {b}Diane{/b}."
    daisy "Ele não se dava muitobem com outras pessoas, mas também não queria ficar sozinho.."
    daisy "Então ele me fez."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Ele fez você?"
    show player 5b
    daisy "Mmhmm."
    show player 10b
    player_name "Como ele fez isso?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Eu não sei..."
    show daisy f_normal_talk b_naked a_naked_sides with dissolve
    daisy "... Talvez ele tenha usado suas mágicas?"
    show daisy f_normal
    pause
    show player 14b
    player_name "Então você realmente o viu fazer mágica então?"
    show player 1b
    show daisy f_laugh
    daisy "Oh sim, mágicas maravilhosas!"
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "Ele poderia remover o polegar ou retirar dinheiro da minha orelha sempre que quisesse!"
    show daisy f_normal
    show player 5b
    player_name "..."
    show daisy f_normal_talk
    daisy "Ele tinha uma nuvem de tempestade que ele prendeu dentro de uma vara!"
    show daisy f_normal
    show player 10b
    player_name "Hã?"
    show player 5b
    show daisy f_normal_talk
    daisy "Sim, se você virou de cabeça para baixo, podia ouvir chovendo por dentro!"
    show daisy f_normal
    player_name "..."
    show daisy f_laugh
    daisy "Oh, oh, oh, e ele tinha uma bola de vidro cheia de neve do pólo norte!"
    show daisy f_normal
    show player 10b
    player_name "Deixe-me adivinhar, você tinha que sacudir e depois a neve cairia?"
    show player 5b
    show daisy f_normal_talk
    daisy "Sim!"
    show daisy f_shy_talk
    daisy "Como você soube disso?!"
    show daisy f_shy
    show player 14b
    player_name "Eles são chamados globos de neve."
    show player 1b
    show daisy f_sad_talk
    daisy "{b}*Gasp*{/b} Você conhece magia também?!"
    show daisy f_sad
    show player 10b
    player_name "{b}Daisy{/b}, Eu não acho que nada disso foi mágico..."
    show player 5b
    show daisy f_normal_talk
    daisy "E a varinha dele então?!"
    show daisy f_normal
    show player 10b
    player_name "Varinha?"
    show player 5b
    show daisy f_normal_talk
    daisy "Sim, faria um som clicável e, em seguida, o fogo sairia da ponta!"
    show daisy f_laugh
    daisy "Definitivamente eram mágicas!"
    show daisy f_normal_talk
    daisy "eu vi."
    show daisy f_normal
    player_name "..."
    return

label daisy_button_milking_business:
    show player 14b
    player_name "Então você gosta quando {b}Diane{/b} ordenha você?"
    show player 1b
    show daisy f_normal_talk
    daisy "Oh, sim!"
    show daisy f_laugh a_naked_up with dissolve
    daisy "Ordenha faz meus peitos se sentirem bem!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "Além disso, ela é muito mais gentil do que a Mestra..."
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "... Eu só queria que não me fizesse cócegas!"
    show daisy f_normal
    show player 14b
    player_name "Tenho certeza que ela descobrirá uma maneira de fazer isso sem fazer cócegas em você."
    show player 1b
    show daisy f_normal_talk
    daisy "acredito que sim."
    daisy "eu quero {b}Diane{/b} vender meu leite também e fazer as pessoas felizes!"
    show daisy f_normal
    return

label daisy_button_how_are_your_flowers_2:
    show player 14b
    player_name "Como estão suas flores?"
    show player 1b
    show daisy f_normal_talk
    daisy "Eles ainda estão indo bem."
    daisy "Eu dou água e luz solar todos os dias, exatamente como você me disse."
    show daisy f_normal
    show player 14b
    player_name "Isso é maravilhoso, {b}Daisy{/b}."
    show player 1b
    daisy "Mmhmm."
    show daisy f_normal_talk
    daisy "{b}Diane{/b} diz que há muitas flores no mundo e elas também vêm em todos os tipos de cores diferentes!"
    daisy "Isso é verdade?"
    show daisy f_normal
    show player 14b
    player_name "Sim, é verdade."
    show player 1b
    show daisy f_laugh a_naked_cover with dissolve
    daisy "Wowzers!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "Espero ver todos eles algum dia..."
    show daisy f_normal
    return

label daisy_button_finished_pizza_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_normal_talk
    daisy "Oi, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Oi, {b}Daisy{/b}."
    player_name "Como você está hoje?"
    show player 1b
    show daisy f_sad_talk
    daisy "Mmm, eu estou entediado."
    show daisy f_normal_talk
    daisy "O que você está fazendo?"
    show daisy f_normal
    return

label daisy_button_get_pizza_has_not_pizza:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Pizza!"
    daisy "Hehehe!"
    show daisy f_normal
    show player 14b
    player_name "Heh, ela está tão animada."
    player_name "Eu deveria ir para {b}Tony's Pizzeria{/b} e levá-la a {b}veggie pizza{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_pizza_has_pizza:
    scene expression player.location.background_blur with None
    show player 719d at left
    show daisy
    with dissolve
    player_name "{b}Daisy{/b}?"
    player_name "Olha o que eu trouxe para você!"
    show player 719c
    show daisy f_laugh
    daisy "Pizza?!"
    show daisy f_normal
    show player 720 with dissolve
    player_name "Mmmhmm!"
    show daisy f_normal_talk
    daisy "Oh, cheira muito bem!"
    show daisy f_normal
    pause
    show daisy f_sad_talk
    daisy "Como eu como?"
    show daisy f_sad
    show player 720b
    player_name "Hehe, deixa eu te mostrar."
    show daisy f_normal
    show player 721 with dissolve
    player_name "Você apenas segura assim e começa a comer desse lado aqui."
    show player 719d with dissolve
    player_name "Mmm, tão bom!!"
    show player 719c
    pause
    show player 719d
    player_name "Agora você tenta."
    show daisy a_naked_pizza_hold f_normal_talk
    show player 1b
    with dissolve
    daisy "Ok."
    show daisy a_naked_pizza_slice f_sad_talk with dissolve
    daisy "Como isso?"
    show daisy f_normal
    show player 14b
    player_name "Sim, assim mesmo."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*Gasp*{/b} Wowzers !!! Minha primeira pizza!"
    show daisy f_normal
    show player 17 with dissolve
    player_name "Hehe!"
    show player 1b
    show daisy a_naked_pizza_eat f_empty with dissolve
    daisy "Mmmhmm!!!"
    show player 11
    player_name "!!!" with hpunch
    pause
    daisy "Mais!"
    show player 10b
    player_name "Sim, coma o quanto quiser..."
    hide player
    hide daisy
    with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene13.jpg"
    show expression FilteredText("A pizza acabou ainda melhor do que eu esperava. Até hoje, nunca vi ninguém jogar comida como {b}Daisy{/b}.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("{b}Daisy{/b} passou por oito pedaços no tempo que me levou a comer dois!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy o_sauce f_burp
    with dissolve
    daisy "{b}*Buuuuurp*{/b}"
    show daisy f_normal
    show player 14b
    player_name "Heh, você está bem lá?"
    show player 1b
    show daisy f_laugh
    daisy "Isso foi tão delicioso!!"
    show daisy f_normal_talk
    daisy "Posso comer pizza todos os dias?!"
    show daisy f_normal
    show player 17
    player_name "Haha, eu não acho que seria uma boa ideia..."
    show player 1b
    show daisy f_sad_talk
    daisy "Oh."
    show daisy f_sad
    show player 14b
    player_name "... mas eu posso trazer alguns de vez em quando."
    show player 1b
    show daisy f_laugh a_naked_up with dissolve
    daisy "Yay!"
    daisy "Eu adoro pizza!"
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Hehe, eu também!"
    show player 433
    show daisy f_normal_talk
    daisy "Obrigado, {b}[firstname]{/b}!"
    hide player
    show daisy b_naked_hug f_empty a_empty o_empty
    with dissolve
    player_name "de nada, {b}Daisy{/b}."
    show daisy f_normal_talk o_sauce b_naked a_naked_sides
    show player 1b at left
    with dissolve
    daisy "Eu vou ver se {b}Diane{/b} quer pizza também!"
    hide daisy with dissolve
    show player 13
    pause
    show player 14
    player_name "É melhor você dizer a ela para se apressar, restam apenas algumas fatias!"
    show player 13
    pause
    show player 18
    player_name "( Estou muito feliz por ter feito isso. )"
    player_name "( {b}Daisy{/b} é tão fofo quando ela está feliz. )"
    show player 13
    pause
    show player 426
    player_name "( Tudo bem, é melhor eu terminar aqui e trabalhar no jardim antes de ficar sem luz do dia. )"
    hide player with dissolve
    return

label daisy_button_leave:
    show player 14b at left
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    else:
        show daisy f_normal
    player_name "Eu deveria voltar ao trabalho."
    player_name "Deixe-me saber se você precisar de alguma coisa, ok?"
    show player 1b
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy_shy_talk at Position (yoffset=10)
    else:
        show daisy f_normal_talk
    daisy "Ok."
    daisy "Tchau, {b}[firstname]{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_jebadiah_delmont:
    show player 10b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "So your old master doesn't sound like a very nice guy, huh?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Mmm, ele {i}could{/i} seja legal ... as vezes."
    daisy "When I was a good girl."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Oh?"
    show player 5b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Ele me trazia presentes e me ensinava músicas."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Bem, isso não parece tão ruim..."
    show player 5b
    show daisy f_shy_sad_talk a_naked_shy_cover at Position (yoffset=10) with dissolve
    daisy "Desde que eu ficasse quieta na cabana e não tocasse nas coisas dele, eu era uma boa garota."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "O que aconteceu se você deixou a cabana?"
    show player 5b
    show daisy f_shy_sad_talk_closed at Position (yoffset=10)
    daisy "Eu não-"
    daisy "ele faria-"
    show daisy b_naked a_naked_cover f_sad_talk_closed with dissolve
    pause
    show player 10b
    player_name "Você quer falar sobre isso??"
    show player 5b
    daisy "Não, por favor não!"
    show player 10b
    player_name "Está tudo bem, não precisamos-"
    show player 433
    daisy "Não, não, não, não-"
    show player 10b
    player_name "{b}Daisy{/b}, está bem..."
    player_name "Não precisamos conversar sobre ele, se você não quiser."
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} Eu sou uma boa garota?"
    show daisy f_sad
    show player 14b
    player_name "Claro!"
    show player 10b
    player_name "Eu não queria incomodá-lo, eu-"
    show player 5b
    pause
    show player 14b
    player_name "Você não precisa se preocupar, {b}Daisy{/b}."
    player_name "{b}Diane{/b} e eu nunca te machucaria."
    show player 1b
    show daisy f_shy_sad_talk a_naked_shy_front b_naked_shy at Position (yoffset=10) with dissolve
    daisy "Ok."
    show daisy f_shy_sad at Position (yoffset=10)
    return

label daisy_button_about_yourself:
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "Fale-me sobre você."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Eu?!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Sim, eu gostaria de saber mais sobre você."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Eu não-"
    daisy "Não tem muito-"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Existe algo que você goste?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Umm, flores?"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 17
    player_name "Heh, qualquer coisa além de flores?"
    show player 1b
    show daisy f_shy_down at Position (yoffset=10)
    daisy "Hmm."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Aveia!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Aveia?"
    show player 5b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Sim, o Mestre costumava me alimentar aveia o tempo todo."
    show daisy f_shy_laugh at Position (yoffset=10)
    daisy "Era gostoso!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "O que é {b}Diane{/b} te alimentando?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oh, muitas coisas..."
    daisy "Ela diz que eu deveria tentar outras coisas e não apenas comer aveia o tempo todo."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Ela está certa."
    player_name "O que você tentou até agora?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Mmm,Mmm, eu tentei alface, cenoura, uvas, bopples-"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Bopples?"
    player_name "O que é um bopple?"
    show player 1b
    show daisy f_shy_down_talk at Position (yoffset=10)
    daisy "Umm, eles são vermelhos e crocantes e fazem minha língua parecer engraçada."
    show daisy f_shy_shy at Position (yoffset=10)
    player_name "Hmm?"
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "{b}Diane{/b} diz que é porque eles são doces."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Você quer dizer uma maçã?"
    show player 1b
    show daisy f_shy_laugh at Position (yoffset=10)
    daisy "Sim é isso!"
    show daisy f_shy_down_talk at Position (yoffset=10)
    daisy "Maçã."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Também era gostoso, mas a aveia é muito melhor!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Heh, ok."
    show player 1b
    return

label daisy_button_how_are_your_flowers_1:
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "Como estão suas flores?"
    player_name "Você os observou de perto?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Sim, muito de perto!"
    daisy "{b}Diane{/b} estava certo, eles bebem a água!"
    daisy "É tão legal!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 17
    player_name "Hehehe."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Você quer vê-los comigo?!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Uhh, não ... desculpe {b}Daisy{/b}, Eu tenho muito trabalho a fazer por aqui."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oh, ok."
    show daisy f_shy_shy at Position (yoffset=10)
    return

label daisy_button_still_nervous:
    show player 14b
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "Eu ainda te deixo nervoso, hein?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "sim, um pouco."
    show daisy f_shy_shy at Position (yoffset=10)
    pause
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Desculpa."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Heh, você não precisa se desculpar."
    player_name "Está tudo bem, eu entendo."
    show player 1b
    pause
    show player 14b
    player_name "Não há pressa."
    show player 1b
    return

label daisy_button_intro_scared:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy b_naked_behind_sad f_empty a_empty
    with dissolve
    player_name "Oi ai-"
    show player 11
    show daisy b_jump_scared
    cow "EEEEP!!!" with hpunch
    show daisy b_naked a_naked_cover f_sad_talk_closed
    pause
    show player 24
    dia "{b}[firstname]{/b}!"
    show diane b_naked a_naked_sides f_shamed_talk_smile at Position (xpos=600)
    dia "Ela ainda está com medo de você!"
    show diane f_shamed
    show player 25
    player_name "Me desculpe, eu não quis assustá-la."
    show player 24
    show diane f_shamed_talk_smile
    dia "Está tudo bem."
    dia "Apenas me dê um pouco mais de tempo com ela, ok?"
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "{b}Avisarei quando ela estiver pronta para falar com você.{/b}"
    show diane f_shamed
    show player 25
    player_name "Ok."
    hide player with dissolve
    return

label daisy_button_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    with dissolve
    player_name "Oi, {b}Daisy{/b}."
    show player 1b
    daisy "..."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oi."
    show daisy f_shy_shy at Position (yoffset=10)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
