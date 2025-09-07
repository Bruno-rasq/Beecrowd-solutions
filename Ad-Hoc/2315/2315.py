class Easy_Difference_Between_Dates:
    @staticmethod
    def days_between(d1, m1, d2, m2):
        DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(d, m):
            return sum(DAYS_PER_MONTH[:m-1]) + d
        
        return to_day_of_year(d2, m2) - to_day_of_year(d1, m1)

d1, m1 = [int(x) for x in input().split()]
d2, m2 = [int(x) for x in input().split()]

print(Easy_Difference_Between_Dates.days_between(d1, m1, d2, m2))