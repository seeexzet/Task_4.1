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
}

def omlet(request):
    servings = int(request.GET.get("servings",1))
    omlet_data = DATA.get('omlet')
    if servings != 1:
        omlet_data.update({'яйца, шт': omlet_data.get('яйца, шт') * servings})
        omlet_data.update({'молоко, л': omlet_data.get('молоко, л') * servings})
        omlet_data.update({'соль, ч.л.': omlet_data.get('соль, ч.л.') * servings})

    context = { 'recipe': omlet_data }
    print(context)
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get("servings",1))
    pasta_data = DATA.get('pasta')
    if servings != 1:
        pasta_data.update({'макароны, г': pasta_data.get('макароны, г') * servings})
        pasta_data.update({'сыр, г': pasta_data.get('сыр, г') * servings})

    context = {'recipe': pasta_data }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get("servings",1))
    buter_data = DATA.get('buter')
    if servings != 1:
        buter_data.update({'хлеб, ломтик': buter_data.get('хлеб, ломтик') * servings})
        buter_data.update({'колбаса, ломтик': buter_data.get('колбаса, ломтик') * servings})
        buter_data.update({'сыр, ломтик': buter_data.get('сыр, ломтик') * servings})
        buter_data.update({'помидор, ломтик': buter_data.get('помидор, ломтик') * servings})

    context = {'recipe': buter_data }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
