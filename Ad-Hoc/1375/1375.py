class Pole_Position:
    @staticmethod
    def set_initial_grid(number_cars):
        pole = {x: 0 for x in range(1, number_cars + 1)}
        grid_error = False
        
        for i in range(1, number_cars + 1):
            car, delta = [int(x) for x in input().split()]
            position = i + delta 
            if position not in pole or pole[position] != 0:
                grid_error = True
                
            pole[position] = car
                
                
        if grid_error: return -1
        
        pole_position = [str(car) for car in pole.values()]
        return " ".join(pole_position)
        
    
while True:
    number_cars = int(input())
    if number_cars == 0: break
    
    out = Pole_Position.set_initial_grid(number_cars)
    print(out)