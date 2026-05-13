from deep_translator import GoogleTranslator
import gradio as gr

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es"
}

def translate_text(text, source_lang, target_lang):

    if text == "":
        return "Please enter text"

    translated = GoogleTranslator(
        source=languages[source_lang],
        target=languages[target_lang]
    ).translate(text)

    return translated

interface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(lines=5, label="Enter Text"),
        gr.Dropdown(list(languages.keys()), label="Source Language"),
        gr.Dropdown(list(languages.keys()), label="Target Language")
    ],
    outputs=gr.Textbox(label="Translated Text"),
    title="Language Translation Tool"
)

interface.launch()