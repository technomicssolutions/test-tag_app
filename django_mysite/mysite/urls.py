from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from problems import views

urlpatterns = patterns('',
    url(r'^problems/', include('problems.urls', namespace="problems")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.HomeView.as_view(), name="home"),
    url(r'^add/',views.AdminAddView.as_view(), name="add"),
    url(r'^add_subject/',views.add_subject.as_view(), name = "add_subject"),
)
