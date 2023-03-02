# Задача: В ячейке ниже представлен код генерирующий DataFrame, которая
# состоит всего из 1 столбца.Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# import random
# import pandas as pd
#
# list = ['robot'] * 10
# list += ['human'] * 10
#
# random.shuffle(list)
#
# def list_1(slovo):
#   arr = []
#   for i in range(len(list)):
#     if list[i] == slovo:
#       arr.append(1)
#     else:
#       arr.append(0)
#   return arr
#
# data = pd.DataFrame({'whoAmI':list, 'robot':list_1('robot'), 'human':list_1('human')})
# print(data.head(10))

