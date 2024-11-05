# Task 1 
# n = int(input()) 
# f = 1  
# for j in range(1, n + 1):
#     n = []  
#     for i in range(j):
#         n.append(str(f + i))  
#     f += j
#     p = ' ' * (n - j)  
#     print(p + ' '.join(n))

# Task 2 

# n = int(input())

# while True:
#     print(n,end=",")
#     if n == 1:
#         break
#     elif n % 2 == 0 :
#         n//= 2
#     else:
#         n*= 3
#         n+=1  

# Task 3

# n = int(input())
# for i in range(1, n):
#     lict = []
#     for j in range(1, i):
#         if i%j == 0:
#             lict.append(j)
#     cnt = 0
#     for l in lict:
#         cnt += l
#     if cnt == i:
#         print(i, end=",")

# Task 4

# n = input()
# dect = {}

# for i in n.lower():
#     dect[i] = dect.get(i, 0) + 1

# print(dect)

# Task 5

# n = input()
# lict = n.split()
# dect = {}
# ind = 0
# for i in lict:
#     if i in dect:
#         dect[i].append(ind)
#     else:
#         dect[i] = [ind]
#     ind += 1
# print(dect)


# Task 6

# dict = {
#     'a': [1, 2, 3],
#     'b': [4, 5],
#     'c': [6]
# }
# dect = {}
# for k, v in dict.items():
#     for i in v:
#         dect[i] = k
# print(dect)

# Task 7

# dict1 ={'a':1, 'b':2, 'c':3}
# dict2 ={'a':2, 'b':3, 'c':4}

# for k, v in dict1.items():
#     if k in dict2:
#         dict2[k]+=v

# print(dict2)

# Task 8


# n = input()
# lict = n.split()
# dect = {}
# for i in lict:
#     dect[i] = dect.get(i, 0) + 1
# print(dect)

# Task 9

n = int(input())

for i in range(1, n + 1):
    f = " " * (n - i)
    for j in range(1, i + 1):
        f += str(j)
    for j in range(i - 1, 0, -1):
        f += str(j)
    print(f)

for i in range(n - 1, 0, -1):
    f = " " * (n - i)
    for j in range(1, i + 1):
        f += str(j)
    for j in range(i - 1, 0, -1):
        f += str(j)
    print(f)

# Task 10

# n = int(input())
# for i in range(1, n):
#     cnt = 0
#     for j in str(i):
#         fac = 1
#         for l in range(1, int(j) + 1):
#             fac *= l
#         cnt += fac
#     if i == cnt:
#         print(i, end=", ")

# Task 11

# n = int(input())

# for i in range(1, n+1):
#     cnt = 0
#     for j in str(i):
#         cnt += int(j)
#     if i % cnt == 0:
#         print(i, end=",")

# Task 12 


# with open("file1.txt", 'r', encoding='utf-8') as file1, open("file2.txt", 'w', encoding='utf-8') as file2:
#     f = 1
#     for i in file1:
#         file2.write(f'{f}: {i}')
#         f += 1

# Task 13
# n = int(input())

# with open("file1.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()
#     for line in lict[-n:]:
#         print(line)

# Task 14


# with open("file1.txt", 'r', encoding='utf-8') as file1, open("file2.txt", 'w', encoding='utf-8') as file2:
#     for i in file1:
#         file2.write(f'{i}')


#  Task 15
# with open("file3.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()
#     n = lict[0]

# nict = n.split()
# dect = {}
# for i in nict:
#     dect[i] = dect.get(i, 0) + 1
# print(dect)


#  Task 16

# with open("file1.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()
# for i in lict:
#     if i == "\n":
#         lict.remove(i)

# with open("file1.txt", 'w', encoding='utf-8') as file1:
#     file1.writelines(lict)

#  Task 17


# with open("file3.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()

# n = lict[0]
# lict2=n.split()
# for i in range(0, len(lict2)):
#     if lict2[i] == 'world':
#         lict2[i]=' Python'

# with open("file3.txt", 'w', encoding='utf-8') as file1:
#     file1.writelines(lict2)


# Task 18


# with open("file3.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()

# n = lict[0]
# lict2=n.split()
# cnt = 0
# for i in lict2:
#     cnt+=1

# print(cnt)

# Task 19

# dict = {'apple':10,'banana':5, 'charry':15}

# lict = []
# for i in dict:
#     lict.append((i, dict[i]))
# for i in range(len(lict)):
#     for j in range(i + 1, len(lict)):
#         if lict[i][1] > lict[j][1]:
#             lict[i], lict[j] = lict[j], lict[i]
# dict2 = {}
# for item in lict:
#     dict2[item[0]] = item[1]
# print(dict2)

# # Task 20

# lict = [5,3,8,6,7]

# def Vozrast(lict):
#     for i in range(len(lict)):
#         for j in range(i + 1, len(lict)):
#             if lict[i] > lict[j]:
#                 lict[i], lict[j] = lict[j], lict[i]
#     return lict

# def Ybivaniy(lict):
#     for i in range(len(lict)):
#         for j in range(i + 1, len(lict)):
#             if lict[i] < lict[j]:
#                 lict[i], lict[j] = lict[j], lict[i]
#     return lict

# print(f"По возрастанию: {Vozrast(lict)}")
# print(f"По Убыванию: {Ybivaniy(lict)}")


