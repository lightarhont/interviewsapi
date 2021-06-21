from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Interview
from django.contrib.auth.models import User
from .serializers import InterviewsSerializer, InterviewSerializer
from .service import reply_question, parse_qr, get_user


# Create your views here.
class InterviewsView(APIView):
    
    def get(self, request):
        interviews = Interview.objects.all()
        serializer = InterviewsSerializer(interviews, many=True)
        return Response({"interviews": serializer.data})
    
    
class InterviewView(APIView):
    
    def get(self, request, pk):
        interview = Interview.objects.filter(id=pk).first()
        serializer = InterviewSerializer(interview)
        return Response({"interview": serializer.data})
    
    def post(self, request, pk):
        '''
        {"userid": 1, "question": 1, "reply": [1, 2]}
        '''
        r = reply_question(request.data)
        return Response(r)


class UserView(APIView):
    
    def get(self, request, pk):
        u = get_user(pk)
        try:
            uql = [(e, u) for e in u.question.all()]
        except Exception:
            pqr = dict(status=False, error_id=1, msg='User not found in system')
        else:
            pqr = parse_qr(uql)
        return Response(pqr)
        