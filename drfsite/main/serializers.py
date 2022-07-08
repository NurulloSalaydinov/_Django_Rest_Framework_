from rest_framework import serializers



class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=555)
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()