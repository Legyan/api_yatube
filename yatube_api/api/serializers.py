from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор постов."""

    author = SlugRelatedField(slug_field='username', read_only=True)
    image = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор групп."""

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'created', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    """Сериализатор подписок."""

    following = serializers.CharField()

    class Meta:
        model = Follow
        fields = '__all__'

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
