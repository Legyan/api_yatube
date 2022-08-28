from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор постов."""

    author = SlugRelatedField(slug_field='username', read_only=True)
    image = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор групп."""

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    """Сериализатор подписок."""

    following = serializers.CharField()

    class Meta:
        fields = '__all__'
        model = Follow

    def create(self, validated_data):
        following_username = validated_data.pop('following')
        user = validated_data['user']
        following = User.objects.get(username=following_username)
        if user == following:
            raise serializers.ValidationError(
                'Невозможно подписаться на самого себя')
        if user.follower.select_related('following').filter(
                following=following):
            raise serializers.ValidationError(
                'Вы уже подписаны на этого автора.')
        follow = Follow.objects.create(following=following, **validated_data)
        return follow
