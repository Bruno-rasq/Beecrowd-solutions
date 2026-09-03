
def create_tree(n):
    line = (' ' * (n // 2)) + "*"
    line2 = (' ' * (n // 2)) + "*"
    print(line)
    count_stars = 1
    
    while count_stars < n:
        line = line[1:] + "*" * 2
        count_stars = line.count("*")
        print(line)
        
    print(line2)
    line2 = line2[1:] + "*" * 2 
    print(line2)

while True:
    try:
        n = int(input())
        create_tree(n)
        print("")
    except EOFError:
        break