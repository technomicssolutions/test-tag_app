import datetime
from django.db import models
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField('Name of the Subject', max_length = 200)
    description = models.TextField('Description', max_length = 500)
    order = models.IntegerField('Order', max_length = 10, default = '1')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Topic(models.Model):
    subject = models.ForeignKey(Subject)
    name = models.CharField('Name of the Topic', max_length = 200)
    description = models.TextField('Description', max_length = 500)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

class Concept(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField('Name of the Concept', max_length = 200)
    description = models.TextField('Description', max_length = 500)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Concept'
        verbose_name_plural = 'Concepts'


class Problem(models.Model):
        concept = models.ForeignKey(Concept, null = True, blank = True) 
        question = models.CharField(max_length=200)
        create_date = models.DateTimeField('date created')

        def was_created_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.create_date < now
        was_created_recently.admin_order_field = 'create_date'
        was_created_recently.boolean = True
        was_created_recently.short_description = 'Created recently?'

        def __unicode__(self):
                return self.question

class Choice(models.Model):
        problem = models.ForeignKey(Problem)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

        def __unicode__(self):
                return self.choice_text

