def TimeStempInSeconds(days, hours, minutes, seconds):
    time = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    return time

def GetTimeInput():
    dia, y = input().split()
    hours, minutes, seconds = [int(x) for x in input().split(" : ")]
    return TimeStempInSeconds(int(y), hours, minutes, seconds)

A = GetTimeInput()
B = GetTimeInput()
C = B - A

days = int(C / 86400)
C %= 86400
hours = int(C / 3600)
C %= 3600
minutes = int(C / 60)
C %= 60
seconds = int(C)

print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")