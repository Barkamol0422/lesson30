class Parent:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print("Name of the parent: ",self.name)
        print("Id number of the parent: ",self.id_number)
class employee(Parent):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        Parent.__init__(self,name,id_number)
    def display(self):
        print("Salary of the employee is: ",self.salary)
        print("Post of the employee is",self.post)
        Parent.display(self)
ob=employee("pinguin",12231343,"$12000","Manager")
ob.display()
