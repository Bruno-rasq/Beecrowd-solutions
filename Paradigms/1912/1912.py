import sys

class Help_Mr_Madruga:
    @staticmethod
    def area_acima(strips, cut_height):
        area = 0.0
        for strip in strips:
            if strip > cut_height:
                area += strip - cut_height
        return area

    @staticmethod
    def binary_search_cut(strips, target_area):
        e, b = 0.0, max(strips)
        EPS = 1e-7
        while b - e > EPS:
            mid = (e + b) / 2.0
            area = Help_Mr_Madruga.area_acima(strips, mid)
            if abs(area - target_area) < EPS:
                return mid
            if area < target_area:
                b = mid
            else:
                e = mid
        return (e + b) / 2.0

    @staticmethod
    def resolve():
        input_lines = sys.stdin.read().splitlines()
        idx = 0
        while idx < len(input_lines):
            line = input_lines[idx].strip()
            idx += 1
            if not line:
                continue
            n_a = list(map(int, line.split()))
            if n_a[0] == 0 and n_a[1] == 0:
                break
            n, a = n_a
            strips = list(map(int, input_lines[idx].strip().split()))
            idx += 1
            total_sum = sum(strips)
            if abs(total_sum - a) < 1e-7:
                print(":D")
                continue
            if total_sum < a:
                print("-.-")
                continue
            cut_height = Help_Mr_Madruga.binary_search_cut(strips, a)
            print(f"{round(cut_height + 1e-8, 4):.4f}")

Help_Mr_Madruga.resolve()