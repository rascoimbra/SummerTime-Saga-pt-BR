label anna_dialogue_anna_dog_hunt:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Ei {b}[firstname]{/b}, você viu um {b}cachorro pequeno{/b} sem trela ??"
    show anna 4
    show player 10
    player_name "Acho que não..."
    show anna 5
    show player 11
    anna "Eu acho que o perdi."
    anna "Eu estava correndo ao longo da trilha pelo {b}forest{/b}, e quando olhei para trás, ele se foi !!"
    show anna 4
    show player 10
    player_name "Você já olhou ao longo da trilha?"
    show anna 5
    show player 11
    anna "Claro! Eu olhei em todos os lugares!"
    anna "Mas não posso cobrir a trilha e o {b}forest{/b} sozinho..."
    show anna 4
    show player 10
    player_name "Como ele é?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Oh, certo. Ele é um {b}pug{/b}, sobre este grande!"
    show anna 5 at right
    anna "O nome dele é {b}Awesomo{/b}."
    anna "Ele está um pouco acima do peso, então ele não poderia ter ido longe."
    anna "Por favor! Você vai me ajudar a encontrá-lo?"
    show anna 4
    return

label anna_dialogue_anna_dog_hunt_yes:
    show player 14
    player_name "Certo. Vou procurá-lo."
    player_name "Há algo que eu deva saber sobre ele?"
    player_name "Algo que vai me ajudar a encontrá-lo?"
    show player 1
    show anna 5
    anna "Bem ... Ele realmente gosta de comer {b}cookies{/b}."
    anna "Se você tiver alguns, tenho certeza que ele sentirá o cheiro deles e sairá..."
    show anna 11
    show player 14
    player_name "OK! Eu vou te ver se eu o encontrar!"
    show anna 12
    show player 1
    anna "Muito obrigado!"
    return

label anna_dialogue_anna_dog_hunt_no:
    show player 10
    player_name "Eu adoraria ajudar, mas tenho algumas coisas que preciso atender..."
    show player 11
    show anna 5
    anna "Oh, desculpe incomodá-lo..."
    return

label anna_dialogue_anna_find_dog_have_dog:
    scene location_park_closeup
    show player 247 at left with dissolve
    show anna 4 at right with dissolve
    player_name "Adivinha quem eu encontrei?"
    show anna 5 with vpunch
    anna "!!!"
    show anna 12
    anna "{b}Awesomo{/b}!!!"
    show player 1
    show anna 9
    with dissolve
    anna "Onde você o encontrou ?!"
    show anna 8
    show player 14
    player_name "Ele estava na floresta próxima, perto da trilha..."
    player_name "E você estava certo! Alguns biscoitos fizeram o truque."
    show anna 10
    show player 1
    anna "Obrigado {b}tão{/b} Muito de!"
    show anna 9
    anna "Certificarei de lhe retribuir de alguma forma."
    show anna 7
    anna "Eu deveria levá-lo para casa agora. Ele provavelmente está ficando com fome depois de tudo isso."
    show anna 10
    anna "Até a próxima!"
    return

label anna_dialogue_anna_find_dog_do_not_have_dog:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Você o encontrou?"
    show anna 4
    show player 10
    player_name "Ainda não..."
    player_name "Você poderia descrevê-lo para mim novamente? E onde eu poderia encontrá-lo?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Ele é desse tamanho e é um {b}pug{/b}!"
    show anna 5 at right
    anna "Ele deveria estar em algum lugar perto da trilha pelo {b}forest{/b}..."
    anna "...E ele ama {b}cookies{/b}!"
    anna "Talvez você possa usar algum {b}cookies{/b} para atraí-lo."
    show anna 11
    show player 14
    player_name "OK! Eu vou procurá-lo!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
