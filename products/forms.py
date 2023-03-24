from django import forms
from .models import ProductReview, ProductPicture, Product, Category
from django.forms.widgets import ClearableFileInput
from django.core.files.base import ContentFile
class MultipleFileInput(ClearableFileInput):
    template_name = 'widgets/multiple_file_input.html'
    input_type = 'file'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['value'] = value or []
        attrs['accept'] = 'image/*'
        return context


class ProductReviewForm(forms.ModelForm):
    stars_given = forms.FloatField(min_value=1, max_value=5)

    class Meta:
        model = ProductReview
        fields = ('stars_given', 'comment')

class LocalProductForm(forms.Form):
    name = forms.CharField(max_length=150, )
    price = forms.DecimalField(max_digits=10, decimal_places=2,)
    description = forms.CharField(widget=forms.Textarea(attrs={'style': 'display:inline-block'}))
    email = forms.EmailField(max_length=150)
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True, 'style': 'display:inline-block'}),required=False)
    category_choices = forms.ChoiceField(choices=[], required=False, label='Choose Category')
    add_category = forms.CharField(max_length=150, required=False, label='or Enter Category')

    def __init__(self, *args, **kwargs):
        super(LocalProductForm, self).__init__(*args, **kwargs)
        self.fields['category_choices'].choices = [(c.id, c.categories) for c in Category.objects.all()]

    def clean(self):
        cleaned_data = super(LocalProductForm, self).clean()
        category_choices = cleaned_data.get('category_choices')
        add_category = cleaned_data.get('add_category')

        if not category_choices and not add_category:
            raise forms.ValidationError('Please choose an existing category or enter a new one.')

        if category_choices and add_category:
            raise forms.ValidationError('Please choose either an existing category or enter a new one, not both.')

        return cleaned_data

    def clean_images(self):
        images = self.cleaned_data.get('images', [])
        return images

    def set_user(self, user):
        self.user = user

    def save(self, product=None, commit=True):
        if product is None:
            product = Product()

        # set the fields of the product instance from the form data
        product.name = self.cleaned_data['name']
        product.price = self.cleaned_data['price']
        product.description = self.cleaned_data['description']
        product.email = self.cleaned_data['email']
        product.local = True
        product.user = self.user

        if self.cleaned_data['category_choices']:
            product.category_id = self.cleaned_data['category_choices']
        elif self.cleaned_data['add_category']:
            category = Category(type='Product', categories=self.cleaned_data['add_category'])
            category.save()
            product.category = category

        # save the product instance to the database
        if commit:
            product.save()

        images = self.files.getlist('images')
        if images:
            for image in images:
                image_data = image.read()
                image_name = image.name
                image_content = ContentFile(image_data, name=image_name)
                ProductPicture.objects.create(product=product, picture=image_content)
        return product










