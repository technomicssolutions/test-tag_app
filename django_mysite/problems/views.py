from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout

from problems.models import Problem, Choice, Subject, Topic, Concept


def vote(request, problem_id):
        p = get_object_or_404(Problem, pk=problem_id)
        try:
                selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
                # Redisplay the problem voting form.
                return render(request, 'problems/detail.html', {
                        'problem': p,
                        'error_message': "You didn't select a choice.",
                })
        else:
                selected_choice.votes += 1
                selected_choice.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('problems:results', args=(p.id,)))

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html',context)

    def post(self, request):
        if request.POST:
            if request.POST['username'] and request.POST['password']:
                data_dict = request.POST
                user = authenticate(username = data_dict['username'], password = data_dict['password'])
                if user is not None:
                    if user.is_superuser:
                        login(request, user)
                        return render(request, 'admin_view.html',{})
                    else:
                        template_name = 'home.html'
                        context = {
                            'error': 'Your are not permitted to this section',
                        }
                        return render(request, template_name, context)
                else:
                    template_name = 'home.html'
                    context = {
                        'error': 'Invalid Login, Please check your username and password',
                    }
                    return render(request, template_name, context)
            else:
                template_name = 'home.html'
                context = {
                    'error':'Username and Password cannot be null',
                }
                return render(request, template_name, context)

        return render(request, 'admin_view.html',{})

def admin_view(request):
    subject = Subject.objects.all().order_by('order')
    context = {
        'subject': subject,
    }
    return render(request, 'admin_view.html' , context)

class AddSubjectView(View):
    def get(self, request):
        return render(request, 'add_subject.html', {})

    def post(self, request):
        if request.POST:     
            subject = Subject(name = request.POST['name'], description=request.POST['desc'], order=request.POST['order'])
            subj_total = Subject.objects.all()
            if subj_total:
                for subj in subj_total:
                    if subject.order >= subj.order:
                        subj.order = subj.order + 1
                        subj.save()
                    else:
                        subj.save()
            subject.save()
            if request.POST['topic_name'] and request.POST['topic_desc']:
                topic = Topic(subject = subject, name = request.POST['topic_name'], description = request.POST['topic_desc'])
                topic.save()
                if request.POST['concept_name'] and request.POST['concept_desc']:
                    concept = Concept(topic = topic, name = request.POST['topic_name'], description = request.POST['topic_desc'])
                    concept.save()
        subject = Subject.objects.all().order_by('order')
        context = {
            'subject': subject,
        }
        return HttpResponseRedirect(reverse('add'))

class AddTopic(View):
    def post(self, request):
        if request.POST: 
            print "post", request.POST   
        #     subject = Subject(name = request.POST['name'], description=request.POST['desc'], order=request.POST['order'])
        #     subject.save()
        # subject = Subject.objects.all().order_by('order')
        # context = {
        #     'subject': subject,
        # }
        return HttpResponseRedirect(reverse('add'))
    # subject = Subject