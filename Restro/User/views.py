from django.shortcuts import render,redirect,get_object_or_404
from .models import User_Register
from Admin.models import Product
from .models import User_Order

def get_username(req):
        username = req.session.get('username')
        if username:
                context = username
        else:
                context = 'Guest'
        return context

# Create your views here.
def Home(request):
        Logout = request.GET.get('Logout')
        if Logout:
                del request.session['username']

        
        items = Product.objects.all()
        context = {'username':get_username(request),'items' : items}
        return render(request, 'home.html', context)

def about(request):
        context = {'username' :  get_username(request)}
        return render(request, 'about.html', context)

def menu(request):
        if request.method == 'POST':
                item_name = request.POST.get('div_text')
                item_qty = request.POST.get('qty')
                current_item = {'item_name' : item_name,'item_qty' : item_qty}
                cart_items = request.session.get('cart_items')
                cart_items[item_name] = current_item
                request.session['cart_items'] = cart_items
                return redirect("../menu")
        else:
                items = Product.objects.all()
                context = {'username':get_username(request),'items' : items}
                return render(request,'menu.html' ,context)

def contact(request):
        context = {'username' :  get_username(request)}
        return  render(request,"contact.html", context)

def cart(request):
        if request.method == 'POST':
                item_name = request.POST.get('div_text')
                item_qty = request.POST.get('qty')
                current_item = {'item_name' : item_name,'item_qty' : item_qty}
                cart_items = request.session.get('cart_items')
                cart_items[item_name] = current_item
                request.session['cart_items'] = cart_items
                
        
        cart_items = request.session.get('cart_items', {})
        context = {}
        Grand_Total = 0
        if cart_items: 
                context['cart_items'] = []
        for i in cart_items:
                item_name = cart_items[i]['item_name']
                item_qty = cart_items[i]['item_qty']
                product = get_object_or_404(Product, name=item_name)
                item_price = product.price
                Grand_Total += int(item_qty)*int(item_price)
        for i in cart_items:
                item_name = cart_items[i]['item_name']
                item_qty = cart_items[i]['item_qty']
                product = get_object_or_404(Product, name=item_name)
                context['cart_items'].append({
                        'name': product.name,
                        'price': product.price,
                        'image': product.image,
                        'category': product.category,
                        'quantity': item_qty,
                        'sub_total': int(item_qty)*int(product.price),
                })
        context['Grand_Total'] = Grand_Total
        context['username'] = get_username(request)
        return  render(request,"cart.html", context)

def checkout(request):
        cart_items = request.session.get('cart_items', {})
        context = {}
        Menu_item = ''
        Grand_Total = 0

        if cart_items: 
                context['cart_items'] = []
        for i in cart_items:
                item_name = cart_items[i]['item_name']
                item_qty = cart_items[i]['item_qty']
                product = get_object_or_404(Product, name=item_name)
                item_price = product.price
                Grand_Total += int(item_qty)*int(item_price)
                Menu_item += item_name + ' '

        for i in cart_items:
                item_name = cart_items[i]['item_name']
                item_qty = cart_items[i]['item_qty']
                product = get_object_or_404(Product, name=item_name)
                context['cart_items'].append({
                        'name': product.name,
                        'price': product.price,
                        'quantity': item_qty,
                        'sub_total': int(item_qty)*int(product.price),
                })

        guest_name = request.session.get('username')
        items = get_object_or_404(User_Register,Guest_name=guest_name)
        context['Grand_Total'] = Grand_Total
        context['username'] = guest_name
        context['number'] = items.Guest_number
        context['email'] = items.Guest_email

        if request.method == 'POST':
                selected_option = request.POST.get('method')
                Order = User_Order.objects.create(Guest_name=items.Guest_name,Guest_email=items.Guest_email,Item_name=Menu_item,grand_Total=Grand_Total,Payment_method=selected_option)
                request.session['cart_items'] = {}
                return redirect('../')
        return render(request, 'checkout.html', context)

def login(request):
        if request.method=='POST':
                guest_email = request.POST.get("email")
                guest_password = request.POST.get("pass")
                items = get_object_or_404(User_Register,Guest_email=guest_email)    
                if(items):
                        if(items.Guest_password == guest_password and items.Guest_email ==guest_email):
                                request.session['username'] = items.Guest_name
                                request.session['cart_items'] = {}
                                return redirect('/')
                        else:
                                return redirect('../login')
                else:
                        return redirect('../registre')
        else:
                return render(request,'login.html')

def profile(request):
        username = request.session.get('username')
        if username:
                items = get_object_or_404(User_Register,Guest_name=username)
                context = {'username' : username,'number':items.Guest_number,'email':items.Guest_email}
        else:
                context = {'username': 'Guest'}
        return render(request, 'profile.html', context)

def registre(request):
        if request.method=="POST":
                guest_name = request.POST.get("name")
                guest_email = request.POST.get("email")
                guest_number = request.POST.get("number")
                guest_password = request.POST.get("pass")
                items = get_object_or_404(User_Register,Guest_name=guest_name)
                if(items.Guest_name == guest_name):
                        return redirect('../login/')
                else:
                        User_1 = User_Register.objects.create(Guest_name=guest_name,Guest_email=guest_email,Guest_number=guest_number,Guest_password=guest_password)
                        return redirect('/')

        else:
                return render(request, 'register.html')
        
def Delete_Cart(request):
        if(request.method == "POST"):
                request.session['cart_items'] = {}
                return redirect('../cart')
        return render(request, 'Delete Cart.html')