import requests

url = "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf"
output_file = "phi-2.Q4_K_M.gguf"

print("Downloading Phi-2 GGUF model...")
response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(output_file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download completed successfully!")
else:
    print(f"Failed to download file. HTTP Status: {response.status_code}")
