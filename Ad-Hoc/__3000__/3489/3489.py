class Cpp_Templates_and_STL_Containers:
    @staticmethod #-> O(n²)
    def findIndicesWithSum(vector, target):
        has_result = False
        for i in range(len(vector)):
            for j in range(i + 1, len(vector)):
                if abs((vector[i] + vector[j]) - target) < 1e-9:  # tolerância para float
                    print(f"{i} {j} {target:.0f}")
                    has_result = True
        
        if not has_result: print("null value")
    
vector, target = [float(x) for x in input().split()], float(input())
Cpp_Templates_and_STL_Containers.findIndicesWithSum(vector, target)