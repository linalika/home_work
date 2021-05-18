staff_dict = {}
count = 1
sername_with_salary_more_20 = []
all_staff_salary = 0
count_staff = 0

with open("task_3.txt", "r") as f:
    for line in f:
        staff = line.replace(',', ' ').split(' ')
        staff_dict[staff[0]] = int(staff[1])

for i in staff_dict:
    all_staff_salary += staff_dict[i]
    count_staff += 1
    if staff_dict[i] > 20:
        sername_with_salary_more_20.append(i)

average_salary = all_staff_salary / count_staff

print(f'Сотрудники с зарплатой больше 20  - {" ".join(sername_with_salary_more_20)}')
print(f'Средняя зарплата всех сотрудников - {average_salary}')
