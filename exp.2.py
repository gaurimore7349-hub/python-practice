#store customer account ID's in a list
ids=[101,205,310,415,520]

# take customer ID from the user
key=int(input("enter customer ID:"))

#----Linear Search----#
#check whether the ID exists in the list
if key in ids:
    print("linear search:iD Not found")
else:
    print("linear saerch:ID not found")

#----binary search----
#set the starting position
low=0

#set the ending position
high=len(ids)-1

#initially,ID is not found
found=False

#continue searching while the range is valid
while low<=high:

#find the middle position
 mid = (low+high) //2

#check if middle ID is the required ID
if ids[mid] ==key:
   found = True
   break

#if key is greater,search the right half
elif ids[mid]<key:
   low=mid+1

#if key is smaller,search the left half
else:
   high=mid-1

#display binary search result 
if found:
   print("binary search:ID found")
else:
   print("binary search :ID not found")