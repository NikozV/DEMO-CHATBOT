import gradio as gr
import openai
import os

#openai.api_key = os.environ.get("OPENAI_API_KEY", None)
openai.api_key = "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"


def openai_process_message(user_message):
    
    messages = [
        {
            "role": "system",
            "content": "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
        }
    ]
    messages.append({"role": "user", "content": user_message})

    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, max_tokens=2000)

    response_text = openai_response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_text})

    return response_text


examples = [
    "Que es un chatbot?",
    "podrias definir que es una IA?",
    "dime cual seria una receta para hacer salsa bechamel?",
]

demo = gr.Interface(
    fn=openai_process_message,
    inputs=gr.Textbox(lines=5, label='Pregunta',
                      placeholder='Escribe tu pregunta'),
    outputs=gr.Textbox(label='Respuesta'),
    examples=examples,
    title="Chatbot OpenAI API",
)

if __name__ == "__main__":
    demo.launch()
