import requests

HF_TOKEN = "put your token here"

API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_comment(code_snippet: str) -> str:
    prompt = f"""
    Please explain the following Python code in detail, step-by-step. 
    Include the purpose of each part of the code, including the loop and the list operations.
    
    Code:
    {code_snippet}
    
    Detailed Comment:
    """
    
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 150}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  
        
        result = response.json()
        
        if "error" in result:
            return f"⚠️ API Error: {result['error']}"
        
        return result[0]["generated_text"].strip()
        
    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {e}"
    except Exception as e:
        return f"❌ Failed to generate comment: {e}"
