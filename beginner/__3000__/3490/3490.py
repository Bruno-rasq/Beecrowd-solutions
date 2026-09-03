while True:
    try:
        digits = input().split()
        print("".join(digits))
        
    except EOFError: break