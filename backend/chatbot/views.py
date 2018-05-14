from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import queryAnalyzer


@api_view(['GET'])
def answer(request):

  """
  API endpoint that retunrs answer to a question
  """

  question = request.GET['question']
  answer = queryAnalyzer.getAnswers(question)

  return Response({"answer": answer})
