#A class that represents a summoner
class Summoner:
    def __init__(self, summonerName, flex, soloQ):
        self.summonerName = summonerName
        self.flex = flex
        self.soloQ = soloQ



#A class that represents a summoners stats related to a game type (flex/soloQ)
class Ranked:
     def __init__(self, tiere, rank, leaguePoints, wins, losses,):
         self.tiere = tiere
         self.rank = rank
         self.leaguePoints = leaguePoints
         self.wins = wins
         self.losses = losses

