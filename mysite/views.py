from django.http import HttpResponse
from django.shortcuts import render
import datetime
import statistics
from school.models import Student, Car, Foto


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'

    return render(request, 'hello.html', context)


def time(request):
    context = {}
    context['now'] = datetime.datetime.now()

    return render(request, 'time.html', context)


def time_plus(request, offset):
    offset = int(offset)
    context = {}
    context['offset'] = offset
    context['dt'] = datetime.datetime.now()+datetime.timedelta(hours=offset)

    return render(request, 'time_plus.html', context)


def students(request):
    studentFam = ['Кудінов', 'Семчук', 'Доронін', 'Сорба', 'Прокопів', 'Зозуляк', 'Постернак', 'Німий', 'Іващук', 'Павлюс', 'age']
    studentName = ['Ігор', 'Андрій', 'Діма', 'Стас', 'Соломія', 'Богдан', 'Володимир', 'Ігор', 'Олена', 'Роман']
    students = dict(zip(studentFam, studentName))

    context = {
        'students': students,
        'h1': 'Список учнів класу',
    }

    return render(request, 'students.html', context)


def products(request):
    towar = ['Кава', 'Хліб', 'Огірки', 'Чай', 'Картопля', 'Сметана', 'Цукор', 'Молоко', 'Риба', 'Капуста']
    price = [45, 4.5, 6.5, 12, 3, 9.8, 10, 8.5, 38, 2.5]
    products = dict(zip(towar, price))
    ser_a = statistics.mean(products.values())

    context = {
        'products': products,
        'ser_a': ser_a,
    }

    return render(request, 'products.html', context)


def progress(request):
    name = ['Анна', 'Віта', 'Катя', 'Марія', 'Микола', 'Олександр', 'Петро', 'Роман', 'Христина', 'Ярослав']
    ukr = [9, 4, 11, 7, 10, 8, 10, 11, 9, 8]
    ang = [8, 7, 10, 8, 10, 9, 10, 12, 10, 10]

    value = [name, ukr, ang]
    
    zagolovki = ['№', "Ім'я", "Укр.мова", "Англ.мова", "С/Б"]

    ocinka = []
    progress = []
    sb_klas = []
    for i in range(len(name)):
        ocinka.append({'ukr': ukr[i], 'ang': ang[i]})
        progress.append({'name': name[i], 'ocinka': ocinka[i], 'sb': float(statistics.mean([value[1][i], value[2][i]]))})
        sb_klas.append(progress[i]['sb'])

    context = {
        'progress': progress,
        'zagolovki': zagolovki,
        'sb_klas': float(statistics.mean(sb_klas)),
    }

    return render(request, 'progress.html', context)


def informatic(request):
    name = ['Ірина', 'Василь', 'Галя', 'Григорий', 'Микола', 'Марія', 'Ольга', 'Петро', 'Олександр', 'Тарас']
    ocinka = [
        ['н', 11, '', 'н', 7, '', 6],
        [12, 'н', 8, 'н', 'н', 10, 10],
        [4, 5, '', 'н', 'н', 'н', 5],
        [9, '', '', '', '', 7, 'н'],
        [9, '', 8, 10, 10, 11, 12],
        [8, '', 'н', '', 4, 'н', 7],
        ['н', 'н', '', '', 6, '', ''],
        ['', 8, 8, 9, '', 'н', 7],
        ['н', 'н', 'н', '', 9, '', 7],
        [10, 10, 8, 'н', 11, 12, 9],
    ]
    
    zagolovki = ['№', "Ім'я", "1", "2", "3", "4", "5", "6", "7"]

    progress = []

    for i in range(len(name)):
        progress.append({'name': name[i], 'ocinka': ocinka[i]})

    context = {
        'progress': progress,
        'zagolovki': zagolovki,
    }

    return render(request, 'informatic.html', context)


def sinformatic(request):
    name = ['Ірина', 'Василь', 'Галя', 'Григорий', 'Микола', 'Марія', 'Ольга', 'Петро', 'Олександр', 'Тарас']
    ocinka = [
        ['н', 11, '', 'н', 7, '', 6],
        [12, 'н', 8, 'н', 'н', 10, 10],
        [4, 5, '', 'н', 'н', 'н', 5],
        [9, '', '', '', '', 7, 'н'],
        [9, '', 8, 10, 10, 11, 12],
        [8, '', 'н', '', 4, 'н', 7],
        ['н', 'н', '', '', 6, '', ''],
        ['', 8, 8, 9, '', 'н', 7],
        ['н', 'н', 'н', '', 9, '', 7],
        [10, 10, 8, 'н', 11, 12, 9],
    ]

    sb = []
    real_sb = []
    for i in ocinka:
        for q in i:
            if q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                sb.append(q)
        i.append(round(statistics.mean(sb), 1))
        real_sb.append(statistics.mean(sb))
        sb.clear()
    del sb

    real_sb = round(statistics.mean(real_sb), 1)
    
    zagolovki = ['№', "Ім'я", "1", "2", "3", "4", "5", "6", "7", "С/Б"]

    progress = []

    for i in range(len(name)):
        progress.append({'name': name[i], 'ocinka': ocinka[i]})

    context = {
        'progress': progress,
        'zagolovki': zagolovki,
        'sb': real_sb,
    }

    return render(request, 'sinformatic.html', context)


