import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views':56},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views':120},
        {'title':'Simple And Interesting Exercises About Python',
        'url':'https://hourofpython.com/',
        'views':198},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'views':77} ]
        
    java_pages = [
        {'title': 'Explanation of Java on Wikipedia',
        'url':'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'views':182},
        {'title':'There Is Everything You Want To Know About Java',
        'url':'http://www.onjava.com/',
        'views':487},
        {'title':'Java SE Technical Documentation',
        'url':'http://docs.oracle.com/javase/8/',
        'views':56},
        {'title':'Rich Java Examples',
        'url':'http://www.javaworld.com/',
        'views':95} ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':87},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views':7},
        {'title': 'How To Tango With Django',
         'url': 'http://www.tangowithdjango.com/',
         'views':129}]

    cProgramming_pages = [
        {'title': 'C Programming Tutorial for Beginners',
        'url': 'https://www.youtube.com/watch?v=KJgsSFOSQv0',
        'views':875},
        {'title': '"C" Programming Language: Brian Kernighan - Computerphile',
        'url': 'https://www.youtube.com/watch?v=de2Hsvxaf8M',
        'views':23},
        {'title': 'Pointers In C',
        'url': 'https://www.youtube.com/watch?v=mw1qsMieK5c',
        'views':75},
        {'title': 'Learn C Programming in 10 Hours',
        'url': 'https://www.youtube.com/watch?v=Bz4MxDeEM6k',
        'views':84}]

    sql_pages = [
        {'title': 'SQL Skills',
        'url': 'https://www.sqlskills.com/',
        'views':19},
        {'title': 'SQL Server Central',
        'url': 'https://www.sqlservercentral.com/',
        'views':12},
        {'title': 'SQL Magazine',
        'url': 'https://www.itprotoday.com/',
        'views':498}]

    cpp_pages = [
        {'title': 'C++ Tutorial For Beginners',
        'url': 'https://www.youtube.com/watch?v=vLnPwxZdW4Y',
        'views':67},
        {'title': 'Where Is C++ Being Used',
        'url': 'https://www.youtube.com/watch?v=UdTzHmjMYBc',
        'views':473},
        {'title': 'Learn C++ Pointers In 2.5 Hours',
        'url': 'https://www.youtube.com/watch?v=kiUGf_Z08RQ',
        'views':29},
        {'title': 'How To Really Learn C++',
        'url': 'https://www.youtube.com/watch?v=_zQqN5OYCCM',
        'views':90}]

    js_pages = [
        {'title': 'Study JavaScript Here!',
        'url': 'http://thecodeplayer.com',
        'views':34},
        {'title': 'Build 30 Things In 30 Days With 30 Tutorials',
        'url': 'https://javascript30.com/c',
        'views':369},
        {'title': 'JavaScript Memory Management',
        'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management',
        'views':9},
        {'title': 'JavaScript Event Loop',
        'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop',
        'views':90}]

    php_pages = [
        {'title': 'PHP Community',
        'url': 'https://phpcommunity.org/',
        'views':34},
        {'title': 'Everything About PHP Developer',
        'url': 'http://www.phpdeveloper.org/',
        'views':369},
        {'title': 'PHP Forum',
        'url': 'http://www.php-forum.com/phpforum/',
        'views':9}]

    practice_pages = [
        {'title': 'Learn To Code',
        'url': 'https://www.sololearn.com/home',
        'views':39},
        {'title': 'Free Code Camp',
        'url': 'https://www.freecodecamp.org/',
        'views':49},
        {'title': 'Codewars',
        'url': 'https://www.codewars.com',
        'views':49},
        {'title': 'CodeFights',
        'url': 'https://app.codesignal.com/',
        'views':49},
        {'title': 'Practice Web Technologies Online',
        'url': 'https://www.w3schools.com/',
        'views':597}]

    cats = {'C Programming': {'pages': cProgramming_pages, 'views':288, 'likes':356},
            'Python': {'pages': python_pages, 'views':256, 'likes':302},
            'Java': {'pages': java_pages, 'views':204, 'likes':208},
            'C++': {'pages': cpp_pages, 'views':197, 'likes':199},
            'JavaScript': {'pages': js_pages, 'views':165, 'likes':176},
            'PHP': {'pages': php_pages, 'views':146, 'likes':168},
            'SQL': {'pages': sql_pages, 'views':137, 'likes':154},
            'Django': {'pages': django_pages, 'views':87, 'likes':132},
            'Websites For Practice': {'pages': practice_pages, 'views':64, 'likes':45}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__=='__main__':
    print('Starting Rango population script...')
    populate()
