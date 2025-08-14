from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  # author is set in the view

    # (Optional) simple example validation
    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }


        from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Process tags
            tags_str = self.cleaned_data['tags']
            tag_names = [name.strip() for name in tags_str.split(',') if name.strip()]
            tag_objects = []
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                tag_objects.append(tag_obj)
            instance.tags.set(tag_objects)
        return instance
