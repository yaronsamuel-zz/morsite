from django.http import HttpResponseRedirect , HttpResponse
from django.template import RequestContext, loader
from django.core.mail import send_mail
from morsite.settings import EMAIL_RECIPIAENTS_LIST , EMAIL_HOST_USER

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


from contact_form import ContactForm

SUBJECT = "Cakes'N'More - You've got a message"


def contact(request):

    # deter fail message displaying
    sendMailSucess = True
    
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
       
        if form.is_valid(): # All validation rules pass
            sendMailSucess = sendMail(SUBJECT, form, 
                    EMAIL_HOST_USER, EMAIL_RECIPIAENTS_LIST)
            if sendMailSucess:
                insertToSession(form , request)            
                return HttpResponseRedirect('/thanks/') # Redirect after POST
            
    else:
        form = ContactForm() # An unbound form
        

    template = loader.get_template('contact_form/contact.html')
    context = RequestContext(request, {
        'form': form,
        'send_mail_fail' : not(sendMailSucess) ,
        'contact_page' : True ,
    })
    
    return HttpResponse(template.render(context))
    
    
def thanks(request):
    
    template = loader.get_template('contact_form/thanks.html')
    
    context = RequestContext(request, {    
    'name' : request.session.get('name', '') ,
    'address' : request.session.get('address', '') ,
    'phone' : request.session.get('phone', '') ,
    'message' : request.session.get('message', '') ,
    'mail': request.session.get('mail' , '') ,    
    })
    
    return HttpResponse(template.render(context))

def insertToSession(form , request):
    
    request.session['name'] = form.cleaned_data['name']
    request.session['address'] = form.cleaned_data['address']
    request.session['phone'] = str(form.cleaned_data['phone'])
    request.session['message'] = form.cleaned_data['message']
    request.session['mail'] = form.cleaned_data['mail']
    

            
def sendMail(subject, form, from_email , recipients):
    '''
    returns true in case there is no exception
    '''
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
    try:
        msg.send()
        return True
    except:
        return False# Create your views here.
