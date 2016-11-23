from django import forms


class homeForm(forms.Form):

    full_name = forms.CharField()