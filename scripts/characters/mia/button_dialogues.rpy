label mia_dialogue_helen_route:
    if player.location == L_miahouse_miaroom:
        scene mia_bedroom_c
    elif player.location == L_school_scienceclassroom:
        scene school_science_c02
    elif player.location == L_miahouse_entrance:
        scene mia_house_c
    show mia 8 at right
    if player.location == L_school_scienceclassroom:
        show mial 1f at right
    show player 10 at left
    with dissolve
    player_name "Olá, {b}Mia{/b}."
    show player 5
    show mia 12
    mia "Oh ... Olá, {b}[firstname]{/b}."
    show mia 8
    show player 10
    player_name "..."
    show player 11
    pause
    show player 10
    player_name " Assim como está você fazendo ?"
    show player 5
    show mia 12
    mia " Eu ainda estou me sentindo um pouco triste por minha família não estar junta ."
    show mia 46f
    mia "Eu sinto falta de acordar e ver o meu pai a cada manhã ."
    mia "E {b}mamãe{/b} parece mais distante ultimamente ."
    show mia 45f
    show player 10
    player_name "Huh..."
    show player 12
    player_name " Ei, você quer fazer algo mais tarde?"
    show player 10
    player_name " Não há outro teste chegando?. Quer estudar ?"
    show player 5
    show mia 46f
    mia "Não, eu não sinto que seria a coisa certa agora ."
    show mia 45f
    show player 24
    player_name "..."
    show player 10
    player_name "Bem, eu vou conversar com você mais tarde , então!"
    show player 5
    mia "..."
    hide player
    hide mia
    hide mial
    with dissolve
    return

label mia_dialogue_helen_change_news:
    if player.location == L_miahouse_miaroom:
        scene mia_bedroom_c
    elif player.location == L_school_scienceclassroom:
        scene school_science_c02
    elif player.location == L_miahouse_entrance:
        scene mia_house_c
    show player 13 at left
    show mia 10 at right
    if player.location == L_school_scienceclassroom:
        show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    mia " O que aconteceu ?"
    show mia 7
    show player 14
    player_name "Eu falei com sua mãe. Eu acho que cheguei até ela! "
    show player 13
    show mia 10
    mia " Você fez ?! Mas como ..."
    show mia 7
    show player 17
    player_name "Eu fiz, é uma longa história ..."
    show player 14
    player_name "... Mas tudo vai estar bem. Eu prometo !"
    player_name "Conversamos e ela concordou em tentar mudar as coisas para que eles pudessem voltar a ficar juntos.!"
    show player 13
    show mia 9
    mia " Isso é incrível !"
    show mia 7
    show player 14
    player_name "Eu acho que ela será mais branda com você também ..."
    player_name "...Eu sinto que ela vai mudar de atitude."
    show player 13
    show mia 10
    mia " Uau ... Você deve ter realmente trabalhado duro para convencê- la !"
    show mia 7
    show player 17
    player_name "Eu tenho um alguns truques na minha manga. Ha ha!"
    show player 13
    show mia 10
    mia " Eu estou tão feliz ! Obrigado, {b}[firstname]{/b}!"
    show mia 7
    pause
    hide player
    show mia 49 at left
    if player.location == L_school_scienceclassroom:
        show mial 1c
    with dissolve
    player_name "!!!"
    show player 11 at left
    show mia 10 at right
    if player.location == L_school_scienceclassroom:
        show mial 1f
    with dissolve
    mia " Eu vou ver você mais tarde, então !"
    show mia 7
    show player 21
    player_name "tchau."
    hide player
    hide mial
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_intro:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia " Estou tão feliz que você veio."
    show mia 7
    show player 14
    player_name "Olá, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Então você quer sair?"
    mia "Ou você está aqui para tentar essa minha nova técnica de estudo?"
    show mia 7
    return

