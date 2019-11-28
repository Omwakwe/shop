from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import OrdersForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import ast


class OrderView(View):
    '''
    a view for adding groups signals
    '''
    form_class = OrdersForm
    template_name = "orders/order.html"
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(OrderView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print('the request data :', request.POST)
        responsedata = {}
        cart = ast.literal_eval(request.POST["cart"])
        cost = 0

        for order in cart:
            print("order ", order)
            if order["size"] == "S":
                cost = cost + (500 * order["quantity"])
            elif order["size"] == "M":
                cost = cost + (800 * order["quantity"])
            elif order["size"] == "L":
                cost = cost + (1200 * order["quantity"])

        responsedata['success'] = 'yes'
        responsedata['cost'] = cost
        responsedata['location'] = request.POST["location"]

        return JsonResponse(responsedata)
