from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from customers.models import Customer
from users.models import CustomUser
from .forms import SendEmailForm


class HomeView(LoginRequiredMixin, ListView):
    """
    this is the home view and lists the customers in your portfolio
    """
    model = Customer
    template_name = 'home/home.html'
    context_object_name = 'customers'

    def get_queryset(self):
        if self.request.user.groups.filter(name='collectors'):
            return Customer.objects.filter(collector_id=self.request.user.id)
        else:
            return Customer.objects.filter(sales_manager=self.request.user.id)


def send_email(request, pk):
    """
    this function allows the user to send the customer an email
    """
    to_email = Customer.objects.get(pk=pk).email
    form = SendEmailForm(request.POST)
    if form.is_valid():
        return redirect('home:landing')

    form = SendEmailForm(initial={'from_email': request.user.email, 'to_email': to_email})
    return render(request, 'home/send-email.html', {'form': form})


@login_required
def landing_view(request):
    """
    this function is just the landing page view and it is required that you are logged in
    """
    return render(request, 'home/landing.html')
