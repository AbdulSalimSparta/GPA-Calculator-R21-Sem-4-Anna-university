log="""
------------------------------------
 Anna University R2021 Semester 4
------------------------------------
Grade	              Grade Points
------------------------------------
O	                 10
------------------------------------
A+	                 9
------------------------------------
A	                 8
------------------------------------
B+	                 7
------------------------------------
B	                 6
------------------------------------
C	                 5
------------------------------------
RA (Re-appearance)       0
------------------------------------
SA (ShortofAttendance)   0
------------------------------------
W (Withdrawal)	         0
-------------------------------------
{------Code by Abdul Saleem---------}
-------------------------------------
"""
print(log)

Alg=int(input("Enter CS3401(Algorithms) Grade Points : "))
os=int(input("Enter CS3451(Operating Systems) Grade Points: "))
Toc=int(input("Enter CS3452(Theory of Computation) Grade Points: "))
OSlab=int(input("Enter CS3461(Operating Systems Lab) Grade Points: "))
DBMSLab=int(input("Enter CS3481(DBMS Lab) Grade Points: "))
AIML=int(input("Enter CS3491(AIML) Grade Points: "))
DBMS=int(input("Enter CS3492(DBMS) Grade Points: "))
Ess=int(input("Enter CS3451(ESS) Grade Points: "))
PD=int(input("Enter SB8024(Naan Mudhalvan) Grade Points: "))

Ci=(((4*Alg)+(os*3)+(Toc*3)+(OSlab*1.5)+(DBMSLab*1.5)+(AIML*4)+(DBMS*3)+(Ess*2)+(PD*2))/(4+3+3+1.5+1.5+4+3+2+2))

print(f"Your GPA is : {Ci}")



