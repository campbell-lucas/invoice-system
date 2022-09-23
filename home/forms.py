from django import forms
from customers.models import Customer


class SendEmailForm(forms.Form):
    """
    this form is used to show which fields are to be shown during the sending of an email to the customer.
    """
    from_email = forms.EmailField()
    to_email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
