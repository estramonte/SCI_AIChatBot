import os
import openai

openai.api_key = "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"

inputPrompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.",

def RemoveResponseHeader(response):
    substring = "Marv:"
    outputString = ""
    str_list = response.split(substring)
    for element in str_list:
        outputString += element
    outputString2 = ""
    str_list = outputString.split("\n")
    for element in str_list:
        outputString2 += element
    return outputString2

while True:
    userInput = input("You: ")
    inputPrompt = str(inputPrompt) + str("\n") + str("You: ") + str(userInput)

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=inputPrompt,
      temperature=0.5,
      max_tokens=60,
      top_p=0.3,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )
    inputPrompt = str(inputPrompt) + str("\n") + str("Marv: ") + str(response.choices[0].text)
    output = RemoveResponseHeader(response.choices[0].text)
    print(output)