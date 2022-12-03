# ''' Get array dimensions '''
dimension = int(input("Define your square dimensions: "))


# ''' Make square array '''
user_numbers_list = []
row = []

for i in range(dimension ** 2):
    if len(row) != dimension:
        row.append(input("Enter your numbers: "))
        if len(row) == dimension:
            user_numbers_list.append(row)
            row = []


# ''' Convert blanks to 0 and strings to integers '''
for row in user_numbers_list:
    for number in range(len(row)):
        if row[number] == '':
            row[number] = 0
        else:
            row[number] = int(row[number])


# ''' Print array '''
print('')
for i in user_numbers_list:
    print(i)


#   ''' Get the total of main axis '''
main_axis = 0
row = 0

for i in user_numbers_list:
    main_axis += i[row]
    row += 1

#   ''' Get the total of side axis '''
side_axis = 0
row = dimension - 1

for i in user_numbers_list:
    side_axis += i[row]
    row -= 1

#   ''' Print the results '''
print(f'\nmain_axis: {main_axis}')
print(f'side_axis: {side_axis}')
print(f'total: {abs(main_axis - side_axis)}')
