# n = int(input("Enter your first number: "))
# x = int(input("Enter your second number: "))
# if n ^ x == 0:
#      print("The numbers are equal!")
# else:
#     print("The numbers are not equal!")    
     
def find_odd_occurence(lst):
     result = 0
     for num in lst:
          result = result ^ num
     return result

print(find_odd_occurence([1,1,2,3,3,6,2,6,6])) 