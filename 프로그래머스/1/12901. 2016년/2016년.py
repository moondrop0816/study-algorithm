def solution(a, b):
    day_name = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_count = sum(month_date[:a-1]) + b + 5

    return day_name[(day_count % 7)-1]


