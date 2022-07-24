from django.contrib import admin
from django.urls import path,include
from quotesMate.views import QuoteCreate, QuoteDetails, QuoteList

urlpatterns = [
    path('list/',QuoteList.as_view(),name='quote-list'),
    path('quote-create/',QuoteCreate.as_view(),name='quote-create'),
    path('<int:pk>/',QuoteDetails.as_view(),name='quote-details')
]