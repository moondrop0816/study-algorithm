x, y = map(int, input().split(' '))
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if x == 1:
    print(days[y % 7 - 1])
else:
    print(days[(sum(month[:x-1]) + y) % 7 - 1])