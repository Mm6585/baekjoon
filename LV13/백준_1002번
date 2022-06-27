import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
	
	if (d == 0):	# 원점이 같은 경우
		if (r1 == r2):	# 같은 원
			print(-1)
		else:	# 동심원
			print(0)
	elif (d == r1+r2):	# 외접
		print(1)
	elif (d > r1+r2):	# 외부에서 접하지 않음
		print(0)
	else:	# 두 원의 원점 사이의 거리가 반지름의 합보다 작은 경우
		if (max(r1, r2)-min(r1,r2) == d):	# 내접
			print(1)
		elif (max(r1, r2)-min(r1,r2) < d):	# 두 점에서 만나는 경우
			print(2)
		else:	# 내부에서 접하지 않음
			print(0)
