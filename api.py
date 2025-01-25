import google.generativeai as genai

# API Key: AIzaSyABrquE_pgOGRGCi8iCeqBbWZs0FOFYz00

genai.configure(api_key="AIzaSyABrquE_pgOGRGCi8iCeqBbWZs0FOFYz00")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)