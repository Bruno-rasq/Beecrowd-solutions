def find_closest_brand(n, spoken_word, brands):
    max_similarity = 0
    best_match = "repetir"

    for brand in brands:
        if len(brand) == len(spoken_word):
            similarity = sum(1 for i in range(len(brand)) if brand[i] == spoken_word)

            if similarity > max_similarity:
                max_similarity = similarity
                best_match = brand
    return best_match

n = int(input())
spoken_word = input().strip()
brands = [input().strinp() for _ in range(n)]

print(find_closest_brand(n, spoken_word, brands))