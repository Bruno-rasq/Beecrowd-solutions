output = ""

while True:

    try:
        word = input()

        combinations = set()

        head = 0
        queue = [word]

        while head < len(queue):
            curr_segment = queue[head]
            head += 1

            combinations.add(curr_segment)

            for idx in range(len(curr_segment)):
                segment = curr_segment[0:idx] + curr_segment[idx+1:]

                comb_len = len(combinations)
                combinations.add(segment)
                new_comb_len = len(combinations)

                if new_comb_len > comb_len:
                    queue.append(segment)

        for segment in sorted(combinations):
            if segment:
                output += segment + "\n"

        output += "\n"

    except EOFError:
        break

print(output, end="")
