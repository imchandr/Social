from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','img','description', 'display_post']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
        'placeHolder': 'Post title',
        'class': ' w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['img'].widget.attrs.update({
        'placeHolder': 'Post image',
        'class': 'w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['description'].widget.attrs.update({
        'placeHolder': 'Post contents',
        'class': ' w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['display_post'].widget.attrs.update({

        'placeHolder': 'Status',
        'class': ' w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })