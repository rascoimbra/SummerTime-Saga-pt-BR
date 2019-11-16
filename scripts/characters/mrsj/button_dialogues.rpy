label button_mrsj_greetings:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Oi, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 17
    mrsjo "Ei, {b}[firstname]{/b}!"
    mrsjo "Como você está?"
    show player 14
    show mrsj 14
    player_name "Estou bem, obrigado! "
    show player 1
    show mrsj 17
    mrsjo "Existe algo que eu possa fazer por você? "
    show mrsj 14
    return


label button_mrsj_sex_ed_intro:
    scene erik_upstairs_night_c
    show mrsj 42 at right
    show player 11 zorder 2 at left
    show erik 1f zorder 1 at Position(xpos=300)
    with dissolve
    mrsjo "Ei, rapazes..."
    show mrsj 41
    show player 21
    player_name "O-Oi, {b}Mrs. Johnson{/b}!"
    show player 13
    show erik 4f
    eri "Você é muito bonita, {b}Mrs. Johnson{/b}."
    show erik 1f
    show mrsj 40b with fastdissolve
    mrsjo "Bem, você só vai ficar me encarando ou quer me perguntar uma coisa? "
    show mrsj 39
    return

label button_mrsj_private_yoga_intro:
    scene erik_upstairs_night_c2
    show mrsj 54 at Position(xpos=734,ypos=650)
    show player 433 zorder 2 at left
    with dissolve
    mrsjo "Olá, {b}[firstname]{/b}..."
    show mrsj 53
    player_name "!!!"
    show mrsj 54
    mrsjo "Há algo de errado?"
    show player 435
    show mrsj 53
    player_name "Você .. você está nu, {b}Mrs. Johnson{/b}."
    show player 434
    show mrsj 54
    mrsjo "Eu gosto de me sentir ... confortável no meu quarto ... "
    mrsjo "Você não estava prestes a me perguntar uma coisa? "
    show mrsj 53
    return

label button_mrsj_about_erik:
    show player 14 at left
    show mrsj 14 at right
    player_name "Eu queria falar sobre {b}Erik{/b}..."
    show player 1
    show mrsj 19
    mrsjo "Oh, ele está bem? "
    show player 14
    show mrsj 19c
    player_name "Sim, ele está bem. "
    player_name "Eu estava conversando com ele sobre o que aconteceu na outra noite ... "
    show player 11
    show mrsj 19
    mrsjo "Ele está chateado? "
    show player 14
    show mrsj 19c
    player_name "Não, de jeito nenhum. "
    show player 10
    player_name "Ele só não tem certeza do que quer ... "
    show player 11
    show mrsj 19
    mrsjo "Como assim?"
    show player 10
    show mrsj 19c
    player_name "Eu acho que ele desistiu de conhecer garotas. "
    player_name "Eu poderia tentar ajudá-lo a conseguir uma namorada, mas acho que ele gosta mais de você ..."
    show player 13
    show mrsj 19
    mrsjo "Oh meu..."
    show mrsj 20
    mrsjo "Eu realmente o abriguei demais? "
    show mrsj 19
    mrsjo "O que você acha que eu deveria fazer?"
    show mrsj 19c
    return

label button_mrsj_route_sex_ed:
    show player 14 at left
    show mrsj 19c at right
    player_name "Eu acho que é melhor se você der a atenção que ele precisa ... "
    show mrsj 19
    show player 1
    mrsjo "Você realmente acha? "
    show mrsj 19c
    show player 14
    player_name "Bem, acho que ele não quer ver outras garotas ... "
    player_name "... E ele realmente gosta de você!"
    show mrsj 19
    show player 1
    mrsjo "Ele sempre esteve perto de mim ... "
    show mrsj 19c
    show player 14
    player_name "Nos divertimos muito na outra noite! "
    player_name "eu nunca vi {b}Erik{/b} tão feliz. "
    show mrsj 19
    show player 11
    mrsjo "Você acha que ... vocês gostariam mais desse tipo de atenção? "
    show mrsj 19c
    show player 21
    player_name "Eu ... acho que sim! "
    show mrsj 20
    show player 13
    mrsjo "Se nenhuma das meninas da escola lhe der a atenção que ele precisa ... "
    show mrsj 19
    mrsjo "...Talvez eu devesse ser o único? "
    show mrsj 14
    show player 14
    player_name "Eu acho que ele gostaria disso. "
    show mrsj 49
    show player 11
    mrsjo "E se eu desse a vocês um pouco de ... educação sexual pessoal? "
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsjo "É apenas para fins educacionais, é claro ... "
    show mrsj 50
    show player 29
    player_name "Ah, eu acho ... eu não me importaria! "
    show mrsj 49
    show player 13
    mrsjo "Eu teria que pensar primeiro, no entanto. "
    show mrsj 50
    show player 14
    player_name "Certo, {b}Mrs. Johnson{/b}!"
    show mrsj 14
    show player 1
    return

