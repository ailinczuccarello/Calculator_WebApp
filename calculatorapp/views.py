from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'home.html')

def result(request): 

    num1 = request.GET.get('number1')
    num2 = request.GET.get('number2')

    if not num1 or not num2:
        ans = "Please insert both numbers :)"
        
    else:
        num1=int(num1)
        num2=int(num2)

        if request.GET.get('add') == "": ans = num1 + num2

        elif request.GET.get('subtract') == "":
            ans = num1 - num2

        elif request.GET.get('multiply') == "":
            ans = num1 * num2

        else: 
            ans = num1 / num2

    return render(request, 'result.html', {'ans': ans})