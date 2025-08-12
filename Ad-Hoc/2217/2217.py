class Nove:
    @staticmethod
    def last_digit_in_Nth_power_of_9(n):
        print(9 if n % 2 else 1)

n = int(input())
for _ in range(n):
    x = int(input())
    Nove.last_digit_in_Nth_power_of_9(x)