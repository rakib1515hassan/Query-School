from django.forms import ModelForm
from .models import Query_Code
from django import forms

class Query_CodeForm(ModelForm):

    class Meta:
        model = Query_Code
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Optionally, you can add Bootstrap specific classes to individual fields
        # Check if the field exists in the form before customizing it
        if 'example_field' in self.fields:
            self.fields['example_field'].widget.attrs['class'] = 'form-control my-custom-class'

        # Add Bootstrap classes to form labels
        self.label_suffix = ""

        # Optionally, you can customize form labels with Bootstrap classes
        # Check if the field exists in the form before customizing its label
        if 'example_field' in self.fields:
            self.fields['example_field'].label = 'Custom Label:'


    def clean_query_no(self):
        query_no = self.cleaned_data['query_no']
        
        # Check if a Query_Code object with the same query_no already exists
        if Query_Code.objects.filter(query_no=query_no).exists():
            raise forms.ValidationError('Query no already exists.')

        return query_no
