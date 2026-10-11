#hash table using chaining
table=[[]for i in range(10)]
def insert(key,value):
    index=key%10
    table[index].append((key,value))
def search(key):
    index=key%10
    for k,v in table[index]:
        if k==key:
            print("value=",v)
            return
        print("key not found")

def delete(key):
    index = key%10
    for item in table[index]:
        if item[0] ==key:
            table[index].remove(item)
            print("key deleted")
            return
        print("key not found")

#insert
n=int(input("enter number of element:"))
for i in range(n):
    key=int(input("enter key:"))
    value=input("enter value:")
    insert(key,value)

#search
key=int(input("\nenter key to search:"))
search(key)

#delete
key=int(input("enter key to delete:"))
delete(key)

#display 
print("\nhash table:")
for i in range(10):
    print(i,":",table[i])
