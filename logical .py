# campus recuriter
skills=input('enter the skills :')
projects=int(input('enter no of project you did :'))
print("your eligible for backend :",(skills== 'python' or skills=='java'and projects>=2))
print('your eligible for frontend :',(skills=='html'or skills=='css' or skills=='js' and projects>=5))
print('your eligible for devloper :',(skills=='python' or skills=='java' and projects>=5))


