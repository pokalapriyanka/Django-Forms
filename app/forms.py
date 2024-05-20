from django import forms

class SchoolForm(forms.Form):
    SName=forms.CharField(max_length=100)
    Sage=forms.IntegerField(min_value=5)
    Url=forms.URLField()
    Email=forms.EmailField()
    Spassword=forms.CharField(widget=forms.PasswordInput)
    Address=forms.CharField(widget=forms.Textarea(attrs={'cols':30,'rows':10}))