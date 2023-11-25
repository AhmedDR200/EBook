from rest_framework import serializers
from .models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only=True, many=True)
    class Meta:
        model = Ebook
        fields = '__all__'