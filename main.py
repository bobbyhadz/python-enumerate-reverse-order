# Iterate over a List in reverse order with Index

my_list = ['a', 'b', 'c', 'd']


for index, item in reversed(list(enumerate(my_list))):
    print(index, item)  # 👉️ 3 d 2 c 1 b 0 a