import sys

declare = []
perform = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    token = line.split()

    if "+" not in line:
        var, _, val = token
        if len(declare) == 2:
            declare.pop(0)
        declare.append((var, int(val)))

    else:
        var_declare, _, val1, _, val2 = token

        valore1 = None
        valore2 = None

        for var, val in declare:
            if var == val1:
                valore1 = val
            if var == val2:
                valore2 = val

        for var, val in perform:
            if var == val1:
                valore1 = val
            if var == val2:
                valore2 = val

        if valore1 is None or valore2 is None:
            print("Compilation Error")
            sys.exit(0)

        sum_result = valore1 + valore2
        sum_already_exists = None
        for idx, (var, _) in enumerate(perform):
            if val == var_declare:
                perform[idx] = (var_declare, sum_result)
                sum_already_exists = True
                break

        if not sum_already_exists:
            if len(perform) == 1:
                perform.pop(0)

            perform.append((var_declare, sum_result))


print("OK")