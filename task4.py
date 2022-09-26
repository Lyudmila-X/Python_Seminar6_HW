#  Все равны как на подбор

def same_by (characteristic, objects):
    print(objects)
    result = [characteristic(item) for item in objects]
    return True if len(set(result)) == 1 else False

values = [0, 2, 10, 6]
if same_by(lambda x: x%0, values):
    print('same')
else:
    print('different')
