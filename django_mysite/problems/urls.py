from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone
from problems.models import Problem

urlpatterns = patterns('',
	# ex: /problems/
	url(r'^$',
		ListView.as_view(
			queryset=Problem.objects.filter(create_date__lte=timezone.now) \
				.order_by('-create_date')[:5],
			context_object_name='latest_problem_list',
			template_name='problems/index.html'),
		name='index'),
	# ex: /problems/5/
	url(r'^(?P<pk>\d+)/$',
		DetailView.as_view(
			queryset=Problem.objects.filter(create_date__lte=timezone.now),
			model=Problem,
			template_name='problems/detail.html'),
		name='detail'),
	# ex: /problems/5/results/
	url(r'^(?P<pk>\d+)/results/$',
		DetailView.as_view(
			model=Problem,
			template_name='problems/results.html'),
		name='results'),
	# ex: /problems/5/vote/
	url(r'^(?P<problem_id>\d+)/vote/$', 'problems.views.vote', name='vote'),
)
