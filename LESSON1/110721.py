num=int(input("Enter a number with 4 digits:"))
'''
    Alafim=4
    Meot=5
    Asarot=6
    Ahadot=7
 '''
#this is Alafim
print("Alafim= " + str (num//1000))
#this is Meot
num=(num%1000)
print("Meot= " + str (num//100))
#this is Asarot
num=(num%100)
print("Asarot= " + str (num//10))
#this is Ahadot
num=(num%10)
print("Ahadot= " + str (num))