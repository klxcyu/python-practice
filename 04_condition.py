misemonji = int(input('농도 입력 :'))

if misemonji > 150:
    print('매우나쁨')
elif misemonji < 151 and misemonji > 80:
    print('나쁨')
elif misemonji < 81 and misemonji > 30:
    print('보통')
else:
    print('좋음')
    
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