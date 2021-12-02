from django.urls import path

from .views import identifier_code_create, log_message_create

urlpatterns = [
    path('code/create/', identifier_code_create, name="identifier-code-create"),

    path('log-message/create/', log_message_create, name="log-message-create"),
]
