from django import forms
from .models import Question, Answer, Tag


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title' , 'body' , 'tag' ]
    #to customize tag field
    tag = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        choices= Tag.objects.all().values_list('name','name')
    )


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
        }






class SearchForm(forms.Form):
    query = forms.CharField()



class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
