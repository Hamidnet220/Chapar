from django.urls import path
from web.views import *

urlpatterns=[
    path('',chapar_view,name='chapar'),
    path('recive/',get_recives,name='recive_letters'),
    path('recive/<int:my_id>/',get_letter_by_id,name='letter'),
    path('recive/addnew/',ReciveLetterView.as_view(),name='new_recive_letter'),
    path('send/addnew/',SendLetterView.as_view(),name='new_send_letter'),
    path('recive/search/',search_letter,name='search_letter'),
    path('send/',get_sends,name='send_letters'),
    path('delete/<int:my_id>',delete_view,name='delete_letter'),
    path('organization/new/',OrganizationView.as_view(),name='create_organization_view')
]