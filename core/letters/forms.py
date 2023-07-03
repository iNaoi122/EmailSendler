from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email')
    message = forms.CharField(label='Messsage')
    time = forms.DateTimeField(label='Time_of_sending')
