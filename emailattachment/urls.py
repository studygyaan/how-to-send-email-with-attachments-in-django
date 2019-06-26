from django.urls import path
from emailattachment.views import EmailAttachementView

urlpatterns = [
    path('', EmailAttachementView.as_view(), name='emailattachment')

]