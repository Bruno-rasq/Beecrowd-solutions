
while True:
    try:
        words = input().split()
        count = 0
        prev_letter = ''
        group_size = 1
    
        for i in range(1, len(words)):
            current_letter = words[i][0].lower()
            prev_letter = words[i-1][0].lower()
    
            if current_letter == prev_letter:
                group_size += 1
            else:
                if group_size >= 2:
                    count += 1
                group_size = 1  # reinicia o grupo
    
        # caso o último grupo tenha sido uma aliteração
        if group_size >= 2:
            count += 1
    
        print(count)
    except EOFError:
        break