from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Comment, LikeComment
from .serializers import CommentSerializer
from  rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()

class CommentViewsSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
    # if detail=True in urls appemd id
    @action(['POST'], detail=False)
    def like(self, request):
        author_id=request.data.get('author')
        comment_id = request.data.get('comment')
        author = get_object_or_404(User, id=author_id)
        # print(author)
        comment = get_object_or_404(Comment,id=comment_id)
        if LikeComment.objects.filter(author=author, comment=comment).exists():
            LikeComment.objects.filter(author=author, comment=comment).delete()
        else:
            LikeComment.objects.create(author=author, comment=comment)
        return Response(status=201)
        # return Response('ok')
        









