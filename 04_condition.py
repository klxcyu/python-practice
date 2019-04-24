# misemonji = int(input('농도 입력 :'))

# if misemonji > 150:
#     print('매우나쁨')
# elif misemonji < 151 and misemonji > 80:
#     print('나쁨')
# elif misemonji < 81 and misemonji > 30:
#     print('보통')
# else:
#     print('좋음')

'''   
alist = []
blist = []

ranges = (range(1,11))

for num in ranges:
    
    if num % 2:
        alist.append(num)
    else:
        blist.append(num)
        
print(alist)
print(blist)
'''

#1. 집합처럼 중복을 허용하지 않는 리스트 만들기
'''
numbers = [2,4,6,7,4,3,1,2,3]

new_numbers = []

for num in numbers:
    if num not in new_numbers:
        new_numbers.append(num)

print(sorted(new_numbers))
'''
    

#2. fizzbuzz
# 조건
#1. 만약 해당 숫자가 3으로 나누어지면 'Fizz'
#2. 만약 해당 숫자가 5로 나누어지면 'Buzz'
#3. 만약 해당 숫자가 3고 5로 모두 나누어지면 'FizzBuzz'

'''
ranges = (range(1,101))

for num in ranges:
    
    if num % 15 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

'''


