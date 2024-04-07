from django.shortcuts import render,get_object_or_404,redirect
from .models import Admin_Details
from .models import Product
from User.models import User_Order

def Admin_Login(request):
    # Admin_Create = Admin_Details.objects.create(Username='admin@123',Password='admin@123') 
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        print(Username)
        print(Password)
        if(Username and Password):
            Admin_Cridentials = Admin_Details.objects.all()
            for cradential in Admin_Cridentials:
                if cradential.Username == Username and cradential.Password == Password:
                    return redirect('../Admin_Dashboard/')
                else:
                     return render(request, 'Admin Login.html')
        else:
            return render(request, 'Admin Login.html')
    else:                
        return render(request, 'Admin Login.html')
    
def Admin_Dashboard(request):
    Grand_total = 0
    Order_data = User_Order.objects.all()
    Revenue = User_Order.objects.values_list('grand_Total')
    for price in Revenue:
        Grand_total += int(price[0])
    context = {'Order_items' : Order_data,'Total_Order': len(Order_data),'Grand_Total':Grand_total}
    return render(request, 'Admin dashboard.html',context)

def Admin_Menu(request):
    Grand_total = 0
    Order_data = User_Order.objects.all()
    Revenue = User_Order.objects.values_list('grand_Total')
    for price in Revenue:
        Grand_total += int(price[0])
    Menu_items = Product.objects.all()
    context = {'Menu_items':Menu_items,'Total_Order': len(Order_data),'Grand_Total':Grand_total}
    return render(request, 'Admin menu.html',context)

def Admin_Order(request):
    Grand_total = 0
    Order_data = User_Order.objects.all()
    Revenue = User_Order.objects.values_list('grand_Total')
    for price in Revenue:
        Grand_total += int(price[0])
    context = {'Order_items' : Order_data,'Total_Order': len(Order_data),'Grand_Total':Grand_total}
    return render(request, 'Admin order.html',context)

def Add_Menu(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        price = request.POST.get('item_price')
        image = request.POST.get('item_image')
        category = request.POST.get('item_category')   
        Product.objects.create(name=name, price=price, image=image, category=category)
        return redirect('../Admin_Menu') 

    else:
        return render(request, 'Add Menu.html')
    
def Update_Menu(request):
    item_name = request.GET.get('item_name')
    if(request.method == 'POST'):
        name = request.POST.get('item_name')
        price = request.POST.get('item_price')
        image = request.POST.get('item_image')
        category = request.POST.get('item_category')
        Menu_item = Product.objects.get(name=item_name)
        Menu_item.name = name
        Menu_item.price = price
        Menu_item.image = image
        Menu_item.category = category
        Menu_item.save()
        return redirect('../Admin_Menu')
    else:
        items = get_object_or_404(Product,name = item_name)  
        context = {'items' : items }
        return render(request, 'Update Menu.html', context)

def Delete_Menu(request):
    item_name = request.GET.get('item_name')
    if(request.method == "POST"):
        Menu_item = Product.objects.get(name=item_name)
        Menu_item.delete()
        return redirect('../Admin_Menu')
    else:
        context = {'item_name':item_name}
        return render(request, 'Delete Menu.html', context)