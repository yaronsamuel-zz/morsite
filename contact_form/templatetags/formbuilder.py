from contact_form.contact_form import ContactForm
from django import template


register = template.Library()

def build_contact_form(parser, token):
    """
    {% menu menu_name %}
    """
    return ContactFormObject()

    
class ContactFormObject(template.Node):

    def render(self, context):

        context['form'] = ContactForm()

            
        return ''
    
register.tag('contact_form_tag', build_contact_form)

