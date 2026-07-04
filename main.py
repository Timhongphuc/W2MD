#-----------------------Setup-----------------------
from exa_py import Exa
from dotenv import load_dotenv
import os
from openai import OpenAI
from supabase import create_client, Client

load_dotenv()

categories = []
category_completions = []
category_citations = []
citations_politics = ""
citations_technology = ""
citations_economy = ""
citations_warVAR = ""

try:
    exa = Exa(api_key=os.environ.get("EXA_API_KEY"))

    client = OpenAI(
      base_url = "https://api.exa.ai",
      api_key = os.environ.get("EXA_API_KEY"),
    )

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
except:
    print("An error occured while connecting to one of the API's. (Exa)")
    response = ( #Try reaching Supabase
        supabase.table("NewsStorage")
        .insert({"politics": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "technology": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "economy": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "war": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me"})
        .execute()
    )

#-----------------------Gather information from sources-----------------------

try:
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
      urls = ["https://www.abc.net.au/news/topic/unrest-conflict-and-war"],
      highlights=False,
      text = {
          "max_characters": 25000
      }
    )
    categories.insert(3, results_war)
    print(results_war)
    print("-------------------------------------------------------------")
except:
    print("An error occured while connecting to one of the API's. (Exa)")
    response = ( #Try reaching Supabase
        supabase.table("NewsStorage")
        .insert({"politics": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "technology": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "economy": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "war": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me"})
        .execute()
    )
    exit()
#-----------------------Convert information to grounded small paragraphs/texts (category specific)-----------------------

try:
    completion_pol = client.chat.completions.create(
      model = "exa",
      messages = [{"role":"system","content":"Write a brief and also short paragraph about the recent political progress based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
                  {"role":"user","content":f"{categories[0]}"},],
      stream = False
    )

    parsed_pol = completion_pol.choices[0].message.content

    category_completions.insert(0, parsed_pol)
    print(parsed_pol)

    data_dictP = completion_pol.model_dump()
    citations_pol = data_dictP["choices"][0]["message"].get("citations", []) #AI helped me with this (HAVE TO LEARN AND PRACTICE JSON IN PYTHON!)
    category_citations.insert(0, citations_pol)
    citations_politics = citations_pol


    completion_tech = client.chat.completions.create(
      model = "exa",
      messages = [{"role":"system","content":"Write a brief and also short paragraph about the new tech progress made recently based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
                  {"role":"user","content":f"{categories[1]}"},],
      stream = False
    )

    parsed_tech = completion_tech.choices[0].message.content

    category_completions.insert(1, parsed_tech)
    print(parsed_tech)

    data_dictT = completion_tech.model_dump()
    citations_tech = data_dictT["choices"][0]["message"].get("citations", [])
    category_citations.insert(1, citations_tech)
    citations_technology = citations_tech


    completion_eco = client.chat.completions.create(
      model = "exa",
      messages = [{"role":"system","content":"Write a brief and also short paragraph about the new economic progress made recently based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
                  {"role":"user","content":f"{categories[2]}"},],
      stream = False
    )

    parsed_eco = completion_eco.choices[0].message.content

    category_completions.insert(2, parsed_eco)
    print(parsed_eco)

    data_dictE = completion_eco.model_dump()
    citations_eco = data_dictE["choices"][0]["message"].get("citations", [])
    category_citations.insert(2, citations_eco)
    citations_economy = citations_eco


    completion_war = client.chat.completions.create(
      model = "exa",
      messages = [{"role":"system","content":"Write a brief and also short paragraph about the wars on our world recently based on the information given to you. Ground your answers by researching the web. Stay specific and accurate."},
                  {"role":"user","content":f"{categories[3]}"},],
      stream = False
    )

    parsed_war = completion_war.choices[0].message.content

    category_completions.insert(3, parsed_war)
    print(parsed_war)

    data_dictW = completion_war.model_dump()
    citations_war = data_dictW["choices"][0]["message"].get("citations", [])
    category_citations.insert(3, citations_war)
    citations_warVAR = citations_war

    print("-------------------------------------------------------------")

    print(citations_pol)
    print("-------------------------------------------------------------")
    print(citations_tech)
    print("-------------------------------------------------------------")
    print(citations_eco)
    print("-------------------------------------------------------------")
    print(citations_war)
    print("-------------------------------------------------------------")

except:
    print("An error occured while connecting to one of the API's. (Exa)")
    response = ( #Try reaching Supabase
        supabase.table("NewsStorage")
        .insert({"politics": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "technology": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "economy": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                 "war": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me"})
        .execute()
    )
    exit()
#-----------------------Database access-----------------------

response = (
    supabase.table("NewsStorage")
    .insert({"politics": category_completions[0],
             "technology": category_completions[1],
             "economy": category_completions[2],
             "war": category_completions[3],
            "all_citations": category_citations,
            "citations_politics": citations_politics,
            "citations_technology": citations_technology,
            "citations_economy": citations_economy,
            "citations_war": citations_war})
    .execute()
)
#-----------------------Clear all variables-----------------------

categories = []
category_completions = []
category_citations = []
citations_politics = ""
citations_technology = ""
citations_economy = ""
citations_warVAR = ""
#-----------------------Drafts-----------------------

#from openrouter import OpenRouter

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