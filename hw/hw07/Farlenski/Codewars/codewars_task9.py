def are_you_playing_banjo(name):
    name = name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"
    return name


print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("bravo"))
print(are_you_playing_banjo("rolf"))
