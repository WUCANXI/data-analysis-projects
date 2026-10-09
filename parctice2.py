# for i in range(1,21):
#     print(i)
# for i in range(2,100,2):
#     print(i)
# n=int(input('输入一个数字：'))
# # for i in range(n,0,-1):
# #     print(i)
# n='*'
# for i in range(1,6):
#     print(n*i)
# n='*'
# for i in range(1,6):
#     print(n*(6-i))
# total=0
# for i in range(1,101):
#     total=total+i
# print(total)
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total=total+i
# print(total)
# n=int(input())
# total=1
# for i in range(1,n+1):
#     total=total*i
# print(total)
# numbers=int(input('请问您要输入几个数字：'))
# total=0
# average=0
# for i in range(numbers):
#     n=float(input())
#     total+=n
#     average=total/numbers
# print(total)
# print(average)
# n=int(input())
# total=0
# for i in range(1,n+1):
#     if i%3==0:
#         total+=i
# print(total)
#
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{j}x{i}={i*j}',end='\t')
#     print()
#
# import random
# numbers=random.randint(1,100)
# while True:
#     guess=int(input("Guess a number between 1 and 100: "))
#     if guess == numbers:
#         print("You guessed right!")
#         break
#     elif guess < numbers:
#         print("Too low!")
#     else:
#         print("Too high!")
# total=0
# for i in range(1,101):
#     total=total+i
# print(total)
# n=int(input())
# total=1
# for i in range(1,n+1):
#     total=total*i
# print(total)
# numbers=int(input())
# total=0
# average=0
# for i in range(numbers):
#     real_numbers=float(input())
#     total=total+real_numbers
#     average=total/numbers
# print(total)
# print(average)
# n=int(input())
# total=0
# for i in range(1,n+1):
#     if(i%3==0):
#         total=total+i
# print(total)
for i in range(10):
    for j in range(10):
        print(f'{j}x{i}={i*j}',end='\t')
    print()

