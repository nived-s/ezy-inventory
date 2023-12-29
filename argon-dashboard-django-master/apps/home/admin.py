# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import SalesValue, TotalOrders, PurchaseList, SoldProducts

# Register your models here.
admin.site.register(SalesValue)
admin.site.register(TotalOrders)
admin.site.register(PurchaseList)
admin.site.register(SoldProducts)
