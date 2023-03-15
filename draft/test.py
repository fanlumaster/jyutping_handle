import os.path

file_path = os.path.join(os.path.dirname(__file__), 'test.txt')

with open(file_path, 'rb+') as myfile:
    contents = myfile.read().decode()
    c = '0'
    count = 0
    for cur in contents:
        if cur != c:
            print('fany full')
            break
        print(cur)
        if c == '0':
            c = '1'
        else:
            c = '0'
        count += 1

print(count)
