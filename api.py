import os
import google.generativeai as genai

# API Key: AIzaSyABrquE_pgOGRGCi8iCeqBbWZs0FOFYz00

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

genai.configure(api_key="AIzaSyABrquE_pgOGRGCi8iCeqBbWZs0FOFYz00")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What does RBC stand for?")
print(response.text)