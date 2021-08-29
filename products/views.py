"""Products Views."""

# Django
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Models
from .models import *
from orders.models import *


# Forms
from .forms import ProductForm
from orders.forms import OrderProductForm


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_update.html'
    success_url = reverse_lazy('products:list')
    success_message = 'Successfully created product.'


class ProductsUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_update.html'
    success_url = reverse_lazy('products:list')
    success_message = 'Successfully updated product.'


class ProductsDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
    success_message = 'Successfully deleted product.'


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    queryset = model.objects.all()
    template_name = 'products/list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            queryset = queryset.filter(
                enabled=True
            )
        return queryset


class ProductOrderCreateView(LoginRequiredMixin, CreateView):
    model = OrderProducts
    form_class = OrderProductForm
    template_name = 'products/add_to_order.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


    def form_valid(self, form, **kwargs):
        """
        Validate and save
        """
        if form.is_valid():
            product_id = self.kwargs['product_id']
            product = Product.objects.get(pk=product_id)
            order = form.cleaned_data['order']

            order_product_taken = OrderProducts.objects.filter(
                order_id=order.uuid,
                product_id=product.uuid
            ).exists()

            if not order_product_taken:
                order_products = OrderProducts(product=product, **form.cleaned_data)
                order_products.save()

            msg = f'Product added to order {product.name}.'
            messages.info(
                self.request,
                msg
            )

            return HttpResponseRedirect(reverse('products:list'))

    def get_context_data(self, **kwargs):
        context = super(ProductOrderCreateView, self).get_context_data(**kwargs)
        context['product_id'] = self.kwargs['product_id']
        return context


@login_required
def check_exists_order(request, product_id):
    """
    Method for verifying if there is
    a order created for an user
    """
    try:
        Order.objects.get(created_by=request.user, sent=False, paid_out=False)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('products:add_product_order_default', args=(
            product_id,
        )))
    except MultipleObjectsReturned:
        pass

    return HttpResponseRedirect(reverse('products:add_product_order_select', args=(
        product_id,
    )))


@login_required
def add_product_order_default(request, product_id):
    """
    It allows us to add product to order
    :param product_id: id product to add
    """
    order = Order.objects.create(
        created_by=request.user
    )

    product = Product.objects.get(
        uuid=product_id
    )

    OrderProducts.objects.create(
        order=order,
        product=product
    )

    msg = f'Product added to order {product.name}.'
    messages.info(
        request,
        msg
    )

    return HttpResponseRedirect(reverse('products:list'))



