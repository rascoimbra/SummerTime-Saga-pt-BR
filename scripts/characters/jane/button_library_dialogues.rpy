label jane_library_dialogue_bissette_find_dictionary:
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Não consigo encontrar um {b}dicionário de francês{/b}."
    show player 5f
    show jane f_normal_talk
    jan "Hmm, deixa eu ver..."
    show jane f_normal_down
    pause
    show jane f_normal_talk_down
    jan "Deve estar lá na prateleira, ao lado da sala dos fundos."
    show jane f_normal
    show player 14f
    player_name "Tudo bem, vou dar uma olhada. Obrigado."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Bem, encontrei parte de um dicionário francês."
    show player 503f
    show jane f_sad_talk
    jan "O que?"
    show player 5f
    show jane f_complain_down a_dressed_book1
    with dissolve
    jan "Oh não!"
    jan "Vou precisar pedir um novo, mas levará algum tempo para chegar."
    show jane f_sad_talk
    jan "Você ainda queria dar uma olhada?"
    show jane f_sad
    show player 10f
    player_name "Sim, estou desesperado. Só espero que não precise das páginas que faltam..."
    show player 5f
    show jane f_sad_talk
    jan "Ok, bem, desculpe novamente!"
    show jane f_normal_talk
    jan "Você pode ficar com ele. Não vai ser muito útil por aqui..."
    show jane f_normal a_dressed_sides with dissolve
    show player 504f with dissolve
    player_name "Obrigado!"
    show player 503f
    show jane f_laugh
    jan "Não tem problema, tenha um bom dia!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( acho que devo levar isso para {b}Miss Bissette{/b} e ver o que ela pensa... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane f_normal at flip
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "Encontrei todos os livros em atraso!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    show jane f_normal_talk
    jan "Sério? Vamos ver..."
    show player 13f
    show jane f_normal_talk a_dressed_book3 with dissolve
    jan "Você conseguiu! Muito obrigado!"
    jan "Eu também tenho algo para você."
    show jane f_normal
    show player 10f
    player_name "Você sabe?"
    show jane f_normal_talk a_dressed_book2 with dissolve
    jan "Sim, o livro que você pediu chegou."
    show jane f_normal
    pause
    show player 521f
    show jane f_normal a_dressed_sides
    with dissolve
    player_name "Obrigado!"
    player_name "{b}101 tipos de queijos{/b}..."
    show player 5f with dissolve
    show jane f_normal_talk
    jan "Isso vai funcionar?"
    show jane f_normal
    show player 10f
    player_name "Err, vou ter que me virar."
    show player 14f
    player_name "Obrigado novamente!"
    show player 13f
    show jane f_laugh
    jan "Volte e nos veja!"
    return

label jane_library_dialogue_pre:
    show jane f_normal_talk at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Oi! Como posso ajudá-lo?"
    show player 2f
    show jane f_normal
    player_name "Olá, estou procurando um {b}livro{/b}."
    show player 1f
    show jane f_normal_talk
    jan "Claro! Você sabe o nome do livro?"
    show jane f_normal
    return

