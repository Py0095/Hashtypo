from django import forms
from django.core.exceptions import ValidationError


class Atikpawformdjango(forms.Form):
    tit = forms.CharField( label='Tit', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Tit'}), required=True)
    Ote = forms.CharField( label='Ote',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ote'}), required=True)
    kontni = forms.CharField(label='Kotni',max_length=4000, widget=forms.Textarea(attrs={'class': 'form-control','rows':3,'id':'exampleFormControlTextarea1','placeholder':'Kontni'}), required=True)

    def clean(self):
        cleaned_data=super().clean()

        tit = self.cleaned_data['tit']
        Ote = self.cleaned_data['Ote']
        kontni = self.cleaned_data['kontni']

        if len(tit)<5:
            self.add_error("tit","Tit la twò kout")

        nb_txt_Ote=len(Ote.split(" "))
        if nb_txt_Ote<=1:
            self.add_error("Ote","Antre non konple ou")

        if 'politik' in kontni.lower():
            self.add_error("kontni","Atik la pa dwe pale de politik")

