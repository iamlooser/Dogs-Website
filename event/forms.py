from django import forms
from event.models import Event

class EventForm(forms.ModelForm):
        Title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter title", 'class':"mdl-textfield__input",'type':"text" ,'name':"username" ,'id':"sample3"}))
        Date = forms.DateField(widget=forms.SelectDateWidget())
        Commit = forms.CharField(widget=forms.Textarea(attrs={'class':"mdl-textfield__input",'type':"text", 'rows': "3", 'id':"sample5" }))
        Views = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter title", 'class':"mdl-textfield__input",'type':"text" ,'name':"username" ,'id':"sample3"}))
        Document = forms.FileField()


        class Meta:
            model = Event

            fields = ('Title', 'Commit', 'Document', 'Date')
