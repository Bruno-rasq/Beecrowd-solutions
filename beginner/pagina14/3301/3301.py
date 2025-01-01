entrada = [int(x) for x in input().split()]

def get_middle_element_index(list):

    mmax = max(list)
    mmin = min(list)

    for i in range(3):
        if list[i] != mmin and list[i] != mmax:
             return i
    return -1


sobrinhos = ["huguinho", "zezinho", "luisinho"]

print(sobrinhos[get_middle_element_index(input)])