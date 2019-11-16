label button_okita_ingredients_mushroom:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "O {b}Cogumelo Falicum{/b} crescer na floresta aqui em Summerville ".
    show okita 3
    okita "Eles são fáceis de detectar por causa de sua forma fálica ".
    show player 10
    show okita 1
    player_name "... Bruto."
    return

label button_okita_ingredients_toad:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "É época de reprodução para o {b}Sapo com tesão{/b}. Então procure um no {b}lago ou riacho.{/b}"
    okita "Eles devem ser facilmente identificáveis ​​pelas partes traseiras roxas e grumosas ".
    show player 10
    show okita 1
    player_name "Parece um sapo feio ... "
    return

label button_okita_ingredients_flower:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "A {b}Eufórbia psicotrópica{/b} é uma flor luminescente que cresce apenas em lugares escuros ".
    okita "Sua melhor aposta seria uma {b}caverna{/b}."
    show player 35
    show okita 1
    player_name "Hmm, uma {b}caverna{/b}..."
    return

label button_okita_ingredients_stock:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "Precisamos de algo moderado para atuar como base para o soro. O estoque de vegetais funcionaria melhor."
    okita "Você deve conseguir alguns itens no Consumr."
    show player 2
    show okita 1
    player_name "... Pelo menos um dos ingredientes é simples. "
    return

label button_okita_ingredients_tissue:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "Uma amostra de cabelo ou saliva funcionaria melhor ".
    show player 10
    show okita 1
    player_name "Sim, ok, mas como vou conseguir isso? "
    show player 11
    show okita 9
    okita "... Tenho certeza que você pensará em algo. "
    show okita 4
    player_name "..."
    return

label button_okita_got_all_ingredients:
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "Tudo bem senhora, acho que tenho tudo ".
    show player 1
    show okita 3
    okita "... Você pensa?"
    show okita 1
    show player 533 with dissolve
    player_name "Bem, há um pequeno problema ... "
    show okita 3
    show player 532
    okita "... É aquele {b}Caldo de galinha{/b}?"
    show player 533
    show okita 1
    player_name "Sim. É tudo {b}Consumr{/b} teve..."
    player_name "Eu pensei, talvez o {b}Caldo de galinha{/b} ainda funcionaria? "
    show player 532
    show okita 2b
    okita "Hah, sim. Isso deveria estar bem..."
    show player 11 with dissolve
    show okita 6
    player_name "..."
    show okita 7
    okita "Parece que tudo está em ordem. "
    okita "Encontre-me no meu escritório esta noite e começaremos a mixar."
    show player 10
    show okita 6
    player_name "Esta noite?"
    show player 11
    show okita 3
    okita "Problema?"
    show player 10
    show okita 4
    player_name "Não! ... Não. Vejo você então. "

    return

label button_okita_extract_cum:
    scene location_school_science_closeup
    show player 10 at left
    show okita 4 at right
    player_name "Então, temos tudo o que precisamos para fazer seu soro? "
    show player 11
    show okita 5
    okita "... Sim. Não foi isso que eu te disse ?! "
    okita "{b}Encontre-me no meu escritório esta noite{/b} e para que possamos trabalhar nisso ".
    show okita 4
    show player 10
    player_name "... O-okay."
    return

label button_okita_dose_smith:
    scene location_school_science_closeup
    show player 1 at left
    show okita 5 at right
    with dissolve
    okita "Você ainda não administrou {b}Principal Smith{/b}?!"
    show player 5
    show okita 4
    player_name "..."
    show okita 5
    okita "O que você está esperando?"
    show player 12
    show okita 4
    player_name "Isso não é exatamente fácil, você sabe! "
    player_name "Você não pode me dar alguns conselhos ou algo assim ?!"
    show player 16
    show okita 3
    okita "Aqui estão alguns conselhos: Apresse-se e faça já! "
    show okita 5
    okita "Tudo que você tem a fazer é {b}colocá-lo em sua comida ou algo assim{/b}."
    show player 12
    show okita 4
    player_name "Tudo bem, tudo bem. Eu voltarei."
    return

