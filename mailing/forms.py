from django import forms

from mailing.models import Message
from users.forms import StyleFormMixin

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


def clean(cleaned_data):
    for word in FORBIDDEN_WORDS:
        if word in cleaned_data.lower():
            raise forms.ValidationError(f"Название не может содержать слово: {word}")
    return cleaned_data


class MailingManagerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ("body",)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get("name")
        clean(cleaned_data)

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        clean(cleaned_data)
