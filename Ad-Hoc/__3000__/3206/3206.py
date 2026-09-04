class Robot:
    def __init__(self, x, y, sense):
        self.x = x
        self.y = y
        self.sense = sense

    def move(self):
        deltas = {
            'W': (-1, 0),
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1)
        }

        self.x += deltas[self.sense][0]
        self.y += deltas[self.sense][1]

    def rotate(self, shift):
        senses = "NESW"
        idx = senses.index(self.sense)
        self.sense = senses[(idx + shift + 4) % 4]

    def execute(self, command):
        if command == 'F':
            self.move()
        elif command == 'L':
            self.rotate(-1)
        elif command == 'R':
            self.rotate(1)


T = int(input())

for _ in range(T):
    width, height = map(int, input().split())
    nrobots, ncmds = map(int, input().split())

    robots = []
    grid = [[0] * 105 for _ in range(105)]

    for robot_id in range(nrobots):
        x, y, sense = input().split()
        x = int(x)
        y = int(y)

        robots.append(Robot(x, y, sense))
        grid[x][y] = robot_id + 1  # IDs são 1-based

    collided = False
    ans = "OK"

    for _ in range(ncmds):
        ID, cmd, rep = input().split()
        ID = int(ID)
        rep = int(rep)

        if collided:
            continue

        robot = robots[ID - 1]

        # rotações não precisam consultar grid
        if cmd == 'L':
            robot.rotate(-(rep % 4))
            continue

        if cmd == 'R':
            robot.rotate(rep % 4)
            continue

        # cmd == 'F'
        for _ in range(rep):
            cx, cy = robot.x, robot.y

            robot.move()

            x, y = robot.x, robot.y

            # colisão com parede
            if x <= 0 or x > width or y <= 0 or y > height:
                collided = True
                ans = f"Robot {ID} crashes into the wall"
                break

            # colisão com outro robô
            if grid[x][y] != 0 and grid[x][y] != ID:
                collided = True
                ans = f"Robot {ID} crashes into robot {grid[x][y]}"
                break

            # atualiza grid
            grid[cx][cy] = 0
            grid[x][y] = ID

    print(ans)