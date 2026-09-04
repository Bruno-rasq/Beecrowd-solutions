class Throwing_balls:
    @staticmethod
    def is_possible_throw_the_ball_into_the_hole(distance, max_speed):
        for start_speed in range(1, max_speed + 1):
            pos = 0
            v = start_speed
            while v > 0:
                for _ in range(v):  # v saltos nessa velocidade
                    pos += v
                    if pos == distance:
                        return "possivel"
                v -= 1
        return "impossivel"


while True:
    distance, speed = map(int, input().split())
    if distance == speed == 0: break
    print(Throwing_balls.is_possible_throw_the_ball_into_the_hole(
        distance, speed
    ))