label jane_library_dialogue_production_ask_librarian:
    scene librarydesk
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Por acaso você não tem livros sobre o aumento da ordenha, não é?"
    show player 5f
    show jane f_sad_talk
    jan "... Umm, essa é uma pergunta estranha."
    show jane f_normal
    show player 29f with dissolve
    player_name "Ehh, sim. Suponho que sim."
    player_name "É para o meu uhh ... Amigo."
    show player 3f at Position (xoffset=-8)
    show jane f_laugh
    jan "Heh, com certeza é."
    show jane f_eyeroll_talk a_dressed_up with dissolve
    jan "Umm, eu não sei."
    jan "Tenho certeza que temos coisas para vacas, mas no que diz respeito à ordenha ..."
    show jane f_normal_talk
    jan "{b}Tente essa prateleira por lá.{/b}"
    show jane f_normal a_dressed_sides
    show player 14f
    with dissolve
    player_name "Obrigado!"
    hide player with dissolve
    pause
    show jane f_sad_talk
    jan "Que esquisito..."
    hide jane
    with dissolve
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "Você tem alguma poesia francesa?"
    show player 5f
    show jane f_normal_down
    jan "Hmm..."
    show jane f_normal_talk
    jan "Na verdade ..."
    jan "Algumas meninas estavam aqui lendo algo assim {b}ontem à tarde{/b}."
    show jane f_normal
    show player 10f
    player_name "Serio?"
    show player 12f
    player_name "Elas deram uma olhada?"
    show player 5f
    show jane f_normal_talk
    jan "Não."
    show jane f_normal
    show player 10f
    player_name "Você sabe onde está?"
    show player 5f
    show jane f_normal_down
    jan "..."
    show jane f_sad_talk
    jan "Não..."
    jan "Mas talvez elas estejam aqui novamente esta {b}tarde{/b}."
    jan "Você pode perguntar a uma delas onde elas colocaram."
    show jane f_normal
    show player 12f
    player_name "Obrigado."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "Eu queria saber se você tem algum livro em francês sobre comida?"
    show player 13f
    show jane f_laugh
    jan "Esse é um assunto interessante..."
    show jane f_normal
    show player 14f
    player_name "Sim, preciso dele para um trabalho escolar."
    show player 13f
    show jane f_normal_talk
    jan "Tudo bem, deixe-me olhar e ver o que temos."
    show jane f_normal_down
    jan "..."
    show player 11f
    player_name "..."
    show player 5f
    show jane f_normal_talk_down
    jan "Hmm, parece que não temos nada parecido."
    show jane f_normal
    show player 12f
    player_name "Nada?"
    show player 5f
    show jane f_normal_talk_down
    jan "Não ... Oh, espere um segundo!"
    jan "Aqui está dizendo que nossa filial tem um livro em francês sobre queijo."
    show jane f_normal_talk
    jan "Isso funcionaria?"
    show jane f_normal
    show player 14f
    player_name "Claro, eu amo queijo! Onde preciso buscá-lo?"
    show player 13f
    show jane f_normal_talk
    jan "Posso solicitar que eles enviem aqui. Deve levar apenas alguns dias ..."
    jan "Enquanto isso, eu me pergunto se você poderia me ajudar com alguma coisa."
    show jane f_normal
    show player 10f
    player_name "... Claro, suponho. Do que você precisa?"
    show player 5f
    show jane f_normal_talk
    jan "{b}Alguns de seus colegas de classe têm livros em atraso{/b} que eu gostaria de que eles devolvessem."
    jan "Eu tenho enviado cartas para suas casas, mas isso não parece estar funcionando."
    jan "Eu odiaria perder os livros."
    show jane f_normal
    show player 10f
    player_name "Sim, eu poderia tentar {b}falar com eles{/b}. Quais são os nomes deles?"
    show player 5f
    show jane f_normal_talk_down
    jan "Hmm, o primeiro é uma tal de {b}Miss Martinez{/b}."
    jan "O segundo é um tal de {b}Mr. Erik J-{/b}."
    show jane f_normal
    show player 14f
    player_name "{b}Erik{/b} tem um livro publicado?!"
    player_name "Isso deve ser fácil."
    show player 13f
    show jane f_normal_talk_down
    jan "... e finalmente..."
    jan "Hein. Apenas diz {b}Dexter{/b}."
    jan "Toca alguns sinos?"
    show jane f_normal
    show player 12f
    player_name "Oh cara, não {b}Dexter{/b}... Você tem certeza?"
    show player 11f
    show jane f_normal_talk
    jan "Isso é o que o sistema diz..."
    show jane f_normal
    show player 12f
    player_name "Merda! Tudo bem, vou ver o que posso fazer."
    show player 5f
    show jane f_laugh
    jan "Obrigado, eu realmente aprecio isso!"
    hide jane with dissolve
    show player 12 at center with dissolve
    player_name "Ugh, por que tinha que ser {b}Dexter{/b}?"
    return

label jane_library_dialogue_french_food_book_holders:
    show player 10f
    player_name "Como eram os nomes dos alunos de novo?"
    player_name "Você sabe, aqueles com os livros em atraso."
    show player 5f
    show jane f_normal_talk
    jan "One second..."
    show jane f_normal_talk_down
    jan "Hmm, {b}Miss Martinez{/b}, {b}Mr. Erik{/b}, e um {b}Dexter{/b}."
    show jane f_normal
    show player 12f
    player_name "Ugh, eu esqueci o {b}Dexter{/b}..."
    player_name "Tudo bem, estou nisso."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "Estou fazendo uma colagem para a aula de arte e preciso de revistas antigas."
    player_name "Você poderia me mostrar onde encontrar algumass?"
    show player 1f
    show jane f_normal_talk
    jan "Acho que você está sem sorte. Paramos de carregá-las há alguns meses atrás."
    show player 10f
    show jane f_normal
    player_name "Você não tem nenhuma?"
    show player 1f
    show jane f_normal_talk
    jan "Receio que não. Enviamos todas as que tínhamos para serem recicladas."
    show player 10f
    show jane f_normal
    player_name "Oh cara..."
    player_name "De qualquer forma, obrigado."
    show player 11f
    show jane f_normal_talk
    jan "Desculpa."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "O que eu vou fazer agora?"
    show player 11
    player_name "..."
    show player 10
    player_name "Acho que {b}vou voltar para a escola e dar uma olhada{/b}."
    player_name "Tem que haver algumas revistas em algum lugar."
    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "Então não tem uma única revista por aqui?"
    show player 11f
    show jane f_normal_talk
    jan "Não".
    jan "Cancelamos as assinaturas e jogamos fora o que tínhamos".
    show jane f_normal
    show player 10f
    player_name "Ok, obrigado de qualquer maneira."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{b}*Suspiro*{/b}"
    player_name "Acho que devo {b}voltar para a escola e procurar por lá.{/b}"
    player_name "... Talvez eu tenha sorte?"
    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "Gostaria de devolver um livro."
    show player 13f
    show jane f_laugh
    jan "Ótimo!"
    return

label jane_library_dialogue_return_books_first:
    show jane f_normal_talk
    jan "Poucas pessoas fazem."
    show jane f_normal
    show player 10f
    player_name "O que acontece então?"
    show player 5f
    show jane f_mad_talk
    jan "Eu os caço e quebro uma das pernas para que não o façam novamente."
    show jane f_mad
    show player 22f
    player_name "!!!"
    show jane f_laugh
    jan "Brincadeira!"
    show jane f_normal
    show player 29f with dissolve
    player_name "Oh."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane f_normal_talk
    jan "Apenas coloque os livros que você deseja devolver no balcão e eu cuidarei disso."
    show jane f_laugh
    jan "E volte logo!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane f_sad_talk
    player_name "Desculpe. Voltarei assim que me lembrar do nome do livro."
    show player 5f
    show jane f_normal_talk
    jan "Vejo você então."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
