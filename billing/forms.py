
from django import forms
from django.forms import Form
from django.forms import formset_factory
from billing.models import Order, Order_detail, customer, Products


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = "__all__"


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['tot_price'].widget.attrs['readonly'] = True
        self.fields['tot_price'].widget.attrs.update(
            {'class': 'form-control', 'name': 'subtotal'})
        self.fields['cust'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prod'].queryset = Products.objects.filter()
        self.fields['prod'].widget.attrs.update(
            {'class': ' form-control ', 'required': 'true'})
        self.fields['ord_qty'].widget.attrs.update(
            {'class': ' form-control ', 'min': '0', 'required': 'true'})
        self.fields['itm_price'].widget.attrs.update(
            {'class': ' form-control ', 'min': '0', 'required': 'true'})

    class Meta:
        model = Order_detail
        fields = '__all__'


# formset used to render multiple 'SaleItemForm'
OrderItemFormset = formset_factory(OrderItemForm, extra=1)
