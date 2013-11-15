from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from problems import views

urlpatterns = patterns('',
	url(r'^$',views.HomeView.as_view(), name="home"),
    url(r'^problems/', include('problems.urls', namespace="problems")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/',views.admin_view, name="add"),
    url(r'^add_subject/',views.AddSubjectView.as_view(), name = "add_subject"),
    # url(r'^add_topic/',views.AddTopic.as_view(), name="add_topic"),
)
