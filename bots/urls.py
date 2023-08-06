from django.urls import path

from .views import *


urlpatterns = [

    path('bots/', home_view, name='bot_home_view'),
    path('bots/list', BotListView.as_view(), name='bot_list'),
    path('bots/create', BotCreateView.as_view(), name='bot_create'),
    path('bots/<int:pk>', BotDetailView.as_view(), name='bot_detail'),
    path('bots/<int:pk>/update', BotUpdateView.as_view(), name='bot_update'),
    path('bots/<int:pk>/delete', BotDeleteView.as_view(), name='bot_delete'),
    path('bots/remove_home_filters', bot_remove_home_filters, name='bot_remove_home_filters'),
    path('bots/remove_list_filters', bot_remove_list_filters, name='bot_remove_list_filters'),
    path('bots/temizle', bot_clean, name='bot_clean'),
    path('bots/link_clicked/<int:pk>', link_clicked, name='link_clicked'),



]
