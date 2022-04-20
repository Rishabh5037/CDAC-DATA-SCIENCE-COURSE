class Student:
    def __init__(self):
        self.sid=0
        self.name=""
        self.marks=[]

    def calsum(self):
        sx=0
        if len(self.marks)<5:
            print("Not enough data to print sum")
        else:
            sx=sum(self.marks)
            print("Sum:",sx)
        return sx

    def inputdetails(self):
        self.sid=int(input("Enter the sid of student:"))
        self.name=input("Enter the name:")
        for x in range(5):
            self.marks.append(int(input("Enter the marks for subject {}:".format(x+1))))

    def show(self):
        print("Showing Student Record")
        print("Sid {}\nName {}\nList of marks {}".format(self.sid,self.name,self.marks))
        self.grade()

    def grade(self):
        sumx=self.calsum()
        print("s",sumx)
        if sumx>450:
            print("Grade A")
        elif sumx>350:
            print("Grade B")
        elif sumx>200:
            print("Grade C")
        else:
            print("Grade D")


st1=Student()
st2=Student()
st1.inputdetails()
st2.inputdetails()
st1.show()
st2.show()




