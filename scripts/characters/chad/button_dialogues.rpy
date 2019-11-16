label button_chad_get_eve_drawing_first:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "Ei cara, eu estou tentando encontrar {b}Eve's Art Pad{/b}."
    player_name "Ela disse que você pode ter."
    show player 1
    show chad 2
    chad "Sim, está certo."
    show player 10
    show chad 1
    player_name "Então, eu poderia obtê-lo de você?"
    show player 11
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Tch, Não é de graça."
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "..."
    show player 10
    player_name "O que você quer?"
    show player 11
    show chad 6
    chad "Cara, {b}Eve's{/b} um artista bonito, você sabe o que estou dizendo'?"
    show player 10
    show chad 5
    player_name "Sim, então eu ouvi."
    show player 11
    show chad 6
    chad "Ela tem esse desenho'..."
    chad "Merda é acesa pra caralho, cara!"
    chad "Eu pensei que seria nela {b}art pad{/b} mas sem dados."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Você tem que {b}me pegue esse desenho'{/b}, Dawg!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "... E se eu fizer, você me dará o {b}Art Pad{/b}?"
    show player 11
    show chad 6
    chad "Haaah, esse é o negócio."
    show chad 2
    chad "Você para baixo?"
    show player 10
    show chad 1
    player_name "Certo. Como é o desenho?"
    show player 11
    show chad 6
    chad "Ah, é esse auto-retrato que ela fez."
    chad "Deve ser como uma garota de anime ou algo assim"
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Tudo o que sei é ... É sexy, porra!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Alguma idéia de onde poderia estar?"
    show player 11
    show chad 3
    chad "Mmm, cara, se eu tivesse que adivinhar..."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Aposto que ela está mantendo essa merda {b}no armário dela{/b}."
    show player 2
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Tudo bem, eu vou dar uma olhada."
    show player 1
    show chad 2
    chad "Volte depressa, cara."
    return

label button_chad_get_eve_drawing:
    scene location_school_right_hall_day_blur
    show player 10 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "O que você queria para isso {b}Art Pad{/b} novamente?"
    show player 11
    show chad 2
    chad "Você esquece ou algo assim'?"
    show player 10
    show chad 1
    player_name "Sim, meio."
    show player 11
    show chad 2
    chad "Tch, eu quero aquele auto-retrato {b}Eve{/b} fez."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Ela provavelmente tem isso em segredo {b}no armário dela{/b},sabe o que estou dizendo?"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Tudo bem."
    return

label button_chad_get_eve_drawing_completed:
    scene location_school_right_hall_day_blur
    show player 1 at left
    show chad 6 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    chad "Ey, cara. Você entendeu?"
    show chad 1
    show player 612 with dissolve
    player_name "Sim, você estava certo. É bem sexy..."
    show chad 6
    show player 611
    chad "Deixe-me ver essa merda!"

    $ player.remove_item("eve_drawing")
    show player 1 with dissolve
    show chad 7 at Position(xpos=0.765, ypos=1.0) with dissolve
    pause
    show chad 8
    chad "Narcótico!"
    chad "Droga! Agora isso é uma mulher!"
    show player 2
    show chad 7
    player_name "Eu posso ter aquilo {b}Art Pad{/b} agora?"
    show player 1
    show chad 9
    chad "Ah sim. Minha culpa! Estou por aqui babando e merda!"
    show chad 10 at Position(xpos=0.725, ypos=1.0) with dissolve
    chad "Aqui vai."
    show player 598
    show chad 7 at Position(xpos=0.765, ypos=1.0)
    with dissolve
    show expression "boxes/popup_item_artpad1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_artpad1.png"
    player_name "Thanks, Chad."
    show player 596
    show chad 8
    chad "Prazer em fazer negócios com você."
    return

label button_chad_generic:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at right
    with dissolve
    player_name "Ei, o que se passa, cara?"
    show player 1
    show chad 3
    chad "Droga, {b}[firstname]{/b}! Você não vê que estou praticando minhas rimas aqui!"
    show player 10
    show chad 1
    player_name "Uhh, ok?"
    show player 11
    show chad 2
    chad "O que você quer de qualquer maneira?"
    return

label button_chad_nothing:
    show player 2
    show chad 1
    player_name "Só pensei em dizer olá."
    show player 1
    show chad 3
    chad "Beat it, yo."
    show player 11
    chad "Estou lutando com algumas coisas sérias agora."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
