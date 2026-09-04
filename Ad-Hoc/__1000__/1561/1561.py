class Binary_Watch:
    @staticmethod
    def to_bin_str(value):
        return f"{value:06b}"  # 6 bits
    
    @staticmethod
    def display(HH, MM):
        bin_hour = Binary_Watch.to_bin_str(int(HH))
        bin_min  = Binary_Watch.to_bin_str(int(MM))

        # Bits horas (8,4,2,1 → índices 2..5)
        A = "o" if bin_hour[2] == "1" else " "
        B = "o" if bin_hour[3] == "1" else " "
        C = "o" if bin_hour[4] == "1" else " "
        D = "o" if bin_hour[5] == "1" else " "

        # Bits minutos (32..1 → índices 0..5)
        E = "o" if bin_min[0] == "1" else " "
        F = "o" if bin_min[1] == "1" else " "
        G = "o" if bin_min[2] == "1" else " "
        Hm = "o" if bin_min[3] == "1" else " "
        I = "o" if bin_min[4] == "1" else " "
        J = "o" if bin_min[5] == "1" else " "

        print(" ____________________________________________")
        print("|                                            |")
        print("|    ____________________________________    |_")
        print("|   |                                    |   |_)")
        print("|   |   8         4         2         1  |   |")
        print("|   |                                    |   |")
        print(f"|   |   {A:<1}{' ' * 9}{B:<1}{' ' * 9}{C:<1}{' ' * 9}{D:<1}  |   |")
        print("|   |                                    |   |")
        print("|   |                                    |   |")
        print(f"|   |   {E:<1}{' ' * 5}{F:<1}{' ' * 5}{G:<1}{' ' * 5}{Hm:<1}{' ' * 5}{I:<1}{' ' * 5}{J:<1}  |   |")
        print("|   |                                    |   |")
        print("|   |   32    16    8     4     2     1  |   |_")
        print("|   |____________________________________|   |_)")
        print("|                                            |")
        print("|____________________________________________|")
        print()

while True:
    try:
        HH, MM = input().split(":")
        Binary_Watch.display(HH, MM)
    except EOFError:
        break