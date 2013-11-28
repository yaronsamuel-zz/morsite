from django import forms
from django.http import HttpResponseRedirect , HttpResponse
from django.template import RequestContext, loader



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    
    
    address = forms.CharField(max_length=100)
    phone = forms.DecimalField()
    mail = forms.EmailField()
    message = forms.CharField()
    
    
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    template = loader.get_template('contact_form/contact.html')
    context = RequestContext(request, {
        'form': form,
    })
    
    return HttpResponse(template.render(context))
