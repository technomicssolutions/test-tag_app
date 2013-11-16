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

class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html',context)

    def post(self, request):
        template_name = 'login.html'
                        
        if request.POST:
            if request.POST['username'] and request.POST['password']:
                data_dict = request.POST
                user = authenticate(username = data_dict['username'], password = data_dict['password'])
                if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse('tree_view'))
                else:
                    context = {
                        'error': 'Invalid Login, Please check your username and password',
                    }
                    return render(request, template_name, context)
            else:
                context = {
                    'error':'Username and Password cannot be null',
                }
                return render(request, template_name, context)

        return HttpResponseRedirect(reverse('tree_view'))

class AddSubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()

        return render(request, 'add_subject.html', {
                'subjects': subjects
            })

    def post(self, request):
        if request.POST: 
            if request.POST['subject']:            
                subject = Subject.objects.create(name = request.POST['subject'])
            else:
                context = {
                    'error': 'Name of the Subject cannot be null',
                }
                return render(request, 'add_subject.html', context)
        return HttpResponseRedirect(reverse('tree_view'))

class AddTopicView(View):
    def post(self, request):
        if request.POST: 
            if request.POST['subject'] and request.POST['topic']:
                subject = Subject.objects.get(id=request.POST['subject'])
                topic = Topic.objects.create(name = request.POST['topic'], subject=subject)
            else:
                context = {
                    'error': 'Name of the Topic cannot be null',
                }
                return render(request, 'add_subject.html', context)
        return HttpResponseRedirect(reverse('tree_view'))

class AddConceptView(View):
    def post(self, request):
        if request.POST: 
            if request.POST['topic'] and request.POST['concept']:
                topic = Topic.objects.get(id=request.POST['topic'])
                concept = Concept.objects.create(name = request.POST['concept'], topic=topic)
            else:
                context = {
                    'error': 'Name of the Concept cannot be null',
                }
                return render(request, 'add_subject.html', context)
        return HttpResponseRedirect(reverse('tree_view'))


class DeleteTagView(View):
    def get(self, request, tag_id):
        if tag_id:
            subject = Subject.objects.get(id = tag_id)
            subject.delete()
                        
        return HttpResponseRedirect(reverse('tree_view'))    


class DeleteConceptView(View):
    def get(self, request, concept_id):
        if concept_id:
            concept = Concept.objects.get(id = concept_id)
            concept.delete()                    
        return HttpResponseRedirect(reverse('tree_view'))  

class DeleteTopicView(View):
    def get(self, request, topic_id):
        if topic_id:
            topic = Topic.objects.get(id = topic_id)
            topic.delete()                    
        return HttpResponseRedirect(reverse('tree_view'))    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('tree_view'))
