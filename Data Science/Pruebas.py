medical_cost = {}
medical_cost['Marina'] = 6607.0
medical_cost['Vinay'] = 3225.0
medical_cost.update({'Connie': 8886.0, 'Issac': 16444.0, 'Valentina': 6420.0})
print(medical_cost)
medical_cost['Vinay'] = 3325.0
print(medical_cost)

total_cost = 0
for cost in medical_cost.values():
    total_cost += cost
average_cost = total_cost/len(medical_cost)
print(f'\nAverage Insurance Cost: ${average_cost:.2f}\n')

names = ['Marina', 'Vinay', 'Connie', 'Issac', 'Valentina']
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)

names_to_ages = {name: age for name, age in zipped_ages}
print(names_to_ages)
marina_age = names_to_ages.get('Marina', None)
print(marina_age)
print()

medical_records = {}
medical_records['Marina'] = {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2,
                             'Smoker': 'Non-smoker', 'Insurance_cost': 6607.0}
medical_records['Vinay'] = {'Age': 24, 'Sex': 'Male', 'BMI': 26.9, 'Children': 0,
                             'Smoker': 'Non-smoker', 'Insurance_cost': 3225.0}
medical_records['Connie'] = {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3,
                             'Smoker': 'Non-smoker', 'Insurance_cost': 8886.0}
medical_records['Isaac'] = {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4,
                             'Smoker': 'Smoker', 'Insurance_cost': 16444.0}
medical_records['Valentina'] = {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1,
                             'Smoker': 'Non-smoker', 'Insurance_cost': 6420.0}
print(medical_records)

print(f'Connie\'s insurance cost is: {medical_records["Connie"]["Insurance_cost"]: .2f} dollars')
print(f'Isaac\'s insurance cost is: {medical_records["Isaac"].get("Insurance_cost", 5500.0): .2f} dollars')
medical_records.pop('Vinay')
print()

for name, data in medical_records.items():
    print(f'{name} is a {data["Age"]} years old {data["Sex"]} {data["Smoker"]} with a BMI of {data["BMI"]}'
          f' and insurance cost of{data["Insurance_cost"]: .2f}.')

def update_medical_records_by_sex(individual, medical_data):
    new_pacient_record = {}
    new_pacient_record[individual] = medical_data
    if medical_data['Sex'] == 'Male':
        medical_data['Insurance_cost'] += 500
    return new_pacient_record

abelardo_data = update_medical_records_by_sex('Abelardo', {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4,
                             'Smoker': 'Smoker', 'Insurance_cost': 16444.0})
print(abelardo_data)
print()

def discount_female(dict):
    for name, record in dict.items():
        if record['Sex'] == 'Female':
            record['Insurance_cost'] -= 500
    return dict
discount_female(medical_records)
print(medical_records)