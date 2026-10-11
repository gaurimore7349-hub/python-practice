#call center Queue using FIFO
queue=[]
while True:
    print("\n---CALL CENTER---")
    print("1.Add call")
    print("2.Answer call")
    print("3.view pending calls")
    print("4.check queue empty")
    print("5.exist")
    choice=int(input("enter your choice:"))
    if choice==1:
        customerID=input("enter customer ID:")
        calltime=int(input("enter call time:"))
        queue.append((customerID, calltime))
        print("call added.")
    elif choice==2:
        if len(queue)==0:
            print("no call to answer.")
        else:
            call=queue.pop(0)
            print("answering customer ID:",call[0])
            print("call time:",call[1],"minutes")
    elif choice==3:
        if len(queue)==0:
            print("no pending calls.")
        else:
            print("pending callls:")
            for call in queue:
                print("customer ID:",call[0],"call time:",call[1],"minutes")
    elif choice==4:
     if len (queue)==0:
         print("queue is empty.")
     else:
         print("queue is not empty")
    elif choice==5:
        print("program ended.")
        break
    else:
        print("invalid choice.")
