from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path

from .views import *

urlpatterns = [
  re_path(r'$', ListCreateOrder_items.as_view(), name='create-list-order_items')
]

urlpatterns = format_suffix_patterns(urlpatterns)