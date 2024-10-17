from django import forms 


# class BikeForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     company = forms.CharField(max_length=100)
#     price = forms.IntegerField()
#     color = forms.CharField(max_length=100)

class UserProfile(forms.Form):
    username = forms.CharField(max_length=100)
    age = forms.IntegerField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    
    def clean_username(self):
        uname=self.cleaned_data['username']
        if ord(uname[0])>=48 and ord(uname[0])<=57:
            raise forms.ValidationError('name should not start with numbers')
        return uname
    def clean_age(self):
        age=self.cleaned_data['age']
        if age<1:
            raise forms.ValidationError('age should be positive')
        return age
    def clean_phone(self):
        phone =self.cleaned_data['phone']
        if len(str(phone))!=10:
            raise forms.ValidationError('phone number should be 10 digits')
        return phone
    
    def clean_password2(self):
        password2=self.cleaned_data['password2']
        password1=self.cleaned_data['password1']
        if password2!=password1:
            raise forms.ValidationError('password must be same')
        return password2