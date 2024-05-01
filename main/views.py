from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core import settings
from .models import Test, Question, CheckTest, CheckQuestion
from .forms import TestForm, QuestionForm
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.utils.timezone import datetime
from django.db.models import Q


# Create your views here.

# @login_required(login_url="login")

def index(request):
    tests = Test.objects.all()
    if request.method == "GET":
        query = request.GET.get('q', "")
        tests = Test.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
    return render(request, "index.html", {'tests': tests})


@login_required(login_url="login")
def my_tests(request):
    tests = Test.objects.filter(author=request.user)
    return render(request, "my_tests.html", {'tests': tests})


@login_required(login_url="login")
def create_test(request):
    form = TestForm()
    if request.method == "POST":
        form = TestForm(data=request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            form.save(commit=True)
            return redirect("index")
        else:
            return render(request, "create_test.html", {"form": form})
    return render(request, "create_test.html", {"form": form})


@login_required(login_url="login")
def create_question(request, test_id):
    test = Test.objects.get(id=test_id)
    form = QuestionForm()

    if request.method == "POST":
        add_again = request.POST.get("add-again")
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.test = test
            form.save(commit=True)
            if add_again == "on":
                return redirect("create_question", test.id)
            else:
                return redirect("kirish")
        else:
            return render(request, "create_question.html", {'form': form, "test": test})
    return render(request, "create_question.html", {'form': form, "test": test})


@login_required(login_url="login")
def update_test(request, test_id):
    test = Test.objects.get(id=test_id)
    user = request.user

    if user == test.author:
        form = TestForm(instance=test)
        if request.method == "POST":
            form = TestForm(instance=test, data=request.POST, )
            if form.is_valid():
                form.save()
                return redirect("my_tests")
            else:
                return render(request, "update_test.html", {"form": form, 'test': test})
        return render(request, "update_test.html", {"form": form, 'test': test})
    else:
        messages.error(request, "Bu test sizga tegishli emas!")
        return redirect('index')


@login_required(login_url="login")
def detail_test(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test=test)

    return render(request, "detail_test.html", {"test": test, "questions": questions})


@login_required(login_url="login")
def update_question(request, question_id):
    question = Question.objects.get(id=question_id)
    user = request.user
    author = question.test.author

    if user == author:
        form = QuestionForm(instance=question)
        if request.method == "POST":
            form = QuestionForm(instance=question, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Savol muvaffaqiyatli yangilangi.")
                return redirect("detail_test", question.test.id)
            else:
                return render(request, "update_question.html", {"form": form, "question": question})

        return render(request, "update_question.html", {"form": form, "question": question})
    else:
        messages.error(request, "Bu savol sizga tegishli emas!")
        return redirect('index')


@login_required(login_url="login")
def ready_to_test(request, test_id):
    test = Test.objects.get(id=test_id)
    attemps = CheckTest.objects.filter(test=test, student=request.user).count()
    if str(test.start_date) > str(datetime.now()):
        return HttpResponse("Testni boshlanish vaqti kelmagan.")
    elif str(test.end_date) < str(datetime.now()):
        return HttpResponse("Testni  vaqti o'tib ketgan.")
    elif attemps >= test.maximum_attemps:
        return HttpResponse("Urunishlar tugadi")
    else:
        return render(request, "ready_to_test.html", {'test': test})


from random import sample


import random

@login_required(login_url="login")
def test(request, test_id):
    test = Test.objects.get(id=test_id)
    attemps = CheckTest.objects.filter(test=test, student=request.user).count()
    all_questions = list(Question.objects.filter(test=test))

    if str(test.start_date) > str(datetime.now()):
        return HttpResponse("Testni boshlanish vaqti kelmagan.")
    elif str(test.end_date) < str(datetime.now()):
        return HttpResponse("Testni vaqti o'tib ketgan.")
    elif attemps >= test.maximum_attemps:
        return HttpResponse("Urinishlar tugadi")
    else:
        if request.method == "POST":
            checktest = CheckTest.objects.create(student=request.user, test=test)
            for question in all_questions:
                answer = request.POST.get(str(question.id))
                if answer:  # Check if answer is provided
                    true_answer = question.true_answer
                    CheckQuestion.objects.create(checktest=checktest, question=question, given_answer=answer,
                                                 true_answer=true_answer)
                else:
                    # Handle the case when no answer is provided for a question
                    # For simplicity, let's print an error message
                    print(f"No answer provided for question ID {question.id}")

            messages.info(request, "Testni yechib bo'ldingiz.")
            checktest.save()
            return redirect("check_test", checktest.id)

        # Randomly shuffle the order of questions
        random.shuffle(all_questions)
        # Select the first 10 questions
        questions = all_questions[:min(10, len(all_questions))]

        return render(request, "test.html", {"questions": questions, "test": test})



@login_required(login_url='login')
def check_test(request, checktest_id):
    checktest = CheckTest.objects.get(id=checktest_id)
    checkquestions = CheckQuestion.objects.filter(checktest=checktest)
    if request.user == checktest.student:
        return render(request, "checktest.html", {"checktest": checktest, "checkquestions": checkquestions})
    else:
        raise Http404("Siz ushbu testni yechmagansiz")


@login_required(login_url='login')
def my_results(request):
    # tests = Test.objects.all()
    check_tests = CheckTest.objects.filter(student=request.user)
    tests = []
    for checktest in check_tests:
        if not checktest.test in tests:
            tests.append(checktest.test)

    return render(request, "my_results.html", {'tests': tests, "checktests": check_tests})


@login_required(login_url='login')
def results(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.user == test.author:
        checktests = CheckTest.objects.filter(test=test)
        return render(request, "results.html", {"checktests": checktests, "test": test})
    else:
        messages.error(request, "Siz bu testni yaratmagansiz.")
        return redirect("index")


@login_required(login_url="login")
def certificate(request):
    test = Test.objects.all()
    checktest = CheckTest.objects.filter(student_id=request.user.id).order_by('-id').first()
    # if checktest is not None:
    percentage = checktest.percentage
    user = request.user
    full_name = user.first_name + ' ' + user.last_name
    context = {'test': test, 'percentage': percentage, 'full_name': full_name}
    return render(request, 'certificate.html', context)



