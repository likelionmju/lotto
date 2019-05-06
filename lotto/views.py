from django.shortcuts import render, redirect
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    # input number
    number_list = list()
    for i in range(0,6):
        number = request.GET['number'+str(i+1)]
        # if number is null, redirect home.html
        if number == '':
            return redirect('home')
        number_list.append(int(number))
 
    # random number
    rand_list = list() 
    for i in range(0,7):
        rand = random.randrange(1,46)
        # when rand in rand_list
        while rand in rand_list:
            rand = random.randrange(1,46)
        rand_list.append(rand)

    # count same number
    count=0
    for i in range(0,6):
        for j in range(0,7):
            if number_list[i]==rand_list[j]:
                count+=1

    return render(request, 'result.html', {'number_list':number_list, 'rand_list':rand_list, 'count':count })