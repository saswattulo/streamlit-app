import os
import streamlit as st
from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain,SequentialChain

from apikey import openai_key
os.environ['OPEN_AI_KEY'] = openai_key

#app framework
st.title('🔗YouTube GPT')
prompt = st.text_input('Enter your prompt')

title_template = PromptTemplate(
    input_variables=['topic'],
    template='Write me a youtube video title about {topic}'
)
script_template = PromptTemplate(
    input_variables=['title'],
    template='Write me a youtube video script based on this title TITLE: {title}'
)

#llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
#script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)


#in the SimpleSequentialChain, one need to pass the chain sequentially in a list
#overall_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)

if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)
    #st.write("Response :", response)