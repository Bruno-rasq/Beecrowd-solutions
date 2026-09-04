class corredor:
    @staticmethod
    def kadane_algorthm():
        n = int(input())
        arr = [int(x) for x in input().split()]

        local_max = arr[0]
        global_max = arr[0]

        for i in range(1, n):
            local_max = max(arr[i], local_max + arr[i])
            if local_max > global_max:
                global_max = local_max

        print(global_max)

corredor.kadane_algorthm()