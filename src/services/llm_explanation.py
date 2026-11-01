import requests as rq
from src.llm_resources.llm_properties import llama_chat_url, model
from src.llm_resources.llm_prompt import prompt
import json

def generate_llm_response(alert_payload):
    try:
        print("inside llm response")
        message = [{
            "role": "system",
            "content": prompt
        },
        {
            "role":"user",
            "content": json.dumps(alert_payload, ensure_ascii=False)
        }
        ]
        payload = {
            "model": model,
            "messages": message,
            "stream": False
        }
        response = rq.post(url=llama_chat_url, json=payload, timeout=15)
        response.raise_for_status()
        return response
    except rq.exceptions.ConnectionError as e:
        print(f"Unable to connect to the model server: {e}")
    except rq.exceptions.ConnectTimeout as e:
        print(f"Connection timedout: {e}")
    except rq.exceptions.Timeout as e:
        print(f"Model took too long to respond: {e}")
    except rq.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except rq.exceptions.JSONDecodeError as e: 
        print(f"The response was not valid JSON: {e}")
    except rq.exceptions.RequestException as e:
        print(f"Some other request error happened: {e}")