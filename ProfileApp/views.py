from django.shortcuts import render, redirect

from ProfileApp.forms import ProductForm
from ProfileApp.models import Product


# Create your views here.
def profile(request):
    return render(request,'profile.html')

def education(request):
    return render(request,'education.html')

def attention(request):
    return render(request,'attention.html')

def career(request):
    return render(request, 'career.html')

def idol(request):
    return render(request,'idol.html')

lstOurProduct = []

def listProduct(request):
    context = {'product':lstOurProduct}
    return render(request,'listProduct.html',context)

def showData(request):
    name = 'นายอันดา แก้วภู'
    nickname = 'ริว'
    id = '65342310191-3'
    age = '22'
    birthday = '22 กันยายน 2544'
    national = 'ไทย'
    address = 'บ้านโนนสง่า 10/6 ต.เมืองใหม่ อ.ศรีบุญเรือง จ.หนองบัวลำภู'
    hobby = 'ชอบฟังเพลง-เล่นเกม'
    food = 'ก๋วยเตี๋ยว'
    motto = 'นกที่ตื่นเช้า คือนกที่หิวข้าว'
    product = [
        ['MON-01','1 Monster Energy Reserve Orange Dreamsicle','35 ฿','/static/images/mon-1.webp'],
        ['MON-02', '2 Monster Energy Reserve Kiwi Strawberry', '35 ฿', '/static/images/mon-2.webp'],
        ['MON-03', '3 The Original Green Monster Energy', '35 ฿', '/static/images/mon-3.webp'],
        ['MON-04', '4 The Original Lo-Carb Monster Energy', '35 ฿', '/static/images/mon-4.webp'],
        ['MON-05', '5 NEW Zero Sugar Monster Energy', '45 ฿', '/static/images/mon-5.webp'],
        ['MON-06', '6 Monster Energy Reserve Watermelon', '55 ฿', '/static/images/mon-6.webp'],
        ['MON-07', '7 Monster Energy Reserve White Pineapple', '55 ฿', '/static/images/mon-7.webp'],
        ['MON-08', '8 Monster Energy Nitro Super Dry', '55 ฿', '/static/images/mon-8.webp'],
        ['MON-09', '9 Monster Energy Assault', '55  ฿', '/static/images/mon-9.webp'],
        ['MON-10', '10 The Original Monster Energy Super-Premium Import', '65 ฿', '/static/images/mon-10.webp'],
    ]
    context = {'name':name, 'nickname':nickname, 'id':id, 'age':age, 'birthday':birthday,
               'national':national, 'address':address, 'hobby':hobby, 'food':food,
               'motto':motto,'product':product}
    return render(request,'showData.html',context)

def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            brand = form.get('brand')
            model = form.get('model')
            screen = form.get('screen')
            size = form.get('size')
            pressure = form.get('pressure')
            weight = form.get('weight')
            price = form.get('price')
            amount = form.get('amount')

            sum = price * amount

            if sum < 1500:
                discount = sum * 5 / 100
            elif sum < 3000:
                discount = sum * 7 / 100
            else:
                discount = sum * 10 / 100

            total = sum - discount

            ProductList = Product(id,brand,model,screen,size,pressure,weight,price,amount)
            lstOurProduct.append(ProductList)
            return redirect('listProduct')

        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'inputProduct.html',context)