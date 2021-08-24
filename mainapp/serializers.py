from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Category, Product


class ProductListSerializers(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name', read_only='True')
    features = serializers.SlugRelatedField(
        slug_field='feature', read_only='True', many=True)

    class Meta:
        model = Product
        exclude = ('slug',)
