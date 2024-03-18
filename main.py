import json


def normalizing(val):
    standard_lower = ['firstname', 'lastname', 'department', 'salary']
    standard = ['firstName', 'lastName', 'department', 'salary']
    for i in range(0, len(standard)):
        if val.lower() == standard_lower[i].lower():
            return standard[i]


def employees_rewrite(sort_type):
    result = normalizing(sort_type)
    with open(file='employees.json', mode='r') as json_file:
        json_data = json.load(json_file)
        if result == 'salary':
            sort = sorted(json_data['employees'], key=lambda employee: employee[result], reverse=True)
        else:
            sort = sorted(json_data['employees'], key=lambda employee: employee[result])

    with open(file=f'my_employees_{sort_type}_sorted.json', mode='w') as file:
        json.dump(sort, file, indent=4)


employees_rewrite('firstNAME')
employees_rewrite('LASTNAME')
employees_rewrite('DEpartment')
employees_rewrite('salary')
# employees_rewrite('f_n')
