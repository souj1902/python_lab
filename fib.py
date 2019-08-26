Num = int(input("\nPlease Enter the Range Number: "))
i = 0
First = 0
Second = 1

while(i < Num):
           if(i <= 1):
                      Next = i
           else:
                      Next = First + Second
                      First = Second
                      Second = Next
           print(Next)
           i = i + 1
