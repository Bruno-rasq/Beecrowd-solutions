stickers = set()
repeated_stickers = 0

n_stickers = int(input())
for _ in range(n_stickers):
    sticke = int(input())
    length = len(stickers)
    stickers.add(sticke)
    current_len = len(stickers)
    if current_len == length:
        repeated_stickers += 1
        
print(len(stickers))
print(repeated_stickers)