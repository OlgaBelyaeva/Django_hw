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


def dish_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    dishes = {dish: {key: value * servings for key, value in ingred.items()} for dish, ingred in DATA.items()}
    reciep = dishes.get(dish)
    context = {
        'reciep': reciep
    }
    return render(request, template_name, context)