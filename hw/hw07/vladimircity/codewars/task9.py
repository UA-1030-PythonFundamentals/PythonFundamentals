# Are You Playing Banjo?
def are_you_playing_banjo(name):
    match name.lower().startswith('r'):
        case True:
            return name + " plays banjo"
        case False:
            return name + " does not play banjo"



print(are_you_playing_banjo('Robert'))
print(are_you_playing_banjo('Jane'))