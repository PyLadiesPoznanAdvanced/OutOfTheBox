from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(label='Search text', max_length=64,
                                  widget=forms.TextInput(attrs={'placeholder': 'search text'}))
