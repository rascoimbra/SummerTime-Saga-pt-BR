label school_lock_check(destination_screen, destination_label):
    $ temp_bg = player.location.background_blur

    if M_smith.is_state(S_smith_go_to_athletics) and destination_screen not in ["School Left Hallway", "Boy's Lockerroom"]:
        scene expression temp_bg
        show player 1
        with dissolve
        player_name "( Eu deveria entrar no {b}Vestiário dos Meninos{/b} me trocar para {b}Classe de Atletismo{/b}. )"
        player_name "( Está no {b}salão esquerdo{/b}."

    elif M_smith.is_state(S_smith_intro) and destination_screen.lower() not in ("school hall", "school second floor", "school third floor", "principal smith's office"):
        scene expression temp_bg
        show player 1 with dissolve
        player_name "A diretora Smith queria me ver {b}em seu escritório, no terceiro andar.{/b}"
        player_name "É melhor eu ir rápido para evitar uma detenção."

    elif M_smith.is_state(S_smith_go_to_locker) and destination_screen.lower() not in ("school hall", "school second floor", "school third floor", "principal smith's office", "school locker"):
        scene expression temp_bg
        show player 2 with dissolve
        player_name "Eu devo esperar por {b}Annie{/b} no meu armário..."

    elif M_bridget.get_state() == S_bridget_intro and destination_screen not in ["School Hall", "School Courtyard"]:
        scene expression temp_bg
        show jersey 10 with dissolve
        player_name "( Eu deveria ir ao {b}Campo{/b} para o meu {b}Atletismo{/b} classe. )"

    elif M_bissette.get_state() == S_bissette_intro and destination_screen not in ["French Classroom"]:
        scene expression temp_bg
        show player 35 with dissolve
        player_name "( Eu deveria ir para a aula da {b}Miss Bissette agora.{/b} )"

    elif M_dewitt.is_state(S_dewitt_paint_trail) and destination_screen not in ["School Right Hallway", "School Hall", "School Second Floor", "School Third Floor", "Principal Smith's Office"]:
        scene expression temp_bg
        show player 12 with dissolve
        player_name "A trilha não leva assim."

    elif L_school_girlsroom.locked and destination_screen == "School Girl's Lockerroom":
        scene expression temp_bg
        show player 14 with dissolve
        player_name "(O vestiário da menina está em construção no momento...)"

    elif M_roxxy.is_state(S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once) and destination_screen not in ["French Classroom", "School Hall", "School Locker"]:
        scene expression temp_bg
        if player.has_item("roxxy_homework"):
            show player 10 with dissolve
            player_name "Eu deveria pegar isso {b}Lição de casa para Roxxy{/b}."
            hide player with dissolve
        else:
            show player 10 with dissolve
            player_name "Eu deveria pegar meu {b}Lição de casa francesa fora do meu armário para Roxxy{/b}."
            hide player with dissolve
    else:

        if player.location == L_school_floor2 and destination_screen in ["Computer Lab", "Teacher's Lounge"]:
            $ playSound()
            play audio sfxDoor()
        if player.location == L_school_floor2 and destination_screen == "Cafeteria":
            $ playSound()
        if player.location == L_school_floor3 and destination_screen != "School Second Floor":
            $ playSound()
            play audio sfxDoor()
        if destination_screen == "Bridget's Office":
            $ playSound()
            play audio sfxDoor()
        jump expression destination_label

    hide dewitt
    hide jersey
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
