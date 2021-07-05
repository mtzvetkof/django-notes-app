from django import forms

from notes.note.models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            ),
        }