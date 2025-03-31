from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.utils.normalization import normalize_keys 
from api.notifications.presentation.serializers import NotificationSerializer
from api.notifications.application.use_cases.send_notification import SendNotificationUseCase


@api_view(['POST'])
def post_notifications(request):
    
    normalized_data = normalize_keys(request.data)
    serializer = NotificationSerializer(data=normalized_data)

    if serializer.is_valid():
        
        topic = serializer.validated_data["topic"]
        description = serializer.validated_data["description"]
        
        use_case = SendNotificationUseCase()
        try:
            data = use_case.execute(topic, description)
            return Response(data, status=status.HTTP_202_ACCEPTED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
