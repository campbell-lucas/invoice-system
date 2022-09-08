from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from users.models import CustomUser
from . import models


class CustomerView(LoginRequiredMixin, ListView):
    model = models.Customer
    template_name = 'customers/customer_list_view.html'
    context_object_name = 'customers'


class CreateCustomerView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Customer
    fields = [
        'number',
        'name',
        'bill_to_address',
        'ship_to_address',
        'country',
        'phone_number',
        'email',
        'credit_limit',
        'order_limit',
        'credit_limit_currency_code',
        'payment_terms',
        'collector',
        'sales_manager',

    ]
    template_name = 'customers/create_customer.html'
    login_url = reverse_lazy('home:home')
    permission_required = 'customers.add_customer'
    raise_exception = False
    success_url = reverse_lazy('home:home')

    def get_form(self, *args, **kwargs):
        form = super(CreateCustomerView, self).get_form(*args, **kwargs)
        form.fields['collector'].queryset = CustomUser.objects.all().filter(is_collector=True)
        form.fields['sales_manager'].queryset = CustomUser.objects.all().filter(is_sales_manager=True)
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = models.Customer
    template_name = 'customers/customer_detailed_view.html'
