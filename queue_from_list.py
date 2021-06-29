# QUEUE USING LIST :
x=[]
def enqueue(x):
    x.append(int(input("Enter the element --> ")))

def dequeue():
    x.pop(0)

def traversal(x):
    print("Elements of queue are --> ",x)

print("1.Insertion of an element in queue")
print("2.Deletion of an element from queue")
print("3.Traversal of elements in queue")
choice=1
while choice==1:
    ch=int(input("Enter the choice of operation : "))
    if ch==1 :
        enqueue(x)
        flag=1
        while flag==1:
            flag=int(input("Do you want to continue the same operation ? (0-->NO and 1-->YES) :"))
            if flag==0:
                break
            enqueue(x)
    elif ch==2:
        flag = 1
        while flag == 1:
            if not x:
                print("Queue has no more elements !")
                break
            else:
                dequeue()
                print("First element deleted", x)
            flag = int(input("Do you want to continue the same operation ? (0-->NO and 1-->YES) : "))
            if flag == 0:
                break
    elif ch==3:
        traversal(x)
    else:
        print("Wrong choice of operation !")
    choice=int(input("Do you want to perform more operations ? (0-->NO and 1-->YES) :"))
    if choice==0 :
        break