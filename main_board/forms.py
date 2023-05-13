from django import forms
from .models import Post, Message
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['author','title','text','image','category']

class MessageForm(forms.ModelForm):
   class Meta:
       model = Message
       fields = ['sender','text','post']
