
from django.urls import path
from EstateHub.views import (home,baseview,create_property_unit,
                             create_tenant,create_lease, user_logout,success,property_all, unit_details,leas_success,sign,logins)

urlpatterns = [
    path('login/', logins,name='custom_login'),
    path('signup/', sign,name='custom_signup'),
    path('home/', home,name='home'),
    path('', baseview,name='baseview'),
    path('create_property_unit/', create_property_unit,name='create_property_unit'),
    path('tenant-list/', create_tenant,name='create_tenant'),
    path('lease-list/', create_lease,name='create_lease'),
    path('logout/', user_logout,name='logout'),
    path('success/', success,name='success'),
    path('property_all/', property_all,name='property_all'),
    path('property_unit_details/<int:property_unit_id>/', unit_details,name='property_unit_details'),
    path('leas_success/', leas_success,name='leas_success'),





]