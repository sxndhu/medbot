from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from .open_ai_key import secret_key

openai_api_key = secret_key
openai.api_key = openai_api_key

# Create your views here.

def ask_medbot(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are Medbot, a helpful virtual assistant for a nurse"},
            {"role": "user", "content": "What can you help me with?"},
            {"role": "assistant", "content": "I can provide medical literature, information about symptoms and diseases."},
            {"role": "user", "content": message},
        ],
        max_tokens = 300,
        temperature = 0.4,
    )
    print(response)
    required_response = response['choices'][0]['message']['content']
    return required_response

def chatapp(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_medbot(message)
        return JsonResponse({'message' : message, 'response' : response})
    return render (request, 'chatapp.html')

def screening(request):
    screening_questions = {
        'q1' : 'What brings you here today?',
        'q2' : 'Where does it hurt and does it radiate?',
        'q3' : 'When did it start/how long has it been going on for?',
        'q4' : 'Is it a new problem?',
        'q5' : 'What is the quality of the pain? (Dull, sharp/knife like, achy, tightness, tingling, etc.)',
        'q6' : 'What triggered the symptoms?',
        'q7' : 'What makes it better or worse?',
        'q8' : 'Any recent illnesses? (Infections, allergies, etc.)',
        'q9' : 'Any recent injuries or traumas?',
        'q10' : 'Any family history?',
        'q11' : 'Any trouble in the daily routine?'
    }
    if request.method == 'POST':
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4 = request.POST['answer4']
        answer5 = request.POST['answer5']
        answer6 = request.POST['answer6']
        answer7 = request.POST['answer7']
        answer8 = request.POST['answer8']
        answer9 = request.POST['answer9']
        answer10 = request.POST['answer10']
        answer11 = request.POST['answer11']

        screening_answers = {
            'a1' : answer1,
            'a2' : answer2,
            'a3' : answer3,
            'a4' : answer4,
            'a5' : answer5,
            'a6' : answer6,
            'a7' : answer7,
            'a8' : answer8,
            'a9' : answer9,
            'a10' : answer10,
            'a11' : answer11
        }
        
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant for a nurse who is asking patients questions"},
                {"role": "user", "content": "What can you help me with?"},
                {"role": "assistant", "content": "After I get the anaswers given by the patient, I will give only the possible diagnoses, treatment and further suggestions."},
                {"role": "user", "content": f"These are the questions: {screening_questions} and their answers: {screening_answers}, give the possible diagnoses only"},

            ],
            max_tokens = 300,
            temperature = 0.4,
        )
        # print(response)
        required_response = response['choices'][0]['message']['content']
        return render(request, 'screening.html', {'response' : required_response}) 

    
    return render(request, 'screening.html')