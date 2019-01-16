import sc2, sys
from __init__ import run_ladder_game
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer
import random

# Load bot
from additionalpylons import AdditionalPylons
bot = Bot(Race.Protoss, AdditionalPylons())
#bot = Bot(Race.Random, ExampleBot())


allmaps = ['AutomatonLE', 'BlueshiftLE', 'CeruleanFallLE', 'DarknessSanctuaryLE', 'KairosJunctionLE', 'PortAleksanderLE', 'ParaSiteLE'] # all maps

#allmaps = ['CeruleanFallLE'] # all maps



_realtime = False
_difficulty = Difficulty.CheatVision #CheatInsane, CheatMoney, CheatVision
_opponent = random.choice([Race.Zerg, Race.Terran, Race.Protoss, Race.Random])
#_opponent = Race.Protoss




# Start game
if __name__ == '__main__':
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        run_ladder_game(bot)
    else:
        # Local game
        print("Starting local game...")
        # sc2.run_game(sc2.maps.get("Abyssal Reef LE"), [
        #     bot,
        #     Computer(Race.Protoss, Difficulty.VeryHard)
        # ], realtime=True)
        
        sc2.run_game(sc2.maps.get(random.choice(allmaps)), [
            Bot(Race.Protoss, AdditionalPylons()),
            Computer(_opponent, _difficulty)
        ], realtime=_realtime)