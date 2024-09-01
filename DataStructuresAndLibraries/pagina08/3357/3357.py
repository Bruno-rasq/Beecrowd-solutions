class CircularList:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def next(self):
        if not self.lst:
            raise IndexError("The list is empty")
        item = self.lst[self.index]
        self.index = (self.index + 1) % len(self.lst)
        return item


# quantidade pessoas, litros, cabeça 
p, litros, cabaca = input().split(" ")
pessoas = CircularList(input().split(" "))

litros = float(litros)
cabaca = float(cabaca)
rico = ""

while litros >= cabaca:
  litros -= cabaca
  rico = pessoas.next()

rico = pessoas.next() #o último 

print(f"{rico} {litros:.1f}")