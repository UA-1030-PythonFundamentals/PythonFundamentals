def are_you_playing_banjo(name):
    if name and name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"