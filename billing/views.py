
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from billing.models import Products, customer, Order, Order_detail
from billing.forms import OrderItemFormset, ProductsForm, OrderForm
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['username'] = username.capitalize()

            return redirect('/home')

        else:
            messages.error(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request, 'index.html')


def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        username = username.capitalize()

        user = User.objects.create_user(
            username=username, password=password, email=email)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request, 'register.html')


@login_required(login_url='/')
def home(request):
    customers = customer.objects.all()
    total_customers = customers.count()
    request.session['tot_cust'] = total_customers

    products = Products.objects.all()
    total_products = products.count()

    request.session['tot_prod'] = total_products

    Ord_detail = Order_detail.objects.all()

    request.session['tot_prod'] = total_products

    order = Order.objects.all()
    total_order = order.count()
    request.session['total_ord'] = total_order

    prod = Products.objects.all()
    return render(request, 'nav.html', {'prod': prod, 'customers': customers, 'order': order, 'ordd': Ord_detail})


@login_required(login_url='/')
def custom(request):

    return render(request, 'custom.html')


@login_required(login_url='/')
def products(request):
    context = {}
    context['form'] = ProductsForm
    if request.method == 'POST':
        prod_name = request.POST['prod_name']
        prod_code = request.POST['prod_code']
        prod_rate = request.POST['prod_rate']
        prod_gst = request.POST['prod_gst']
        prod_stock = request.POST['prod_stock']
        # print(prod_name,prod_code,prod_rate,prod_gst,prod_stock)
        prod_code = prod_code.upper()

        product = Products(prod_name=prod_name, prod_code=prod_code,
                           prod_rate=prod_rate, prod_gst=prod_gst, prod_stock=prod_stock)
        product.save()
        return redirect('/home')

    return render(request, 'products.html')


def info(request):
    prod_names = request.POST['prod_names']
    print(prod_names)


@login_required(login_url='/')
def order(request):
    form = OrderForm(request.POST)
    # recieves a post method for the formset
    formset = OrderItemFormset(request.POST)
    print(form.is_valid())
    print(formset.is_valid())
    print(formset.errors)
    if form.is_valid():
        # saves bill
        billobj = form.save(commit=False)
        ord = billobj
        # create bill details object

        for f in formset:
            cd = f.cleaned_data

            print(ord)
            ord_qty = cd.get('ord_qty')
            prod_nme = Products.objects.get(prod_name=cd.get('prod'))
            print(prod_nme.prod_id)
            prod_id = prod_nme.prod_id
            itm_price = cd.get('itm_price')
            billdetailsobj = Order_detail(
                ord=ord, prod_id=prod_id, ord_qty=ord_qty, itm_price=itm_price)
        billobj.save()
        # for loop to save each individual form as its own object
        for form in formset:

            # false saves the item and links bill to the item

            # links the bill object to the items

            # gets the stock item
            stock = get_object_or_404(Products, prod_id=billdetailsobj.prod_id)
            # calculates the total price

            # updates quantity in stock db
            stock.prod_stock -= billdetailsobj.ord_qty
            # saves bill item and stock
            stock.save()
            billdetailsobj.save()
        messages.success(
            request, "Sold items have been registered successfully")
        return redirect('/home')
    form = OrderForm(request.GET or None)
    formset = OrderItemFormset(request.GET or None)
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'order.html', context)


@login_required(login_url='/')
def customers(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        c_name = request.POST['cn']
        country = request.POST['selection']
        houseadd = request.POST['houseadd']
        apartment = request.POST['apartment']
        city = request.POST['city']
        state = request.POST['state']
        postal = request.POST['zip']
        tel = request.POST['tel']
        email = request.POST['email']
        f_name = f_name.capitalize()
        l_name = l_name.capitalize()
       # print(f_name,l_name,c_name,country,houseadd,apartment,city,state,postal,tel,email)
        cust = customer(f_name=f_name, l_name=l_name, company_name=c_name, country=country,
                        street_address=houseadd, town=city, state=state, postal_code=postal, contact=tel, email=email)

        cust.save()
        return redirect('/home')
    return render(request, 'customer.html')


def logout(request):

    auth.logout(request)
    return redirect('/')
