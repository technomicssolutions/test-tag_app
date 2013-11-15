from django.contrib import admin
from problems.models import Problem, Choice, Subject, Topic, Concept
   
class ConceptInline(admin.TabularInline):
    model = Concept
    list_display =('topic','name', 'description')

class TopicInline(admin.StackedInline):
    model = Topic
    fieldsets = [
        (None,               {'fields':['subject']}),
        (None,               {'fields':['name']}),
        (None,               {'fields':['description']}),
    ]
    list_display =('subject','name', 'description')
    inlines = [ ConceptInline, ]

class SubjectAdmin(admin.ModelAdmin):
    inlines = [ TopicInline ]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class ProblemAdmin(admin.ModelAdmin):
    # order the fields
    # fields = ['create_date', 'question']

    fieldsets = [
        (None,               {'fields':['question']}),
        (None,               {'fields':['concept']}),
        ('Date information', {'fields':['create_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('concept','question', 'create_date', 'was_created_recently')
    list_filter = ['create_date']
    search_fields = ['question']
    date_hierarchy = 'create_date'

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Problem, ProblemAdmin)
