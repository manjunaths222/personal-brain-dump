---
title: "Filter IT department and Salary > 60000"
---

Python Snippets

Flatten Multi-Dimensional List:
my_list = [[10,20,30],[40,50,60],[70,80,90]]
flat = [x for sublist in my_list for x in sublist]

Palindrome Check:
```python
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))  # False
```

Pandas Filter:
```python
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 29],
    'Department': ['HR', 'IT', 'IT', 'Finance'],
    'Salary': [50000, 60000, 70000, 52000]
}
df = pd.DataFrame(data)
# Filter IT department and Salary > 60000
filtered_df = df[(df['Department'] == 'IT') & (df['Salary'] > 60000)]
```

Django Custom Middleware:
```python
from django.utils.timezone import now

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.timezone = now()
        response = self.get_response(request)
        return response

# In settings.py:
MIDDLEWARE = [
    'myapp.middleware.TimezoneMiddleware',
]
```

Django Form Validation:
```python
class ContactForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email.endswith('@example.com'):
            raise forms.ValidationError("We do not accept @example.com emails.")
        return email

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        if not name or not email:
            raise forms.ValidationError("Both name and email are required.")
        return cleaned_data
```
