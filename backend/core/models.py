from django.db import models
from django_extensions.db.models import (
	TimeStampedModel, 
	TitleDescriptionModel
)

class AttributeName(
	TimeStampedModel, 
	TitleDescriptionModel,
	):

	class Meta:
		verbose_name_plural = "Attribute names"


	id = models.IntegerField(verbose_name="Id", primary_key=True)
	nazev = models.CharField(verbose_name="nazev", default="", max_length=256)
	zobrazit = models.BooleanField(verbose_name="zobrazit", default=True)
	kod = models.CharField(max_length=255, verbose_name="kod", default="")
	def __str__(self):
		return f'{self.title}'

class AttributeValue(
	TimeStampedModel, 
	TitleDescriptionModel,
	):

	class Meta:
		verbose_name_plural = "Attribute values"


	id = models.IntegerField(verbose_name="Id", primary_key=True)
	hodnota = models.CharField(verbose_name="hodnota", max_length=256)

	def __str__(self):
		return f'{self.title}'
	
class Attribute(
	TimeStampedModel, 
	TitleDescriptionModel,
	):

	class Meta:
		verbose_name_plural = "Attributes"


	id = models.IntegerField(verbose_name="id", primary_key=True)
	nazev_atributu_id = models.ForeignKey(AttributeName, name="nazev_atributu_id", on_delete=models.CASCADE)
	hodnota_atributu_id = models.ForeignKey(AttributeValue, name="hodnota_atributu_id", on_delete=models.CASCADE)
	
	def __str__(self):
		return f'{self.title}'

class Product(
	TimeStampedModel, 
	TitleDescriptionModel,
	):

	class Meta:
		verbose_name_plural = "Attributes"


	id = models.IntegerField(verbose_name="id", primary_key=True)
	nazev = models.CharField(verbose_name="nazev", default="", max_length=1024)
	description = models.CharField(verbose_name="description", default="", max_length=5012)
	cena = models.CharField(verbose_name="cena", default="", max_length=256)
	mena = models.CharField(verbose_name="měna", default="", max_length=256)
	published_on = models.DateTimeField(verbose_name="published_on", default=None, null=True)

	is_published = models.BooleanField(verbose_name="is_published", default=False)

	def __str__(self):
		return f'{self.title}'

class ProductAttributes(
	TimeStampedModel, 
	TitleDescriptionModel,
	):

	class Meta:
		verbose_name_plural = "Attributes"


	id = models.IntegerField(verbose_name="Id", primary_key=True)
	attribute = models.ForeignKey(Attribute, name="attribute", on_delete=models.CASCADE)
	product = models.ForeignKey(Product, name="product", on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.title}'

class Image(
	TimeStampedModel, 
	TitleDescriptionModel,
	):

	class Meta:
		verbose_name_plural = "Attributes"


	id = models.IntegerField(verbose_name="Id", primary_key=True)
	nazev = models.CharField(verbose_name="nazev", default="", max_length=256)
	obrazek = models.CharField(name="obrazek", default="", max_length=5012)
	def __str__(self):
		return f'{self.title}'

class ProductImage(
	TimeStampedModel, 
	TitleDescriptionModel,
	):
	class Meta:
		verbose_name_plural = "Attributes"
	id = models.IntegerField(verbose_name="Id", primary_key=True)
	product = models.ForeignKey(Product, verbose_name="product", default=None, on_delete=models.CASCADE)
	obrazek_id = models.ForeignKey(Image, name="obrazek_id", default=None, on_delete=models.CASCADE)
	nazev = models.CharField(verbose_name="nazev", default="", max_length=256)
	
	def __str__(self):
		return f'{self.title}'

class Catalog(models.Model):
	nazev = models.CharField(max_length=255)
	obrazek_id = models.ForeignKey(Image, name="obrazek_id", default=None, on_delete=models.CASCADE)
	zalozeno = models.DateField(verbose_name="zalozeno", default=None, null=True)
	products_ids = models.ManyToManyField(Product, related_name="products_ids")
	attributes_ids = models.ManyToManyField(Attribute, related_name="attributes_ids")

	def __str__(self):
		return self.nazev


#Dict to get model from its name.
MODELS_DICT = {
    'AttributeName': AttributeName,
    'AttributeValue': AttributeValue,
    'Attribute': Attribute,
    'Product': Product,
    'ProductAttributes': ProductAttributes,
    'Image': Image,
    'ProductImage': ProductImage,
    'Catalog': Catalog,
}