from django.conf.urls import url,include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from . import views
app_name = 'todoapp'

# urlpatterns = [
#     #Normal Urls calls to get html page as response
#
#     # url(r'^$',views.index,name='index'),
#     # url(r'^getlist/$',views.getlist,name="getlist"),
#     # url(r'^getdata/(?P<list_id>[0-9]+)/$',views.getdata,name="getdata"),
#
#     #Rest API calls to get JSON response
#     url(r'^lists/$', views.GetLists.as_view(),name="getlists"),
#     url(r'^alterlist/(?P<pk>[0-9]+)/$', views.AlterList.as_view(),name="editlists"),
#     url(r'^items/(?P<pk>[0-9]+)/$',views.Itemgetpost.as_view(),name="listitems"), # Getitems.as_view()
#     # url(r'^lists/(?P<pk>[0-9]+)/items/$',views.Itemgetpost.as_view(),name="getlistitems"),
#     url(r'^alter/(?P<pk>[0-9]+)/$' , views.Alteritem.as_view() , name="alteritems"),
#
#
# ]

urlpatterns =[
    url(r'^home/$', views.getHome,name="getHome"),
    url(r'^loggined/$', TemplateView.as_view(template_name="registration/loggedin.html")),
    url(r'^lists/showlists.html/$', TemplateView.as_view(template_name="registration/get_lists.html")),
    url(r'^lists/show_items.html/$', TemplateView.as_view(template_name="registration/show_items.html")),
    url(r'^lists/$',csrf_exempt(views.GetLists.as_view()),name="getlists"),
    url(r'^alterlist/(?P<pk>[0-9]+)/$', views.AlterList.as_view(),name="editlists"),
    # url(r'^items/(?P<pk>[0-9]+)/$',views.Getitems,name="listitems"),
    url(r'^lists/(?P<pk>[0-9]+)/items/$',views.Itemgetpost.as_view(),name="getlistitems"),
    url(r'^lists/create_list.html/$', TemplateView.as_view(template_name="registration/create_list.html")),
    url(r'^alter/(?P<pk>[0-9]+)/$',views.Alteritem.as_view(),name="alteritems"),

]