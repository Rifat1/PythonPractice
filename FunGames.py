arcades = ["Dark Den", "Krazy Bend", "City Arcade", "On the Top Arcade"]
games = ["Star Wars", "Angry Birds Go", "Jurassic Park"]
gamesPlayed = [[100, 250, 200],
               [500, 600, 700],
               [200, 225, 230],
               [120, 520, 500]]
print("Arcade", 15*" ", "Total Games Played")
print(arcades[0], (15+len("Arcade")-len(arcades[0]))*" ",gamesPlayed[0][0]+gamesPlayed[0][1]+gamesPlayed[0][2])
print(arcades[1], (15+len("Arcade")-len(arcades[1]))*" ",
      gamesPlayed[1][0]+gamesPlayed[1][1]+gamesPlayed[1][2])

print(arcades[2], (15+len("Arcade")-len(arcades[2]))*" ",
      gamesPlayed[2][0]+gamesPlayed[2][1]+gamesPlayed[2][2])
print(arcades[3], (15+len("Arcade")-len(arcades[3]))*" ",
      gamesPlayed[3][0]+gamesPlayed[3][1]+gamesPlayed[3][2],"\n")

print("Game", (15-len("game")+len("Arcade"))*" ", "Total Games Played")
print(games[0], (15-len(games[0])+len("Arcade"))*" ", gamesPlayed[0][0]+gamesPlayed[1][0]+gamesPlayed[2][0]+gamesPlayed[3][0])
print(games[1], (15-len(games[1])+len("Arcade"))*" ", gamesPlayed[0]
      [1]+gamesPlayed[1][1]+ gamesPlayed[2][1]+gamesPlayed[3][1])
print(games[2], (15-len(games[2])+len("Arcade"))*" ", gamesPlayed[0]
      [2]+gamesPlayed[1][2]+ gamesPlayed[2][2]+gamesPlayed[3][2])

