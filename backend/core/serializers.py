from rest_framework import serializers
from .models import Attribute, AttributeName, AttributeValue, Catalog, Image, Product, ProductAttributes, ProductImage

from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.source != 'id':
                field.required = False
        

class AttributeNameSerializer(BaseSerializer):
    class Meta:
        model = AttributeName
        fields = '__all__'


class AttributeValueSerializer(BaseSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'


class AttributeSerializer(BaseSerializer):
    nazev_atributu_id = serializers.PrimaryKeyRelatedField(queryset=AttributeName.objects.all())
    hodnota_atributu_id = serializers.PrimaryKeyRelatedField(queryset=AttributeValue.objects.all())
    class Meta:
        model = Attribute
        fields = '__all__'


class CatalogSerializer(BaseSerializer):
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())
    class Meta:
        model = Catalog
        fields = '__all__'


class ImageSerializer(BaseSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(BaseSerializer):
    published_on = serializers.DateTimeField(allow_null = True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAttributesSerializer(BaseSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = ProductAttributes
        fields = '__all__'


class ProductImageSerializer(BaseSerializer):
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductImage
        fields = '__all__'


SERIALIZERS_DICT = {
    'attributename': AttributeNameSerializer,
    'attributevalue': AttributeValueSerializer,
    'attribute': AttributeSerializer,
    'catalog': CatalogSerializer,
    'image': ImageSerializer,
    'product': ProductSerializer,
    'productattributes': ProductAttributesSerializer,
    'productimage': ProductImageSerializer,
}