label button_okita_wait_for_smith_serum:
    scene location_school_science_closeup
    show player 2 at left
    show okita 6 at right
    player_name "Tudo bem, {b}Miss Okita{/b}. Está feito."
    show player 1
    show okita 7
    okita "Maravilhoso!"
    okita "Agora esperamos para ver os efeitos ..."
    show player 10
    show okita 6
    player_name "Quanto deve demorar?"
    show player 11
    show okita 7
    okita "Vai funcionar rápido. Por que você não fica por aqui e a veremos depois da aula? "
    show player 2
    show okita 6
    player_name "Certo."
    pause 1
    hide player
    hide okita
    scene black
    with dissolve
    scene location_school_lounge_day_blur
    show okita 5f zorder 1 at Position(xpos=0.3, ypos=1.0)
    show player 11 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show principal 33 at right
    with dissolve
    okita "*ahem*"
    show okita 4f
    show principal 32 with dissolve
    smi "Hmm? Oh, olá Tori ... "
    smi "Como está a pequena senhorita Knowitall hoje?"
    show principal 31
    okita "... Hmmph."
    show okita 3f
    okita "Eu estava apenas checando o status do meu escritório? "
    show okita 4f
    show principal 32
    smi "Seu escritório?"
    show okita 5f
    show principal 31
    okita "Bem, outro dia você parecia bastante adoravel em mudar as fechaduras. "
    show okita 4f
    show principal 32
    smi "Eu estava? "
    smi "Isso é engraçado ... não me lembro."
    show okita 3f
    show principal 31
    okita "Sério?"
    smi "..."
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "Bawk bawk."
    show principal 31 at right with dissolve
    show okita 8f
    show player 10
    okita "..."
    show okita 3f
    okita "... Você está bem?"
    show okita 4f
    show principal 32
    smi "... Hã?"
    smi "Eu estou bem, por quê?"
    show player 11
    show okita 5f
    show principal 31
    okita "Você estava dizendo alguma coisa, a respeito da fechadura do meu escritório? "
    show okita 4f
    show principal 32
    smi "Eu estava? "
    smi "Isso é engraçado ... eu não-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "BAWK!!! Bawk bawk bawk..."
    show principal 31 at right with dissolve
    show okita 6f
    show player 10
    player_name "Uhh..."
    show okita 9f
    show player 11
    okita "Shh!"
    show principal 33 with dissolve
    okita "Não nos interrompa {b}[firstname]{/b}."
    show okita 4f
    show principal 32 with dissolve
    smi "... Este café tem um gosto engraçado. "
    show principal 31
    player_name "..."
    show okita 7f
    okita "Eu contei sobre a nova invenção em que estava trabalhando? "
    show okita 6f
    show principal 32
    smi "Invenção?"
    smi "Não, eu não acho que você-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "Bawk bawk..."
    smi "Bawk bawk BAWK!!"
    show principal 31 at right with dissolve
    show okita 7f
    okita "Vou ter que levá-lo ao seu escritório algum dia. É realmente fascinante! "
    show principal 32
    show okita 6f
    smi "Claro, tudo bem! "
    show okita 7f
    show principal 31
    okita "Oh meu Deus, olha a hora. "
    okita "Nós realmente deveríamos ir."
    show okita 7 at Position(xpos=0.05, ypos=1.0) with dissolve
    okita "Venha comigo, {b}[firstname]{/b}."
    hide okita with dissolve
    player_name "..."
    show principal 32

    smi "... Este café tem um gosto engraçado. "


    hide principal
    hide okita
    hide player
    scene black
    with dissolve
    scene location_school_science_closeup
    show player 11 at left
    show okita 7 at right
    okita "Então eu acho que {b}Caldo de galinha{/b} criou um efeito colateral, afinal ... "
    show okita 2b
    okita "Pffft, hahaha!!"
    show player 12
    show okita 6
    player_name "Como isso é engraçado ?! "
    player_name "Nós ferramos com a cabeça dela e ela está lá cacarejando como uma galinha!"
    show player 11
    show okita 2b
    okita "Sim, ela é! Hahaha! "
    show player 16
    show okita 7
    okita "Oh, você relaxaria? "
    okita "É apenas temporário."
    show okita 9
    okita "... Eu acho que."
    show player 12
    show okita 6
    player_name "Você pensa?!"
    show player 16
    show okita 9
    okita "Quero dizer, tenho certeza. "
    show okita 7
    okita "Quero dizer, tenho certeza: "Veja o importante aqui é que o soro funcionou!"
    okita "Ela é completamente imparcial com meus experimentos agora!"
    okita "... E ela nem se lembrava de querer me trancar fora do meu escritório!"
    show player 12
    show okita 6
    player_name "Sim, mas ela está cacarejando como uma galinha! "
    show player 16
    show okita 2b
    okita "Pffftt, hahahaaaah!"
    show player 12
    player_name "Bem, eu estou feliz que você acha isso tão engraçado ... "
    show okita 6
    player_name "E agora?"
    show player 16
    show okita 7
    okita "Agora, preciso de um tempo para estudar os efeitos do outro soro ".
    show player 10
    show okita 6
    player_name "Ah, eu esqueci completamente do outro soro! "
    player_name "Você está se sentindo diferente?"
    show player 11
    show okita 7
    okita "Mmm, talvez ... "
    show okita 2b
    okita "Hehehe!"
    show player 10
    player_name "Você parece meio diferente. "
    show player 11
    show okita 7
    okita "Como assim?"
    show player 10
    show okita 6
    player_name "Você é como ... Giddy. "
    show player 11
    show okita 2b
    okita "Hehehe! Estou apenas feliz."
    show player 10
    player_name "Está meio que me assustando para ser honesto. "
    show player 11
    show okita 7
    okita "... E quente."
    show okita 3
    okita "Você é gostosa? Está quente aqui!"
    show player 10
    show okita 6
    player_name "Não, eu estou bem."
    show player 11
    show okita 7
    okita "Tudo bem, bem, eu vou para o meu escritório e fazer algum trabalho. "
    okita "Venha me ver em alguns dias."
    show player 10
    show okita 6
    player_name "Umm, ok. "
    show player 11
    show okita 2b
    okita "Tchau, {b}[firstname]{/b}!"
    okita "Hehehehe..."
    hide okita with dissolve
    hide player
    show player 10f
    with dissolve
    player_name "Espero que ela fique bem ... "
    return

