albums = [
  ("Welcome to my Nightmare", "Alice Cooper", 1975,
    [
      (1, "Welcome to my Nightmare"),
      (2, "Devil's Food"),
      (3, "The Black Widow"),
      (4, "Some Folks"),
      (5, "Only Women Bleed"),
    ]
    ),
  ("Bad Company", "Bad Company", 1974,
    [
      (1, "Can't Get Enough"),
      (2, "Rock Steady"),
      (3, "Ready for Love"),
      (4, "Don't Let Me Down"),
      (5, "Bad Company"),
      (6, "The Way I Choose"),
      (7, "Movin' On"),
      (8, "Seagull"),
    ]
    ),
  ("Nightflight", "Budgie", 1981,
    [
      (1, "I Turned to Stone"),
      (2, "Keeping a Rendezvous"),
      (3, "Reaper of the Glory"),
      (4, "She Used Me Up"),
    ]
  )
]

# constantS
SONGS_LIST_INDEX = 3 
SONG_TITLE_INDEX = 1

while True:
  print("Choose your album (invalid choice exits):")
  for index, (title, artist, year, songs) in enumerate(albums): # unpacking tuples
    print("{}: {}".format(index + 1, title))

  choice = int(input())
  if 1 <= choice <= len(albums):
    songs_list = albums[choice -1][SONGS_LIST_INDEX]
  else:
    break
  
  print("Choose your song:")
  for index, (track_number, song) in enumerate(songs_list):
    print("{}: {}".format(index + 1, song))
  
  song_choice = int(input())
  if 1 <= song_choice <= len(songs_list):
    title = songs_list[song_choice -1][SONG_TITLE_INDEX]
    print("Playing {}".format(title))
  
  print("-" * 40)
  