label mia_dialogue_mia_bedroom_mia_end_study:
    player_name " Quer para ... estudo nu novamente ?"
    show player 13
    show mia 10
    mia "Yeah!"
    mia "Sente-se na cama enquanto eu me troco."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_leave:
    show mia 8
    show player 10
    player_name "Eu adoraria ... Mas está ficando tarde..."
    show mia 12
    show player 5
    mia "Oh, tudo bem..."
    mia "...Você vai voltar em breve? "
    show player 14
    show mia 8
    player_name "Sim . Vou ver o que posso fazer!"
    show mia 12
    show player 1
    mia "boa noite..."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_tattoo_help:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia " Ei !"
    mia " Estou tão feliz que você conseguiu !"
    show mia 7
    show player 17
    player_name "Está bem. Parecia que você tinha algo importante para conversar. "
    show player 14
    player_name "Você queria me perguntar uma coisa? "
    show player 13
    show mia 10
    mia "Bem, não é tão importante ... "
    mia "...Eu esperava poder ter sua opinião sobre alguma coisa, e talvez você possa me ajudar. "
    show mia 7
    show player 10
    player_name "Uhh ... acho que sim. Sobre o que é isso?"
    show player 11
    show mia 10
    mia "Você sabe alguma coisa sobre tatuagens? "
    show mia 7
    show player 10
    player_name "Tatuagens?!"
    show player 12
    player_name "Por quê? Você está pensando em fazer uma? "
    show player 11
    show mia 12
    mia "Eu sei que é ruim ... "
    mia "...Mas estou cansada de saber o que fazer! "
    mia "Eu apenas sinto vontade de fazer algo ... espontâneo e me divertir! "
    mia "Sentir-se livre..."
    show mia 8
    show player 10
    player_name "Sua mãe vai ficar bem com isso? "
    show player 5
    show mia 12
    mia "Eu não ligo mais."
    show mia 8
    show player 11
    player_name "..."
    show player 14
    player_name "Tatuagens são bem legais. Eu só não quero que você tenha problemas. "
    show player 13
    show mia 12
    mia "Você vai me ajudar?"
    show mia 8
    show player 14
    player_name "Claro, mas como?"
    show player 13
    show mia 10
    mia "Eu sei que você gosta de desenhar coisas na sala de aula o tempo todo, e eu vi sua arte ... "
    mia "...Eu estava esperando que você desenhasse algo para a minha tatuagem! "
    show mia 7
    show player 22
    player_name "!!!" with hpunch
    show player 29
    player_name "Você tem certeza?"
    show player 13 with dissolve
    show mia 10
    mia "sim! Você é tão bom nisso."
    show mia 7
    show player 21
    player_name "Obrigado, mas eu nem sei o que você quer! "
    show player 13
    show mia 10
    mia "Hmm ... eu quero algo fofo! "
    show mia 9
    mia "Com cores bonitas! "
    show mia 7
    show player 24
    player_name "E se for ruim, e você acabar odiando? "
    show player 13
    show mia 10
    mia "Tenho certeza que vai ficar bom! "
    show mia 7
    show player 14
    player_name "Se você diz..."
    show player 13
    show mia 10
    mia "Venha me ver quando você tiver alguma coisa. "
    show mia 7
    show player 14
    player_name "Tudo bem."
    show player 13
    show mia 10
    mia "Eu tenho que ir dormir. Vejo você na escola! "
    show mia 7
    show player 36 with dissolve
    player_name "Boa noite!"
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_church_plan:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 12 at right
    with dissolve
    player_name "Ei, {b}Mia{/b}."
    player_name "Pensei em me aproximar e ver você. "
    show player 5
    show mia 10
    mia "Aww, obrigado. Eu agradeço."
    mia "E aí?"
    show mia 7
    return

label mia_dialogue_mia_bedroom_intro:
    scene location_mia_bedroom_closeup
    show mia 10 at right
    show player 13 at left with dissolve
    mia "Estou tão feliz que você veio! "
    show mia 7
    show player 21
    player_name "Olá, {b}Mia{/b}!"
    show player 29
    player_name "Parece meio estranho esgueirar-se pela casa de alguém à noite ... "
    show mia 9
    show player 13
    mia "Está bem! Nós não vamos ter problemas ... "
    show mia 10
    show player 11
    mia "...Nós apenas temos que {b}ficar quietos{/b}!"
    show mia 7
    show player 17
    player_name "Se você diz. Haha "
    show mia 12
    show player 1
    return