label button_okita_wait_for_okita_serum:
    scene location_school_science_closeup
    show player 10 at left
    show okita 6 at right
    with dissolve
    player_name "Você está bem, senhora? "
    player_name "Você já notou algum efeito colateral com o seu soro?"
    show player 11
    show okita 7
    okita "Eu ainda estou testando. "
    okita "... eu agradeço que você tenha me consultado."
    show player 10
    show okita 6
    player_name "... Você faz?"
    show okita 7
    show player 11
    okita "Claro!"
    show okita 2b
    okita "Isso me faz sentir quente e confuso! "
    show player 11
    show okita 6
    player_name "..."
    show player 10
    player_name "Ok, sério! Você está agindo muito estranho! "
    show player 11
    show okita 7
    okita "Sou eu? "
    show okita 2b
    okita "Eu não sei o que te dizer. Eu me sinto ótimo!"
    show player 10
    show okita 6
    player_name "Ok, bem, tenha cuidado, eu acho. "
    show player 11
    show okita 7
    okita "Vai fazer, bonito! "
    show okita 2b
    okita "Hehehe!"
    player_name "..."
    return

label button_okita_serum_effects:
    scene location_school_science_closeup
    show player 10 at left
    show okita 6 at right
    with dissolve
    player_name "Algum resultado do soro ainda? " 
    show player 11
    show okita 7
    okita "Na realidade, {b}[firstname]{/b}, Eu estava esperando que você pudesse me ajudar a testar minha mais nova invenção? "
    show player 10
    show okita 6
    player_name "Oh cara, você quer que eu construa outra coisa? "
    show player 11
    show okita 3
    okita "Hmm? Não não!"
    show okita 7
    okita "Eu mesmo construí este. É revolucionário! "
    show player 10
    show okita 6
    player_name "Você construiu? "
    player_name "Mas construir é trabalho de macaco. Pensei que você não fizesse trabalho de macaco."
    show player 11
    show okita 7
    okita "Desta vez fiz uma exceção porque ... "
    okita "Bem, eu fiz esta invenção para você; como uma surpresa."
    show player 10
    show okita 6
    player_name "Para mim?"
    show player 11
    show okita 7
    okita "Sim, venha ao meu escritório hoje à noite depois da escola e eu mostro a você. "
    show player 10
    show okita 7
    player_name "Isso está começando a me preocupar ... "
    player_name "O que você está fazendo?"
    show player 11
    show okita 2b
    okita "Não seja um bebê! Você tem que vir e ver! "
    show player 10
    show okita 6
    player_name "Bem."
    show player 11
    show okita 7
    okita "Você promete? "
    show player 10
    show okita 6
    player_name "Uhh, sim. "
    player_name "... eu prometo."
    show player 11
    show okita 2b
    okita "Yay!"
    show okita 7
    okita "Te vejo em breve, {b}[firstname]{/b}!"
    hide okita with dissolve
    hide player
    show player 11f
    with dissolve
    player_name "..."
    return

