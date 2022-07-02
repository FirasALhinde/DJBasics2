
from django import forms
from.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # field=['title','content']
        fields ='__all__'
        exclude =('publish_date',)



