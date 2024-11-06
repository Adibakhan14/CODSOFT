class TASK1:
 def __init__(self):  
     self.tasks = []
     
 def Addtask(self):
     task = input("Enter Task: ")
     self.tasks.append(task)
     print(f"Task Added Successfully")
    
 def Edittask(self, index, newtask):
     self.tasks[index-1]=newtask
     print(f"Task Update Successfully")
    
 def Deletetask(self, index):
     delete_task = self.tasks.pop(index-1)
     print(f"Task Delete Successfully")
     
 def Viewlist(self):
        print("\n--- Task List ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

def main():
    obj=TASK1()
    while True:
         
        print("\n ...To Do List...")
        print("\n1. ADD TASK: ")
        print("\n2. UPDATE TASK: ")
        print("\n3. VIEW LIST: ")
        print("\n4. DELETE TASK: ")
        print("\n5. EXIT!!!")
        
        choice = input("Enter Your Choice: ")
        
        if choice == '1':
            obj.Addtask()
        elif choice == '2':
            index = int(input("Enter index of task to update: "))
            newtask = input("Enter new task: ")
            obj.Edittask(index, newtask)
        elif choice == '3':
            obj.Viewlist()
        elif choice == '4':
            obj.Deletetask(index)
        
        else:
            print("\nInvalid Choice!!!")
            
if __name__ == "__main__":
    main()