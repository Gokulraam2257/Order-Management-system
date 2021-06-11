from django.db import models, transaction
import uuid


class customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50, null=True)
    l_name = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True)
    street_address = models.CharField(max_length=50, null=True)
    town = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=50, null=True)

    contact = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    # status=models.BooleanField()

    def __str__(self):
        return self.f_name

    class Meta:
        db_table = 'tbl_customers'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=100)  # apptitude,true,para
    prod_code = models.CharField(max_length=100)
    prod_rate = models.FloatField(max_length=100)
    prod_gst = models.FloatField(max_length=100)
    prod_stock = models.BigIntegerField()

    def __str__(self):
        return self.prod_name

    class Meta:
        db_table = 'tbl_products'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Order(models.Model):

    ord_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    ord_date = models.DateTimeField(auto_now_add=True)  # apptitude,true,para
    cust = models.ForeignKey(customer,  on_delete=models.CASCADE)
    tot_price = models.FloatField(max_length=100)

    def __str__(self):
        return '{}'.format(self.ord_id)

    class Meta:
        db_table = 'tbl_order'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Order_detail(models.Model):
    det_id = models.AutoField(primary_key=True)
    ord = models.ForeignKey(Order, on_delete=models.CASCADE)
    prod = models.ForeignKey(
        Products, on_delete=models.CASCADE)  # apptitude,true,para
    ord_qty = models.BigIntegerField()
    itm_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.det_id)

    class Meta:
        db_table = 'tbl_order_details'

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
