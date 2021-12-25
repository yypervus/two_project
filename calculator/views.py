import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def hello(request):
    current_time = datetime.datetime.now()
    msg = f'Привет, текущее время: {current_time}'
    return HttpResponse(msg)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def create_dishes(request, a):
    recipes_dishes = 'calculator/index.html'
    n = int(request.GET.get('servings', 1))

    if a == 'omlet':
        context = {
        'recipe': {
            'яйца, шт': round((2 * n), 1),
            'молоко, л': round((0.1 * n), 1),
            'соль, ч.л.': round((0.5 * n), 1),
        }
        }
        return render(request, recipes_dishes, context)
    elif a == 'pasta':
        context = {'recipe': {
            'макароны, г': round((0.3 * n), 1),
            'сыр, г': round((0.05 * n), 1),
        }
        }
        return render(request, recipes_dishes, context)
    elif a == 'buter':
        context = {'recipe': {
            'хлеб, ломтик': 1 * n,
            'колбаса, ломтик': 1 * n,
            'сыр, ломтик': 1 * n,
            'помидор, ломтик': 1 * n,
        }
        }
        return render(request, recipes_dishes, context)
    else:
        context = {}
        return render(request, recipes_dishes, context)



