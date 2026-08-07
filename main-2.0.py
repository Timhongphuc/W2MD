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
category_citations = [] #Deprecated
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


except Exception as e:
    print(f"An error occured while connecting to one of the API's. (Exa.ai) Error: {e}")
    response = (  # Try reaching Supabase
        supabase.table("NewsStorage")
        .insert({
                    "politics": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                    "technology": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                    "economy": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me",
                    "war": "Ooops, something broke. If you're reading this, the Exa API failed. Please contact: timhongphuc@proton.me"})
        .execute()
    )
    exit()

#-----------------------Gather information from sources-----------------------

try:
    #Politics
    webresult_pol = exa.search(
        "Latest news and progress made in the field of world politics.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        include_domains=["reuters.com", "nytimes.com", "dw.com", "bbc.com", "economist.com", "wsj.com",
                         "theguardian.com", "apnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(0, webresult_pol)
    # citations_politics = f"{webresult_pol["results"][0]["id"]}, {webresult_pol["results"][1]["id"]}, {webresult_pol["results"][2]["id"]}, {webresult_pol["results"][3]["id"]}, {webresult_pol["results"][4]["id"]}, {webresult_pol["results"][5]["id"]}}, {webresult_pol["results"][6]["id"]}, {webresult_pol["results"][7]["id"]}, {webresult_pol["results"][8]["id"]}, {webresult_pol["results"][9]["id"]}" #Didn't work
    #citations_politics = webresult_pol.results[0].id + ", " + webresult_pol.results[1].id + ", " + webresult_pol.results[2].id + ", " + webresult_pol.results[3].id + ", " + webresult_pol.results[4].id + ", " + webresult_pol.results[5].id + ", " + webresult_pol.results[6].id + ", " + webresult_pol.results[7].id + ", " + webresult_pol.results[8].id + ", " + webresult_pol.results[9].id #Didn't work
    citations_politics = ", ".join(r.id for r in webresult_pol.results) #AI helped me
    print(citations_politics)

    #Technology
    webresult_tech = exa.search(
        "Latest news and progress made in the field of technology around the world.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        include_domains=["reuters.com", "nytimes.com", "dw.com", "bbc.com", "economist.com", "wsj.com",
                         "theguardian.com", "apnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(1, webresult_tech)
    citations_technology = ", ".join(r.id for r in webresult_tech.results)  # AI helped me
    print(citations_technology)

    #Economy
    webresult_eco = exa.search(
        "Latest news and progress made in the field of economy around the world.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        include_domains=["reuters.com", "nytimes.com", "dw.com", "bbc.com", "economist.com", "wsj.com",
                         "theguardian.com", "apnews.com", "theverge.com", "techcrunch.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(2, webresult_eco)
    citations_economy = ", ".join(r.id for r in webresult_eco.results)  # AI helped me
    print(citations_economy)

    #War
    webresult_war = exa.search(
        "Latest news and progress made in the field of war in the affected countries around the world.",
        end_published_date=str(current_date),
        exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
        include_domains=["reuters.com", "nytimes.com", "dw.com", "bbc.com", "economist.com", "wsj.com",
                         "theguardian.com", "apnews.com"],
        num_results=10,
        start_published_date=str(current_date),
        type="auto",
        contents={
            "highlights": True
        }
    )
    categories_web.insert(3, webresult_war)
    citations_warVAR = ", ".join(r.id for r in webresult_war.results)  # AI helped me
    print(citations_warVAR)



except Exception as e:
    print(f"An error occured while connecting to one of the API's. (Exa.ai) Error: {e}")
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
                {"role": "user", "content": f"Write a brief and also short paragraph (about 70-100 Words) about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. The Structure is always the same: 1. The text with a few sentences about the current progress, 2. In the end, point out the sources, which are displayed 'down below', say: 'You will find the associated sources below this article.'. Remember that staying NEUTRAL and ACCURATE, WITHOUT making up any information is the/your TOP PRIORITY. Your sources are: {categories_web[0]}"}
            ],
            stream=False,
        )
    category_completions.insert(0, completion_pol.choices[0].message.content)


    completion_tech = client.chat.send(
                model="anthropic/claude-sonnet-5",
                messages=[
                    {"role": "user", "content": f"Write a brief and also short paragraph (about 70-100 Words) about the latest technological progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. The Structure is always the same: 1. The text with a few sentences about the current progress, 2. In the end, point out the sources, which are displayed 'down below', say: 'You will find the associated sources below this article.'. Remember that staying NEUTRAL and ACCURATE, WITHOUT making up any information is the/your TOP PRIORITY. Your sources are: {categories_web[1]}"}
                ],
                stream=False,
            )
    category_completions.insert(1, completion_tech.choices[0].message.content)


    completion_eco = client.chat.send(
                model="anthropic/claude-sonnet-5",
                messages=[
                    {"role": "user", "content": f"Write a brief and also short paragraph (about 70-100 Words) about the latest economic progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. The Structure is always the same: 1. The text with a few sentences about the current progress, 2. In the end, point out the sources, which are displayed 'down below', say: 'You will find the associated sources below this article.'. Remember that staying NEUTRAL and ACCURATE, WITHOUT making up any information is the/your TOP PRIORITY. Your sources are: {categories_web[2]}"}
                ],
                stream=False,
    )
    category_completions.insert(2, completion_eco.choices[0].message.content)


    completion_war = client.chat.send(
                model="anthropic/claude-sonnet-5",
                messages=[
                    {"role": "user", "content": f"Write a brief and also short paragraph (about 70-100 Words) about the latest progress made in the field of war in the affected countries around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. The Structure is always the same: 1. The text with a few sentences about the current progress, 2. In the end, point out the sources, which are displayed 'down below', say: 'You will find the associated sources below this article.'. Remember that staying NEUTRAL and ACCURATE, WITHOUT making up any information is the/your TOP PRIORITY. Your sources are: {categories_web[3]}"}
                ],
                stream=False,
    )
    category_completions.insert(3, completion_war.choices[0].message.content)


    print("-------------------------------------------------------------")
    print(completion_pol.choices[0].message.content)
    print("-------------------------------------------------------------")
    print(completion_tech.choices[0].message.content)
    print("-------------------------------------------------------------")
    print(completion_eco.choices[0].message.content)
    print("-------------------------------------------------------------")
    print(completion_war.choices[0].message.content)
    print("-------------------------------------------------------------")


except Exception as e:
    print(f"An error occured while connecting to one of the API's. (Exa.ai) Error: {e}")
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

             "all_citations": "-|NA|-",
             "citations_politics": citations_politics,
             "citations_technology": citations_technology,
             "citations_economy": citations_economy,
             "citations_war": citations_warVAR

            # "all_citations": "Citations can be found separately now.",
            # "citations_politics": categories_web[0].results.id,
            # "citations_technology": categories_web[1].results.id,
            # "citations_economy": categories_web[2].results.id,
            # "citations_war": categories_web[3].results.id
            })
    .execute()
)
#-----------------------Clear all variables and lists-----------------------

categories = []
category_completions = []
category_citations = []
citations_politics = ""
citations_technology = ""
citations_economy = ""
citations_warVAR = ""
