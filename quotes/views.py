from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.functions import Random
from .serializers import QuoteSerializer
from .models import Quote
from .throttling import GlobalRateThrottle, IPRateThrottle

# Health Check View
class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        content = {'status': 'ok'}
        return Response(content, status.HTTP_200_OK)

# Random Response API view
class RandomResponseView(APIView):
    permission_classes = [permissions.AllowAny]
    throttle_classes = [GlobalRateThrottle, IPRateThrottle]

    def get(self, request, *args, **kwargs):
        # Get query set (qs)
        qs = Quote.objects.all()

        # Get tag param from request
        tag = request.query_params.get('tag')

        # Filter based on tag param (all quotes tagged 'inspirational')
        if tag:
            qs = qs.filter(tag__iexact=tag)

        # Get a random quote based on filtered list
        quote = qs.order_by(Random()).first()

        # If the quote or tag does not exist, return 404
        if not quote:
            detail = f"No quote found for tag '{tag}'." if tag else "No quotes available."
            return Response({'detail': detail}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and shape payload (200)
        data = QuoteSerializer(quote, context={'request': request}).data
        payload = {
            'type': tag or 'any',
            'count': 1, # Default value for now
            'results': [data]
        }
        return Response(payload, status=status.HTTP_200_OK)