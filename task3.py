# пам-парам парам-пам парам
data = open("input3.txt", encoding='utf-8')
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
input_text = data.read()
def rhythm_check (input_text):
    phrases_list = list(map(str, input_text.lower().split(' ')))
    previous_count =  sum(map(lambda letter: letter in vowels, phrases_list[0]))
    for item in phrases_list:
        count = 0
        for j in item:
            if j in vowels:
                count+=1
        if count == previous_count:
            answer = 'Парам пам-пам'
        else:
            answer = 'Пам парам'    
    return answer
print (rhythm_check(input_text))
data.close
