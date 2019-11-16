label button_richard_intro_day:
    show player 14 at left
    show richard
    with dissolve
    player_name "Ei, {b}Richard{/b}."
    show player 13
    show richard f_confused_talk
    rich "Ah não, {b}Lucy{/b} não pediu outro lote desse leite, pediu? "
    show richard f_confused
    show player 12
    player_name "Hã?"
    show player 10
    player_name "Não, eu estava no bairro e pensei- "
    show player 5
    show richard f_phone_talk
    rich "Graças a Deus!"
    show richard f_normal_talk
    rich "Eu juro que a mulher não tem conceito de dinheiro. "
    show richard f_normal
    pause
    show richard f_normal_talk
    rich "{b}*Suspiro*{/b} Agora, o que você quer? "
    show richard f_normal
    return

label button_richard_intro_night:
    show player 10 at left
    show richard f_normal
    with dissolve
    player_name "Ei, {b}Richard{/b}."
    show player 5
    show richard f_angry_talk
    rich "O que você está fazendo aqui, garoto? "
    rich "Você não vê que estou tentando relaxar na privacidade da minha própria casa ?!"
    show richard f_angry
    show player 10
    player_name "Eu errei"
    player_name "Sinto muito."
    show player 5
    pause
    show richard f_phone_talk
    rich "{b}*Suspiro*{/b}"
    show richard f_normal_talk
    rich "O que você quer?"
    show richard f_normal
    return

label button_richard_take_it_easy_lucy:
    show player 10 at left
    show richard f_normal
    player_name "Por que você é sempre tão rigoroso com sua esposa? "
    show player 5
    show richard f_angry_talk
    rich "O que você disse?!"
    show richard f_angry
    pause
    show richard f_angry_talk
    rich "Isso não é da sua conta, não é? "
    show richard f_angry
    show player 10
    player_name "Eu só-"
    player_name "Ela parece uma moça muito legal e está tentando muito-"
    show player 5
    show richard f_normal_talk
    rich "Hah! É muito fácil para você dizer, garoto. "
    show richard f_angry_talk
    rich "Você não é quem ela está colocando na casa pobre com todas as suas idéias estúpidas de creche! "
    show richard f_angry
    show player 12
    player_name "sim mas-"
    show player 5
    show richard f_angry_talk
    rich "Estou aqui fora, rebentando, todos os dias, tentando começar algo real! "
    rich "Eu tenho problemas suficientes sem adicionar sua boca à lista."
    rich "Então, a menos que você tenha negócios reais comigo, sugiro que prossiga."
    show richard f_angry
    return

label button_richard_hows_the_business:
    show player 10 at left
    show richard f_normal
    player_name "Como vai o seu negócio de carpintaria? "
    show player 5
    show richard f_normal_talk
    rich "Por que você lidera algum trabalho para mim ?! "
    show richard f_normal
    show player 10
    player_name "N-não, na verdade não ..."
    show player 5
    show richard f_phone_talk
    rich "Ugh, figuras. "
    show richard f_normal_talk
    rich "Os negócios estão progredindo. "
    rich "Lentamente".
    show richard f_normal
    show player 14
    player_name "Bem, qualquer progresso é bom, certo? "
    show player 13
    show richard f_normal_talk
    rich "Sim, suponho. "
    rich "Ainda assim, depois de todos esses anos, eu realmente pensei que estaria mais adiantado."
    show richard f_normal
    show player 5
    return

label button_richard_nothing_day:
    show player 10 at left
    show richard f_normal
    player_name "Eu não preciso de nada. "
    player_name "Desculpe incomodá-lo."
    show player 5
    show richard f_normal_talk
    rich "Uh huh."
    hide player
    hide richard
    with dissolve
    return

label button_richard_nothing_night:
    show player 10 at left
    show richard f_normal
    player_name "Eu não preciso de nada. "
    show player 5
    show richard f_angry_talk
    rich "Bem, pare com isso! "
    show richard f_normal_talk
    rich "{b}Tempo da ferramenta{/b} está começando a qualquer segundo e eu não quero perder nenhuma das piadas! "
    show richard f_normal
    show player 11
    player_name "..."
    hide player
    hide richard
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
