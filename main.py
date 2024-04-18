music.set_built_in_speaker_enabled(True)
music.play(music.string_playable("G B A C5 F B G F ", 120),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
