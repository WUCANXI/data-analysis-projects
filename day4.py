# n=1
# while n<=10:
#     print(n)
#
# total=0
# for i in range(1,101):
#     total=total+i
#     print(total)
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(f'{i}x{j}={i*j}',end='\t')
#     print()
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}x{j}={i*j}',end='\t')
#     print()
import random
target=random.randint(1,100)
count=0
while True:
    guess=int(input("Guess a number between 1 and 100: "))
    count+=1
    if guess==target:
        print("You guessed right!")
        break
    elif guess<target:
        print("Too low!")
    else:
        print("Too high!")