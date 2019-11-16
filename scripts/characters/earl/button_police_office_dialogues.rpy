label earl_police_office_dialogue_roxxy_ask_earl_release:
    show earl 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Com licença senhor?"
    show player 5
    show earl 2
    ear "Hã?"
    ear "O que vocês estão fazendo aqui?"
    show earl 3 with dissolve
    show player 10
    player_name "Estamos apenas tentando obter algumas informações sobre uma prisão que vocês fizeram hoje mais cedo."
    show player 5
    show earl 2 with dissolve
    ear "Hmm, você é {b}Crystal's{/b} filha, não é? "
    show earl 1
    show roxxy 1jf
    rox "..."
    show player 10
    player_name "Sim, ela é, senhor."
    player_name "Você poderia nos contar o que está acontecendo?"
    show player 5
    show earl 2
    ear "Receio não ter permissão para discutir esses assuntos com ninguém que não seja a família dela."
    ear "Se você quiser vir comigo, senhorita. Vou lhe informar como tudo isso funciona."
    show earl 1
    show player 10
    player_name "... Sim, tudo bem. Vou esperar mais-"
    show player 11
    show roxxy 2c at Position (xpos=500) with dissolve
    rox "Não!"
    show roxxy 2cf at Position (xpos=434)
    with dissolve
    rox "... Quero dizer."
    show roxxy 33f at Position (xpos=400) with dissolve
    rox "Eu quero que ele fique. Está tudo bem."
    show roxxy 32f
    show player 13
    ear "..."
    show earl 2
    ear "Você tem certeza."
    show earl 1
    show roxxy 33f
    rox "Sim."
    show roxxy 32f
    show earl 2
    ear "Adapte-se."
    ear "Recebemos uma dica anônima nesta manhã sobre um grande estoque de drogas em sua residência."
    ear "Então nós dirigimos para dar uma olhada."
    ear "Você sabia que {b}your mother{/b} havia mais de meio quilo de metanfetamina de cristal escondida embaixo do sofá? "
    show earl 1
    show roxxy 1if
    show player 23
    player_name "Uma libra?!"
    show player 22
    show roxxy 27f at Position (xoffset=67)
    rox "..."
    show earl 2
    ear "Temo que sim."
    ear "Essa é uma acusação criminal de drogas."
    orelha "Estamos segurando {b}your mother{/b} por posse com intenção de vender ".
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "..."
    show player 10
    player_name "Isso não é bom."
    show player 5
    show roxxy 1jf with dissolve
    show earl 2
    ear "Não, filho. Certamente não é."
    ear "... Agora, eu conheço {b} Crystal {/b} há muito tempo."
    ear "Fomos juntos à escola naquele dia."
    ear "Ela sempre foi boa em se meter em problemas ..."
    ear "... Mas depois de interrogá-la esta manhã, posso dizer sem dúvida que ela não sabe a primeira coisa sobre cozinhar metanfetamina".
    ear "Agora, ela afirma que fez tudo sozinha e estava olhando para movê-la ..."
    ear "... Mas eu apostaria um bom dinheiro que ela estava apenas segurando por outra pessoa!"
    show earl 1
    rox "..."
    show earl 2
    ear "Infelizmente, a menos que eu tenha provas. Ela vai ficar na prisão por muito tempo."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "{b}*Sniff*{/b}."
    show player 10
    player_name "Ok, bem, e a casa do meu amigo?"
    show roxxy 1jf with dissolve
    show player 5
    show earl 2
    ear "Oh, o trailer?"
    ear "... bem, se {b}Crystal{/b} for condenado, será recuperado pelo Estado e vendido. "
    show earl 1
    show player 25
    player_name "Sheesh..."
    show player 12
    player_name "Existe algo que possamos fazer para evitar isso?"
    show player 5
    show earl 2
    ear "Não, a menos que você possa convencer {b}Crystal{/b} desistir de quem ela está protegendo ... "
    show earl 1
    rox "..."
    show player 11
    player_name "..."
    show player 5
    show earl 2
    ear "Sinto muito como tudo isso aconteceu, senhorita."
    show earl 1
    rox "{b}*Sniff*{/b}"
    show earl 2
    ear "Todos vocês podem {b} ir até as celas e visitá-la {/b}, se quiserem."
    ear "Eles devem terminar de interrogá-la agora."
    show earl 1
    show player 14
    player_name "Tudo bem, obrigado pela informação, oficial."
    show player 13
    hide earl with dissolve
    pause
    show player 5
    show roxxy 33bf
    rox "... {b}*Fungar*{/b} Tudo isso para esse idiota consumado ... "
    show roxxy 1j with dissolve
    show player 10
    player_name "Vamos lá, vamos conversar com {b}your mom{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label earl_police_office_dialogue_first_visit:
    show earl 2 at right
    show player 11 at left
    with dissolve
    ear "O que você está fazendo aqui ?!"
    show earl 3
    ear "É mais um daqueles \" Traga seus filhos para o trabalho \ "dias?"
    show earl 1
    show player 14
    player_name "Oh, não, só estou passando, senhor."
    player_name "Eu queria falar com {b}Harold{/b}."
    show earl 2
    show player 1
    ear "Espere um minuto ... Você não vai à escola com minha filha?"
    show earl 3
    show player 14
    player_name "Oh, certo! Você é {b}Ronda's dad{/b}!"
    show earl 2
    show player 1
    ear "Shiiiiiiiiiiieeeeeet!"
    show player 11
    ear "É melhor você se vigiar da minha filha, ou eu vou ter que vigiar {b}you{/b}."
    show earl 4
    ear "Entendi?!"
    show earl 1
    show player 29
    player_name "Uhh ... é claro, senhor!"
    player_name "Eu nunca-"
    show earl 2
    show player 13 at left
    ear "Relaxe, eu estou apenas brincando com você! Siga em frente agora."
    return

