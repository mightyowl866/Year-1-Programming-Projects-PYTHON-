class ninten:
    def __init__(self,game):
        self.game = game
mario = ninten('Super Mario Bros')
zelda = ninten('Ocarina Of Time')
metroid = ninten('Metroid Prime')

print(mario.game)
print(zelda.game)
print(metroid.game)