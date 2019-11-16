label eve_classroom_dialogue_eve_intro:
    scene classroom
    show evedesk 1 at left
    with fade
    eve "Uau ... eu pensei que você estava morto, com certeza!"
    show evedesk 2
    player_name "O que? Como assim?"
    show evedesk 1
    eve "Não sei ... Você está desaparecido o mês todo e as pessoas começaram a inventar rumores sobre como sua família havia sido assassinada ou algo assim ..."
    show evedesk 3
    player_name "Ugh ... Não é nada disso!"
    show evedesk 4
    eve "Eu imaginei. As pessoas gostam de fofocar, e essa escola é apenas uma grande piada."
    eve "Fico feliz que nosso último ano esteja quase no fim ..."
    show evedesk 5
    player_name "Sim, eu sei o que você quer dizer."
    show evedesk 6
    eve "Você deveria sair conosco no {b} park {/b} em algum momento ... Evite todos esses idiotas na escola e relaxe, sabe?"
    show evedesk 5
    eve "Certifique-se de vir à {b} noite {/b} ... geralmente é quando vamos lá."
    player_name "Ehh ... Eu acho que eu poderia ir uma noite."
    show evedesk 6
    eve "Você decide. Faça o que você quiser!"
    show evedesk 4
    eve "Oh, ei, você ouviu o anúncio da {b}Miss Bissette's{/b} sobre uma recompensa especial?"
    show evedesk 1
    eve "Ou você estava dormindo nessa parte?"
    show evedesk 3
    player_name "Ei! Eu estava acordado ... nessa parte."
    show evedesk 4
    eve "Eu me pergunto qual será a recompensa."
    eve "Ela realmente não falou muito sobre isso. Provavelmente algo estúpido de qualquer maneira."
    eve "Eu já estou indo muito bem, então nem vale a pena tentar."
    show evedesk 2
    player_name "Por que não?"
    show evedesk 6
    eve "Como está indo de um B para um A seria uma coisa muito melhor?"
    eve "Você seria mais provável ganhar ..."
    show evedesk 5
    player_name "Eu?"
    show evedesk 1
    eve "Bem, sim ... você está ruim agora, não está?"
    eve "Você pode melhorar muito."
    show evedesk 6
    eve "Além disso, {b} Miss Bissette {/b} favorece homens de qualquer maneira."
    eve "Você deve considerar seriamente."
    hide evedesk with dissolve
    return

label eve_classroom_dialogue_intro:
    show evedesk 4 at left with dissolve
    eve "Olá, {b}[firstname]{/b}."
    show evedesk 5
    player_name "Oi, {b}Eve{/b}."
    show evedesk 4
    eve "E aí?"
    return

label eve_classroom_dialogue_talent_show_help:
    show evedesk 5
    player_name "Você toca algum instrumento?"
    show evedesk 4
    eve "Não, eu não toco nenhum instrumento. Eu sempre quis aprender, mas não tive tempo, sabia?"
    show evedesk 5
    player_name "Ok, bem, e quanto a cantar?"
    show evedesk 1
    eve "Oh, umm..."
    show evedesk 4
    eve "Sim, eu gosto de cantar, eu acho. Não sei se sou bom."
    show evedesk 5
    player_name "Eu aposto que você é! Você deve se inscrever no show de talentos comigo!"
    show evedesk 3
    player_name "Estamos realmente sofrendo por mais voluntários."
    show evedesk 1
    eve "... Sim, eu não sei."
    eve "Você quer que eu cante na frente de toda a escola? Isso parece bastante embaraçoso."
    eve "... E eu não canto há um tempo. Desde que minha máquina de karaokê quebrou."
    eve "Estou sem prática."
    show evedesk 5
    player_name "Hmm..."
    player_name "Sabe, acho meu amigo {b}Erik{/b} tem um {b}karaoke machine{/b} no porão dele."
    show evedesk 4
    eve "Oh sim?"
    show evedesk 5
    player_name "Totalmente! Você deve vir algum dia e praticar!"
    show evedesk 4
    eve "Heh, você quer que eu cante para você e seu amigo?"
    show evedesk 5
    player_name "Não, todos nós podemos cantar juntos! Vamos lá, hoje à noite, será divertido!"
    eve "..."
    show evedesk 4
    eve "Tudo bem, eu acho que posso parar por um tempo."
    show evedesk 5
    player_name "Impressionante! {b}I'll encontro você em Erik's house{/b} esta noite."
    return

label eve_classroom_dialogue_adehsive:
    show evedesk 5
    player_name "Qual era o plano de novo?"
    show evedesk 4
    eve "Você deveria conhecer {b}Kevin{/b} no {b}science lab depois da aula{/b}."
    eve "Lembrar?"
    show evedesk 5
    player_name "Ah, está certo. obrigado, {b}Eve{/b}!"
    return

label eve_classroom_dialogue_bissettes_reward:
    show evedesk 5
    player_name "Você vai se inscrever para receber tutoria de {b}Miss Bissette{/b}?"
    show evedesk 4
    eve "Eu já estou indo muito bem, então nem vale a pena tentar."
    show evedesk 2
    player_name "Por que não?"
    show evedesk 6
    eve "Como está indo de um B para um A muito melhoria?"
    eve "Você teria mais chances de ganhar..."
    show evedesk 5
    player_name "Eu?"
    show evedesk 1
    eve "Bem, sim ... você está falhando agora, não está?"
    eve "Você tem muito espaço para melhorias."
    show evedesk 6
    eve "Mais, {b}Miss Bissette{/b} favorece os caras de qualquer maneira."
    eve "Você deve considerar seriamente."
    return

label eve_classroom_dialogue_hang_out:
    show evedesk 5
    player_name "Onde você disse que estava?"
    show evedesk 4
    eve "Meus amigos e {b}Eu saio no parque{/b}."
    eve "Apenas certifique-se de {b}venha à noite{/b}... geralmente é quando vamos lá fora."
    show evedesk 5
    player_name "Tudo bem. Eu posso parar uma noite."
    show evedesk 6
    eve "Você decide. Faça o que você quiser!"
    return

label eve_classroom_dialogue_leave:
    show evedesk 5
    player_name "Nada, só queria dizer olá."
    show evedesk 4
    eve "Oh Falo com você mais tarde então."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
