from django import forms

choices = [
  ('Intern', 'Intern'),
  ('CEO', 'Chief Executive Officer'),
  ('COO', 'Chief Operating Officer'),
  ('CTO', 'Cheif Technical Officer'),
  ('DS', 'Data Scientist'),
  ('DPA', 'Data Processing Analyst'),
  ('Lead', 'Tech Lead'),
  ('SSWE', 'Senior Software Engineer'),
  ('SWE', 'Software Engineer')
]

class EmployeeForm(forms.Form):
  name = forms.CharField()
  email = forms.EmailField(label='E-Mail')
  role = forms.ChoiceField(choices=choices)
  department = forms.CharField()
  reports_to = forms.CharField()
  location = forms.CharField()
  is_manager = forms.BooleanField(required=False)