def propusk(request):
    name = ['Ірина', 'Василь', 'Галя', 'Григорий', 'Микола', 'Марія', 'Ольга', 'Петро', 'Олександр', 'Тарас']
    ocinka = [
        ['н', 11, '', 'н', 7, '', 6],
        [12, 'н', 8, 'н', 'н', 10, 10],
        [4, 5, '', 'н', 'н', 'н', 5],
        [9, '', '', '', '', 7, 'н'],
        [9, '', 8, 10, 10, 11, 12],
        [8, '', 'н', '', 4, 'н', 7],
        ['н', 'н', '', '', 6, '', ''],
        ['', 8, 8, 9, '', 'н', 7],
        ['н', 'н', 'н', '', 9, '', 7],
        [10, 10, 8, 'н', 11, 12, 9],
    ]

    sb = list()
    prop = int()
    for i in ocinka:
        for q in i:
            if q == "н":
                sb.append(q)
        i.append(len(sb))
        prop += len(sb)
        sb.clear()
    del sb
    
    zagolovki = ['№', "Ім'я", "1", "2", "3", "4", "5", "6", "7", "Проп."]

    progress = []

    for i in range(len(name)):
        progress.append({'name': name[i], 'ocinka': ocinka[i]})

    context = {
        'progress': progress,
        'zagolovki': zagolovki,
        'prop': prop,
    }

    return render(request, 'propusk.html', context)


def better(request):
    name = ['Ірина', 'Василь', 'Галя', 'Григорий', 'Микола', 'Марія', 'Ольга', 'Петро', 'Олександр', 'Тарас']
    ocinka = [
        ['н', 11, '', 'н', 7, '', 6],
        [12, 'н', 8, 'н', 'н', 10, 10],
        [4, 5, '', 'н', 'н', 'н', 5],
        [9, '', '', '', '', 7, 'н'],
        [9, '', 8, 10, 10, 11, 12],
        [8, '', 'н', '', 4, 'н', 7],
        ['н', 'н', '', '', 6, '', ''],
        ['', 8, 8, 9, '', 'н', 7],
        ['н', 'н', 'н', '', 9, '', 7],
        [10, 10, 8, 'н', 11, 12, 9],
    ]

    sb = []
    all_sb = []
    for i in ocinka:
        for q in i:
            if q in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                sb.append(q)
        i.append(round(statistics.mean(sb), 1))
        all_sb.append(round(statistics.mean(sb), 1))
        sb.clear()
    del sb

    max_sb = list()
    for i in range(3):
        max_sb.append(name[all_sb.index(max(all_sb))])
        all_sb[all_sb.index(max(all_sb))] = 0

    zagolovki = ['№', "Ім'я", "1", "2", "3", "4", "5", "6", "7", "С/Б"]

    progress = []

    for i in range(len(name)):
        progress.append({'name': name[i], 'ocinka': ocinka[i]})

    context = {
        'progress': progress,
        'zagolovki': zagolovki,
        'max_sb': max_sb,
    }

    return render(request, 'better.html', context)


def studentsView(request):
    all = Student.objects.all()

    context = {
        'h1': 'Список працівників та учнів школи',
        'students': all,
    }

    return render(request, "studentsView.html", context)


def uch(request):
    all=Student.objects.filter(post="учень")

    context = {
        'h1': 'Список учнів школи',
        'students': all,
    }

    return render(request, "uch.html", context)


def uch_rev(request):
    all=Student.objects.filter(post="учень")

    context = {
        'h1': 'Список учнів школи',
        'students': all,
    }

    return render(request, "uch_rev.html", context)


def uch_ost(request):
    all=Student.objects.filter(post="учень")[:12]

    context = {
        'h1': 'Список учнів школи',
        'students': all,
    }

    return render(request, "uch_ost.html", context)


def uch_find(request):
    post_lastname = ''
    if request.method == "POST" and len(request.POST.get("fam")) > 0:
        post_lastname = request.POST.get("fam")
        all = Student.objects.filter(lastname=post_lastname)
        if all.count() > 0:
            powid="Знайдено!"
        else:
            powid="Не знайдено!"
    else:
        all = Student.objects.filter(post="учень")
        powid = "Всі учні класу!"

    context = {
        'students': all,
        'p': powid,
        'text': post_lastname
        }

    return render(request, "uch_find.html", context)


def uch_add(request):
    all = Student.objects.all()
    if request.method == "POST":
        pers = Student()
        pers.lastname = request.POST.get("fam")
        pers.name = request.POST.get("nam")
        pers.post = request.POST.get("pos")
        if (pers not in all):
            pers.save()
        powid=str(pers.lastname)+" "+str(pers.name)+" "+str(pers.post)+" - додано!"
    else:
        powid="Всі учні класу!"

    context = {
        'students': all,
        'p': powid,
        }

    return render(request, "uch_add.html", context)


def auto(request):
    if request.method == "GET":
        n = request.GET.get('id')

    if n == None:
        n = 1

    menu = Car.objects.all()
    foto = Foto.objects.all().filter(id_car=n)

    del n

    context = {
        'menu': menu,
        'foto': foto,
        'logo': "Кращі автомобілі світу",
        }

    return render(request, "auto.html", context)


def no_urls(request):
    return HttpResponse("<h2>Таких url немає</h2>")

