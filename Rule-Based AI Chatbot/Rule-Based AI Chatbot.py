import gradio as gr


def get_answer(question):
    question = question.strip().lower()

    knowledge = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! What would you like to know?",
        "how are you": "I'm doing well. Thank you for asking!",
        "what is the capital of france": "The capital of France is Paris.",
        "who is elon musk":
            "Elon Musk is a businessman associated with companies such as Tesla and SpaceX.",
        "what color is this apple": "This apple is green.",
        "what is ai":
            "Artificial Intelligence is the development of computer systems "
            "that can perform tasks that normally require human intelligence."
    }

    if not question:
        return "Please ask a question."

    if question in ["exit", "quit", "bye"]:
        return "Goodbye!"

    return knowledge.get(
        question,
        "I don't know the answer yet. Please try another question."
    )


demo = gr.Interface(
    fn=get_answer,
    inputs=gr.Textbox(
        label="Your Question",
        placeholder="Ask me something..."
    ),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Rule-Based AI Chatbot",
    description="A simple chatbot that responds using predefined rules."
)

demo.launch()