class Mountain_ranges:
    @staticmethod
    def max_n_of_scenic_viewpoints_can_be_visited(vps, limit):
        max_count = 1
        current_count = 1
        
        for i in range(1, len(vps)):
            if vps[i] - vps[i - 1] <= limit:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 1
                
        print(max_count)


n_viewpoints, limit = map(int, input().split())
scenic_viewpoints = list(map(int, input().split()))

Mountain_ranges.max_n_of_scenic_viewpoints_can_be_visited(
    scenic_viewpoints, limit
)