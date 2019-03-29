from django.urls import path
from web.views import chapar_view,get_recives,get_letter_by_id,search_letter,new_letter,create_letter_view

urlpatterns=[
    path('',chapar_view,name='chapar'),
    path('recive/',get_recives,name='recive_letters'),
    path('recive/<int:my_id>/',get_letter_by_id,name='letter'),
    path('recive/addnew/',new_letter,name='new_letter'),
    path('recive/savenew/',create_letter_view,name='create_letter'),
]