from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.forms.models import inlineformset_factory

from .models import Question, Choice

# Create a formset for the choices
ChoiceFormSet = inlineformset_factory(
    Question, Choice, fields=("choice_text",), extra=3
)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class CreateQuestionView(generic.CreateView):
    model = Question
    fields = ["question_text"]
    template_name = "polls/create_question.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["choices"] = ChoiceFormSet(self.request.POST)
        else:
            data["choices"] = ChoiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        choices = context["choices"]
        form.instance.pub_date = timezone.now()
        self.object = form.save()
        if choices.is_valid():
            choices.instance = self.object
            choices.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("polls:index")

def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return HttpResponseRedirect(reverse("polls:index"))