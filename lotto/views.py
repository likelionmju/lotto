from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    # input number
    input = list();
    for i in range(0,6):
        input.append(int(request.GET['number'+str(i+1)]))

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