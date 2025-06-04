class Solution:
    @staticmethod
    def question_1300() -> None:
        while True:
            try:
                print("Y" if int(input()) % 6 == 0 else "N")
            except EOFError: break
            
Solution.question_1300()