from django import forms
from django.contrib.comments.forms import CommentForm

from django.utils.translation import ungettext, ugettext, ugettext_lazy as _

class MyCommentForm(CommentForm):    
    email   = forms.EmailField(label=_("Email address") , required=False)
    name          = forms.CharField(label=_("Name"), max_length=50 , required=False)
