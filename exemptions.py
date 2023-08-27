MyMusic = [
    {"name": "Hope", "album": "Hope", "artist": "NF"},
    {"name": "Shake It Up", "album": "1989", "artist": "Taylor Swift"},
    {"name": "The Search", "album": "The Search", "artist": "NF"},
    {"name": "Kante", "album": "Timeless", "artist": "Davido"},
    {"name": "FEM", "album": "A Better Time", "artist": "Davido"},
    {"name": "Over Dem", "album": "Timeless", "artist": "Davido"},
    {"name": "Sunlight", "album": "A Better Time", "artist": "Davido"},
    {"name": "Running", "album": "Hope", "artist": "NF"},
    {"name": "Leave Me Alone", "album": "The Search", "artist": "NF"},
    {"name": "Bad Blood", "album": "1989", "artist": "Taylor Swift"},
    {"name": "Red", "album": "Red", "artist": "Taylor Swift"},
    {"name": "State Of Grace", "album": "Red", "artist": "Taylor Swift"},
    {"name": "Mistake", "album": "Hope", "artist": "NF"},
    {"name": "Godfather", "album": "Timeless", "artist": "Davido"},
    {"name": "Clean", "album": "1989", "artist": "Taylor Swift"}
]

def f(query):
    return query["album"]

MyMusic.sort(key=f)
print(MyMusic)