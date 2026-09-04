from collections import defaultdict
class Grades:
    @staticmethod
    def most_frequent_note(notes):
        freq = defaultdict(int)
        for note in notes:
            freq[note] += 1
            
        #compara primeiro pela frequência, depois pelo valor
        most_freq= max(freq, key=lambda x: (freq[x], x))
                
        print(most_freq)

n = int(input())
notes = [int(x) for x in input().split()]

Grades.most_frequent_note(notes)