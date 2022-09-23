from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from invoices.models import Invoice
from users.models import CustomUser
from . import models


# class CustomerView(LoginRequiredMixin, ListView):
#     """
#     Class CustomerView uses ListView to show a list of all customers under the specific user.
#     """
#     model = models.Customer
#     template_name = 'customers/customer_list_view.html'
#     context_object_name = 'customers'


class CreateCustomerView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class CreateCustomerView is for creating a new customer and uses LoginRequiredMixin and
    PermissionRequiredMixin to make sure that only users in group sales manager can access it.
    """
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
        """
        Gets the form / information that was input into the form shown.
        """
        form = super(CreateCustomerView, self).get_form(*args, **kwargs)
        form.fields['collector'].queryset = CustomUser.objects.all().filter(is_collector=True)
        form.fields['sales_manager'].queryset = CustomUser.objects.all().filter(is_sales_manager=True)
        return form

    def form_valid(self, form):
        """
        makes the instance owner of the form the requester, and then returns the super of get_form
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    """
    This class is based on model Customer, and it used to show the details of the customer i.e. Email, Phone Number
    """
    model = models.Customer
    template_name = 'customers/customer_detailed_view.html'


class CustomerInvoicesView(LoginRequiredMixin, ListView):
    """
    This class is based on the model Invoice, and uses ListView to list all the customers invoices individually
    """
    model = Invoice
    template_name = 'customers/customer_invoice_view.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        """
        This returns the specific customers queryset to show only that customers invoices.
        """
        return Invoice.objects.filter(customer_id=self.kwargs.get('pk'))
