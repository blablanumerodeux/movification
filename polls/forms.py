from django import forms

class NameForm(forms.Form):
    test = "toto"
    movie_type = forms.CharField(label='movie type', max_length=100)