label mia_dialogue_science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Ei, {b}[firstname]{/b}..."
    show mia 8
    show player 10
    player_name "Como você está?"
    show player 5
    show mia 12
    mia "Eu estou bem, mas realmente não deveríamos estar conversando. "
    mia "Já estou com problemas o suficiente ... Desculpe. "
    show mia 8
    show player 24
    player_name "..."
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_consult:
    scene school_science_c02
    show player 1 at left
    show mia 9 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Ei, {b}Mia{/b}!"
    show mia 10
    show player 13
    mia "Queria agradecer por ter vindo me visitar na outra noite ... "
    show player 11
    mia "... Eu realmente gostei, mas ... "
    show mia 7
    player_name "..."
    show mia 8
    show player 10
    player_name "Algo está errado?"
    show mia 12
    show player 11
    mia "Bem, minha mãe está ficando desconfiada. "
    show mia 8
    show player 10
    player_name "De mim?"
    show mia 12
    show player 5
    mia "Sim, acho que ela sabe que você veio. "
    show mia 8
    show player 10
    player_name "Será que é realmente de um grande negócio?"
    show mia 12
    show player 5
    mia "Ela definitivamente NÃO está bem com isso. "
    show player 11
    mia "Quero dizer, talvez se de alguma forma ... você ficou do lado bom do meu pai? Tenho certeza que ele poderia falar com ela. "
    show mia 8
    show player 10
    player_name "Seu pai? Mas como?"
    show mia 7
    player_name "Ele parece bem rigoroso também! "
    show mia 9
    show player 11
    mia "De jeito nenhum, ele é um grande manteiga derretida..."
    show mia 10
    show player 1
    mia "Ele costumava ser muito legal, sabia? "
    show mia 7
    show player 14
    player_name "Ok, então como posso ficar do seu lado bom? "
    show mia 10
    show player 1
    mia "Hmm ... não tenho certeza ... "
    mia "Talvez tente conseguir algo que ele goste, como uma caixa de donuts! "
    show mia 7
    show player 14
    player_name "Donuts?"
    show mia 9
    show player 1
    mia "Ha ha. Eu sei ... Tão típico. Mas ele realmente gosta deles! "
    show mia 8
    show player 14
    player_name "Ele tem um tipo rei da rosquinha? "
    show mia 12
    show player 1
    mia "Ah, não tenho muita certeza ... "
    show mia 7
    show player 14
    player_name "Tudo bem! Talvez eu possa descobrir e conseguir algo para ele. "
    show mia 10
    show player 1
    mia "Obrigado! Você é tão doce ... Tenho certeza que ele vai adorar! "
    return

label mia_dialogue_science_classroom_mia_parent_unblock:
    scene school_science_c02
    show player 1 at left
    show mia 9 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 10
    show player 11
    mia "Você não vai acreditar nisso! "
    show player 14
    show mia 7
    player_name "Hã? O que aconteceu?"
    show player 1
    show mia 10
    mia "Ontem à noite, ouvi meu pai falando sobre você com minha mãe! "
    show player 14
    show mia 7
    player_name "Sobre mim? Sério?"
    show player 1
    show mia 9
    mia "Sim!"
    show mia 10
    mia "Ele estava dizendo o quão importante era fazer amigos na minha idade ... "
    mia "... como ele pensou que ela deveria me deixar te ver, já que você é uma boa pessoa e tudo ... "
    show player 14
    show mia 7
    player_name "Eita..."
    player_name "Então, sua mãe é legal comigo agora ?! "
    show player 11
    show mia 10
    mia "Bem, ela não estava muito satisfeita com a ideia, isso é certo! "
    show player 1
    show mia 9
    mia "Mas acho que pode ter funcionado um pouco ".
    show player 17
    show mia 7
    player_name "Eu acho que é alguma coisa. "
    show player 13
    show mia 10
    mia "Obrigado por falar com meu pai ... "
    show player 14
    show mia 7
    player_name "Não é grande coisa, e seu pai parece um cara legal, na verdade! "
    show player 1
    show mia 10
    mia "Sim ... Ele costumava ter mais voz em nossas vidas. "
    show player 14
    show mia 8
    player_name "Enfim, eu deveria voltar para a aula- "
    show player 11
    show mia 12
    mia "Esperar!! EU..."
    mia "Eu queria ter sua opinião sobre alguma coisa. "
    show player 14
    show mia 8
    player_name "Alguma coisa?"
    show player 11
    show mia 12
    mia "Eu realmente não me sinto confortável falando sobre isso aqui ... "
    show player 13
    mia "Mas talvez ... você possa me visitar hoje à noite? "
    show player 14
    show mia 7
    player_name "Eu adoraria!"
    show player 1
    show mia 9
    mia "Doce!"
    show mia 10
    mia "Estarei esperando por você em casa, então. "
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_favor:
    scene school_science_c02
    show player 13 at left
    show mia 10 at right
    show mial 1f at right
    with dissolve
    mia "Bom dia, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Bom dia, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Eu estava esperando que você pudesse me ajudar com algo ... mais uma vez? "
    show mia 7
    show player 14
    player_name "Claro, {b}Mia{/b}. Eu não me importo! "
    show player 13
    show mia 10
    mia "Quero que você trabalhe sua mágica e faça meu pai sair para jantar com minha mãe e eu. "
    mia "Ele ouve você ... "
    show mia 7
    show player 14
    player_name "Jantar? Parece que seus pais estão em condições de bens novamente. "
    player_name "Vou parar no trabalho dele e ver o que posso fazer! "
    show player 13
    show mia 12
    mia "Eu aprecio sua ajuda, {b}[firstname]{/b}. Só não sei o que faria comigo se não voltarem a ficar juntos. "
    show mia 46f
    mia "Eu sinto que tudo isso é culpa minha ... "
    show mia 45f
    show player 10
    player_name "Oh vamos lá, {b}Mia{/b}... Você não pode pensar assim! "
    show player 14
    player_name "Não se preocupe, vou levar seu pai para o jantar. "
    show player 13
    show mia 46f
    mia "Obrigado ... Você é doce. "
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_need_space:
    scene school_science_c02
    show player 10 at left
    show mia 8 at right
    show mial 1f at right
    with dissolve
    player_name "Ei, {b}Mia{/b}..."
    player_name "Como você está?"
    show player 5
    show mia 12
    mia "Estou bem."
    show mia 8
    mia "..."
    show player 3 with dissolve
    player_name "..."
    show mia 12
    mia "Eu acho que só quero um pouco de espaço agora. "
    show mia 8
    show player 10 with dissolve
    player_name "Tudo bem..."
    player_name "Falo com você mais tarde. Apenas me avise se você precisar de algo. "
    show player 5
    show mia 12
    mia "Obrigado, {b}[firstname]{/b}..."
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_church_plan:
    scene school_science_c02
    show player 12 at left
    show mia 8 at right
    show mial 1f at right
    with dissolve
    player_name "Ei, {b}Mia{/b}!"
    player_name "Como você está?"
    show player 5
    show mia 12
    mia "Tudo bem."
    mia "Mas eu gostaria que as coisas pudessem voltar ao que eram antes em casa ".
    show mia 8
    show player 10
    player_name "Desculpa..."
    show player 5
    show mia 12
    mia "Você gostaria de falar sobre algo? "
    show mia 8
    return

