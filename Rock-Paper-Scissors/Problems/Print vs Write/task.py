numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
f = open('file_with_list.txt', 'w')
print(numbers, end="", file=f)
f.close()
