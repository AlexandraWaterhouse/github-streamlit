#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import streamlit as st


# In[2]:


openai.api_key='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'


# In[3]:


#Main function. Each step you select will take you to the function that will be executed.
def main():
    st.sidebar.header('AI Blog Writing Tool')
    st.sidebar.info('An AI tool that can generate blog content')
    st.sidebar.info('Start with the first option\n before you proceed to the next.')
    op = st.sidebar.selectbox('Steps', ['topics', 'section', 'content'])
    if op == 'topics':
        topics()
    elif op == 'section':
        section()
    else:
        content()


# In[4]:


#writing a blog article with Python programming being the selected niche. We narrow down the niche to data science.
##the prompt is the question that we will feed to the model.
def topics():
    st.header('AI Blog Writing Tool')
    st.info('To generate blog topic, please follow the pattern given below:')
    prompt = st.text_area('Write your words', height=50, value='Generate blog topic on data science with Python')
    if st.button('Send'):
        st.text(BlogTopics(prompt))


# In[5]:


#The prompt will be fed to the follwoing function
def BlogTopics(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3", #ideal for generating unique blog posts
      prompt=prompt,
      temperature=0.7,
      max_tokens=100, #the max number of words that we want the model to generate
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text


# In[ ]:




