from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsOrganizationOwner

from .models import Organization
from .serializers import OrganizationSerializer

# Create your views here.

class OrganizationListCreateView(generics.ListCreateAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Organization.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsOrganizationOwner]

    def get_queryset(self):
        return Organization.objects.filter(owner=self.request.user)
    