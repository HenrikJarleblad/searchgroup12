from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from time import sleep
import queryAnalyzer



@api_view(['GET'])
def answer(request):

  """
  API endpoint that retunrs answer to a question
  """

  question = request.GET['question']
  sleep(0.5)
  try:
    answerDic = queryAnalyzer.getAnswers(question)
    answer = answerDic['answer']
  except IndexError:
    answer = "Jag har inget svar på din fråga: " + question
    answerDic = {"confidence": 1}

  return Response({"answer": answer, "confidence": answerDic['confidence']})
