class Shuffle:
    @staticmethod
    def solve(amount_musics, playlist_size):
        musics = [int(x) for x in input().split()]
        playlistorder = [int(x) for x in input().split()]
        
        duration = 0 
        takes = {i: False for i in range(1, amount_musics + 1)}
        
        for idx in range(playlist_size):
            music = playlistorder[idx]
            takes[music] = True 
            duration += musics[music - 1]
            
            if all(takes.values()): return duration
            
        return -1
        
while True:
    try:
        amount_musics, playlist_size = [int(x) for x in input().split()]
        out = Shuffle.solve(amount_musics, playlist_size)
        print(out)
    except EOFError: break