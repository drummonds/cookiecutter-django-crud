from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from {{ cookiecutter.app_name }}.models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          self.helper = FormHelper(self)
          self.helper.form_method = 'post'
          self.helper.form_action = '.'
          self.helper.label_class = 'col-lg-2'
          self.helper.field_class = 'col-lg-8'
          self.helper.form_class = 'form-horizontal'
          self.helper.add_input(Submit('submit', 'Submit'))
          super({{ cookiecutter.model_name }}Form, self).__init__(*args, **kwargs)
        
    class Meta:
        model = {{ cookiecutter.model_name }}

