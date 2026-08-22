"""Serializers — the pydantic equivalent in the Django world.

A serializer declares the shape of the API's input/output: which fields,
what types, what validation rules. It then does three jobs:
  1. deserialize: JSON dict -> validated Python objects (.is_valid())
  2. validate:    type checks, required checks, custom rules
  3. serialize:   model instance -> JSON-ready dict (.data)
"""

from rest_framework import serializers

from .models import Book


# ---------------------------------------------------------------------------
# 1. A plain serializer — fields declared by hand, like a Django Form.
# ---------------------------------------------------------------------------
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    author = serializers.CharField(max_length=80)
    year = serializers.IntegerField(min_value=1900, max_value=2100)
    rating = serializers.FloatField(min_value=0.0, max_value=10.0)

    # Custom rule, same idea as pydantic's @field_validator.
    def validate_title(self, value: str) -> str:
        if value.strip() == "":
            raise serializers.ValidationError("title cannot be blank")
        return value

    # Save support: plain Serializer doesn't know how to persist, so we
    # show it. (ModelSerializer below gets create/update for free.)
    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)


# ---------------------------------------------------------------------------
# 2. ModelSerializer — fields, create() and update() derived from the model.
#    This is the one you reach for 95% of the time.
# ---------------------------------------------------------------------------
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "year", "rating"]
        # extra_kwargs = {"year": {"min_value": 1900}} would add constraints
