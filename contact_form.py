from django import forms
from django.http import HttpResponseRedirect , HttpResponse
from django.template import RequestContext, loader
from django.core.mail import send_mail
from morsite.settings import EMAIL_RECIPIAENTS_LIST , EMAIL_HOST_USER

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



SUBJECT = "Cakes'N'More - You've got a message"

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
            sendMail(SUBJECT, form, 
                    EMAIL_HOST_USER, EMAIL_RECIPIAENTS_LIST)
                    
            return HttpResponseRedirect('/thanks/') # Redirect after POST
            
    else:
        form = ContactForm() # An unbound form

    template = loader.get_template('contact_form/contact.html')
    context = RequestContext(request, {
        'form': form,
    })
    
    return HttpResponse(template.render(context))
    
    
def thanks(request):
    
    template = loader.get_template('contact_form/thanks.html')
    context = RequestContext(request, {
    })
    
    return HttpResponse(template.render(context))

    

            
def sendMail(subject, form, from_email , recipients):

    plaintext = get_template('contact_form/email.txt')
    htmly     = get_template('contact_form/email.html')

    d = Context({   'address' : form.cleaned_data['address'] , 
                    'phone' : form.cleaned_data['phone'] , 
                    'name' : form.cleaned_data['name'] , 
                    'message' : form.cleaned_data['message'] ,
                    'mail': form.cleaned_data['mail'] ,
    })

    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
            