from llama_cpp import Llama

# Load your local GGUF model
llm_model = Llama(
    model_path="mistral-7b-instruct-v0.2.Q2_K.gguf",  # ✅ Use exact filename
    n_ctx=512,  # context window size, adjust as needed
    verbose=False
)

# ✅ Function that takes a prompt and returns the response
def llm(prompt: str) -> str:
    response = llm_model.create_chat_completion(
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=256,
        stop=["</s>"]
    )
    return response["choices"][0]["message"]["content"].strip()
