from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):

    return render(request, 'home.html')

def count(request):

    text = request.GET['fulltext']
    word_list = text.split()
    word_dict = {}

    for word in word_list:
        if word.lower() not in word_dict:
            word_dict[word.lower()] = 1
        else:
            word_dict[word.lower()] += 1
    
    sorted_list = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = True)
   

    return render(request, 'count.html', {'sorted_list':sorted_list, 'count_letters':len(word_list), 'text':text})

def about(request):

    return render(request, 'about.html')
