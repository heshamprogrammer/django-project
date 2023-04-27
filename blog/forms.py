from django import forms

class Test(forms.Form):
    name = forms.CharField( max_length= 100,label='Enter Your Name:) ', required=False)
    salary = forms.FloatField( required=False , label='salary:) ')
    emp_email = forms.EmailField(label='Enter Your Email', required=False)
    address = forms.CharField(label='enter your address', max_length=100, required=False)