from collections import defaultdict

def top_ids(size_class):
    classify_average = defaultdict(list)
    
    for _ in range(size_class):
        id, average = [int(x) for x in input().split()]
        classify_average[average].append(id)
        
    _max = max(classify_average)
    for id in classify_average[_max]:
        print(id, end=' ')
    print()
    
class_nmb = 1
while True:
    size_class = int(input())
    if size_class == 0: break 

    print(f"Turma {class_nmb}")
    top_ids(size_class)
    print()
    class_nmb += 1