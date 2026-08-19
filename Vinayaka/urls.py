from django.urls import path

from .views import (
    vinayaka_list,
    vinayaka_detail,
)


urlpatterns = [
    path(
        "Vinayaka",
        vinayaka_list
    ),

    path(
        "Vinayaka/<int:mid>",
        vinayaka_detail
    ),
]