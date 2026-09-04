class Musical_Loop:
    @staticmethod
    def resolve():
        while True:
            number_of_samples_in_the_musical_loop = int(input())
            if number_of_samples_in_the_musical_loop == 0: break
        
            musical_loop = [int(x) for x in input().split()]
            
            number_of_peaks = 0

            for idx in range(number_of_samples_in_the_musical_loop):
                prev = musical_loop[(idx - 1) % len(musical_loop)]
                next = musical_loop[(idx + 1) % len(musical_loop)]
                curr = musical_loop[idx]
                
                if prev < curr > next or prev > curr < next: number_of_peaks += 1 
                
            print(number_of_peaks)
                
Musical_Loop.resolve()