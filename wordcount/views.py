
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html', {'name' : 'venky'})

def count(request):
	w = request.GET['words']
	mylist = w.strip().split(' ')
	lsize = len(mylist)
	mydict = {}
	for i in mylist:
		if i not in mydict:
			mydict[i] = 1
		else:
			mydict[i] += 1
	max_count = 0
	for key in mydict:
		if mydict[key] > max_count:
			max_count = mydict[key]
			max_key = key
	print(mydict.items())
	return render(request, 'count.html', {'count' : lsize, 'text' : w, 'max' : max_key, 'cmax' : max_count})

def about(request):
	return render(request, 'about.html')