label mia_dialogue_science_classroom_mia_urgent_help:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Ei, {b}[firstname]{/b}!"
    mia "Por favor {b}pare em minha casa hoje mais tarde{/b}, Tudo bem?"
    show mia 8
    show player 10
    player_name "Tudo bem."
    show player 5
    show mia 12
    mia "Mais alguma coisa que você precisava? "
    show mia 8
    return

label mia_dialogue_science_classroom_intro:
    scene school_science_c02
    show player 14 at left
    show mia 7 at right
    show mial 1f at right
    with dissolve
    player_name "Ei, {b}Mia{/b}!"
    player_name "Como você está?"
    show player 13
    show mia 10
    mia "Estou bem."
    show mia 12
    mia "Não estou realmente ansioso para a minha próxima aula. "
    show mia 7
    show player 17
    player_name "Sim. Eu ouvi você. "
    show player 13
    show mia 10
    mia "Você gostaria de falar sobre algo? "
    show mia 7
    return

label mia_dialogue_mias_house_entrance_mia_favor:
    scene mia_house_c with fade
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Bom dia, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Bom dia, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Eu estava esperando que você pudesse me ajudar com algo ... mais uma vez? "
    show mia 7
    show player 14
    player_name "Claro, {b}Mia{/b}. Eu não me importo! "
    show player 13
    show mia 10
    mia "Quero que você trabalhe sua mágica e faça meu pai sair para jantar com minha mãe e eu. "
    mia "Ele ouve você ... "
    show mia 7
    show player 14
    player_name "Jantar? Parece que seus pais estão em condições de bens novamente. "
    player_name "Vou parar no trabalho dele e ver o que posso fazer! "
    show player 13
    show mia 12
    mia "Eu aprecio sua ajuda, {b}[firstname]{/b}. Só não sei o que faria comigo se não voltarem a ficar juntos. "
    show mia 46f
    mia "Eu sinto que tudo isso é culpa minha ... "
    show mia 45f
    show player 10
    player_name "Oh vamos lá, {b}Mia{/b}... Você não pode pensar assim! "
    show player 14
    player_name "Não se preocupe, vou levar seu pai para o jantar. "
    show player 13
    show mia 46f
    mia "Obrigado... Você é doce. "
    hide mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_helen_talk:
    scene mia_house_c
    show player 5 at left
    show mia 12 at right
    with dissolve
    mia "Você pode falar com minha mãe? Ela está dentro {b}do quarto dela no andar de cima{/b}..."
    show player 10
    show mia 8
    player_name "Vou tentar, {b}Mia{/b}."
    hide mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_church_plan:
    scene mia_house_c
    show player 13 at left
    show mia 12 at right
    with dissolve
    mia "Oi, {b}[firstname]{/b}."
    show player 5
    pause
    show player 10
    show mia 8
    player_name "Olá, {b}Mia{/b}."
    show player 5
    show mia 12
    mia "E aí?"
    show mia 8
    return

label mia_dialogue_mias_house_entrance_intro:
    scene mia_house_c
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Oi, {b}[firstname]{/b}."
    show player 14
    show mia 7
    player_name "Olá, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "E aí?"
    show mia 7
    return

