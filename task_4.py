user_str = list(input('Введите строку, состоящую из нескольких слов: ').split())
user_dict = dict()
for i in range(len(user_str)):
    user_dict[i] = user_str[i]

for key, value in user_dict.items():
    print(f'{key}  {value[0:10]}')
