import openai
import streamlit as st




API_KEY = st.sidebar.text_input('OpenAI API key')

openai.api_key = API_KEY



def main():
    st.sidebar.header('AI Book Writing Tool')
    st.sidebar.info('An AI tool that can generate content for your book')
    st.sidebar.info('Start with topics\n than chapters\n than content.')
    op = st.sidebar.selectbox('Steps', ['title', 'chapter', 'content'])
    if op == 'title':
        title()
    elif op == 'chapter':
        chapter()
    else:
        content()




def title():
    st.header('AI Book Writing Tool')
    st.info('To generate book Title, please write your prompt below:')
    prompt = st.text_area('Your prompt here', height=50, value=' ')
    if st.button('Send'):
        st.text(BookTitle(prompt))


def chapter():
    st.header('AI Book Writing Tool')
    st.info('To generate book Chapter title, please write your prompt below:')
    prompt = st.text_area('Your prompt here', height=50, value='Write book chapters titles for a book with the Title: ' )
    if st.button('Send'):
        st.text(BookChapters(prompt))


def content():
    st.header('AI Book Writing Tool')
    st.info('To generate book topic, please follow the below steps:')
    prompt = st.text_area('Your prompt here', height=50, value="Write the book chapters \n\nBlog Title:\n\nChapter:")
    if st.button('Send'):
        st.text(BookContent(prompt))

def BookTitles(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=prompt,
      temperature=0.7,
      max_tokens=50,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response.choices[0].text

def BookChapters(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=prompt,
      temperature=0.6,
      max_tokens=50,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response.choices[0].text


def BookContent(prompt):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt=prompt,
      temperature=0.7,
      max_tokens=800,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response.choices[0].text



if __name__ == '__main__':
    main()
