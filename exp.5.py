Python
from collections import deque
queue=deque()
while True:
 print("/n---event processing system---")
 print("1.add event")
 print("2.process next event")
 print("3.display pending events")
 print("4.cancle event")
 print("5.exist")

 choice=int(input("enter your choice:"))

 #add event 
 if choice==1:
  event=input("enter event:")
  queue.append(event)
  print("event added:",event)

#process next event
 elif choice==2:
  if queue:
   event=queue.popleft()
   print("event processed:",event)
  else:
   print("Queue is empty:")

#display pending events
 elif choice==3:
  if queue:
   print("pending events:",list(queue))
  else:
   print("No pending events.")

#cancel event
 elif choice==4:
  event=input("enter event to cancel:")
  if event in queue:
   queue.remove(event)
   print("event cancelled:",event)
  else:
   print("event not found.")

#exist
 elif choice==5:
  print("program ended.")
  break
 else:
  print("invalid choice.")
