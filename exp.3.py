#employee salaries
salaries=[45000.0,38000.0,52000.75,61000.0,47000.0,70000.0,49000.5]

#-----Selection sort-----
def selection_sort(a):
    for i in range(len(a)):
        min_index=i

    for j in range(i+1,len(a)):
        if a[j]<a[min_index]:
            min_index=j
            a[i],a[min_index]=a[min_index],a[i]
        return a  

#-----Bubble sort-----
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
             a[j], a[j+1]=a[j+1],a[j]
        return a

#-----Selection sort-----
s1=salaries.copy()
selection_sort(s1)
print("top 5 salaries using selection sort:")
print(s1[-5:][::-1])

#-----bubble sort-----
s2=salaries.copy()
bubble_sort(s2)
print("\n top 5 salaries using bubble sort:")
print(s2[-5:][::-1])
