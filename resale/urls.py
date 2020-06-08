"""resale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from home import views as home_views
from itempost import views as item_views
from product import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', home_views.index, name='home_page'),
    url('home/', include('home.urls', namespace='home')),
    path('accounts/', include('allauth.urls')),  # allauth url
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    url('product/', include('product.urls', namespace='products')),
    url('itempost/', item_views.item_post, name='item_post'),


    path('contact/', home_views.contact, name='contact'),
    path('contact/', home_views.contact, name='contact'),
    path('faq/', home_views.faq, name='faq'),
    path('feedback/', home_views.feedback, name='feedback'),
    path('howitworks/', home_views.howitworks, name='howitworks'),
    path('privacy/', home_views.privacy, name='privacy'),

    url('home/category/(?P<cate>.+)/$',
        home_views.category_page, name='category_page'),
    url('home/item/(?P<item>.+)/$', home_views.single_item, name='single_item'),

    # RESTFRAMEWORK URLS
    path('api/', include('api.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
