robots = int(input())

for i in range(robots):
    n_instructions = int(input())
    instructions = []
    position = 0

    for _ in range(n_instructions):
        instruction = input()

        if instruction == "LEFT":
            position -= 1
            instructions.append(-1)

        elif instruction == "RIGHT":
            position += 1
            instructions.append(1)

        else:
            same = int(instructions.split()[-1])
            position += instructions[same - 1]
            instructions.append(instructions[same - 1])

    print(position)