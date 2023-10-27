
# fitness_app/forms.py
from django import forms
from .models import UserProfile, FitnessTip
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'sex', 'address', 'profile_image']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def save(self, commit=True):
        instance = super(UserProfileForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class FitnessTipForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = FitnessTip
        fields = ['title', 'cover_image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super(FitnessTipForm, self).save(commit=False)
        instance.author = self.user  # Assign the author as the currently logged-in user
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FitnessTipForm, self).__init__(*args, **kwargs)
