from ChocolateCount import birthday

print("First line: Input the total number of squares.")
print("Second Line: Input the number in each square with a space in between.")
print("Third Line: Input the day and month, with a space in between.")

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)

print("You can portion the chocolate in " + str(result) + " ways.")
