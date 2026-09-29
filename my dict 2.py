M={}
n=int(input("enter how many students:"))
for i in range(n):
    roll,marks=eval(input("enter roll no,marks:"))
    M[roll]=marks
print(M)