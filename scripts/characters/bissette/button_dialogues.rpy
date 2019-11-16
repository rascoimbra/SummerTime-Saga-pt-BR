label bissette_dialogue_meet_in_office:
    show player 10 at left
    show teacher 1 at right
    with dissolve
    player_name "{b}Miss Bissette{/b}, o que você precisa que eu faça?"
    show player 5
    show teacher 12
    bis "Oh, {b}[firstname]{/b}. Aqui não. {b}Venha me ver no meu escritório depois da escola{/b}, sim?"
    show teacher 13
    show player 14
    player_name "Ok, eu te encontro lá."
    return

label bissette_dialogue_check_dictionary:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Ei, {b}Miss Bissette{/b}. Encontrei um dicionário na biblioteca, mas faltam algumas páginas."
    show player 239_240 with dissolve
    pause
    show player 503 with dissolve
    pause
    show player 5
    show teacher 22b
    with dissolve
    bis "Oh meu!"
    bis "Isso vai dificultar as coisas, acho."
    bis "A seção Francês para Inglês está intacta, mas faltam muitas palavras..."
    bis "Receio que alguns deles possam ser cruciais para os assuntos que iremos estudar."
    show teacher 21b
    show player 10
    player_name "Ugh, eu tinha medo disso.."
    show player 5
    show teacher 21
    bis "Hmm, talvez nem tudo esteja perdido. Tenho certeza {b}a classmate of yours{/b} estaria disposto a permitir que você copie as páginas ausentes do dicionário."
    bis "Você pode usar o {b}photo copier in the computer lab{/b}."
    show teacher 22
    show player 14
    player_name "Essa é uma boa ideia!"
    show player 13
    show teacher 2 with dissolve
    bis "De nada, {b}[firstname]{/b}."
    bis "Certifique-se de obter palavras em inglês que começam com a letra 'B' para a próxima lição."
    show teacher 1
    show player 14
    player_name "Tudo bem, hora de rastrear outro dicionário..."
    show player 13
    show teacher 12
    bis "Já trabalhando tão duro. Eu posso dizer que você está desejando a recompensa especial, muito, sim?"
    show teacher 13
    show player 10
    player_name "Quaisquer pensamentos sobre cujo dicionário eu deveria pedir emprestado?"
    show player 13
    show teacher 11
    bis "Hmm..."
    show teacher 2
    bis "Possivelmente {b}Judith{/b}?"
    bis "Ela mostra muito talento para a língua francesa..."
    show teacher 1
    show player 14
    player_name "Ok, eu vou começar com {b}Judith{/b} então."
    return

label bissette_dialogue_intro:
    show player 1 at left
    show teacher 2 at right
    with dissolve
    bis "Oi, {b}[firstname]{/b}!"
    show player 17 at left
    show teacher 1 at right
    player_name "Oi, {b}Miss Bissette{/b}!"
    show player 1 at left
    show teacher 2 at right
    bis "Você conseguiu acompanhar seus estudos?"
    bis "Eu realmente espero que você faça!"
    bis "Agora, há algo que você gostaria de falar?"
    show teacher 1
    return

label bissette_dialogue_food_assignment_intro:
    show player 10
    player_name "Qual minha próxima tarefa?"
    show player 5
    show teacher 2
    bis "eu quero que você {b}escreva alguns parágrafos sobre sua comida favorita, em Frances{/b}."
    bis "Então vamos discutir isso juntos, sim?"
    show teacher 1
    show player 14
    player_name "Oh sim!"
    return

label bissette_dialogue_food_assignment_prepare_assignment:
    player_name "Eu deveria visitar esse bibliotecário novamente. Talvez ela pudesse encontrar um livro sobre {b}French food{/b} para mim."
    player_name "Então eu posso digitar algo no meu computador."
    player_name "Obrigado, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_food_assignment_do_assignment:
    player_name "Eu deveria digitar algo no meu computador."
    player_name "Obrigado, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_poem_assignment_intro:
    show player 10
    player_name "Lembre-me, qual foi a tarefa novamente?"
    show player 5
    show teacher 2
    bis "O que? Você já esqueceu?"
    bis "{b}Você deve escrever um poema romântico em Frances{/b}!"
    show teacher 1
    show player 14
    player_name "Oh certo!"
    player_name "Obrigado, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Volte para mim quando estiver completo."
    bis "Não me deixe esperando, meu homem bonito."
    return

label bissette_dialogue_poem_assignment_do_assignment:
    show player 14
    player_name "Eu deveria digitar algo no meu computador."
    return

label bissette_dialogue_poem_assignment_print_assignment:
    show player 14
    player_name "Eu terminei o poema, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Ótimo, deixa eu ver!"
    show teacher 1
    show player 10
    player_name "Ah, eu preciso imprimi-lo primeiro..."
    show player 5
    show teacher 2
    bis "Bem, a impressora está no {b}computer lab{/b}, sim?"
    show teacher 1
    show player 14
    player_name "Sim, já volto!"
    return

label bissette_dialogue_private_tutoring:
    show player 10
    player_name "Você acha que poderíamos nos encontrar hoje à noite no seu escritório??"
    show player 26
    player_name "Você sabe, para alguns ... Explicações?"
    show player 13
    show teacher 12
    bis "Ah, tutoria. sim!"
    bis "Vejo você hoje à noite por alguém de uma vez, sim?"
    show teacher 13
    show player 33
    player_name "Sim!"
    show player 13
    show teacher 12
    bis "Muito bom, meu homem bonito!"
    return

