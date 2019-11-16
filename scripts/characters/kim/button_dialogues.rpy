label kim_button_dialogue_intro:
    show player 13 at left
    show kim 2 at right
    with dissolve
    kim "Herro lá!"
    kim "O que posso fazer para entrar em um veículo novo hoje?"
    show kim 1
    show player 10
    player_name "Oh, uhh..."
    show player 4 with dissolve
    return

label kim_button_dialogue_button:
    show player 14 with dissolve
    player_name "Gostei do seu botão."
    player_name "Você é fã do {b}prefeito Rump{/b}?"
    show player 13
    show kim 2
    kim "Oh, o {b}prefeito Rump{/b} é o numero 1, o melhor prefeito."
    kim "Ele e {b}Kim{/b} são bons amigos!"
    show kim 3
    show player 10
    player_name "Você é amigo do {b}prefeito Rump{/b}?"
    show player 13
    show kim 2
    kim "Sim, eu o ajudo com seus poricies em troca de financiamento."
    show kim 6 with dissolve
    kim "Quando eu subir ao meu trono!"
    show kim 3 with dissolve
    show player 10
    player_name "... Trono?"
    show player 5
    show kim 2
    kim "Sim!"
    kim "Quando eu assumir esse cargo, erigirei um poderoso trono."
    show kim 5 with dissolve
    kim "Hue hue hue hue!"
    show player 12
    player_name "Bem, boa sorte com tudo isso ..."
    show player 5
    show kim 2 with dissolve
    kim "Eu não preciso de rock ..."
    hide kim with dissolve
    show player 10
    player_name "Hmm, por que o nosso {b}prefeito{/b} estaria com esse cara?"
    show player 12
    player_name "... Estranho."
    hide player with dissolve
    return

label kim_button_dialogue_browsing:
    show player 14 with dissolve
    player_name "Estou aqui apenas para navegar."
    show player 13
    show kim 2
    kim "Hmmph, um navegador, não é?"
    kim "Muito bem."
    kim "... Mas se você quiser comprar alguma coisa, eu insisto que você fale comigo e ninguém se oponha!"
    kim "Você entende ?!"
    show kim 1
    show player 10
    player_name "Uhh, sim ..."
    player_name "Com certeza."
    show player 5
    show kim 2
    kim "Bom".
    kim "Eu estarei assistindo!"
    hide kim
    hide player
    with dissolve
    return

label kim_button_dialogue_sign:
    show player 14 with dissolve
    player_name "É você que está no letreiro?"
    show player 13
    show kim 5 with dissolve
    kim "Oh, você percebe sinal, hein ?!"
    kim "Sim, {b}Kim{/b} é o número 1, melhor vendedor de carros!"
    kim "Em breve, eu possuo esse privilégio."
    show kim 4
    show player 12
    player_name "Ah, é??"
    show player 13
    show kim 6 with dissolve
    kim "Ah, sim ... eu vou conquistar esse carro caridade!"
    kim "Vou expandi-lo para a cadeia nacional!"
    show player 11
    kim "Um dia, irei cobrir toda a pranet com minhas concessionarias!"
    show kim 3
    show player 3
    with dissolve
    player_name "..."
    show kim 5 with dissolve
    kim "Hue hue hue hue!"
     kim "Eu serei uma amado DEUS!!!"
    show kim 4
    show player 10 with dissolve
    player_name "... Certo."
    player_name "Bem, eu vou dar uma olhada agora ..."
    show player 5
    show kim 2 with dissolve
    kim "Sim, você vai à torre."
    kim "Venha me encontrar se quiser fazer uma compra."
    hide kim with dissolve
    show player 12
    player_name "Que sujeito estranho."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
