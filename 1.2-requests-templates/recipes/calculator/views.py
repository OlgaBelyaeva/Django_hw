from django.shortcuts import render

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

print(DATA.items())

# ЗАМЕНИТЬ РЕЦЕПТ НА ССЫЛКУ НА РЕЦЕПТ БЛЮДА В ПЕРЕМЕННОЙ DATA
# СДЕЛАТЬ УМНОЖЕНИЕ НА КОЛИЧЕСТВО БЛЮД ЧЕРЕЗ ДИКТ КОМПРЕХЕНШЕН
def omlet_viev(request):
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/omlet.html'
    recipe = {DATA['omlet']}
    # {
    #     'omlet': {
    #     'яйца, шт': servings * 2,
    #     'молоко, л': servings * 0.1,
    #     'соль, ч.л.': servings * 0.5,
    # }
    # }
    return render(request, template_name, context=recipe)

def pasta_viev(request):
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/pasta.html'
    recipe = {
        'pasta': {
        'макароны, кг': servings * 0.3,
        'сыр, кг': servings * 0.05,
    }
    }
    return render(request, template_name, context=recipe)

def buter_viev(request):
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/buter.html'
    recipe = {
        'buter': {
            'хлеб, ломтик': servings * 1,
            'колбаса, ломтик': servings * 1,
            'сыр, ломтик': servings * 1,
            'помидор, ломтик': servings * 1,
    }
    }
    return render(request, template_name, context=recipe)

# РАЗОБРАТЬСЯ ПОЧЕМУ index.html НЕ СРАБАТЫВАЕТ, ГДЕ-ТО ОН НЕ ПОДВЯЗАЛСЯ
# ЕЩЕ ДВЕ ФУНКЦИИ ДЛЯ ДРУГИЗ РЕЦЕПТОВ


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
