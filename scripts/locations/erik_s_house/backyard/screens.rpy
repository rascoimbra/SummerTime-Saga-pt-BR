screen eriks_backyard():
    use mods_screens_hook("eriks_backyard")

    add game.timer.image("backgrounds/location_erik_house_backyard_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,395)
        idle game.timer.image("objects/object_door_69{}.png")
        hover HoverImage(game.timer.image("objects/object_door_69{}.png"))
        action If(
            erik.in_progress(erik_thief),
            [Hide("eriks_backyard"), Jump("erik_thief_block2")],
            [Hide("eriks_backyard"), Jump("eriks_house_dialogue")]
        )

    if erik.in_progress(erik_thief):
        imagebutton:
            focus_mask True
            pos (778,393)
            idle "objects/object_door_70_thief_night.png"
            hover HoverImage("objects/object_door_70_thief_night.png")
            action Hide("eriks_backyard"), Jump("erik_thief")

    else:
        imagebutton:
            focus_mask True
            pos (778,393)
            idle game.timer.image("objects/object_door_70{}.png")
            hover HoverImage(game.timer.image("objects/object_door_70{}.png"))
            action If(
                not erik.over(erik_intro),
                [Hide("eriks_backyard"), Jump("door18_locked_dialogue")],
                [Hide("eriks_backyard"),
                 If(
                    mrsj.known(mrsj_intro),
                    If(
                        not game.timer.is_dark(),
                        [Play("audio", sfxDoor()),
                         If(
                            erik.in_progress(erik_gf_stolen),
                            Jump("erik_gf_stolen"),
                            Jump("erik_indoors")
                         )
                        ],
                        [Function(playSound), Play("audio", sfxDoor()),
                         If(
                            erik.in_progress(erik_gf_stolen),
                            Jump("erik_gf_stolen"),
                            Jump("erik_indoors")
                         )
                        ],
                    ),
                    Jump("closed_erik")
                 )
                ]
            )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
