from self import self

import re
class login:

    def __init__(self):
        self.pin = ""
        self.user_login()
    def user_login(self):
        user_input = input("""
        **WELCOME TO LEARNING SITE**
        1.CREATE PASSWORD FOR STUDENT
        2.CREATE PASSWORD FOR INSTRUCTOR
        3.STUDENT LOGIN
        4.INSTRUCTOR LOGIN
        """)

        if user_input == "1":
            self.stud_pass()
        elif user_input == "2":
            self.inst_pass()
        elif user_input == "3":
            self.student_login()
        else:
            self.instruct_login()

    def stud_pass(self):


        self.pin = input("CREATE YOUR PASSWORD")

        print("THE STUDENT PASSWORD IS CREATED SUCCESSFULLY")

    def inst_pass(self):
        self.passw = input('[1-5]{2}[a-zA-Z]{20}[*]{2}')
        print("THE INSTRUCTOR PASSWORD IS  CREATED SUCCESSFULLY")




    def student_login(self):
        temp = input("ENTER YOUR PASSWORD")
        if temp == self.pin:
           self.enter = input("ENTER YOUR NAME BELOW WITH THE GIVEN FORMAT")
           if self.enter == input('[a-zA-Z]{6}'):
               print("SUCCESSFULLY LOGGED IN")
           else:
               print("INVALID USERNAME")
        else:
            print("INVALID PASSWORD")

    def instruct_login(self):
        temp = input("ENTER YOUR PASSWORD")
        if temp == self.passw:
            print("YOU ARE SUCCESSFULLY LOGGED IN")
        else:
            print("PLEASE RE-CHECK THE PASSWORD")

obj = login()

obj.user_login()
obj.stud_pass()
obj.inst_pass()
obj.student_login()

obj.instruct_login()

