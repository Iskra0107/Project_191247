from django import forms
from .models import Glucose

class GlucoseForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(GlucoseForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			field.field.widget.attrs["class"] = "form-control"
	class Meta:
		model = Glucose
		exclude = ("user",)