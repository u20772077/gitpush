#pre defined factorial eexplanation

class  mathexplained:
    def factorial(self):
       print("The factorial is " +str(self.tempo))

m1 = mathexplained()
def facts(n):
    temp = 1
   
    for i in range(1,n+1):
        temp = temp*i
    return temp
res = facts(5)
m1.tempo = res   

out =  m1.factorial()
print(out)
'''

def facts(n):
    temp = 1
    
    for i in range(1,n+1):
        temp = temp*i
    return temp
  
facts(5)
print(facts(5))
'''
# descriptor object




# simple 