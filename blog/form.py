from django import forms
from .models import ToDoList, Item


class CreatNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)


class CreateNewToDo(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = ('name', )


class CreateNewItem(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('text', 'completed', )