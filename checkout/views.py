from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K8CDdCkLZOdDrTBFCJBVoSbLvfXWgKCxC4lk1thYpYWPVuAUC13gxD2Cg4cvjD7SNTxcM3cLF0esVEHBK0YSLOF00z4RdMZm6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
