import pandas as pd
import json
from pprint import pprint
# Открываем файл и связываем его с объектом "f"
with open('read_files/recipes.json') as f:
    recipes = json.load(f) # Загружаем содержимое открытого файла в переменную recipes
#узнаем к-во ингредиентов в первом блюде
#pprint(len(recipes[0]['ingredients']))
#К какой кухне относится блюдо с id = 13121?
for recipe in recipes:
    if recipe['id']  == 13121:
        print(recipe['cuisine'])
        break
      
#Какое количество уникальных национальных кухонь присутствуют в нашем наборе данных?
cuisines = []
for recipe in recipes:
    if not(recipe['cuisine'] in cuisines):
        cuisines.append(recipe['cuisine'])
#print(len(cuisines))

#СОЗДАНИЕ DATAFRAME ИЗ JSON(ОН ВЫГЛЯДИТ НЕ КАК ТАБЛИЦА, НО МОЖНО ПЕРЕДЕЛАТЬ В НЕЕ)
df = pd.read_json('read_files/recipes.json')
#print(df.info()) # такой вид не очень интересен, так как ингредиенты находятся списком. Нужносделать их по столбцам.
#чтобы это сделать:Создадим функцию для заполнения значения в каждой ячейке.
#Функция будет проверять наличие конкретного ингредиента в столбце ingredients для текущего блюда
#и возвращать 1, если ингредиент есть в рецепте, и 0, если он отсутствует.
all_ingredients = set() # Создаем пустое множество для хранения реестра уникальных ингредиентов
for recipe in recipes: # Начинаем перебор всех блюд входящих в список
    for ingredient in recipe['ingredients']: # Начинаем перебор всех ингредиентов, входящих в состав текущего блюда
        all_ingredients.add(ingredient) # Добавляем уникальный ингредиент в реестр
def contains(ingredient_list): # Определяем имя функции и передаваемые аргументы
    if ingredient_name in ingredient_list: # Если ингредиент есть в текущем блюде,
        return 1 # возвращаем значение 1
    else: # Если ингредиента нет в текущем блюде,
        return 0 # возвращаем значение 0
for ingredient_name in all_ingredients: # Последовательно перебираем ингредиенты в реестре all_ingredients
    # В DataFrame cоздаем столбец с именем текущего ингредиента и заполняем его единицами и нулями
    df[ingredient_name] = df['ingredients'].apply(contains)
df['ingredients'] = df['ingredients'].apply(len) # Заменяем список ингредиентов в рецепте на их количество 
df.to_csv('read_files/recipes.csv', index = False)


                                #ПЕРЕВОД ИЗ PANDAS В JSON (обратная процедура)
import pandas as pd
df = pd.read_csv('recipes.csv') # Читаем содержимое файла и создаем объект df
ids = list(df['id'].unique()) # Создаем список уникальных значений id-блюд
ingredients = list(df.columns)[3:] # Создаем список уникальных значений ингредиентов
new_recipes = [] # Создаём пустой список для хранения итоговой структуры
for current_id in ids: # Организуем цикл с параметром current_id
    cuisine = df[df['id'] == current_id]['cuisine'].iloc[0] # Получаем значение соответствующей кухни, применив фильтр по текущему значению параметра цикла к DataFrame;
    current_ingredients = make_list(df[df['id'] == current_id]) # Получаем перечень ингредиентов, входящих в состав текущего блюда
    current_recipe = {'cuisine': cuisine, 'id': int(current_id), 'ingredients': current_ingredients} # Создаём текущий словарь
    new_recipes.append(current_recipe) # Добавляем созданный словарь к списку
def make_list(row): # Определяем имя функции и передаваемые аргументы
    ingredient_list=[] # Создаём пустой список ингредиентов текущего блюда
    for ingredient in ingredients: # Последовательно перебираем ингредиенты из реестра
        if row[ingredient].item()==1: # Если текущий ингредиент входит в состав текущего блюда
            ingredient_list.append(ingredient) # Добавляем ингредиент в список ингредиентов текущего блюда
    return ingredient_list # Возвращаем сформированный список ингредиентов
import json # Импорт модуля json
new_recipes = json.dumps(new_recipes) # Функция dumps() модуля json сериализирует объект Python в строку формата JSON. 
with open("data/new_recipes.json", "w") as write_file: # Откроем файл new_recipes.json для записи
    write_file.write(new_recipes) # Записываем содержимое подготовленные данные в файл