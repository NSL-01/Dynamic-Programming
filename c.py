n = int(input())
steps = int(input())
 
def rec(level):
    ans =0
    if (level ==n):
        return 1
    elif (level > n):
        return 0
    else:
        for i in range (1,steps+1):
             if level+ i<=n:
                ways =rec(level+i)
                ans = ans + ways
        return ans
print(rec(0))

    
 
    

     
   
          



 


    