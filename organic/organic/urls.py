"""organic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from organic import settings
from django.conf.urls.static import static
from pulses import views as demo
from customer import views as demo1


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', demo.h1, name='h1'),
    url(r'^start/$',demo.start,name='start'),
    url('^login/$',demo.login,name='login'),
    #url('^vendor/$',demo.vendor,name='vendor'),
    #url('^view_ven/$',demo.view_ven,name='view_ven'),
    #url('^pple/$',demo1.pple,name='pple'),
    #url('^view_ppl/$',demo1.view_ppl,name='view_ppl'),
    url(r'^view_p/$',demo.view_p,name='view_p'),
    url(r'^update_p/(?P<pk>\d+)/$',demo.update_p,name='update_p'),
    url(r'^delete_p/(?P<pk>\d+)/$',demo.delete_p,name='delete_p'),
    url(r'^pulses/$',demo1.pulses,name='pulses'),
    url('^review_r/$',demo1.review_r,name='review_r'),

    url(r'^select/(?P<pk>\d+)/$',demo1.mark,name='select'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
