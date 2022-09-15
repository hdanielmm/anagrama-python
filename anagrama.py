my_array = [1,3,5,2,1,1,1,3,5,2,1,2]

my_array_ordered = sorted(my_array)
print(my_array_ordered)

my_list = [1,2,3,4,5]

for i in my_list:
    asteriscos = ''
    for j in my_array_ordered:
        if i == j:
            asteriscos += '*'
    print(str(i) + ': ' + asteriscos)
