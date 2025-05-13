from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'quantity', 'location', 'code', 'description', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 10 * 1024 * 1024:  # 10MB
                raise forms.ValidationError("O tamanho da imagem não deve exceder 10MB.")
        return image
