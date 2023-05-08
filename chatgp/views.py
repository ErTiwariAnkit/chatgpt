from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import openai
import os
def chatgp(message):
    openai.api_key = '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'
    messages = [
    {"role": "system", "content" : "You’re a kind helpful assistant"}
    ]
    content = message
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    chat_response = completion.choices[0].message.content
    #print(f'ChatGPT: {chat_response}')
    return chat_response
def submit(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-field')
        # Do some processing with the input text here...
        response=chatgp(input_text)
        output_text = response
        response_message_lines = output_text.split('\n')
        response_message_formatted = ''
        for i, line in enumerate(response_message_lines):
            response_message_formatted += f'<p>{line}</p>'
            print(response_message_formatted)
        # Pass the formatted response message to the template
        context = {
            'response_message': response_message_formatted
        }
        #return render(request, 'chatgp/chatgp.html', context)
        return JsonResponse({'response': response_message_formatted})
    else:
        return render(request, 'chatgp/chatgp.html')
