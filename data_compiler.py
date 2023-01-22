import os
import openai

openai.api_key = "<Insert your API key>"

inp = ""
response = ""
app_chatbot_active = False
app_citation_active = False
age = 0

#the method for selecting which bot tool you want to use upon signing into the bot
tool = int(input("What tool would you like to use?\n\t[1] Chatbot\n\t[2] Citation Machine (Early Testing)\n\t[3] Quit\n"))
if tool == 1:
  app_chatbot_active = True
elif tool == 2:
  app_citation_active = True
elif tool == 3:
  quit()
else:
  print("Invalid selection. Defaulting to chatbot.")

#get a response from the bot when asking a question
def yield_response():
  response = get_bot_reply("respond to the following question: "+inp+". A "+age+"-year old should be able to understand this information.")
  print(response["choices"][0]["text"])

#ask the user how accurate the reply was, then provide options on what to do next
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

#elaborate on the already given reply. Usually involves a rewording
def elaborate():
  elaboration = get_bot_reply("provide elaboration on the following response, "+response+", that was given to the question, "+inp+". A "+age+"-year old should be able to understand this information.")
  print(elaboration["choices"][0]["text"])
  get_confidence()

#returns a variety of sources on the given reply.
def provide_resources():
  resources = get_bot_reply("provide a few resources with URLs (articles, blogs, videos) on the following subject, "+inp+". A "+age+"-year old should be able to understand this information.")
  print("Sure. Here are some resources on the topic:\n"+resources["choices"][0]["text"])
  get_confidence()

#check if the user has more questions/sources to cite
def check_more_questions():
  more_questions = input("Do you have any other prompts for me? (Y/N, defaults to Y) ")
  if more_questions == 'Y':
    print("Understood! Please continue.")
  elif more_questions == 'N':
    print("Understood! Thank you for using XX")
    quit()
  else:
    print("Invalid selection. Defaulting.")

#returns a cited version of the inputted source in the given style
def generate_citation():
  form = int(input("What style guide should the citation follow?\n\t[1] MLA (Default)\n\t[2] APA\n\t[3] Chicago\n"))
  text_form = "MLA"
  if form == 2: text_form = "APA"
  if form == 3: text_form = "Chicago"
  citation = get_bot_reply("Attempt to generate a bibliographical citation in "+text_form+" style for the following source:"+inp)
  print(citation["choices"][0]["text"])

#generalized method for turning prompts into replies
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

#sets the age for complexity later in the program
def set_age():
  value = 0
  try:
    value = int(input("Please input your age in years: "))
  except:
    print("Invalid age. Please try again!")
    value = set_age()
  return str(value)

#set the age
age = set_age()

#use the chatbot
while(app_chatbot_active):
  inp = input("Ask the bot a question: ")
  yield_response()
  get_confidence()

#use the citation machine
while(app_citation_active):
  inp = input("Input a source to cite: ")
  generate_citation()
  check_more_questions()
