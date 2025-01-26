import os
import google.generativeai as genai

# API Key: AIzaSyABrquE_pgOGRGCi8iCeqBbWZs0FOFYz00

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

def prompt_gemini(report_dict):
    genai.configure(api_key="AIzaSyABrquE_pgOGRGCi8iCeqBbWZs0FOFYz00")
    model = genai.GenerativeModel("gemini-1.5-flash")
    query = create_query(report_dict)
    response = model.generate_content(query)
    #print("\n", response.text)
    return response.text

def create_query(report_dict):
    tests = report_dict.keys()
    query = "What can you tell me about my blood given that my "
    for test in tests:
        result = report_dict[test]
        query += test + " is " + str(result) + ", "
    return query