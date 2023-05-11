from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserQuestion, Question, MainTest, RegisterTest
from .serializers import UserQuestionSerializer, MainTestSerializer, RegisterTestSerializer, QuestionDetailSerializer, \
    QuestionListSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RegisterTestListAPIView(generics.CreateAPIView):
    queryset = RegisterTest.objects.all()
    serializer_class = RegisterTestSerializer


class MainTestListAPIView(generics.ListAPIView):
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer


class MainTestCheck(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
            ans = self.request.data['answers']
            ans = list(ans)
            if not ans:
                return Response('Error', status=400)
            lst = []
            for i in range(1, len(ans) + 1):
                main = MainTest.objects.filter(id=i).first()
                if not main:
                    return Response('Error', status=400)
                if main.true_answer != ans[i - 1][f'{i}']:
                    lst.append(i)
                    te = UserQuestion.objects.filter(user=self.request.user, question_id=i)
                    if not te:
                        try:
                            quest = Question.objects.get(id=i)
                            test = UserQuestion.objects.create(user=self.request.user, question=quest, is_paid=True)
                            test.save()
                        except:
                            pass
            return Response({'message': f'Sizda {len(lst)} ta savol chiqdi'}, status=200)


class QuestionListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = UserQuestion.objects.filter(user=self.request.user)
        data = []
        for i in queryset:
            question = Question.objects.get(id=i.question_id)
            data.append(dict(
                id=i.question_id,
                question=question.question,
                is_paid=i.is_paid
            ))
        return Response(data, status=200)


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    lookup_field = 'pk'
