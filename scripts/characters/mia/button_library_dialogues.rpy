label mia_library_dialogue_bissette_find_poem_reference_book:
    show player 14 at left
    show mia 7 at right
    with dissolve
    player_name "Oi, {b}Mia{/b}! O que está rolando?"
    show player 13
    show mia 10
    mia "Olá, {b}[firstname]{/b}!estava prestes a estudar para o próximo teste de química ".
    show mia 7
    show player 12
    player_name "Eu pensei que sua mãe não permitiu que você fizesse nada depois da escola? "
    show player 13
    show mia 12
    mia "Ela geralmente não, mas ... "
    show mia 10
    mia "Eu disse a ela que {b}Miss Okita{/b} pode me escrever uma recomendação da faculdade se eu a impressionar indo bem em nosso próximo teste. "
    show mia 7
    player_name "Ela realmente fará isso? "
    show mia 10
    mia "Provavelmente não, mas não custa tentar, certo? "
    mia "E eu realmente saio com {b}Judith{/b} fora da minha casa também! "
    show mia 7
    show player 14
    player_name "Sim, suponho que não. "
    show player 13
    show mia 10
    mia "O que você está fazendo aqui?"
    show mia 7
    show player 14
    player_name "{b}Miss Bissette{/b} me deu uma tarefa. Pensei que talvez pudesse me inspirar aqui. "
    show player 13
    show mia 10
    mia "Oh sim? Qual é a tarefa? "
    show mia 7
    show player 10
    player_name "Bem, é meio embaraçoso ... "
    show player 5
    show mia 9
    mia "Hehe, sério ?! Bem, você tem que me dizer agora! "
    show mia 7
    show player 10
    player_name "* Suspiro * Eu devo escrever um poema romântico em francês. "
    show player 5
    show mia 10
    mia "Isso não é embaraçoso! "
    show mia 7
    show player 12
    player_name "Não?"
    show player 5
    show mia 10
    mia "Não! Todos nós tivemos que fazer isso! "
    show mia 12
    mia "Bem, todos menos {b}Roxxy{/b}... Ela nunca faz a lição de casa. "
    show mia 7
    show player 14
    player_name "Eu não sabia Qual foi o seu poema? ​​"
    show player 13
    show mia 12
    mia "Ah eu ... "
    show mia 56 with dissolve
    mia "...Você sabe, isso e aquilo, hehe ... "
    show mia 55
    show player 14
    player_name "Aha! Veja, é embaraçoso! "
    show player 13
    show mia 10 with dissolve
    mia "Sim, acho que é um pouco. "
    show mia 7
    show player 10
    player_name "Eu nem sei como começar a escrever essa coisa! "
    player_name "Eu provavelmente deveria procurar um livro sobre {b}Romance francês{/b}..."
    show player 13
    show mia 10
    mia "Você sabe, {b}Judith{/b} e eu achei um realmente informativo ".
    show mia 7
    show player 10
    player_name "Sério?"
    show player 13
    show mia 10
    mia "Sim, era bastante gráfico ... "
    show mia 7
    show player 12
    player_name "Você se lembra como foi chamado? "
    show player 13
    show mia 12
    mia "Hmm, não, na verdade não. "
    show mia 10
    mia "{b}Judith{/b} teve por último. Ela estava usando {b}na sala dos fundos{/b} lá, eu acho. "
    show mia 7
    show player 10
    player_name "Huh, você acha que ela pode ter deixado lá? "
    show player 13
    show mia 10
    mia "Talvez."
    show mia 7
    show player 14
    player_name "Acho que vou dar uma olhada então. Obrigado pela ajuda, {b}Mia{/b}!"
    show player 13
    show mia 10
    mia "Sem problemas! Boa sorte, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Você também!"
    return

label mia_library_dialogue_bissette_mia_book_feedback:
    show mia 10 at right
    show player 13 at left
    with dissolve
    mia "Alguma sorte em encontrá-lo? "
    show mia 7
    show player 10
    player_name "Sim, eu achei ... "
    show player 14
    player_name "Você não estava brincando, é realmente gráfico! "
    show player 13
    show mia 56 with dissolve
    mia "...Sim!"
    show mia 55
    show player 10
    player_name "eu imagino o que {b}Judith{/b} estava fazendo isso lá atrás sozinha ".
    show player 5
    show mia 56
    mia "Heh, sim, eu não sei ... "
    mia "... eu realmente deveria voltar a estudar. "
    show mia 55
    show player 14
    player_name "Oh, certo! Desculpa!"
    player_name "obrigado novamente, {b}Mia{/b}."
    show player 13
    show mia 56
    mia "Sem problemas, {b}[firstname]{/b}."
    hide mia with dissolve
    show player 14
    player_name "Tudo bem, é melhor eu levar essa casa para {b}meu computador{/b} e começar a escrever sobre esse poema para {b}Miss Bissette{/b}."
    return

label mia_library_dialogue_do_not_disturb:
    show player 10 with dissolve
    player_name "Não, eu deveria deixá-la estudar em paz ... "
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
