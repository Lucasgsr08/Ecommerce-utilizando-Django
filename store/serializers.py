from rest_framework import serializers
from .models import Product
from .models import Comment

#--------------------------------------------------------
# 🔹 Serializador para exibir e criar produtos via API
#--------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'available', 'image', 'created', 'updated']



#--------------------------------------------------------
# 🔹 Serializador para exibir e criar comentários via API
#--------------------------------------------------------
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # mostra o nome do usuário, não o ID
    total_likes = serializers.SerializerMethodField()  # campo adicional calculado

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'rating', 'created_at', 'updated_at', 'total_likes']

    def get_total_likes(self, obj):
        return obj.total_likes()
