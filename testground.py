# from datetime import date
# from exa_py import Exa
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# current_date = date.today()
#
# exa = Exa(api_key=os.environ.get("EXA_API_KEY"))
#
# webresult_pol = exa.search(
#         "Latest news and progress made in the field of world politics.",
#         end_published_date=str(current_date),
#         exclude_domains=["reddit.com", "x.com", "truthsocial.com", "foxnews.com"],
#         num_results=10,
#         start_published_date=str(current_date),
#         type="auto",
#         contents={
#             "highlights": True
#         }
#     )
#
# citations_politics = webresult_pol.results[0].id + ", " + webresult_pol.results[1].id + ", " + webresult_pol.results[2].id + ", " + webresult_pol.results[3].id + ", " + webresult_pol.results[4].id + ", " + webresult_pol.results[5].id + ", " + webresult_pol.results[6].id + ", " + webresult_pol.results[7].id + ", " + webresult_pol.results[8].id + ", " + webresult_pol.results[9].id
# print(citations_politics)
#---------------------------------------------------------------------
#import os
# from dotenv import load_dotenv
# from openrouter import OpenRouter
#
# load_dotenv()
#
# client = OpenRouter(
#     api_key=os.environ.get("HACK_CLUB_AI_API_KEY"),
#     server_url="https://ai.hackclub.com/proxy/v1",
# )
#
# response = client.chat.send(
#     model="anthropic/claude-sonnet-5",
#     messages=[
#         {"role": "user", "content": "Write a brief and also short paragraph about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate."}
#     ],
#     stream=False,
# )
# print(response.choices[0].message.content)
#
#
# response = client.chat.send(
#     model="anthropic/claude-sonnet-5",
#     messages=[
#         {"role": "user", "content": "Write a brief and also short paragraph about the latest technological progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate."}
#     ],
#     stream=False,
# )
# print(response.choices[0].message.content)
#
#
# response = client.chat.send(
#     model="anthropic/claude-sonnet-5",
#     messages=[
#         {"role": "user", "content": "Write a brief and also short paragraph about the latest economic progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate."}
#     ],
#     stream=False,
# )
# print(response.choices[0].message.content)
#
#
# response = client.chat.send(
#     model="anthropic/claude-sonnet-5",
#     messages=[
#         {"role": "user", "content": "Write a brief and also short paragraph about the latest changes in the topic war around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate."}
#     ],
#     stream=False,
# )
# print(response.choices[0].message.content)


# from openrouter import OpenRouter
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# client = OpenRouter(
#         api_key=os.environ.get("HACK_CLUB_AI_API_KEY"),
#         server_url="https://ai.hackclub.com/proxy/v1",
#     )
#
# response = client.chat.send(
#             model="anthropic/claude-sonnet-5",
#             messages=[
#                 {"role": "user", "content": f"Write a brief and also short paragraph about the latest political progress made around the world based on the sources you got provided with. Ground your answers with the provided sources ONLY. Stay specific and accurate. For testing purposes, just make up something stupid."}
#             ],
#             stream=False,
#         )
# print(response.choices[0].message.content)