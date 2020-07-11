import csv



class Student():

    def __init__(self,file_name):
        self.file_name = file_name



    def view_course_of_study(self,course_filename):
        print("i am from 1")
        #read through csv
        pass

    def create_student_info(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        amount_paid = int(input("Enter paid amount : "))
        list1 = [first_name,last_name,amount_paid]

        with open(self.file_name,'a+') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(list1)


    def check_balance(self):
        # show payments and remaining payments
        print("i am from 2")
        name = input("Enter the student name: ")
        
        with open(self.file_name,'r') as readFile:
            reader = csv.reader(readFile)
            next(reader)
            for row in reader:
                if name ==row[0]:
                    print("First-Name: ",row[0])
                    print("Last-Name: ",row[1])
                    print("Balance: ",row[2])
                    break
        

    def update_student_info(self):
        print(" i am from 3")
        # update name address and payments
        name = input("Enter the student name: ")
        balance = int(input("Enter the balance to update: "))
        lines = list()
        update = list()
        with open(self.file_name,'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                if name ==row[0]:
                    update.append(row)
                    lines.remove(row)
                
        
        update[0][2] = int(update[0][2]) + balance
        lines.append(update[0])
        print(lines)

        with open(self.file_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
      

    def delete_student_info(self):
        print(" i am from 4")
        #delete the row
        name = input("Enter the student name: ")
        lines = list()
        with open(self.file_name,'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                if name ==row[0]:
                    lines.remove(row)
        print(lines)
        with open(self.file_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def formating(self):
        fmt_head = '{{:{}}}{{:>{}}}'.format(40, 10)
        fmt = '{{:{}}}{{:>{}.0f}}'.format(40, 10)
        print('='*60)
        print(fmt_head.format('CONTENTS','NUMBER'))
        print('_'*60)
        print(' '*60)
        print(fmt.format('View Course Of Study',1))
        print('_'*60)
        print(' '*60)
        print(fmt.format('Create Student Information ',2))
        print('_'*60)
        print(' '*60)
        print(fmt.format('Update Student Information',3))
        print('_'*60)
        print(' '*60)
        print(fmt.format('Delete Student Information',4))
        print('_'*60)
        print(' '*60)
        print(fmt.format('Check Balance',5))
        print('_'*60)
        print(' '*60)
        print(fmt.format('Stop the program',0))
        print('_'*60)
        print(' '*60)


#main function
filename = "academy.csv"
obj = Student(filename)
obj.formating()
file_name = 'records.csv'
# dictionary for switch case
switcher = {
    1 : obj.view_course_of_study,
    2 : obj.create_student_info,
    3 : obj.update_student_info,
    4 : obj.delete_student_info,
    5 : obj.check_balance,
}

# user_input is 1 for first loop
user_input = 1
while(bool(user_input)):
    print('_'*60)
    print(' '*60)
    try: 
        user_input = input("Enter the information number you want to get : ") 
        a = switcher.get(int(user_input))
        a()
        
    except:
        print("!!!!!!!!!!!!!!! {} is NOT Allowed !!!!!!!!!!!!!!".format(user_input))
        print("Please enter again")
        continue

else:
    print('_'*60)
    print(' '*60)
    print("Thank you for using Rajesh Console app!!")
    print('_'*60)
    print(' '*60)


