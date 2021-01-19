from django import forms

class EntryForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':15}))

