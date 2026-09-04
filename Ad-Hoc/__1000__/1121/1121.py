class Sticker_Collector_Robot:
    move_system = {
        "N": {"D": "L", "E": "O", "F": (-1, 0)}, # sobe 1 linha
        "S": {"D": "O", "E": "L", "F": (1, 0)},  # desce 1 linha
        "L": {"D": "S", "E": "N", "F": (0, 1)},  # vai pra direita
        "O": {"D": "N", "E": "S", "F": (0, -1)}  # vai pra esquerda
    }
    
    @staticmethod
    def go(grid, curr_pos, direction):
        x, y = Sticker_Collector_Robot.move_system[direction]["F"]
        dx, dy = curr_pos[0] + x, curr_pos[1] + y 
        
        if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
            if grid[dx][dy] != '#': return (dx, dy)
            
        return curr_pos #caso não se mova

        
    @staticmethod
    def execute_commands(grid, robot, commands):
        stickerd_collecteds = 0
        x, y, direction = robot
        
        for command in commands:
            
            if command == 'F':
                nx, ny = Sticker_Collector_Robot.go(grid, [x, y], direction)
                if grid[nx][ny] == '*':
                    stickerd_collecteds += 1
                    grid[nx][ny] = '.'  # REMOVE o sticker depois de coletar
                x, y = nx, ny
                
            else:
                direction = Sticker_Collector_Robot.move_system[direction][command]
                
        print(stickerd_collecteds)
            

    @staticmethod
    def resolve():
        while True:
            N, M, num_commands = [int(x) for x in input().split()]
            if N == M == num_commands == 0: break
        
            grid, robot = [], None
            for i in range(N):
                line = [str(c) for c in input()]
                for j in range(M):
                    if line[j] in ['N', 'S', 'L', 'O']:
                        robot = (i, j, line[j])
                grid.append(line)
                
            commands = input()
            Sticker_Collector_Robot.execute_commands(grid, robot, commands)
            
Sticker_Collector_Robot.resolve()