label mia_dialogue_chat:
    show mia 7
    show player 2
    player_name "Certo!"
    show player 10
    player_name "Umm ... Você não precisa responder isso, mas ... "
    show mia 8
    player_name "Você não acha estranho que seus pais não deixem você ter amigos? "
    show player 5
    mia "..."
    show mia 12
    mia "É só ... do jeito que está, com minha mãe. "
    show mia 8
    show player 12
    player_name "E você não se importa ?? "
    show player 11
    show mia 12
    mia "Ela só está sendo protetora! "
    mia "Eu sei que ela apenas me ama muito e quer o melhor para mim ... "
    show mia 8
    show player 12
    player_name "Mas você tem que se encontrar com amigos secretamente ... "
    show mia 12
    show player 5
    mia "Eu sei ... Mas ela não entenderia. "
    show mia 8
    show player 24
    player_name "Entendo..."
    show player 21
    player_name "Contanto que você seja feliz? "
    show mia 9
    show player 13
    mia "Sim!"
    return

label mia_dialogue_talent_show_help:
    show player 10
    player_name "Você toca algum instrumento ou canta? "
    show player 5
    show mia 9
    mia "Sim, eu canto no coral da igreja o tempo todo! "
    show mia 7
    show player 14
    player_name "Você faz? Impressionante!"
    player_name "Você deveria cantar {b}Ms. Dewitt's{/b} show de talentos!"
    player_name "Nós realmente precisamos de mais pessoas para ser voluntário. "
    show player 13
    show mia 12
    mia "Oh, umm."
    mia "Eu gostaria, mas não posso. "
    show mia 8
    show player 10
    player_name "Hã? Por que não?"
    show player 5
    show mia 12
    mia "Minha mãe nem me deixa ir ao show de talentos, muito menos participar ".
    show mia 8
    show player 12
    player_name "Por quê?"
    show player 5
    show mia 12
    mia "Ela não quer que eu ouça rock ou rap ... "
    mia "Ela tem medo de manchar minha mente jovem ou algo assim. "
    show mia 8
    show player 12
    player_name "Isso é péssimo! "
    show player 5
    show mia 12
    mia "Sim. Desculpa."
    show player 10
    player_name "Tudo bem, {b}Mia{/b}. Obrigado enfim!"
    return

label mia_dialogue_parents:
    show player 14
    player_name "Então, como estão seus pais? "
    show player 13
    show mia 10
    mia "Ocupados. Minha mãe está sempre na igreja e o pai está sempre trabalhando. "
    show mia 12
    mia "Provavelmente é melhor assim. "
    show mia 8
    show player 10
    player_name "Como assim?"
    show player 11
    show mia 12
    mia "Quando meus pais se reúnem, tudo o que fazem é discutir. "
    show player 5
    mia "Eu odeio tanto. "
    mia "Eu gostaria que eles se dessem melhor, como costumavam ... "
    show mia 8
    show player 10
    player_name "Eu não sabia que era assim. Eles pareciam tão bem."
    show player 5
    show mia 12
    mia "Sim, minha mãe parece mexer mais no pote ".
    mia "Ela é muito pesada e não aceita não como resposta."
    mia "assim {b}Papai{/b} apenas segue tudo o que ela diz agora ... "
    show mia 8
    show player 10
    player_name "Isso é péssimo. "
    show player 5
    show mia 12
    mia "Ela está me forçando a fazer estudos bíblicos ultimamente ... "
    mia "... E diz que eu deveria encontrar um garoto da igreja, quando estiver pronto."
    show mia 8
    show player 11
    player_name "..."
    show mia 12
    mia "Eu sei, é ... estranho. "
    show mia 9
    mia "De qualquer forma! Vamos falar de outra coisa. "
    show mia 7
    show player 13
    return

label mia_dialogue_mia_clues:
    show player 10
    player_name "Onde você disse que eu poderia encontrar pistas sobre paradeiro de {b}Harold's{/b} ?"
    show player 5
    show mia 12
    mia "Comece questionando seus colegas de trabalho no {b}Delegacia de polícia{/b}..."
    mia "...E procure {b}clues{/b} em torno de seu local de trabalho ".
    show mia 8
    show player 12
    player_name "Suponho que posso pedir para ver onde ele poderia estar ... "
    show player 5
    show mia 12
    mia "Obrigada..."
    return

label mia_dialogue_mia_convince_harold:
    show player 10
    player_name "O que você precisava que eu fizesse com que seu pai fizesse novamente? "
    show player 13
    show mia 10
    mia "Quero que você o convide para jantar com minha mãe e eu. "
    mia "Vocês dois se dão tão bem juntos. Talvez você possa torcer o braço dele, se necessário."
    show mia 7
    show player 14
    player_name "Certo! Eu vou encontrá-lo no {b}Delegacia de polícia{/b}."
    show player 13
    show mia 10
    mia "Obrigado, {b}[firstname]{/b}."
    return

