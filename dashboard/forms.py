from django import forms

from .models import userdb

class user_registry(forms.ModelForm):
    class Meta:
        model = userdb
        fields = ['uname',
                  'passwd'
                  ]
    def __init__(self, *args, **kwargs):
        super(user_registry, self).__init__(*args, **kwargs)
        self.fields['uname'].label = "Username"
        self.fields['passwd'].label = "Password"