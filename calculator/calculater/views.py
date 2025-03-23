from django.shortcuts import render


def calc(request):
    ans=''
    try:
        if request.method == "POST" :
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                ans=n1+n2
            elif opr=="-":
                ans=n1-n2
            elif opr=="*":
                ans=n1*n2
            elif opr=="/":
                ans=n1/n2

        print(ans)

    except:
        ans="invalid oprations"
    return render(request,"calc.html",{'ans':ans})