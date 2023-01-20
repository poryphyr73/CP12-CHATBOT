import os
import openai

openai.api_key = "<Insert your API key>"

inp = ""
response = ""
app_chatbot_active = False
app_citation_active = False
age = 0

tool = int(input("What tool would you like to use?\n\t[1] Chatbot\n\t[2] Citation Machine (Early Testing)\n\t[3] Quit\n"))
if tool == 1:
  app_chatbot_active = True
elif tool == 2:
  app_citation_active = True
elif tool == 3:
  quit()
else:
  print("Invalid selection. Defaulting to chatbot.")

def get_input(prompt):
  return input(prompt)

def yield_response():
  response = get_bot_reply("respond to the following question: "+inp+". A "+age+"-year old should be able to understand this information.")
  print(response["choices"][0]["text"])

def get_confidence():
  conf = int(input("Is this answer clear enough?\n\nSelections:\n\t[1]: 'I would like some elaboration'\n\t[2]: 'I would like some additional resources'\n\t[3]: 'That answer was clear'\n"))
  if conf == 1:
    elaborate()
  elif conf == 2:
    provide_resources()
  elif conf == 3:
    check_more_questions()
  else:
    print("Invalid selection. Please try again!")

def elaborate():
  elaboration = get_bot_reply("provide elaboration on the following response, "+response+", that was given to the question, "+inp+". A "+age+"-year old should be able to understand this information.")
  print(elaboration["choices"][0]["text"])
  get_confidence()

def provide_resources():
  resources = get_bot_reply("provide a few resources (articles, blogs, videos) on the following subject, "+inp+". A "+age+"-year old should be able to understand this information.")
  print("Sure. Here are some resources on the topic:\n"+resources["choices"][0]["text"])
  get_confidence()

def check_more_questions():
  more_questions = input("Do you have any other prompts for me? (Y/N, defaults to Y) ")
  if more_questions == 'Y':
    print("Understood! Please continue.")
  elif more_questions == 'N':
    print("Understood! Thank you for using XX")
    quit()
  else:
    print("Invalid selection. Defaulting.")

def generate_citation():
  form = int(input("What style guide should the citation follow?\n\t[1] MLA (Default)\n\t[2] APA\n\t[3] Chicago\n"))
  text_form = "MLA"
  if form == 2: text_form = "APA"
  if form == 3: text_form = "Chicago"
  citation = get_bot_reply("Attempt to generate a bibliographical citation in "+text_form+" style for the following source:"+inp)
  print(citation["choices"][0]["text"])

def get_bot_reply(text_prompt):
  return openai.Completion.create(
    model="text-davinci-003",
    prompt=text_prompt,
    temperature=0,
    max_tokens=128,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

def set_age():
  value = 0
  try:
    value = int(input("Please input your age in years: "))
  except:
    print("Invalid age. Please try again!")
    value = set_age()
  return str(value)

age = set_age()
while(app_chatbot_active):
  inp = get_input("Ask the bot a question: ")
  yield_response()
  get_confidence()

while(app_citation_active):
  inp = get_input("Input a source to cite: ")
  generate_citation()
  check_more_questions()
