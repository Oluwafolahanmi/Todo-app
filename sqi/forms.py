from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=100, 
                           widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name e.g. Adebowale toyeeb', 
                            'aria-label': 'Todo', 'aria-describedby': 'add-btn' }))