label earl_police_office_dialogue_pre:
    show earl 2 at right
    show player 1 at left
    with dissolve
    ear "E ai, como vai?"
    show earl 3
    return

label earl_police_office_dialogue_donuts:
    show earl 1
    show player 14
    player_name "Isso pode parecer uma pergunta boba, mas que tipo de rosquinha faz {b}Harold{/b} gostar?"
    show player 1
    show earl 2
    ear "Hah!"
    ear "{b}Harold{/b} só os come se estiverem {b}[harold_glaze]{/b}..."
    show earl 3
    ear "... Mas não tenho certeza do que mais ele coloca neles."
    show player 14
    show earl 1
    player_name "Entendo."
    show player 11
    show earl 2
    ear "Por que você pergunta?"
    show player 17
    show earl 1
    player_name "Oh, sem motivo."
    show player 11
    show earl 4
    ear "Espere, você não deveria estar na escola? O que você está fazendo aqui-"
    show player 14
    show earl 3
    player_name "Errr..."
    show player 17
    player_name "Obrigado, tchau!"
    return

label earl_police_office_dialogue_harold:
    show player 10
    player_name "Você sabe onde {b}Harold{/b} poderia estar?"
    player_name "Eu preciso errar ... devolver algo para ele!"
    show player 11
    show earl 2
    ear "Não sei para onde ele foi, mas o vi ontem no escritório ..."
    ear "... Ele parecia mal, com certeza!"
    ear "Por um segundo eu pensei que ele estava saindo ..."
    ear "... Então eu disse a ele para tirar uma folga."
    show earl 1
    show player 12
    player_name "Ele mencionou onde estaria enquanto estava de folga?"
    show player 5
    show earl 2
    ear "Eu não queria fazer muitas perguntas, sabia?"
    ear "Às vezes os caras só precisam de um tempo sozinhos ..."
    show earl 1
    show player 14
    player_name "Tudo bem, obrigado."
    return

label earl_police_office_dialogue_roxxys_mom:
    show earl 1
    show player 12
    player_name "Onde podemos falar com o meu {b}friend's mom{/b} novamente?"
    show player 5
    show earl 2
    ear "Ela é {b}downstairs in a cell{/b}."
    ear "Policial {b}Yumi{/b} está lá embaixo, mas ela oferece privacidade a todos para conversar. "
    show earl 1
    show player 14
    player_name "Tudo bem, obrigada."
    return

label earl_police_office_dialogue_leave:
    show player 14
    player_name "Só de passagem, senhor."
    show earl 2
    show player 1
    ear "Tudo bem então."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
