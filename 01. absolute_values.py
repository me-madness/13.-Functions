value_list = input().split()
new_value = [eval(i) for i in value_list]
absolute_values = map(abs, new_value)
print(list(new_value))
