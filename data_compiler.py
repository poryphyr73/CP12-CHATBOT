import os
import openai

openai.api_key = "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"

inp = ""
response = ""
app_is_active = True
age = 0

def get_input():
  return input("Ask the bot a question: ")

def yield_response():
  response = get_bot_reply("respond to the following question: "+inp+". A "+age+"-year old should be able to understand this information.")
  print(response["choices"][0]["text"])

def get_confidence():
  conf = int(input("Is this answer clear enough?\n\nSelections:\n\t[1]: 'I would like some elaboration'\n\t[2]: 'I would like some additional resources'\n\t[3]: 'That answer was clear'\n"))
  if conf == 1:
    elaborate()
    return True
  elif conf == 2:
    provide_resources()
    return True
  elif conf == 3:
    return check_more_questions()
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
  more_questions = input("Do you have any other questions for me? (Y/N)")
  if more_questions == 'Y':
    print("Understood! Please continue.")
    return True
  elif more_questions == 'N':
    print("Understood! Thank you for using XX")
    return False
  else:
    print("Invalid selection. Please try again!")
    return check_more_questions()

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
    value = int(input("Please input you age in years: "))
  except:
    print("Invalid age. Please try again!")
    value = set_age()
  return str(value)

age = set_age()
while(app_is_active):
  inp = get_input()
  yield_response()
  app_is_active = get_confidence()