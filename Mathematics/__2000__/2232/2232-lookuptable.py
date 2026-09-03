#versao usando look_up table
class Pascals_triangle:
    #como N, tal (1 <= N <= 31) há 31 resultados possiveis.
    pre_process_table = [
        1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047,
        4095, 8191, 16383, 32767, 65535, 131071, 262143,
        524287, 1048575, 2097151, 4194303, 8388607, 16777215,
        33554431, 67108863, 134217727, 268435455, 536870911,
        1073741823, 2147483647
    ]
    
    @staticmethod
    def sum_of_the_first_N_lines(n: int) -> None:
        out = Pascals_triangle.pre_process_table[n - 1]
        print(out)
        
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    Pascals_triangle.sum_of_the_first_N_lines(n)