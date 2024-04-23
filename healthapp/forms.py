from django import forms

class HealthForm(forms.Form):
    name = forms.CharField(max_length=100, 
                           widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient name e.g. Adebowale toyeeb', 
                            'aria-label': 'Todo', 'aria-describedby': 'add-btn' }))
    Age = forms.IntegerField(widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient age', 
                            'aria-label': 'Todo', 'aria-describedby': 'add-btn' }))
    Address = forms.CharField(max_length=200, 
                           widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient Address e.g. Oluyole extension, ibadan', 
                            'aria-label': 'Todo', 'aria-describedby': 'add-btn' }))

