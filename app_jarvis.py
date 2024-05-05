import requests
from dotenv import load_dotenv
import os

#* Load environment variables
load_dotenv()
HUGGINGFACEHUB_API_KEY = os.getenv("HUGGINGFACEHUB_API_KEY")

API_URL = "https://dd6zmw2btenawj1g.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Authorization": f"Bearer {HUGGINGFACEHUB_API_KEY}",
	"Content-Type": "application/json" 
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
print("Type you question.....")
user_input = input()
output = query({
	"inputs": user_input,
	"parameters": {"temperature":0.1, "max_new_tokens": 1000}
})
print(output[0]['generated_text'])
#print(output)
