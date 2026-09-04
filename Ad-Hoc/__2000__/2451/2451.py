class Pacman:
    @staticmethod
    def max_food_collected(n):
        food_collecteds, max_food, left_right = 0, 0, True
        
        for _ in range(n):
            line = input()
            if left_right:
                for i in range(n):
                    cell = line[i]
                    if cell == ".": continue
                    if cell == "o": food_collecteds += 1
                    if cell == "A":
                        max_food = max(food_collecteds, max_food)
                        food_collecteds = 0
                
                left_right = False
                continue
                
        
            for i in range(n - 1, -1, -1):
                cell = line[i]
                if cell == ".": continue
                if cell == "o": food_collecteds += 1
                if cell == "A":
                    max_food = max(food_collecteds, max_food)
                    food_collecteds = 0
            
            left_right = True
         
        max_food = max(max_food, food_collecteds)  
        print(max_food)

n = int(input())
Pacman.max_food_collected(n)