label button_mrsj_route_gf:
    show player 14 at left
    show mrsj 19c
    player_name "Acho que devemos tentar encontrar uma namorada para ele ".
    show player 1
    show mrsj 19
    mrsjo "Você realmente acha? "
    show player 14
    show mrsj 19c
    player_name "Bem, acho que ele ficaria mais feliz ... "
    player_name "... e isso aumentaria sua confiança!"
    show player 1
    show mrsj 20
    mrsjo "Ele precisa sair mais ... "
    show player 10
    show mrsj 19c
    player_name "Não me interpretem mal, nos divertimos muito na outra noite ... "
    show player 14
    player_name "... mas eu acho {b}Erik{/b}que você  precisa conhecer outras garotas. "
    show player 13
    show mrsj 20
    mrsjo "Você está certo..."
    show player 11
    show mrsj 19
    mrsjo "Mas e quanto a mim? "
    show player 10
    show mrsj 19c
    player_name "O que você quer dizer?"
    show player 11
    show mrsj 19
    mrsjo "Bem..."
    mrsjo "Se {b}Erik{/b} encontra uma namorada ... O que vou fazer? "
    show mrsj 20
    mrsjo "Não terei ninguém para dar atenção a ... "
    show player 21
    show mrsj 19c
    player_name "Oh, eu tenho certeza que você encontrará alguém {b}Mrs. Johnson{/b}!"
    show mrsj 14
    player_name "Você é muito ... atraente e amoroso! "
    show player 13
    show mrsj 17
    mrsjo "Aww, é muito gentil da sua parte dizer ".
    show mrsj 50
    mrsjo "Hmm..."
    show mrsj 49
    show player 1
    mrsjo "Eu tenho uma ideia diferente! "
    mrsjo "E se eu tomasse essa atenção ..."
    show player 11
    mrsjo "...e der para {b}você{/b}?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsjo "O que há de errado?"
    mrsjo "Só se você quiser, é o que eu quis dizer ..."
    show player 21
    show mrsj 50
    player_name "Eu-eu não me importaria! "
    player_name "Mas, apenas enquanto {b}Erik{/b} está bem com isso ".
    show player 1
    show mrsj 49
    mrsjo "Apenas pergunte a ele! "
    mrsjo "Tenho certeza que ele ficaria bem com isso ..."
    show player 13
    mrsjo "... especialmente se ele está muito ocupado brincando com outra garota! Ha ha "
    show player 29
    show mrsj 50
    player_name "Suponho que sim, ha ha. "
    show player 14
    player_name "Vou tentar encontrar alguém para ele ... "
    show player 13
    show mrsj 49
    mrsjo "Volte e me diga o que acontece. "
    show player 17
    show mrsj 50
    player_name "Certo, {b}Mrs. Johnson{/b}!"
    show mrsj 14
    show player 1
    return

