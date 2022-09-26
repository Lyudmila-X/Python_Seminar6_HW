#  мимикрия
data = open("input1.txt", "r")
transformation = lambda x: x
values = list(map(lambda x:x, data.read().split(' ')))
transformed_values = list(map(transformation, values))
if values==transformed_values:
    print("ok")
else:
    print("fail")
data.close
