from django.contrib import admin
from django import forms
from .models import Interview, Question, QuestionReply, Variant


# Register your models here.
@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    
    fields = ['name',
              'description',
              'date_start',
              'date_end']
    
    def get_readonly_fields(self, request, obj=None):
        try:
            e = [f.name for f in obj._meta.fields if not f.name != 'date_start']
            return e
        except Exception:
            return ""


choices = [[1,'ответ текстом'],
    #[2,'выбором одного варианта'],
    [3,'нескольких вариантов']]


class InterviewAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InterviewAdminForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget = admin.widgets.AdminRadioSelect(choices=choices)


class VariantInstanceInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = Variant


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    
    form = InterviewAdminForm
    
    fields = ['interview',
              'text',
              'type',]
    
    inlines = [VariantInstanceInline,]


@admin.register(QuestionReply)
class QuestionReplyAdmin(admin.ModelAdmin):
    
    readonly = True
    
    fields = ['user','question', 'reply']
