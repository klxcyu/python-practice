numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = []
for num in numbers:
    
    newlist.append(num*2)
 
    for nums in number:
        
        print(num,'X',nums,'=',num*nums)
        
print(newlist)

