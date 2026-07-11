from collections import deque

TARGET = 1023
MASKS = [0, 18, 53, 106, 68, 163, 470, 300, 816, 736, 384]

class Stage:
    def __init__(self, state, buttons):
        self.state = state
        self.buttons = buttons
        
def BFS(start):
    queue = deque()
    visiteds = [False for _ in range(1024)]
    queue.append(start)
    visiteds[start.state] = True
    while queue:
        curr = queue.popleft()
        if curr.state == TARGET: return curr
        for i in range(1, 10 + 1):
            nextState = curr.state ^ MASKS[i]
            if not visiteds[nextState]:
                nextButtons = curr.buttons + [i]
                visiteds[nextState] = True
                queue.append(Stage(nextState, nextButtons))
    return start

def main():
    leds = [int(x) for x in input().split()]
    state = 0
    for i in range(10):
        if leds[i] == 1:
            state |= (1 << i)

    if state == TARGET:
        print("0")
        return 

    start = Stage(state, [])
    ans = BFS(start)

    if len(ans.buttons) == 0:
        print("-1")
        return

    print(len(ans.buttons))
    print(" ".join(map(str, ans.buttons)))

main()