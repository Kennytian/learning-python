# conding: utf-8
age = 10
if(age > 18):
    print('你的年龄是', age)
    print('成年')
elif age >= 6:
    print('你的年龄是', age)
    print('十几岁的青少年')
else:
    print('儿童')

birth = int(input('生日:'))
if birth < 2000:
    print('00前')
else:
    print('00后')

list = ('过轻', '正常', '过重', '肥胖', '严重肥胖')

weight = float(input('你的体重(kg)？'))
height = float(input('你的身高(m)?'))

bmi = weight / height / height

if bmi < 18.5:
    print('您的体重BMI指数%.2f，判定为%s' % (bmi, list[0]))
elif bmi < 25:
    print('您的体重BMI指数%.2f，判定为%s' % (bmi, list[1]))
elif bmi < 28:
    print('您的体重BMI指数%.2f，判定为%s' % (bmi, list[2]))
elif bmi < 32:
    print('您的体重BMI指数%.2f，判定为%s' % (bmi, list[3]))
else:
    print('您的体重BMI指数%.2f，判定为%s' % (bmi, list[4]))
