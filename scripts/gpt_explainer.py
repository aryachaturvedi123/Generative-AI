import streamlit as st
from huggingface_hub import InferenceClient

# 🔐 Hugging Face Inference Client
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-alpha",
    token=st.secrets["Hugging_face_key"]
)

def get_gpt_explanation(text: str) -> str:
    """
    Sends the article text to Hugging Face Zephyr model and returns the explanation.
    """
    prompt = f"Can you explain the potential biases in this news article?\n\n{text}"

    try:
        response = client.chat_completion(
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        # ✅ Correct way to access the content
        if response and response.choices:
            return response.choices[0].message.content.strip()
        else:
            return "❗ Model did not return a valid response."

    except Exception as e:
        return f"⚠️ Error while generating explanation: {str(e)}"


