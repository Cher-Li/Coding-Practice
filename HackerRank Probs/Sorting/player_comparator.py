from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"Player(name={self.name!r}, score={self.score!r})"
        
    def comparator(a, b):
        # if same score, sort by name, -1 if a < b, 0 if a == b, 1 otherwise
        
        if a.score != b.score:
            # high score first
            return -1 if a.score > b.score else 1
         
        # equal scores, sort ascending by name
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
            
        return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)