A,B,C=list(map(int,input().split(" ")))

HAPPY=':)'
SAD=':('

if (B < A and C >= B):
    print(HAPPY)

elif (B > A and C <= B):
    print(SAD)
  
elif (B > A and C > B and C - B < B - A):
    print(SAD)
  
elif (B > A and C > B and C - B >= B - A):
    print(HAPPY)
  
elif (B < A and C < B and B - C < A - B):
    print(HAPPY)
  
elif (B < A and C < B and B - C >= A - B):
    print(SAD)
  
elif (A == B):
    if (C > B):
        print(HAPPY)
    else:
        print(SAD)