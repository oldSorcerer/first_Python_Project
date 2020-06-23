#Данный код не полностью решает задачу,
# чтобы даже при копировании у вас была возможность сделать часть задания самостоятельно
#Будьте внимательны!
A = [1, 3, 7, 9, 14, 16, 17, 19, 19, 19, 20, 21, 25, 26, 26, 27, 27, 27, 28, 29]
K = int(input("Введите новые элемент: "))
mid = len(A)//2
low = 0
high = len(A) - 1
s = 0

if K > A[0] and K <= A[len(A) - 1]:
    while low <= high:
       if A[mid] < K < A[mid + 1]:
            s = mid + 1
            break
       elif A[mid] == K:
           if mid != len(A) - 1:
               i = mid + 1
               while A[i] == K:
                   i+=1
               s = i
               break
           else:
               s = len(A)
               break
       elif K > A[mid]:
           low = mid + 1
       else:
           high = mid - 1
       mid = (low + high) // 2
    print(A)
    print(s)
else:
    print("Элемент К не соответствует критериям поиска")

