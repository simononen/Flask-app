grades = [77, 80, 90, 95, 100]
tuple_grades = (77, 80, 90, 95, 107, 108, 109)
set_grades = {77, 80, 99, 100}

# print(sum(grades) / len(grades))

grades.append(108)
tuple_grades = tuple_grades + (100,)

grades[0] = 50
set_grades.add(60)
set_grades.add(61)
set_grades.add(61)
# print(set_grades)

your_lottery_numbers = {1, 2, 3, 4, 5, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# print(your_lottery_numbers.intersection(winning_numbers))
# print(your_lottery_numbers.union(winning_numbers))
# print({1, 2, 3, 4}.difference({1, 2}))

my_list = [20, 30, 50]

# print(sum(my_list))

my_tuple = (5,)

# print(my_tuple)

set1 = {14, 5, 9, 51, 12, 77, 67, 4}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))
