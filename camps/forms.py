from django import forms
from .models import Camp, Category


class CampForm(forms.ModelForm):

    class Meta:
        model = Camp
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'my-2'
