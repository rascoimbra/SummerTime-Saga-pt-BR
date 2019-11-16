label ronda_dialogue_intro:
    scene gym
    show ronda b_jersey a_jersey_sides f_normal at right
    show player 36 at left
    with dissolve
    player_name "Ei, {b}Ronda{/b}. Como você está?"
    show player 13 with dissolve
    show ronda f_normal_talk
    ron "Eu estou bem. A questão é que você está treinando? "
    show ronda f_normal
    show player 11
    player_name "..."
    show player 10
    player_name "Não-"
    show player 11
    show ronda f_upset_angry
    ron "Então pare de mover os lábios e comece a mover as ... pernas! "
    show ronda f_upset
    show player 34
    player_name "???"
    show ronda f_normal_talk
    ron "Deixa pra lá. É apenas algo que meu pai sempre diz ... "
    show player 5
    ron "De qualquer forma, é melhor você se apressar, porque os testes estão chegando rapidamente!"
    show ronda f_normal
    return

label ronda_dialogue_talent_show_help:
    show player 10
    player_name "Eu não acho que você estaria interessado em ser voluntário para {b}Ms. Dewitt's{/b} no show de talentos musicais? "
    show player 5
    show ronda b_jersey a_jersey_sides f_normal_talk
    ron "Talento musical? Não, eu não estaria interessado. "
    show ronda f_normal
    show player 10
    player_name "Você tem certeza? Você não toca nenhum instrumento ou canta? "
    show player 5
    show ronda f_normal_talk
    ron "Umm, você não vê que tenho coisas mais importantes para focar? Como pista e natação ... "
    ron "Coisas em que você deveria se concentrar também!"
    ron "Você nunca fará parte do time se continuar ignorando seu treinamento!"
    show ronda f_normal
    show player 30
    player_name "Você sabe, há mais na vida do que esportes, {b}Ronda{/b}..."
    show player 5
    show ronda f_normal_talk
    ron "Pfft, sim, certo. "
    return

label ronda_dialogue_model_help:
    show player 2 at left
    show ronda b_jersey a_jersey_sides f_normal at right
    player_name "Estou trabalhando em um projeto para {b}Miss Ross{/b} e requer um modelo ativo ".
    player_name "Você estaria interessado?"
    show player 1
    show ronda f_normal_talk
    ron "Ocupada."
    show player 10
    show ronda f_normal
    player_name "Ocupado?"
    player_name "Fazendo o que?"
    show player 11
    show ronda f_upset_angry
    ron "Sério, {b}[firstname]{/b}?!"
    ron "Eu tenho que correr 10 quilômetros e tomar um banho de gelo antes do treino de futebol. "
    show player 10
    show ronda f_upset
    player_name "Uhh..."
    show player 11
    show ronda f_upset_angry
    ron "Depois, só tenho 40 minutos para dar algumas voltas antes que a piscina feche. "
    show player 10
    show ronda f_upset
    player_name "isso é loucura" 
    show player 11
    show ronda f_upset_angry
    ron "Depois, volta para casa com uma almofada de aquecimento e flexões ".
    show player 12
    show ronda f_upset
    player_name "OK! OK! Deixa comigo..."
    hide ronda
    hide player
    show player 12
    with dissolve
    player_name "Essa garota é louca! "
    return

label ronda_dialogue_leave:
    show player 10
    player_name "Tudo bem."
    player_name "Vejo você mais tarde."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
