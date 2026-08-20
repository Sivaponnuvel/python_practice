def calculate_average(marks):
    total_mark = 0
    for i in marks:
        total_mark += i
    return total_mark / len(marks)

def find_highest(marks):
    max_mark = marks[0]
    for i in marks:
        if i > max_mark:
            max_mark = i
    return max_mark

def find_lowest(marks):
    min_mark = marks[0]
    for i in marks:
        if i < min_mark:
            min_mark = i
    return min_mark

