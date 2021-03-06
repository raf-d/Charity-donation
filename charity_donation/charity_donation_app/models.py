from django.db import models

ORGANIZATIONS = (
    ('1', 'Fundacja'),
    ('2', 'Organizacja pozarządowa'),
    ('3', 'Zbiórka lokalna')
)


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Category name')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=32, verbose_name='Institution name')
    description = models.CharField(max_length=100, verbose_name='Description')
    type = models.CharField(max_length=32, choices=ORGANIZATIONS, default='1')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def categories_id(self):
        categories_list = self.categories.all()
        categories_id_list = [str(cat.id) for cat in categories_list]
        return ';'.join(categories_id_list)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.quantity} bags picked up {self.pick_up_date}'


# class CheckValid(models.Model):
#