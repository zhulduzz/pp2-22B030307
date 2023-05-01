import csv

#username,telephone_number,city,age
row_1 = ['Erick', '+120444000354', 'Canada', '23']
row_2 = ['Emily', '+46766920093', 'Sweden', '45']
row_3 = ['Malik', '+442033188305', 'United Kingdom', '34']

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(row_1)
    writer.writerow(row_2)
    writer.writerow(row_3)
