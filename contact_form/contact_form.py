from django import forms
from django.utils.translation import ugettext as _



class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100 , required=False)
    phone = forms.CharField(max_length=20)
    mail = forms.EmailField(required=False)
    message = forms.CharField()
    
    def clean_phone(self):
        phone_no = self.cleaned_data.get('phone', None)
        if phone_no:
            for ch in [ '-' , ' ']:
              phone_no = phone_no.replace(ch  , '')
              
        if len(phone_no) <7:
            raise forms.ValidationError(_('Too short phone number.'))
        try:
            int(phone_no)
        except (ValueError, TypeError):
            raise forms.ValidationError(_('Please enter a valid phone number.'))
            
        return phone_no


    