label button_okita_generic_after_q3:
    call expression game.dialog_select("button_okita_generic_after_q3_intro")
    menu:
        "Nova invenção." if M_okita.is_state(S_okita_is_hypersexual):
            call expression game.dialog_select("button_okita_generic_after_q3_new_invention")

        "As armadilhas são gays?" if False:
            call expression game.dialog_select("button_okita_are_traps_gay")
        "Nada.":

            call expression game.dialog_select("button_okita_generic_after_q3_leave")
    return

label button_okita_generic_before_q3:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Ei, {b}Miss Okita{/b}."
    show player 1
    show okita 5
    okita "O que é isso, {b}[firstname]{/b}?"
    show player 11
    okita "Eu estou muito ocupado..."
    show okita 4
    return

label button_okita_generic_after_q3_intro:
    scene location_school_science_closeup
    show player 2 at left
    show okita 6 at right
    with dissolve
    player_name "Ei, {b}Miss Okita{/b}."
    show player 1
    show okita 2b
    okita "{b}[firstname]{/b}!"
    show okita 7
    okita "Que gentileza sua em visitar! "
    okita "Em que posso ajudá-lo?"
    show okita 6
    return

label button_okita_generic_after_q3_new_invention:
    show player 2
    player_name "Então você está trabalhando em uma nova invenção, hein? "
    show player 1
    show okita 7
    okita "Ai sim!"
    okita "É revolucionário! Você absolutamente tem que vir e ver!"
    show player 2
    show okita 6
    player_name "Heh, ok! eu vou {b}encontrar você no seu escritório esta noite.{/b}"
    show okita 2b
    show player 1
    okita "Você tem que prometer que virá e verá! "
    show okita 6
    show player 11
    player_name "..."
    show player 10
    player_name "... Sim. Eu prometo."
    show okita 2b
    show player 11
    okita "Mal posso esperar! "
    return

label button_okita_generic_after_q3_leave:
    show player 3
    player_name "Nada, eu só queria dizer oi! "
    show okita 5
    okita "Isso é legal da sua parte"
    show player 2
    okita "No entanto, estou ocupado trabalhando em alguns novos designs no momento ".
    show okita 7
    okita "Venha me ver na minha {b}Sala de aula{/b} se você quer me ajudar. "
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