label mia_dialogue_glasses:
    show player 12
    player_name "O que você quer que eu faça com esses óculos de novo? "
    show player 5
    show mia 10
    mia "Ah, eu esperava que você pudesse deixá-los no trabalho do meu pai. "
    show mia 7
    show player 14
    player_name "É isso mesmo ... eu lembro agora. "
    player_name "Eu vou chegar lá, então!"
    return

label mia_dialogue_donuts:
    show player 14 at left
    show mia 7 at right
    player_name "Alguma idéia de como posso descobrir que tipo de rosquinha seu pai gosta? "
    show player 1
    show mia 10
    mia "Oh, ehmm..."
    mia "Talvez perguntar sobre o trabalho dele? "
    mia "Eles adoram comer rosquinhas por lá ..."
    show mia 7
    show player 17
    player_name "Ha ha, talvez você esteja certo, isso poderia funcionar. "
    show mia 10
    show player 1
    mia "Mais alguma coisa que você queira falar? "
    show mia 7
    show player 1
    return

label mia_dialogue_mia_draw_tattoo:
    show mia 7 at right
    show player 10 at left
    player_name "Sobre a tatuagem que você queria ... "
    show player 5
    show mia 10
    mia "Oh! Você tem?!"
    show mia 7
    show player 10
    player_name "Não, ainda não."
    player_name "Mas, o que você queria de novo?"
    show player 5
    show mia 10
    mia "Hmm ... Algo fofo e colorido! "
    show mia 7
    show player 17
    player_name "Ha ha, Tudo bem."
    show player 14
    player_name "Verei o que posso fazer."
    show player 13
    show mia 9
    mia "Muito obrigado, {b}[firstname]{/b}."
    return

label mia_dialogue_mia_show_tattoo_fail:
    show mia 7 at right
    show player 2 at left
    player_name "Sobre a tatuagem que você queria ... "
    show player 13
    show mia 10
    mia "Oh! Você tem?!"
    show mia 7
    show player 14
    player_name "Sim!"
    show player 239_240 with dissolve
    player_name "Levei um tempo para fazê-lo ... "
    show player 386 with dissolve
    player_name "Aqui está!"
    show player 13
    show mia 32
    if player.location == L_school_scienceclassroom:
        show mial 1b
    with dissolve
    mia "Hmm..."
    show player 10
    player_name "Algo está errado?"
    show player 11
    show mia 33
    mia "Bem, eu esperava algo diferente. "
    show mia 34
    show player 25
    player_name "Oh..."
    show player 24
    show mia 30
    mia "Eu gosto disso!!"
    show mia 33
    mia "Mas talvez você possa tentar outra coisa? "
    show mia 34
    show player 10
    player_name "Como o quê?"
    show player 5
    show mia 30
    mia "Tente algo fofo, que tenha cores bonitas! "
    show mia 31
    show player 14
    player_name "Tudo bem, Vou tentar fazer outra coisa ... "
    show player 13
    show mia 30
    mia "muito obrigado, {b}[firstname]{/b}."
    return

label mia_dialogue_mia_show_tattoo_pass:
    show mia 7 at right
    show player 2 at left
    player_name "Sobre a tatuagem que você queria ... "
    show player 13
    show mia 10
    mia "Oh! Você tem?!"
    show mia 7
    show player 14
    player_name "Sim!"
    show player 239_240 with dissolve
    player_name "Levei um tempo para fazê-lo ... "
    show player 386 with dissolve
    player_name "Aqui está!"
    show player 13
    show mia 29
    if player.location == L_school_scienceclassroom:
        show mial 1b at right
    with dissolve
    mia "WOW!!!"
    show mia 30
    mia "Eu absolutamente amo isso! "
    show mia 31
    show player 17
    player_name "Realmente?"
    show player 18
    show mia 30
    mia "Sim!"
    show mia 29
    mia "É tão bonito..."
    show mia 31
    show player 14
    player_name "Legal! Estou feliz que você gostou. "
    show player 13
    show mia 30
    mia "Deveríamos visitar {b}Sugar Tats{/b} e veja se eles podem fazer isso por mim ".
    show mia 7
    if player.location == L_school_scienceclassroom:
        show mial 1f
    with dissolve
    show player 12
    player_name "Agora?!"
    show player 5
    show mia 9
    mia "Agora não, bobo! "
    show mia 10
    mia "Essese {b}sábado{/b}?"
    show mia 7
    show player 10
    player_name "Ok, eu posso te encontrar lá em {b}Sabado{/b}."
    show player 5
    show mia 10
    mia "Prometa que me encontrará lá {b}durante o dia{/b}!"
    show mia 7
    show player 14
    player_name "Eu prometo!"
    show player 13
    show mia 10
    mia "Ok, bom. Não tenho certeza se posso fazer isso sozinho, ha ha. "
    mia "Vejo você então."
    hide player
    hide mia
    hide mial
    with dissolve
    return

