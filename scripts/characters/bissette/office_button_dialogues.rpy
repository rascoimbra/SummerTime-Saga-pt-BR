label bissette_dialogue_office_bissette_roxxy_exam_convince:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "O que eu deveria estar fazendo de novo?"
    show player 5
    show teacher 5
    bis "Você esqueceu?"
    bis "Você deve convencer {b}Roxxy{/b} para aparecer no exame."
    bis "Caso contrário, a média de notas de toda a classe sofrerá."
    show teacher 4
    show player 14
    player_name "Oh, certo!"
    player_name "Não se preocupe, {b}Miss Bissette{/b}! eu estou trabalhando nisso!"
    return

label bissette_dialogue_office_bissette_roxxy_convinced:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "{b}Miss Bissette{/b}?"
    show player 13
    show teacher 5
    bis "Sim?"
    show teacher 4
    show player 14
    player_name "eu convenci {b}Roxxy{/b} para aparecer no teste!"
    show player 13
    show teacher 2
    bis "Verdadeiramente!?"
    show teacher 1
    show player 17
    player_name "Sim!"
    show teacher 25 zorder 1 with dissolve

    bis "Você salva minha vida!"
    show teacher 26 with dissolve
    bis "O que eu faria sem você?!"
    show teacher 27 with dissolve
    show player 29 with dissolve
    player_name "O que eu faria sem você?..."
    show player 13
    show teacher 16
    with dissolve
    bis "Agora você pode ter certeza de que suas tarefas são sim?"
    show teacher 17
    show player 14
    player_name "Eu vou! Não se preocupe!"
    show player 13
    show teacher 16
    bis "Muito bom Na próxima aula teremos o teste."
    show teacher 17
    show player 14
    player_name "Certo, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_office_intro:
    show teacher 3 at right
    show player 13 at left
    with dissolve
    bis "Bom dia, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Oi, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Com o que posso ajudar?"
    show teacher 1
    return

label bissette_dialogue_office_bissette_wine_sampling:
    player_name "Estou animado para provar esse vinho, {b}Miss Bissette{/b}."
    show player 13
    show teacher 12
    bis "Mal posso esperar!"
    bis "Você vai provar muitas coisas hoje à noite, sim?"
    show teacher 13
    show player 29 with dissolve
    player_name "*Gole * S-Sim..."
    show player 14
    show teacher 3
    bis "Muito bem, eu te vejo no meu escritório hoje à noite."
    show teacher 13
    show player 14 with dissolve
    player_name "Vejo você lá!"
    return

label bissette_dialogue_office_leave:
    show player 14
    player_name "Acho que não preciso de nada agora."
    show player 13
    show teacher 2
    bis "Muito bem!"
    show teacher 1
    show player 36 with dissolve
    player_name "Tchau!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
