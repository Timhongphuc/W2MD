#-----------------------Setup-----------------------
from exa_py import Exa
from dotenv import load_dotenv
import os
#import requests
from openai import OpenAI
#from openrouter import OpenRouter
from supabase import create_client, Client

load_dotenv()

categories = []
category_completions = []

exa = Exa(api_key=os.environ.get("EXA_API_KEY"))

client = OpenAI(
  base_url = "https://api.exa.ai",
  api_key = os.environ.get("EXA_API_KEY"),
)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
#-----------------------Gather information from sources-----------------------

#Politics

results_politics = exa.get_contents(
  urls = ["https://www.cnbc.com/world-politics/"],
  highlights=False,
  text = {
      "max_characters": 25000
  }
)

categories.insert(0, results_politics)
print(results_politics)
print("-------------------------------------------------------------")

#Technology

results_tech = exa.get_contents(
  urls = ["https://www.bbc.com/technology"],
  highlights=False,
  text = {
      "max_characters": 25000
  }
)
categories.insert(1, results_tech)
print(results_tech)
print("-------------------------------------------------------------")

#Economy

results_economy = exa.get_contents(
  urls = ["https://www.ft.com/global-economy"],
  highlights=False,
  text = {
      "max_characters": 25000
  }
)
categories.insert(2, results_economy)
print(results_economy)
print("-------------------------------------------------------------")

#War

results_war = exa.get_contents(
  urls = ["https://apnews.com/hub/war-and-unrest"], #Temporary
  highlights=False,
  text = {
      "max_characters": 25000
  }
)
categories.insert(3, results_war)
print(results_war)
print("-------------------------------------------------------------")
#-----------------------Convert information to grounded small paragraphs/texts (category specific)-----------------------

completion_pol = client.chat.completions.create(
  model = "exa",
  messages = [{"role":"system","content":"Write a brief and also short paragraph about the new tech progress made recently, based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
              {"role":"user","content":f"{categories[0]}"},],
  stream = False
)
category_completions.insert(0, completion_pol)
print(completion_pol)

completion_tech = client.chat.completions.create(
  model = "exa",
  messages = [{"role":"system","content":"Write a brief and also short paragraph about the new tech progress made recently, based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
              {"role":"user","content":f"{categories[1]}"},],
  stream = False
)
category_completions.insert(1, completion_tech)
print(completion_tech)

completion_eco = client.chat.completions.create(
  model = "exa",
  messages = [{"role":"system","content":"Write a brief and also short paragraph about the new tech progress made recently, based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
              {"role":"user","content":f"{categories[2]}"},],
  stream = False
)
category_completions.insert(2, completion_eco)
print(completion_eco)

completion_war = client.chat.completions.create(
  model = "exa",
  messages = [{"role":"system","content":"Write a brief and also short paragraph about the new tech progress made recently, based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
              {"role":"user","content":f"{categories[3]}"},],
  stream = False
)
category_completions.insert(3, completion_war)
print(completion_war)
#-----------------------Database access-----------------------

response = (
    supabase.table("NewsStorage")
    .insert({"politics": f"", "technology": f"", "economy": f"", "war": f""})
    .execute()
)


#-----------------------Drafts-----------------------

# client = OpenRouter(
#     api_key="HACK_CLUB_AI_API_KEY",
#     server_url="https://ai.hackclub.com/proxy/v1",
# )
#
# response = client.chat.send(
#     model="anthropic/claude-sonnet-latest",
#     messages=[
#         {"role": "user", "content": "Tell me a joke."}
#     ],
#     stream=False,
# )
#
# print(response.choices[0].message.content)