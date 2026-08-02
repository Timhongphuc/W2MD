#-----------------------Setup-----------------------
from exa_py import Exa
from dotenv import load_dotenv
import os
from supabase import create_client, Client
from openrouter import OpenRouter
from datetime import date

load_dotenv()

current_date = date.today()

categories_web = []
category_completions = []
category_citations = []
citations_politics = ""
citations_technology = ""
citations_economy = ""
citations_warVAR = ""

try:
    exa = Exa(api_key=os.environ.get("EXA_API_KEY"))

    client = OpenRouter(
        api_key=os.environ.get("HACK_CLUB_AI_API_KEY"),
        server_url="https://ai.hackclub.com/proxy/v1",
    )

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
except:
    print("An error occured while connecting to one of the API's. (Exa.ai)")
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
    webresult_pol = exa.search(
        "Latest news and progress made in the field of world politics.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(0, webresult_pol)


    #Technology
    webresult_tech = exa.search(
        "Latest news and progress made in the field of technology around the world.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(1, webresult_tech)

    #Economy
    webresult_eco = exa.search(
        "Latest news and progress made in the field of economy around the world.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(2, webresult_eco)


    #War
    webresult_war = exa.search(
        "Latest news and progress made in the field of war in the affected countries around the world.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(3, webresult_war)


except:
    print("An error occured while connecting to one of the API's. (Exa.ai)")
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
    completion_pol = client.chat.send(
            model="anthropic/claude-sonnet-5",
            messages=[
                {"role": "user", "content": f"Write a brief and also short paragraph about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. Your sources are: {categories_web[0]}"}
            ],
            stream=False,
        )
    category_completions.insert(0, completion_pol)


    completion_tech = client.chat.send(
                model="anthropic/claude-sonnet-5",
                messages=[
                    {"role": "user", "content": f"Write a brief and also short paragraph about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. Your sources are: {categories_web[1]}"}
                ],
                stream=False,
            )
    category_completions.insert(1, completion_tech)


    completion_eco = client.chat.send(
                model="anthropic/claude-sonnet-5",
                messages=[
                    {"role": "user", "content": f"Write a brief and also short paragraph about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. Your sources are: {categories_web[2]}"}
                ],
                stream=False,
    )
    category_completions.insert(2, completion_eco)


    completion_war = client.chat.send(
                model="anthropic/claude-sonnet-5",
                messages=[
                    {"role": "user", "content": f"Write a brief and also short paragraph about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. Your sources are: {categories_web[3]}"}
                ],
                stream=False,
    )
    category_completions.insert(3, completion_war)


    print("-------------------------------------------------------------")
    print(completion_pol)
    print("-------------------------------------------------------------")
    print(completion_tech)
    print("-------------------------------------------------------------")
    print(completion_eco)
    print("-------------------------------------------------------------")
    print(completion_war)
    print("-------------------------------------------------------------")

except:
    print("An error occured while connecting to one of the API's. (Exa.ai)")
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
             "war": category_completions[3]
            #"all_citations": category_citations,
            #"citations_politics": citations_politics,
            #"citations_technology": citations_technology,
            #"citations_economy": citations_economy,
            #"citations_war": citations_war
            })
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
