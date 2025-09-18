import os
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Gemini
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# response = client.models.generate_content(model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum')
# print(response.text)
# print(f"Prompt tokens: {response.usage_metadata.total_token_count}")
# print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# print(f"Prompt tokens: {19}")
# print(f"Response tokens:")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Inputs
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# query = sys.argv[1]
# response = client.models.generate_content(model='gemini-2.0-flash-001', contents=query)
# print(response.text)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Messages
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# query = sys.argv[1]

# messages = [
#     types.Content(role="user", parts=[types.Part(text=query)]),
# ]

# response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages,)
# print(response.text)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Verbose
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

query = sys.argv[1]
flag = sys.argv[2]

response = client.models.generate_content(model='gemini-2.0-flash-001', contents=query)

if(flag == "--verbose"):
    print(f"User prompt: {query}")
    print(f"Prompt tokens: {response.usage_metadata.total_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

else:
    print(response.text)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


















