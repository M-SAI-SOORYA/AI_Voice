import os
import streamlit as st
import openai
from PIL import Image
openai.organization = "org-EAWKAvX0fNJktesxHitezbNV"
openai.api_key = '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'
#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

#openai.api_key = os.getenv("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")
openai.Model.list()
# function that takes in string argument as parameter

def comp(PROMPT, MaxToken=50, outputs=3):
	# using OpenAI's Completion module that helps execute
	# any tasks involving text
	response = openai.Completion.create(
		# model name used here is text-davinci-003
		# there are many other models available under the
		# umbrella of GPT-3
		model="text-davinci-003",
		# passing the user input
		prompt=PROMPT,
		# generated output can have "max_tokens" number of tokens
		max_tokens=MaxToken,
		# number of outputs generated in one call
		n=outputs
	)
	# creating a list to store all the outputs
	output = list()
	for k in response['choices']:
		output.append(k['text'].strip())
	return output
# prompt="Advantages of open source contributions"
st.title("MY JARVIS")
image = Image.open('jarv.png')  # Replace with your image path
st.image(image,width=250)
prompt= st.text_area("Enter your text:")
if st.button("Generate Output"):
        # Process the input text (You can replace this with your actual processing logic)
        # Display the processed output
        st.write("Your Result:")
        st.write(comp(prompt,MaxToken=3000,outputs=3)[0])

#print(comp(prompt,MaxToken=3000,outputs=3)[0])