label button_mrsj_sex_ed_prep:
    show mrsj 14 at right
    show player 10 at left
    player_name "Como podemos ajudá-lo a se preparar para nossa educação sexual novamente? "

    show player 5
    show mrsj 17
    mrsjo "Vou precisar de um bom livro de instruções, como{b}Kama Sutra{/b}."
    mrsjo "E alguns{b}birth control pillspílulas anticoncepcionais{/b}!"
    show mrsj 49
    mrsjo "Você nunca pode ter muito cuidado ... "
    show mrsj 50
    show player 14
    player_name "Tudo bem."
    player_name "Vou tentar encontrá-los ..."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_got_gf:
    show player 14
    player_name "Acho que fui capaz de apresentar {b}Erik{/b} para uma garota da escola! "
    show player 1
    show mrsj 17
    mrsjo "Realmente?!"
    show player 14
    show mrsj 14
    player_name "Sim!"
    player_name "Eles têm muito em comum, seriam perfeitos um para o outro!"
    show mrsj 17
    show player 17
    player_name "Eu acho que vai dar certo com certeza! "
    show player 1
    show mrsj 18
    mrsjo "Isso é maravilhoso!!"
    show mrsj 17
    mrsjo "Eu não posso acreditar que você tem sido tão bom em {b}Erik{/b}."
    show mrsj 49
    mrsjo "Acho que está na hora de lhe dar uma pequena recompensa ... "
    show player 21
    show mrsj 50
    player_name "... Uma recompensa?"
    show player 11
    show mrsj 49
    mrsjo "HComo eu te dou um pouco de...aulas de yoga {b}privada{/b}..."  
    mrsjo "O tipo que você não vê na academia. "
    show mrsj 50
    show player 21
    player_name "Isso seria incrível, {b}Mrs. Johnson{/b}!"
    show player 13
    show mrsj 49
    mrsjo "Apenas venha me visitar à noite no meu quarto ... verifique se você está bem descansado! "
    show player 11
    mrsjo "Pode ser ... bastante cansativo. "
    show player 21
    show mrsj 50
    player_name "Sim, {b}Mrs. Johnson{/b}."
    show player 13
    show mrsj 49
    mrsjo "Até mais, estarei esperando! "
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_stole_gf:
    show mrsj 19c at right
    show player 10 at left
    player_name "Eu não acho que vai dar certo {b}June{/b}..."
    show player 11
    show mrsj 19
    mrsjo "A garota da escola? "
    show player 10
    show mrsj 19c
    player_name "Sim."
    show player 5
    show mrsj 19
    mrsjo "Que pena ... "
    mrsjo "O que aconteceu?"
    show player 10
    show mrsj 19c
    player_name "Ela simplesmente não está interessada e ... "
    show mrsj 51
    player_name "... ela pode vir mais tarde para minha casa para ficar comigo ".
    show player 5
    show mrsj 52
    mrsjo "Oh meu..."
    mrsjo "E {b}Erik{/b} está bem com isso? "
    show player 10
    show mrsj 51
    player_name "Não tenho certeza ... provavelmente não? "
    show player 5
    show mrsj 52
    mrsjo "Eu tenho que dizer ... Estou um pouco decepcionado com você, {b}[firstname]{/b}."
    show mrsj 51
    player_name "..."
    show mrsj 52
    mrsjo "Você sabia {b}Erik{/b} gostava dela ... "
    mrsjo "... Eu pensei que ele era seu amigo! "
    show player 10
    show mrsj 51
    player_name "Eu sinto Muito, {b}Mrs. Johnson{/b}."
    player_name "Eu vou para casa agora. "
    hide mrsj
    hide player
    return

label button_mrsj_erik_introduce_june:
    show player 14
    player_name "Tem essa garota na escola que eu acho {b}Erik{/b} gosta."
    show player 1
    show mrsj 17
    mrsjo "Realmente?"
    show mrsj 18
    mrsjo "Isso é maravilhoso!"
    show mrsj 17
    mrsjo "Você conhece ela? Como ela é?!"
    show mrsj 14
    show player 14
    player_name "Não, eu ainda não falei com ela. "
    player_name "Ela é de uma classe diferente, eu acho."
    show mrsj 17
    show player 1
    mrsjo "Ah eu vejo."
    show player 11
    mrsjo "E {b}Erik{/b} falando com ela? "
    show mrsj 14
    show player 10
    player_name "Eu acho que não ... Ele diz que é muito tímido. "
    player_name "Eu disse a ele que iria descobrir mais sobre ela e que ele soubesse como ela é."
    show mrsj 18
    show player 13
    mrsjo "Isso é tão agradável de você!!"
    show mrsj 17
    mrsjo "Ele tem muita sorte de ter você como amigo ... "
    show mrsj 14
    show player 14
    player_name "Ah, tenho certeza que ele faria o mesmo por mim! "
    show mrsj 49
    show player 1
    mrsjo "Vou lhe dizer como é que tudo isso acontece ... "
    show player 11
    mrsjo "Se você pode encontrar {b}Erik{/b} uma namorada, há uma recompensa especial esperando por você ... "
    show mrsj 50
    player_name "..."
    show player 21
    player_name "Certo, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 14
    return

