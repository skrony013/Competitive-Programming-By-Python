# ---------------Any number of Space Separated Input as List Start----------------
# Technique 1
lst1 = [int(item) for item in input().split()]
print(lst1)

# Technique 2
lst2 = list(int(n) for n in input().split())
print(lst2)
# ---------------Any number of Space Separated Input as List End----------------


# ---------------N length Space Separated List Input Start----------------------
# Technique 1
N = int(input())
A = list(map(int, input().strip().split(' ')))[:N]
print(A)

# Technique 2
n = int(input())
B = list(map(int, input().split()))[:n]
print(B)
# ----------------N length Space Separated List Input End-----------------------

# ----------------N length Space Separated String List Input Start-----------------------
# Technique 1
N = int(input())
C = list(input().split())[:N]
print(C)
# ----------------N length Space Separated String List Input End-----------------------


# ----------------Test Case Input Start From Here-----------------------
# Technique 1
t1 = int(input())
for i in range(t1):
    print(i)

# Technique 2
t = int(input())
while t:
    print(t)
    """ t-- """
    t = t - 1
# ----------------Test Case Input Start Ended Here-----------------------


# ----------------Test Case Input Start Ended Here-----------------------
# ----------------Test Case Input Start Ended Here-----------------------
