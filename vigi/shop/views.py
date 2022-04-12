from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Order, ProductOrder, Product
from django.template.loader import get_template
from .forms import AddProductForm
from django.forms import inlineformset_factory



from django.http import HttpResponse

def index(request):
    orders = Order.objects.all()
    context = {
        'orders' : orders,
    }

    return render(request, 'index.html', context=context)


def customer(request, customer_id):
    single_customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'customer.html', {'customer': single_customer})


def add_product(request):
    submitted = False
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shop/add_product?submitted=True')
    else:
        form = AddProductForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_product.html', {'form':form, 'submitted':submitted})


def products(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }

    return render(request, 'products.html', context=context)



def test(request):
    OrderFormSet = inlineformset_factory(Order, ProductOrder, fields=('product_id', 'quantity'))
    form = OrderFormSet()


    return render(request, 'test.html', {'form':form})