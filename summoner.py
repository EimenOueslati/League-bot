#A class that represents a summoners stats related to a game type (flex/soloQ)
class Ranked:
    def __init__(
        self,
        queueType,
        tier,
        rank,
        leaguePoints,
        wins,
        losses,
    ):
        self.queueType = queueType
        self.tier = tier
        self.rank = rank
        self.leaguePoints = leaguePoints
        self.wins = wins
        self.losses = losses


#A class that represents a summoner
class Summoner:
    def __init__(self, summonerName: str, flex: Ranked, soloQ: Ranked):
        self.summonerName = summonerName
        self.flex = flex
        self.soloQ = soloQ

    def getSoloQ(self):
        if self.soloQ is not None:
            stats = [
                self.soloQ.tier, self.soloQ.rank, self.soloQ.leaguePoints,
                self.soloQ.wins, self.soloQ.losses
            ]
            return stats
        else:
            return None

    def getFlex(self):
        if self.flex is not None:
            stats = [
                self.flex.tier, self.flex.rank, self.flex.leaguePoints,
                self.flex.wins, self.flex.losses
            ]
            return stats
        else:
            return None


def Parce_ranked(obj):
    return Ranked(obj['queueType'], obj['tier'], obj['rank'],
                  obj['leaguePoints'], obj['wins'], obj['losses'])
