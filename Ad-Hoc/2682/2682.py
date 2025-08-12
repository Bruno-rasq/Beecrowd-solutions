class Fault_Detector:
    counter = 0
    isFail = False
    
    @staticmethod
    def increasing_sequence():
        n = int(input())
        if not Fault_Detector.isFail and n > Fault_Detector.counter:
            Fault_Detector.counter = n 
        
        if n < Fault_Detector.counter:
            Fault_Detector.isFail = True
            
    @staticmethod
    def get_counter(): return Fault_Detector.counter + 1
    
while True:
    try: Fault_Detector.increasing_sequence()
    except EOFError: break

print(Fault_Detector.get_counter())