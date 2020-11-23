from rest_framework import generics, mixins

from technology.models import Technology
from technology.technology_serializers import TechnologySerializer


class TechnologyAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
