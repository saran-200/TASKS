seats=1
while seats<=10:
    a=int(input('enter the no of tickets reuired :'))
    b=a*120
    print('your tickets amount is ',b)
    paid=int(input('your amount paid'))
    if paid==b:
        print('yor ticket has been booked')
    else:
        print('failed due to amount insufficient')
    seats+=a

# seats=1
# while seats<=15:
#     if seats%5!=0 and  seats%2!=0:
#         amt=int(input('enter the amount'))
#         if amt>=190:
#             print('tickets booked',seats)
#             seats+=1
#         else:
#             print('failed')
#     else:
#         seats+=1
#         continue


#hiring 

# hire=1
# while hire<=5:
#     print('employee',hire)
#     skills=input('enter ur skills')
#     pro=int(input('enter your no of projects'))
#     if (skills=='python' or skills=='java') and pro>=3:
#         print('your elgible')
#         hire+=1
#     else:
#         print('we need more skills and projects')
    


    
