from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model =Post
        fields = '__all__' 

    def to_representation(self, instance: Post):
        
        rep= super().to_representation(instance)
        
        rep['author'] = instance.author.username
        
        return rep

