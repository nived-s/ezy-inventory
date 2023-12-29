from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import SalesValue, TotalOrders, PurchaseList, SoldProducts


@login_required(login_url="/login/")
def index(request):
    sales_values = SalesValue.objects.all()
    total_orders = TotalOrders.objects.all()
    purchase_list = PurchaseList.objects.all()
    sold_products = SoldProducts.objects.all()
    
    context = {
        'segment': 'index',
        'sales_values': sales_values,
        'total_orders': total_orders,
        'purchase_list': purchase_list,
        'sold_products': sold_products,
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