label mia_dialogue_mia_get_tattoo:
    show mia 7 at right
    show player 12 at left
    player_name "Sobre essa tatuagem ... "
    show player 5
    show mia 12
    mia "Você ainda vem? "
    show mia 8
    show player 14
    player_name "Claro!"
    show player 10
    player_name "Mas quando você quis ir? "
    show player 11
    show mia 12
    mia "Você já esqueceu ?! "
    show mia 8
    show player 21
    player_name "Acho que tenho muito em mente ultimamente ... "
    show player 13
    show mia 9
    mia "Está tudo bem, ha ha. "
    show mia 10
    mia "Eu preciso que você me encontre no {b}Sabado{/b} no {b}salão de tatuagem{/b}, {b}durante o dia{/b}!"
    show mia 7
    show player 14
    player_name "Tudo bem, Vou me certificar de estar lá com você. "
    show player 13
    show mia 10
    mia "muito obrigado, {b}[firstname]{/b}."
    return

label mia_dialogue_church:
    show player 12
    player_name "Quando sua mãe vai à igreja? "
    show player 5
    show mia 12
    mia "No {b}fim de semana de manhã{/b}."
    show mia 8
    show player 34
    player_name "Hmm..."
    show player 14
    player_name "Tudo bem, Obrigado."
    show player 13
    show mia 12
    mia "O que você vai fazer?!"
    show mia 8
    show player 12
    player_name "Ainda não tenho muita certeza, mas voltarei a você se encontrar um caminho. "
    show player 13
    show mia 12
    mia "Okay..."
    return

label mia_dialogue_art_sessions_intro:
    show player 10
    player_name "Ei, então uh... {b}Miss Ross{/b} me pediu para vir falar com você. "
    show player 11
    show mia 10
    mia "Realmente?"
    show player 10
    show mia 7
    player_name "Sim, ela quer que você seja meu parceiro em algumas sessões particulares de arte. "
    return

label mia_dialogue_art_sessions_stat_pass:
    show player 10
    player_name "Eu realmente gostaria que você viesse ajudar, {b}Mia{/b}."
    show player 5
    show mia 12
    mia "Você poderia?"
    show mia 8
    show player 29 with dissolve
    player_name "Totalmente."
    show player 3
    show mia 8b
    mia "Hmm..."
    show mia 9
    mia "Ok!"
    show player 13 with dissolve
    show mia 10
    mia "Eu vou te buscar, {b}[firstname]{/b}."
    show mia 7
    show player 14
    player_name "Doce! Obrigado, {b}Mia{/b}!"
    show player 13
    show mia 9
    mia "Hehe, sem problemas."
    show mia 7
    show player 14
    player_name "Então, eu vou te ver lá? "
    show player 13
    show mia 10
    mia "Pode apostar!"
    return

label mia_dialogue_art_sessions_stat_fail:
    player_name "[chr_warn]Ela é bastante inflexível, precisa ser você."
    show player 11
    show mia 12
    mia "[chr_warn]... Mas eu nem sou muito bom em arte."
    show player 10
    show mia 8
    player_name "[chr_warn]Você não pode ser tão ruim..."
    show player 11
    show mia 12
    mia "[chr_warn]Confie em mim, eu sou muito ruim!"
    mia "[chr_warn]Você deveria encontrar outra pessoa."
    mia "[chr_warn]Além disso, minha mãe diria não."
    show player 10
    show mia 8
    player_name "[chr_warn]Oh, ok então."
    return

label mia_dialogue_homework_want_parents_back:
    show player 14
    player_name "O que você quer estudar juntos em?"
    show player 13
    show mia 12
    mia "Eu não estou realmente me sentindo bem agora."
    show mia 8
    show player 10
    player_name "Tudo bem..."
    show player 5
    show mia 12
    mia "Desculpa."
    mia "Eu só quero que meus pais voltem a ficar juntos."
    show mia 8
    show player 10
    player_name "eu sei."
    player_name "Apenas me informe se precisar da minha ajuda. "
    show player 5
    show mia 12
    mia "Obrigado, {b}[firstname]{/b}."
    show mia 8
    return

label mia_dialogue_homework_intro:
    show player 14
    player_name "No que vocês queriam estudar juntos? "
    show player 13
    show mia 10
    mia "Estaríamos estudando coisas relacionadas a última {b}Lição de casa da aula de francês{/b}. Você já entregou essa tarefa? "
    show mia 7
    return

