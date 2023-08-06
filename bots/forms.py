from django import forms
from .models import Bot, BotFilter

WIDTH=100

class BotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ['title', 'content', 'keywords', 'category', 'notes', 'link', 'local', 'counter', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'size': WIDTH}),
            'keywords': forms.TextInput(attrs={'size': WIDTH}),
            'link': forms.TextInput(attrs={'size': WIDTH}),
            'local': forms.TextInput(attrs={'size': WIDTH}),
            'content': forms.Textarea(attrs={'cols': WIDTH, 'rows': 10}),
            'notes': forms.Textarea(attrs={'cols': WIDTH, 'rows': 10}),
        }

class BotFilterForm(forms.ModelForm):
    class Meta:
        model = BotFilter
        fields = ['title', 'content', 'keywords','category', 'notes', 'link', 'local']

        widgets = {
            'title': forms.TextInput(attrs={'size': 20}),
            'content': forms.TextInput(attrs={'size': 20}),
            'keywords': forms.TextInput(attrs={'size': 20}),
            'category': forms.TextInput(attrs={'size': 20}),
            'notes': forms.TextInput(attrs={'size': 20}),
            'link': forms.TextInput(attrs={'size': 20}),
            'local': forms.TextInput(attrs={'size': 20}),
        }
