# x = [[3], [1, 2, 3], [2, 4]]
# x = [[3], [1, 2, 3], [2, 4], [5, 1]]
x = [[3], [1, 2, 3], [2, 4], [5, 1], [1, 0, 2, 0, 8]]

#   ''' Make a square array '''
for i in x:
    if len(i) != 5:
        for j in range(5 - len(i)):
            i.append(0)
    print(i)

#   ''' Get the total of main axis '''
main_axis = 0
row = 0

for i in x:
    main_axis += i[row]
    row += 1

#   ''' Get the total of side axis '''
side_axis = 0
row = 4

for i in x:
    side_axis += i[row]
    row -= 1

#   ''' Print the results '''
print(f'\nmain_axis: {main_axis}')
print(f'side_axis: {side_axis}')
print(f'total: {abs(main_axis - side_axis)}')
