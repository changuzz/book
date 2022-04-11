from django.shortcuts import render
from django.views.generic import View
from calculation.forms import OperationForm
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,"home.html")


class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result = int(n1)+int(n2)
            return render(request, "add.html", {"result": result})
            return render(request,"add.html")
        else:
            return render(request, "add.html",{"form":form})
def add(request):
    print(request.method)
    if request.method == 'POST':
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1+n2
        return render(request,"add.html",{"result":result})
    return render(request,"add.html")


class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = int(n1) - int(n2)
            return render(request, "sub.html", {"result": result})
            return render(request,"sub.html")
        else:
            return render(request, "sub.html", {"form": form})

def sub(request):
    if request.method == 'POST':
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1-n2
        return render(request,"sub.html",{"result":result})
    return render(request,"sub.html")


class MulView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"mul.html",{"form":form})
    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = int(n1) * int(n2)
            return render(request, "mul.html", {"result": result})
            return render(request,"mul.html")
        else:
            return render(request, "mul.html", {"form": form})
def mul(request):
    if request.method == 'POST':
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1*n2
        return render(request,"mul.html",{"result":result})
    return render(request,"mul.html")


class DivView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"div.html",{"form":form})
    def post(self, request):
        # n1 = int(request.POST.get("num1"))
        # n2 = int(request.POST.get("num2"))
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = int(n1) / int(n2)
            return render(request, "div.html", {"result": result})
            return render(request,"div.html")
        else:
            return render(request, "add.html", {"form": form})
def div(request):
    if request.method == 'POST':
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        result=n1/n2
        return render(request,"div.html",{"result":result})
    return render(request,"div.html")


def getvowels(request):
    if request.method == 'POST':
        word=request.POST.get("word")
        vowels=[char for char in word if char in ["a","e","i","o","u"]]
        return render(request,"getvow.html",{"result":vowels})
    return render(request,"getvow.html")

# def primenumber(request):
#     if request.method=="POST":
#         result=[]
#         n1 = int(request.POST.get("num1"))
#         n2 = int(request.POST.get("num2"))
#         if n1<=0 or n2<=0:
#             result.append("invalid limit")
#         else:
#             for i in range(n1,n2+1):
#                 for j in range(2,1):
#                     if i==1 or i==2:
#                         result.append(i)
#                     elif i%j==0:
#                         break
#                 else:
#                     result.append(i)
#             return render(request,'pimenumber.html',{"result":result})
#     return render(request,'primenumber.html')

