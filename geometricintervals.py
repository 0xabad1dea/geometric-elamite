import random

intervals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

songB = [6, 5, 1, 6, 5, 6, 1, 6, 5, 1, 6, 5, 1, 6,
	5, 1, 10, 6, 4, 5, 1, 6, 5, 6, 1, 6, 5,
	1, 6, 5, 1, 6, 5, 1, 10, 6, 4, 5, 10, 4, 5, 3,
	10, 3, 9, 4, 5, 10, 4, 1, 5, 3, 2, 6, 5, 10,
	4, 5, 3, 10, 3, 9, 4, 5, 10, 4, 1, 5, 3, 2]

songC = [7, 2, 7, 5, 1, 3, 1, 5, 1, 6, 1, 5, 1, 3, 1,
	5, 1, 6, 1, 6, 1, 6, 1, 6, 1, 10, 1, 6, 1,
	6, 1, 6, 1, 10, 6, 1, 10, 6, 10, 7, 8, 6, 4, 6, 1, 10,
	6, 10, 7, 8, 6, 4, 6, 1, 6, 1, 10, 7, 10, 7, 10, 5, 10,
	7, 10, 7, 10, 7, 10, 5, 6, 1, 10, 2, 7, 11, 1, 6,
	11, 2, 7, 11, 1, 6]

songD = [6, 5, 6, 5, 1, 6, 10, 4, 10, 5, 1, 5, 7,
	10, 5, 1, 10, 6, 1, 5, 1, 3, 1, 3, 1,
	10, 6, 1, 3, 7, 10, 5, 7, 10, 5, 7, 7, 6,
	10, 5, 6, 1, 6, 1, 5, 6]


def findinterval(a, b):
	if(a > b):
		interval = a-b;
	else:
		interval = b-a;
	intervals[interval]+=1


for i in range(len(songB)-1):
	findinterval(songB[i], songB[i+1])
for i in range(len(songC)-1):
	findinterval(songC[i], songC[i+1])
for i in range(len(songD)-1):
	findinterval(songD[i], songD[i+1])

print("intervals of real songs")
print(intervals)

# reset the interval counts
for i in range(len(intervals)):
	intervals[i] = 0

randomsong = []
randomlen = len(songB) + len(songC) + len(songD)
for i in range(randomlen):
	randomsong.append(random.randint(1,11))
for i in range(len(randomsong)-1):
	findinterval(randomsong[i], randomsong[i+1])

print("intervals of random song (will be different every time)")
print(intervals)
