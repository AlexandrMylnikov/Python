import random
import time

def bubble_sort_descending(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0,n-1):
      if arr[j] < arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] 
  return arr

#mass= [60, 30, 90, 66, 80, 15, 42, 4, 67, 50]
'''
[60] [30] [90] [66] [80] - 1
[30 60] [66 90] [80]- 2 
[30 60 66 90] [80] - 4
[30 60 66 90 80] - 8
'''

mass= [random.randint(1, 100) for _ in range(1000000)]
arr=mass
print('Изначальные значения',arr)

def sort_sliyanie(mass):
    k=len(mass)//2
    mass_1=mass[:k]
    mass_2=mass[k:]

    mass_1=sorted(mass_1)
    #print(mass_1)
    mass_2=sorted(mass_2)
    #print(mass_2)
    mass=[]
    i=j=0
    while i<len(mass_1) and j<len(mass_2):
        if mass_1[i]<mass_2[j]:
            mass.append(mass_1[i])
            i+=1
        else:
            mass_2.append(mass_2[j])
            j+=1
    #print(mass)
    #print(mass_2)
    mass.extend(mass_2[j:])
    mass.extend(mass_1[i:])
    return mass
time1 = time.time() #нынешнее время
print('Результат сортировки слиянием', sort_sliyanie(mass))
time2 = time.time()
print('Время выполнения сортировки', time2 - time1)

time1 = time.time()
print('Результат сортировки пузырьком', bubble_sort_descending(arr))
time2 = time.time()
print('Время выполнения сортировки',time2 - time1)

