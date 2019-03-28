from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    # 입력한 값 받아오기
    input = list();
    for i in range(0,6):
        input.append(int(request.GET['number'+str(i+1)]))

    # 추첨
    rand_num = list() 
    for i in range(0,7):
        rand_num.append(random.randrange(1,47))

    # 맞춘 횟수
    count=0
    for i in range(0,6):
        for j in range(0,7):
            if input[i]==rand_num[j]:
                count+=1

    return render(request, 'result.html', {'rand_num':rand_num, 'input':input, 'count':count })