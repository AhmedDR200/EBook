from rest_framework import generics, mixins
from .serializers import EbookSerializer, ReviewSerializer
from .models import Ebook, Review
from rest_framework import permissions
from .pagination import SmallSet


class EbookListCreate(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class EbookDetail(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class Reviews(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by("-id")
    serializer_class = ReviewSerializer
    permission_classes = (permissions.AllowAny, )
    pagination_class = SmallSet


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
