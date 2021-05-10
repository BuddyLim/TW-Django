from .models import Question
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .forms import QuestionForm


def index(request):
    return get_question(request)

def get_question(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data

            print(data)

            Question.objects.create(
                question_text = data["question_text"],
                pub_date = data["pub_date"]
            )
            # redirect to a new URL:
            return HttpResponseRedirect('thank-you')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'polls/index.html', {'form': form})

def thank_you(request):
    return render(request, 'polls/thank-you.html')