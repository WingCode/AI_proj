from unification import *



class Student(object):
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks


data = [Student(1134, 'Ram', 100),
        Student(1234, 'Sham', 90),
        Student(1136, 'Ravi', 80),
        Student(2134, 'Sharma', 30),
        Student(1434, 'Tintu', 50)]

# UNIFY (L1, L2)
# 1. if L1 or L2 is an atom part of same thing do
# (a) if L1 or L2 are identical then return NIL
# (b) else if L1 is a variable then do
# (i) if L1 occurs in L2 then return F else return (L2/L1)
#  else if L2 is a variable then do
# (i) if L2 occurs in L1 then return F else return (L1/L2)
# else return F.
# 2. If length (L!) is not equal to length (L2) then return F.
# 3. Set SUBST to NIL
# ( at the end of this procedure , SUBST will contain all the substitutions used to unify L1 and L2).
# 4. For I = 1 to number of elements in L1 do
# ii) if S = F then return F
# iii) if S is not equal to NIL then do
# (A) apply S to the remainder of both L1 and L2
# (B) SUBST := APPEND (S, SUBST) return SUBST.



x=var('x')
y=var('y')
rollno, name, marks = var('rollno'), var('name'), var('marks')
print("Statement 1 : 1,x,3  Statement 2: 1,2,y")
print unify((1,x,3), (1,2,y))
print("Statement 1 : 1,2,2  Statement 2: x,x,2")
print unify((1,2,2), (x,x,2))
#print [unify(Student(rollno, name, 0), acct) for acct in data]