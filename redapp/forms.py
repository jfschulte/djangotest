from django import forms
from redapp.models import Page, Category, UserProfile
from django.contrib.auth.models import User
from django.conf import settings

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.CharField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        fields = ('title', 'url')

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        print "url is " + url

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())



    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password']:
            self.fields[fieldname].help_text = '*'



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')