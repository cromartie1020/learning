from .models import Topic, Entry
from django import forms


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        labels={ 'text': '' }

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields='__all__'
        labels={ 'text': '' }
        widgets={ 'text': forms.Textarea(attrs={'cols':40})}
        
