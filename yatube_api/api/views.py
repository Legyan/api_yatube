

from rest_framework import viewsets, permissions
from api.permissions import IsAuthorOrReadOnly
from posts.models import Post
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
