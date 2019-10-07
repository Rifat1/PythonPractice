
class Employee:
    def __init__(self, n, d):
        self.__name = n
        self.__dateOfHire = d

    def __repr__(self):
        return "\n[Name: " + self.__name + ", Date of Hire: " + self.__dateOfHire + "]"


class UnionMember(Employee):
    def __init__(self, n, d,payPerHour,hoursWorked,jobType):
        super().__init__(n, d)
        # self.__name=n
        # self.__dateOfHire = d
        self.__payPerHour = payPerHour
        self.__hoursWorked = hoursWorked
        self.__jobType = jobType

    def calcPay(self, payPerHour, hoursWorked, jobType):
        if jobType=="F":
            pay=self.__hoursWorked*self.__payPerHour
        elif jobType=="P":
            pay=0.75*self.__payPerHour*hoursWorked
        return pay
    def __repr__(self):
        return super().__repr__()+"\n[Hourly Pay: "+str(self.__payPerHour)+", Number of Hours worked: "+str(self.__hoursWorked)+", Full-time employee or Part-time employee: "+self.__jobType+"]"

    
class Manager(UnionMember):
    def __init__(self, n, d, payPerHour, hoursWorked, jobType, minEmployess ,actualEmpNum):
        super().__init__(n, d, payPerHour, hoursWorked, jobType)
        # self.__name = n
        # self.__dateOfHire = d
        # self.__payPerHour = payPerHour
        # self.__hoursWorked = hoursWorked
        # self.__jobType = jobType
        self.__minEmployess = minEmployess
        self.__actualEmpNum = actualEmpNum

    def calcPay(self, payPerHour, hoursWorked, minEmployess, actualEmpNum):
        if actualEmpNum >= minEmployess:
            pay = 0.10*self.__payPerHour*hoursWorked
        else:
            pay =self.__payPerHour*hoursWorked
        return pay
    def __repr__(self):
        return super().__repr__()+"\n[Minimum number of Employees Supervised: "+str(self.__minEmployess)+", Actual number of employees supervised: "+str(self.__actualEmpNum) + "]"

uMember=UnionMember("Rifat","2018",10,45,"F")
manager=Manager("shariq","2010",20,60,"F",4,5)
print(uMember)
print(manager)
