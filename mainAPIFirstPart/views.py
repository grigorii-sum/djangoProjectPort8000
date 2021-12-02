from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils import create_random_code
from .models import IdentifierCode, LogMessage
from .serializers import IdentifierCodeSerializer


# Endpoint for creating IdentifierCode
@api_view(['POST'])
def identifier_code_create(request):
    request.data["code"] = create_random_code()

    serializer = IdentifierCodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# Endpoint for creating LogMessage
@api_view(['POST'])
def log_message_create(request):
    try:
        required_identifier_code = IdentifierCode.objects.get(identifier=request.data["identifier"], code=request.data["code"])

        LogMessage.objects.create(id_identifier_code=required_identifier_code, text_message=request.data["text_message"])

        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
