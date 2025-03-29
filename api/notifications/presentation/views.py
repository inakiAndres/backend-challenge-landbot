from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ...utils.normalization import normalize_keys 
from .serializers import NotificationSerializer
from ..application.use_cases import SendNotificationUseCase


@api_view(['POST'])
def post_notifications(request):
    
    normalized_data = normalize_keys(request.data)
    serializer = NotificationSerializer(data=normalized_data)

    if serializer.is_valid():
        
        topic = serializer.validated_data["topic"]
        description = serializer.validated_data["description"]
        
        use_case = SendNotificationUseCase()
        try:
            notification_id = use_case.execute(topic, description)
            data = {"request_id": notification_id}
            return Response(data, status=status.HTTP_202_ACCEPTED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
