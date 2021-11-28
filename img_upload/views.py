from .serializers import ImageSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated

# @permission_classes([IsAuthenticated]) # включить этот декоратор - загрузка изображений будет доступна только авторизованным пользователям
@parser_classes([MultiPartParser, FormParser])
class ImageUploadView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file') # забираем список файлов из запроса
        results = []
        for file in files:
            file_dict = {}
            file_dict['file'] = file # переводим файл из запроса в словарь для сериализатора
            file_serializer = ImageSerializer(data=file_dict)
            if file_serializer.is_valid(raise_exception=True):
                file_serializer.save()
                results.append(file_serializer.data) # добавляем в список с результатами
        return Response(results, status=status.HTTP_201_CREATED)
