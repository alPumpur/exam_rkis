from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import *
from .forms import *
from django.shortcuts import render
from .models import Product


class MainList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/main.html'

    def get_queryset(self):
        return Product.objects.all()[:5]


def profile(request):
    order = Order.objects.filter(user=request.user)

    context = {
        "orders": order,
    }

    return render(request, 'app/profile.html', context)


class ServiceList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/services.html'

    def get_queryset(self):
        return Product.objects.all()


def service_detail(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.product_id = id
            instance.save()
    else:
        form = OrderForm(initial={'user': request.user.pk, 'product': id})

    return render(request, "app/service_detail.html", {'product': product, 'form': form})


class RegisterView(generic.CreateView):
    model = AdvUser
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')


from django.shortcuts import render
from .models import Product

def product_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)

    context = {'query': query, 'products': products}
    return render(request, 'app/product_search.html', context)
