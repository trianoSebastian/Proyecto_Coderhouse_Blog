from django import forms
from .models import Post,Comment,User,Avatar
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('__all__')
 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1','password2',]     
        
class CommentForm(forms.ModelForm):
    content=forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows':4
    }))
    class Meta:
        model=Comment
        fields=('content',)

class AvatarForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('__all__')

class UserEditForm(forms.ModelForm):
    user_name=forms.CharField(label='Username')
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    

    class Meta:
        model=User
        fields=['user_name','email','password1','password1']
        help_text={k:"" for k in fields}
