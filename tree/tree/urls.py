"""tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from geny   import views


urlpatterns = [
    path( 'admin/'  , admin.site.urls),
    path( ''                    , views.NodeListView.as_view(), name='index'    ),
    path('node_create/'         , views.NodeCreateView.as_view()           ),

    # todo: nodes. add child and parent
    path('node_update/<int:pk>/', views.NodeUpdateView.as_view()    ),
    path('node_delete/<int:pk>/', views.NodeDeleteView.as_view()    ),

    #todo: edges
    path('edge_list'            , views.NodeListView.as_view()      ),
    path('edge_create/'         , views.NodeCreateView.as_view()    ),
    path('edge_update/<int:pk>/', views.NodeUpdateView.as_view()    ),
    path('edge_delete/<int:pk>/', views.NodeDeleteView.as_view()    ),

    #todo: draw graph.

    #todo: interact on graph. add child, add parent. connect child, connect parent, delete edge.for

    # todo: givcss give style.


]
