registeredDay, initialValue, variationValue, predictDays = [
    int(x) for x in input().split()]
    
stonks = True if registeredDay % 2 != 0 else False

currentValue = initialValue
for _ in range(predictDays):
    if stonks:
        currentValue += variationValue
        stonks = False
        continue
    currentValue -= variationValue
    stonks = True
    
print(currentValue)