label bissette_dialogue_tutoring:
    show player 10
    player_name "Eu queria saber se você ainda estava oferecendo aulas particulares?"
    show player 5
    show teacher 3
    bis "Ah sim!"
    show teacher 1
    show player 14
    player_name "Impressionante! Quando você estaria disponível-"
    show player 11
    show teacher 2
    bis "Impressionante! Você é o primeiro aluno a perguntar sobre o ensino!"
    show teacher 1
    show player 12
    player_name "Realmente? Isso é estranho..."
    show player 5
    show teacher 5
    bis "Eu estava começando a pensar que ninguém estava interessado na recompensa especial."
    show teacher 1
    show player 12
    player_name "Ah sim, eu esqueci a recompensa especial..."
    show player 5
    show teacher 5
    bis "Quoi !? Você não está desejando a recompensa também?!"
    show teacher 4
    show player 29 with dissolve
    player_name "Err ... Não, quero dizer ... A-uma recompensa especial parece maravilhoso, {b}Miss Bissette{/b}."
    show player 3
    show teacher 3
    bis "Super ah!"
    show teacher 2
    bis "Depois nos encontraremos depois da escola para algumas aulas individuais, sim?"
    show teacher 1
    show player 10 with dissolve
    player_name "Ummm ... Sim, acho que vai-"
    show player 11
    show teacher 2
    bis "Três bons!"
    bis "Apenas certifique-se de trazer seu {b}French dictionary{/b} ao longo."
    show teacher 1
    show player 24
    player_name "Ah, merda. Sobre isso... {b}Miss Bissette{/b}, Não consigo encontrar o meu {b}French Dictionary{/b}."
    show player 25
    player_name "Não está na minha mochila, minha casa ou meu armário..."
    show player 5
    show teacher 5
    bis "Oh não, isso não é bom!"
    bis "Talvez você devesse {b}stop by the library{/b} e ver se eles têm um?"
    show teacher 2
    bis "Eu lhe emprestaria o meu, mas receio que tenha derramado vinho recentemente sobre ele."
    show teacher 1
    show player 14
    player_name "Ah, sim, eu esqueci a biblioteca!"
    show player 13
    show teacher 2
    bis "Sim, eu vou lá muitas vezes."
    show teacher 12
    bis "Adoro a sensação de um bom livro em minhas mãos."
    bis "Abraçado pelo fogo quente com um pouco de vinho forte..."
    bis "É o paraíso."
    show teacher 13
    show player 11
    player_name "..."
    show teacher 2
    bis "Oh, bobo eu, balbuciando sem parar. Deixe-me saber quando você tiver o dicionário, sim?"
    show teacher 1
    show player 14
    player_name "Coisa certa, {b}Miss Bissette{/b}."
    return

label bissette_dialogue_get_dictionary:
    show player 12
    player_name "Lembre-me do que preciso obter antes de podermos estudar juntos?"
    show player 5
    show teacher 2
    bis "Você precisará de um dicionário de francês para inglês."
    bis "{b}Check the library{/b}, sim?"
    show teacher 1
    show player 14
    player_name "Ah, está certo!"
    player_name "Obrigado!"
    return

label bissette_dialogue_replace_missing_pages:
    show player 12
    player_name "O que eu deveria fazer de novo?"
    show player 5
    show teacher 2
    bis "Copie as páginas que estão faltando em um dicionário de colegas de classe."
    show teacher 1
    show player 14
    player_name "Ah, está certo!"
    show player 13
    show teacher 2
    bis "Verificar com {b}Judith{/b}. Ela é muito boa com seu francês."
    show teacher 1
    show player 14
    player_name "E depois {b}o laboratório de informática tem a copiadora{/b}..."
    player_name "Entendi, obrigado novamente!"
    return

label bissette_dialogue_chat:
    show player 29 at left
    show teacher 1 at right
    player_name "{b}Miss Bissette{/b}, Eu só queria dizer que realmente aprecio a ajuda em acompanhar o meu trabalho na escola!"
    show player 13 at left
    show teacher 3 at right
    bis "O prazer é meu! Tudo o que eu quero é ter certeza de que você está motivado para realizar..."
    show teacher 12 at right
    bis "...E eu amo recompensar estudantes que trabalham duro!"
    show teacher 13 at right
    show player 10 at left
    player_name "Eu farei o meu melhor. Eu realmente quero entrar em uma boa faculdade..."
    show teacher 2 at right
    show player 13 at left
    bis "Isto é o que eu gosto de ouvir!"
    bis "Posso revisar sua {b}homework{/b} com você quando entregar, se você quiser!"
    show teacher 1 at right
    show player 17 at left
    player_name "Isso soa bem, {b}Miss Bissette{/b}! Obrigado!"
    return

label bissette_dialogue_leave:
    show player 14
    player_name "Não. Eu só queria dizer olá."
    show teacher 2
    show player 13
    bis "Bem, sente-se. A aula começará em breve!"
    show teacher 3
    bis "Eu tenho uma lição emocionante planejada para hoje!"
    show teacher 1
    show player 2
    player_name "Parece bom, {b}Miss Bissette{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
