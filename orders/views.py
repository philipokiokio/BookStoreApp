from typing import ContextManager
from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe 


# Create your views here.
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
print('api-keuy',stripe.api_key)

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY 
        return context


def charge(request):

    permission = Permission.objects.get(codename='special_status')

    u = request.user

    # add to users permission set

    u.user_permissions.add(permission)

    if request.method == 'POST':

        charge = stripe.Charge.create(amount=3900,
                                     currency='GBP',
                                     description = 'Purchase all books',
                                     source= request.POST['stripeToken'])
        # print(request.POST['stripeToken'])
        return render(request, 'orders/charge.html')