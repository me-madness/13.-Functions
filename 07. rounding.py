rounding = input().split()
new_list = [eval(i) for i in rounding]
map_new_list = map(round, new_list)     
print(list(map_new_list))