label button_mrsj_breastfeeding:
    show mrsj 38 at right
    show player 12 at left
    player_name "Então, há quanto tempo você ... está amamentando {b}Erik{/b}?"
    show player 5
    show mrsj 52
    mrsjo "Ah ... "
    mrsjo "Escute, não é o que você pode pensar."
    mrsjo "Eu sempre o nutrei assim."
    show mrsj 38
    show player 11
    mrsjo "..."
    show mrsj 52
    mrsjo Você sabe que ele não recebe muita atenção das meninas da escola."
    mrsjo "Eu me senti tão mal por ele!"
    mrsjo "eu só queria {b}Erik{/b} experimentar e ver do que se trata as mulheres! "
    show mrsj 20
    mrsjo "Mas talvez eu ... eu acabei de fazer isso? "
    show mrsj 19c
    show player 5
    player_name "..."
    show player 12
    player_name "É ótimo que você se importe tanto e dê atenção a ele! "
    show mrsj 14
    show player 10
    player_name "Eu acho que ele tem muita sorte ... "
    show player 11
    show mrsj 18
    mrsjo "Oh, ha ha!"
    show mrsj 17
    mrsjo "Bem, obrigada ... "
    mrsjo "Eu acho que jovens legais como vocês precisam de toda a atenção que puder ..."
    show mrsj 14
    show player 13
    player_name "..."
    show mrsj 49
    mrsjo "Quero dizer, obrigado pela compreensão, {b}[firstname]{/b}."
    show mrsj 52
    mrsjo "Apenas ... lembre-se de manter isso entre nós, ok? "
    show mrsj 14
    show player 14
    player_name "Sim, {b}Mrs. Johnson{/b}."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_yoga_help_repeat:
    show player 10
    player_name "Em que você precisava de minha ajuda? "
    show player 5
    show mrsj 19
    mrsjo "Ipreciso de alguém para ir e {b}teach my yoga class for me tonightensinar minha aula de ioga para mim hoje à noite{/b}."
    show mrsj 49
    mrsjo "Você acha que poderia ajudar seu ... vizinho favorito? "
    show mrsj 50
    show player 14
    player_name "Claro!"
    show player 13
    show mrsj 17
    mrsjo "Lembrar de {b}estudar os movimentos de ioga dessa lista{/b} Eu dei!"
    return

label button_mrsj_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Tenho que dizer, {b}Mrs. Johnson{/b}, você está realmente em forma! "
    player_name "Você se exercita muito? "
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Ah ... você é tão legal! "
    show mrsj 17 at right
    mrsjo "Bem, eu tento usar o ginásio sempre que posso ... "
    mrsjo "... eu também vou correr! E eu faço yoga no meu quarto à noite também ..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Bem, está funcionando! "
    show player 13 at left
    mrsjo "Você pensa?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "Minha {b}bunda{/b} ainda é um pouco grande ... "
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...E meu {b}peitos{/b} não são como os que costumavam ... "
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*gole*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Você gostaria de falar sobre mais alguma coisa? "
    return

label button_mrsj_invite_poker:
    player_name "Fiquei me perguntando se você gostaria de participar {b}Erik{/b} e eu no poker? "
    show player 1
    show mrsj 17
    mrsjo "Agora mesmo?"
    show player 14
    show mrsj 14
    player_name "Sim ... quero dizer, você não precisa! "
    player_name "{b}Erik{/b} e eu estou apenas procurando por um terceiro jogador ... "
    show player 1
    show mrsj 17
    mrsjo "Ele está esperando lá embaixo? "
    show player 14
    show mrsj 14
    player_name "Sim, gostaríamos de jogar agora, se você estiver livre? "
    show player 1
    mrsjo "Hmm..."
    show mrsj 17
    mrsjo "Eu acho que eu poderia jogar um jogo ou dois. "
    show mrsj 18
    show player 13
    mrsjo "Tudo bem, eu vou encontrar vocês dois lá embaixo daqui a pouco! "
    show player 18
    show mrsj 14
    player_name "Impressionante! obrigado, {b}Mrs. Johnson{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
