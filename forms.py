from  django import forms

class Student(forms.Form):
 inter_rs=forms.IntegerField(max_value=200)
 inter_pt=forms.IntegerField(max_value=20)
 inter_tl=forms.IntegerField(max_value=1000000)


