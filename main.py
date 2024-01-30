class Queue:
    def __init__(self):
        self.queue = []

    def is_Empty(self):
        if len(self.queue) == 0:
            print("The Queue is empty")
            return True
        else:
            print("The Queue is not empty")
            return False

    def is_Full(self):
        return False


    def Enqueue(self, element):
        self.queue.append(element)
        print(f"{element} was enqueued")

    def Dequeue(self):
        if self.is_Empty():
            print("nothing to delete")
        else:
            deleted_element = self.queue.pop()
            print(f"{deleted_element} was dequeued")

    def Show(self):
        print(self.queue)

queue = Queue()
while True:
    print("Menu: ")
    print("1. Check if the Queue is empty")
    print("2. Check if the Queue is full")
    print("3. Add an element to the Queue")
    print("4. Delete an element from the Queue")
    print("5. Show all elements of the Queue")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        queue.is_Empty()

    elif choice == "2":
        if queue.is_Full:
            print("There is no limit")

    elif choice == "3":
        added_element = input("What can I add? ")
        queue.Enqueue(added_element)


    elif choice == "4":
        queue.Dequeue()

    elif choice == "5":
        queue.Show()

    elif choice == "6":
        print("Bye")
        break