from django.shortcuts import render, redirect
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    # input number
    input = list();
    for i in range(0,6):
        number = request.GET['number'+str(i+1)]
        # if number is null, redirect home.html
        if number == '':
            return redirect('home')
        input.append(int(number))
 
    # random number
    rand_num = list() 
    for i in range(0,7):
        rand = random.randrange(1,46)
        while rand in rand_num:
            rand = random.randrange(1,46)
        rand_num.append(rand)

    # count same number
    count=0
    for i in range(0,6):
        for j in range(0,7):
            if input[i]==rand_num[j]:
                count+=1

    return render(request, 'result.html', {'rand_num':rand_num, 'input':input, 'count':count })