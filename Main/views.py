from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question, Language, Option
# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"

firstQuestion = Question.objects.get(is_first=True)
nextQuestion = firstQuestion

def survey(req):
    global nextQuestion

    if req.method == 'POST':
        option_id = req.POST['answer']
        option = Option.objects.get(id=int(option_id))
        if option.language:
            return render(req, "survey.html", {
                'language': option.language,
            })
        else:
            nextQuestion = option.next_question
            return render(req, "survey.html", {
                'question': nextQuestion,
                'options': nextQuestion.options.all(),
            })
    

    return render(req, "survey.html", {
        'question': firstQuestion,
        'options': firstQuestion.options.all(),
    })