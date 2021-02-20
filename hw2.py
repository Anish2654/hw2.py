# HW2
#Due Date: 02/20/2021, 11:59PM

"""                                   
### Collaboration Statement:
             
"""

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        
        self.cid = cid
        self.cname = cname
        self.credits = credits
        
        


    def __str__(self):
        # YOUR CODE STARTS HERE
        
        return '{}({}): {}'.format(self.cid, self.credits, self.cname)
        

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        
        if other == None:
            return False
        
        if self.cid == other.cid:
            return True
        else:
            return False
        
class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
    '''
    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}
        

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        
        
        
        self.courseOfferings[cid] = Course(cid, cname, credits)
        
        return 'Course added successfully'
        
        if self.courseOfferings[cid] in Course:
            return 'Course already added'

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        
        
            
        del self.courseOfferings[cid]
        
        return 'Course removed successfully'
        
        if self.courseOfferings[cid] not in Course:
                return 'Course not found'
            
        
        
        


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name',"zero credits"))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

    def __init__(self, sem_num):
        # --- YOUR CODE STARTS HERE
        self.sem_num = sem_num
        self.courses = []
        
        



    def __str__(self):
        # YOUR CODE STARTS HERE
        if not self.courses:
            return 'No courses'
        else:
            result = []
            for course in self.courses:
                
                result.append(course.cid)
            return ', '.join(result)
        

    __repr__ = __str__
    
    def isValid(self, course):
        
        if isinstance(course,Course) and isinstance(course.cid,str) and isinstance(course.cname, str) and isinstance(course.credits, int):
            return True
        else:
            return False
    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        
        if self.isValid(course) == False:
                return 'Invalid course'
            
        if self.isValid(course):
            if course in self.courses:
                return 'Course already added'
            else:
                
                self.courses.append(course)
        
        
        
        
        

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        
        
        if not self.isValid(course) :
            return 'Invalid course'
        
        if course not in self.courses:
            
            return 'No such course'
        else:
            
            self.courses.remove(course)
        
        
        
        
        

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        
        totalCredits = 0
        
        for course in self.courses:
            
            totalCredits = course.credits + totalCredits
            
        return totalCredits
        
        
        

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        
          
        if self.totalCredits >= 12:
            return True
        else:
            return False
        
    import random    

    
class Loan:
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        
        self.loan_id = self.__loanID  
        self.amount = amount
        
        


    def __str__(self):
        # YOUR CODE STARTS HERE
        
        return '{}: Balance: ${}, {}: Balance:  {}'.format(self.loan_id, self.amount, self.loan_id, self.loan_amount)
        

    __repr__ = __str__


    @property
    def __loanID(self):
        # YOUR CODE STARTS HERE
        
        return random.randint(10000,99999)
        


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        
        self.name = name
        
        self.ssn = ssn
        
        

    def __str__(self):
        # YOUR CODE STARTS HERE
        
        return 'Person({}, ***-**-{})'.format(self.name, self.get_ssn()[-4:])
        

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        
        return self.ssn
        

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        
        if self.get_ssn() == other.get_ssn():
            return True
        else:
            return False
        
        

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        
        self.name
        self.ssn
        self.supervisor = supervisor
        
        


    def __str__(self):
        # YOUR CODE STARTS HERE
        
        return 'Staff({}, {})'.format(self.name, self.id)
        

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        
        return '905' + {} + {} + {}.format(self.name.split()[0][0], self.name.split()[1][0], self.get_ssn()[-4:])
        
        

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        
        return self.supervisor
        

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        
        if isinstance(new_supervisor, Staff):
            
            self.supervisor = new_supervisor
            
            return 'Completed'
        else:
            return None
        


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        
        if not isinstance(student, Student):
            return None
        else:
        
            student.hold = True
            return 'Completed'
        

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if not isinstance(student, Student):
            return None
        else:
        
            student.hold = False
            return 'Completed'
    

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        
        if not isinstance(student, Student):
            return None
        else:
            student.active = False
            return 'Completed'
        
        




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        
        
        random.seed(1)
        self.name = name
        self.ssn = ssn
        self.year = year
        self.active = True
        self.hold = False
        self.semesters = {}
        self.account = self.__createStudentAccount()
        
        
        
        
        # YOUR CODE STARTS HERE
        
        

    def __str__(self):
        # YOUR CODE STARTS HERE
        pass

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        
        if not self.active:
            return None
        else:
            return StudentAccount(self)
        
    
        
        



    @property
    def id(self):
        # YOUR CODE STARTS HERE
         return '905' + {} + {} + {}.format(self.name.split()[0][0], self.name.split()[1][0], self.get_ssn()[-4:])
        

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        
        
        
        if not self.active and self.hold:
            return 'Unsuccessful Operation'
        else:
            
            self.semesters
            
        
    



    def enrollCourse(self, cid, catalog, semester):
        # YOUR CODE STARTS HERE
        
        if not self.active and self.hold:
            return 'Unsuccessful Operation'
        
        if catalog.courseOfferings[cid] in self.semesters.course:
            return 'Course already enrolled'
        else:
            return 'Course not found'
      
                
        

    def dropCourse(self, cid, semester):
        # YOUR CODE STARTS HERE
        
        if not self.active and self.hold:
            return 'Unsuccessful Operation'
        
        
        for course in semester.courses:
            if cid == course.cid:
                semester.courses.remove(course)
                
                return 'Course Dropped Successfully'
               
        return 'Course not found'      
        

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if not self.active:
            return 'Unsuccessful Operation'
        if not self.semesters[str(len(self.semesters))].isFullTime:
            return 'Not Full Time'
            
        



class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
    '''
    
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        
        self.student = student
        self.loans = {}
        self.balance = 0
        
        
        


    def __str__(self):
        # YOUR CODE STARTS HERE
        
        return 'Name: {} \n ID: {} \n Balance: ${}'.format(self.student.name, self.student.id, self.balance)
    

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        
        self.balance -= amount
        return self.balance
    
        
        


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance
        
        




####################### STAND ALONE FUNCTION ###############################################


def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s, Student)
        True
    """
    
    return Student(person.name, person.get_ssn(), 'Freshman')

if __name__=='__main__':
    import doctest
    doctest.testmod() 
    doctest.run_docstring_examples(Loan, globals(), name='HW2',verbose=True)
 