from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from problems import views

urlpatterns = patterns('',
	url(r'^$',views.AddSubjectView.as_view(), name = "tree_view"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/',views.LoginView.as_view(), name = "login"),
	url(r'^logout/',views.logout_view, name = "logout"),
    url(r'^problems/', include('problems.urls', namespace="problems")),
    url(r'^add_topic/',views.AddTopicView.as_view(), name = "add_topic"),
    url(r'^add_concept/',views.AddConceptView.as_view(), name = "add_concept"),
    url(r'^delete_tag/(?P<tag_id>\d+)',views.DeleteTagView.as_view(), name="delete_tag"),
    url(r'^delete_topic/(?P<topic_id>\d+)',views.DeleteTopicView.as_view(), name="delete_topic"),
    url(r'^delete_concept/(?P<concept_id>\d+)',views.DeleteConceptView.as_view(), name="delete_concept"),
)
