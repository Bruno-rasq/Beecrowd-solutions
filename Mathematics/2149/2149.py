class The_Uncle_Phill_Bonati_s_Sequence:
    preprocess_table = [0, 1, 1, 1, 2, 2, 4, 8, 12, 96,
        108, 10368, 10476, 108615168, 108625644, 
        11798392572168192, 11798392680793836
    ]
    
    @staticmethod
    def resolve():
        while True:
            try:
                n = int(input())
                out = The_Uncle_Phill_Bonati_s_Sequence.preprocess_table[n - 1]
                print(out)
            except EOFError: break
        
The_Uncle_Phill_Bonati_s_Sequence.resolve()