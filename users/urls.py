from django.urls import path, re_path
import users.views as user_views 

urlpatterns = [
    re_path(r'^get/$', user_views.TestGet.as_view())
]
