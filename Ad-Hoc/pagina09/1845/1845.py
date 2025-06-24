import sys

class Efiloque:
    @staticmethod
    def resolve():
        write = sys.stdout.write
        for line in sys.stdin:
            y = ''
            for x in line.rstrip('\n'):
                x = x if x != 'b' and x != 'j' and x != 'p' and x != 's' and x != 'v' and x != 'x' and x != 'z' else 'f'
                x = x if x != 'B' and x != 'J' and x != 'P' and x != 'S' and x != 'V' and x != 'X' and x != 'Z' else 'F'
                if (x != 'f' and x != 'F') or (y != 'f' and y != 'F'):
                    write(x)
                y = x
            write('\n')

Efiloque.resolve()