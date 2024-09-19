from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from questions.forms import QuestionForm ,TagForm ,SearchForm , AnswerForm
from questions.models import Question, Answer, Tag


def question_detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'question/question_detail_view.html', {'question': question})


def question_list_view(request):
    questions = Question.objects.all()
    return render(request, 'question/question_list_view.html', {'questions': questions})


def question_update_view(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, id=question_id)
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated successfully')
    else:
        question = get_object_or_404(Question, id=question_id)
        form = QuestionForm(instance=question)

    return render(request, 'question/question_form.html', {'form': form})

def question_delete_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    messages.success(request, 'Question deleted successfully')
    return redirect('questions:question_list')


def question_upvote_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.user not in question.upvoters.all() and request.user not in question.downvoters.all():
        question.upvoters.add(request.user)
        messages.success(request, 'Question upvoted successfully')
    else:
        messages.success(request, 'You already upvoted this question')
    return redirect('questions:question_detail', question_id=question_id)

def question_downvote_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.user not in question.downvoters.all() and request.user not in question.upvoters.all():
        question.downvoters.add(request.user)
        messages.success(request, 'Question downvoted successfully')
    else:
        messages.success(request, 'You already downvoted this question')
    return redirect('questions:question_detail', question_id=question_id)


def question_create_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.user = request.user
            new_question.save()
            messages.success(request, 'Question created successfully')
    else:
        form = QuestionForm()

    return render(request, 'question/question_form.html', {'form': form})


def question_search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            questions = Question.objects.filter(title__icontains=query)
        else:
            questions = []
    else:
        form = SearchForm()
        questions = []

    return render(request, 'question/question_search.html', {'form': form, 'questions': questions})
def answer_create_view(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.user = request.user
            new_answer.question = get_object_or_404(Question, id=question_id)
            new_answer.save()
            messages.success(request, 'Answer created successfully')
    else:
        form = AnswerForm()

    return render(request, 'question/question_form.html', {'form': form})


def answer_update_view(request, answer_id):
    if request.method == 'POST':
        answer = get_object_or_404(Answer, id=answer_id)
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Answer updated successfully')
    else:
        answer = get_object_or_404(Answer, id=answer_id)
        form = AnswerForm(instance=answer)

    return render(request, 'question/question_form.html', {'form': form})

def answer_delete_view(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answer.delete()
    messages.success(request, 'Answer deleted successfully')
    return redirect('questions:question_detail', question_id=answer.question.id)


def answer_upvote_view(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.upvoters.all() and request.user not in answer.downvoters.all():
        answer.upvoters.add(request.user)
        messages.success(request, 'Answer upvoted successfully')
    else:
        messages.success(request, 'You already upvoted this answer')
    return redirect('questions:question_list')


def answer_downvote_view(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.upvoters.all() and request.user not in answer.downvoters.all():
        answer.downvoters.add(request.user)
        messages.success(request, 'Answer downvoted successfully')
    else:
        messages.success(request, 'You already downvoted this answer')
    return redirect('questions:question_list')


def tag_list_view(request):
    tags = Tag.objects.all()
    return render(request,'tag/tag_list_view.html',{'tags' : tags})


def tag_create_view(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TagForm()

    return render(request, 'tag/create_tag_form.html', {'form': form})