label mia_dialogue_homework_still_busy:
    show player 24
    player_name "Ainda estou trabalhando nisso. "
    show player 13
    show mia 10
    mia "Bem, uma vez que você tenha feito, {b}pare na minha casa{/b}."
    hide mia
    hide mial
    with dissolve
    show player 5 with dissolve
    player_name "( Eu deveria tentar terminar meu {b}lição de casa de frances{/b}, para que eu possa estudar com {b}Mia{/b}. )"
    show player 4 with dissolve
    pause
    player_name "( Eu me pergunto por que ela me escolheu para ajudá-la a estudar. ) "
    player_name "(ela geralmente estuda com {b} Judith {/ b} e é muito boa em francês ...)"
    player_name "(... não sei como poderia ajudá-la.)"
    show player 13 with dissolve
    player_name "( Pelo menos nós vamos sair, e ela é muito fofa ...) "
    hide player with dissolve
    return

label mia_dialogue_homework_study:
    show player 14
    player_name "Eu a entreguei não faz muito tempo. "
    show player 13
    show mia 10
    mia "Quando você tiver tempo, {b}esgueirar-se para o meu quarto{/b} à noite para que possamos estudar então. "
    show mia 7
    show player 17
    player_name "Vai fazer!"
    show player 13
    return

label mia_dialogue_study_repeat:
    show player 14
    player_name "Claro!"
    scene mia_bedroom_closeup
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Obrigado por esgueirar-se aqui de novo. "
    show mia 13
    show player 142
    player_name "Não é tão difícil com seus pais colados na TV ".
    show player 143
    show mia 16
    mia "Sim, é a única coisa que os impede de gritar um com o outro. "
    mia "Eles realmente gostam de assistir reprises."
    mia "Às vezes eu assisto com eles quando termino a lição de casa."
    show mia 22
    mia "Na maioria das vezes eu fico aqui em cima ... É mais calmo. "
    show mia 14
    show player 146
    player_name "É meio chato que seus pais não se dão bem ".
    show player 141
    show mia 18
    mia "...Sim!"
    mia "Talvez volte ao que costumava ser ".
    show mia 14
    pause
    show mia 16
    mia "É melhor você ir antes que meus pais percebam você. "
    show mia 13
    show player 142
    player_name "Vou parar de novo, ok? "
    show player 141
    show mia 15
    mia "Ótimo! Boa noite {b}[firstname]{/b}!"
    show mia 13
    show player 142
    player_name "Boa noite, {b}Mia{/b}."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_study_first:
    show mia 7
    show player 21
    player_name "Acho que deveríamos estar estudando? "
    show mia 9
    show player 13
    mia "Claro!"
    show mia 10
    mia "Vamos fazer isso então. "
    show player 11
    mia "Deixe-me pegar todos os livros e configurar {b}na minha cama{/b}?"
    show mia 7
    show player 21
    player_name "Uh... Okay!"
    return

label mia_dialogue_study_want_parents_back:
    show player 12
    player_name "Você quer estudar juntos? "
    show player 5
    show mia 12
    mia "Eu não estou realmente disposto a fazer isso agora. "
    show mia 8
    show player 10
    player_name "Tudo bem..."
    show player 5
    show mia 12
    mia "Desculpa."
    mia "Eu só quero que meus pais voltem. "
    show mia 8
    show player 10
    player_name "Eu sei."
    player_name "Entre em contato se precisar da minha ajuda."
    show player 5
    show mia 12
    mia "Obrigado, {b}[firstname]{/b}."
    show mia 8
    return

label mia_dialogue_mias_bedroom_leave:
    show mia 8
    show player 10
    player_name "Eu adoraria ... Mas está ficando tarde ... "
    show mia 12
    show player 5
    mia "Oh, okay..."
    mia "... Você voltará em breve? "
    show player 14
    show mia 8
    player_name "Sim. Verei o que posso fazer!"
    show mia 12
    show player 1
    mia "Boa noite..."
    return

label mia_dialogue_science_classroom_leave:
    show player 10
    player_name "Na verdade, é melhor eu voltar para a aula. "
    show player 5
    show mia 12
    mia "Oh, ok ... Falo com você mais tarde! "
    show mia 8
    show player 14
    player_name "Até mais!"
    return

label mia_dialogue_mias_house_entrance_leave:
    show player 10
    player_name "Na verdade, lembro que tinha algo que precisava fazer ".
    show player 5
    show mia 12
    mia "Oh, ok ... Falo com você mais tarde! "
    show mia 8
    show player 14
    player_name "Até mais!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
