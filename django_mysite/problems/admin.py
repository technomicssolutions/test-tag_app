from django.contrib import admin
from problems.models import Problem, Choice, Subject, Topic, Concept
   
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
    list_filter = ['create_date', 'concept', 'concept__topic', 'concept__topic__subject']
    search_fields = ['question']
    date_hierarchy = 'create_date'

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Concept)
admin.site.register(Problem, ProblemAdmin)
