
from .models import  Cart, CartItem, MenuItem,  ItemsCategory, Order, generate_order_id
from account_app.models  import Profile
from .forms import AddToCartForm
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404


class MenuListView(ListView):
    model = MenuItem
    template_name = 'items/menu_list.html'

def menu_list_view(request):
    item_list = MenuItem.objects.all()

    context = {'item_list': item_list,
                'item_categories':reversed(ItemsCategory.objects.all()),
                'item_categories_side_nav':reversed(ItemsCategory.objects.all())}

    return render(request, 'menu_app/menu_list.html', context)

def home(request):
    category_menu = ItemsCategory.objects.all()
    context = {'category_menu': category_menu}
    return render (request, 'homepage.html', context)

def menu_item_detail(request, **kwargs):
    item = MenuItem.objects.filter(id=kwargs.get('pk')).first()

    context = {'item':item}

    return render(request, 'menu_app/item_details.html', context)


def new_order_info(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order, created = Order.objects.get_or_create(customer=user_profile.user, is_ordered=False)
    if created:
        order.ref_code = generate_order_id()
        order.save()
    context = {'order':order}

    return render(request, 'items/order_info.html', context)

def menu_details (request, name):
    try: 
        category = ItemsCategory.objects.get(name = name)
    except ItemsCategory.DoesNotExist:
        print ("not saving")
        category = None 

    menu_details = MenuItem.objects.filter(category = category)
    context = {'menu_details': menu_details, 'category': name, 'user':request.user}

    if request.method == "POST":
        form = AddToCartForm(request.POST or None)
        form.cart = Cart.objects.get_or_create(user= request.user, current = True)
            form.is
        form.save ()
    return render (request, 'menu_app/menu_list.html', context)

def cart (request):
    cart = Cart.objects.get(user = request.user, current = True)
    print (request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    context = {'cart_items':cart_items}
    return render (request, 'menu_app/cart.html', context )
    

