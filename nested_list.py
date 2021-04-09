

students = [['Harry', 37.21], ['Berry', 37.2], ['Tina', 37.21], ['Akriti', 41], ['Harsh', 39]]
print(students)

lowest_score = min(students, key=lambda x: x[1])
print(lowest_score[1])

next_lowest = set([x[1] for x in students])
next_lowest.remove(min(next_lowest))
second_lowest = (min(next_lowest))

pre_string = sorted([x[0] for x in students if x[1] == second_lowest])
post_string = '\n'.join(pre_string)
print(post_string)


#print(min([x for x in students if x[1] != lowest_score[1]], key=lambda x: x[1]))

'''
my_list = [1,2,3,4,9,9]
new_list = set(my_list)
new_list.remove(max(new_list))
print(max(new_list))
'''




