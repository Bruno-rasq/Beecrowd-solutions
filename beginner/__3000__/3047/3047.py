mr_monica_ages = int(input())
children_1 = int(input())
children_2 = int(input())
children_3 = mr_monica_ages - (children_1 + children_2)

eldest = children_1

if children_2 > eldest:
    eldest = children_2

if children_3 > eldest:
    eldest = children_3

print(eldest)