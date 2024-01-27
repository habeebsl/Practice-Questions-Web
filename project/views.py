from django.shortcuts import render
from .forms import YourForm
from .utils import generate_pq

# Create your views here.

def questionView(request):
    form = YourForm(request.POST or None)
    generated_content = None
    question = None
    selected_option = None

    if request.method == 'POST' and form.is_valid():
        selected_option = form.cleaned_data['choose']
        question = generate_pq(selected_option)
    return render(request, 'practice_question.html', {'form': form, 'selected':selected_option, 'generated_pq':question})
