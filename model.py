import requests

# Replace this with your own Hugging Face token
HF_TOKEN = "your_hugging_face_token_here"

API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_comment(code_snippet: str) -> str:
    # Creating a prompt to ask for a code explanation
    prompt = f"Explain the specific functionality of this Python code:\n\n{code_snippet}\n\nProvide a detailed comment about what this code does."
    
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()
        if "error" in result:
            return f"⚠️ API Error: {result['error']}"
        return result[0]["generated_text"].split("Comment:")[-1].strip()
    except Exception as e:
        return f"❌ Failed to generate comment: {e}"
