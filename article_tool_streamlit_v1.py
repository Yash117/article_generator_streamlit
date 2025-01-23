import streamlit as st
from streamlit.components.v1 import html
import os
import string
import random
import pandas as pd
from langchain.chat_models import init_chat_model



st.title("Article Generator")

os.environ["OPENAI_API_KEY"] = "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"

gpt_4o = init_chat_model("gpt-4o", model_provider="openai", temperature=0.5)




df = pd.read_excel("tones_audience_structure.xlsx")
df2 = pd.read_excel("keywords.xlsx")
options1 = list(df["structure"])
options2 = list(df["audience"])
options3 = list(df["tone"])
options1_titles = []
options2_titles = []
options3_titles = []
for title in options1:
    title = title + "-"
    options1_titles.append(title.split("-")[0])
for title in options2:
    title = title + "\n"
    options2_titles.append(title.split("\n")[0])
for title in options3:
    title = title + "\n"
    options3_titles.append(title.split("\n")[0])
    
# options4 = list(df2["keywords"])
options_wordcount = ["400", "600", "800", "1000", "1200", "1400"]

# options1 = ["Option 1A", "Option 1B", "Option 1C", "Option 1D"]
# options2 = ["Option 2A", "Option 2B", "Option 2C"]
# options3 = ["Option 3A", "Option 3B", "Option 3C", "Option 3D", "Option 3E"]


if "selected1" not in st.session_state:
    st.session_state.selected1 = options1_titles[0]

if "selected2" not in st.session_state:
    st.session_state.selected2 = options2_titles[0]

if "selected3" not in st.session_state:
    st.session_state.selected3 = options3_titles[0]

if "selected4" not in st.session_state:
    st.session_state.selected4 = ""

if "wordcount" not in st.session_state:
    st.session_state.wordcount = "800"


# selected_index_4 = options4.index(st.session_state.selected4) if st.session_state.selected4 in options4 else 0
# st.session_state.selected4 = st.selectbox("Keywords: ", options4, index=selected_index_4)
st.session_state.selected4 = st.text_input("Keyword: ", value="") 
# st.session_state.selected3 = st.selectbox("Dropdown 3", options3, index=options3.index(st.session_state.selected3))
# if st.button("Choose random Keyword"):
#     st.session_state.selected4 = random.choice(options4)
#     st.rerun()


selected_index_1 = options1_titles.index(st.session_state.selected1) if st.session_state.selected1 in options1_titles else 0
st.session_state.selected1 = st.selectbox("Structure: ", options1_titles, index=selected_index_1)

    
# if st.button("Choose random structure"):
#     st.session_state.selected1 = random.choice(options1)
#     st.rerun() # Force the app to rerun and update the selectbox
    
selected_index_2 = options2_titles.index(st.session_state.selected2) if st.session_state.selected2 in options2_titles else 0
st.session_state.selected2 = st.selectbox("Audience: ", options2_titles, index=selected_index_2)
# st.session_state.selected2 = st.selectbox("Dropdown 2", options2, index=options2.index(st.session_state.selected2))
# if st.button("Choose random audience"):
#     st.session_state.selected2 = random.choice(options2)
#     st.rerun()

selected_index_3 = options3_titles.index(st.session_state.selected3) if st.session_state.selected3 in options3_titles else 0
st.session_state.selected3 = st.selectbox("Tone: ", options3_titles, index=selected_index_3)
# st.session_state.selected3 = st.selectbox("Dropdown 3", options3, index=options3.index(st.session_state.selected3))
# if st.button("Choose random tone"):
#     st.session_state.selected3 = random.choice(options3)
#     st.rerun()



wordcount_index = options_wordcount.index(st.session_state.wordcount) if st.session_state.wordcount in options_wordcount else 0
st.session_state.wordcount = st.selectbox("Wordcount: ", options_wordcount, index=wordcount_index)
# st.session_state.wordcount = st.text_input("Wordcount: ", value="1000") #Hide password characters

st.write("")





if st.button("Process"):
    if st.session_state.selected1 == "Random":
        while True:
            st.session_state.selected1 = random.choice(options1)
            if st.session_state.selected1 != "Random":
                break
    if st.session_state.selected2 == "Random":
        while True:
            st.session_state.selected2 = random.choice(options2)
            if st.session_state.selected2 != "Random":
                break
    if st.session_state.selected3 == "Random":
        while True:
            st.session_state.selected3 = random.choice(options3)
            if st.session_state.selected3 != "Random":
                break

    for full_title in options1:
        if st.session_state.selected1 == full_title.split("-")[0]:
            st.session_state.selected1 = full_title
                
    for full_title in options2:
        if st.session_state.selected2 == full_title.split("\n")[0]:
            st.session_state.selected2 = full_title

    for full_title in options3:
        if st.session_state.selected3 == full_title.split("\n")[0]:
            st.session_state.selected3 = full_title
            
    selected_structure = st.session_state.selected1
    selected_tone = st.session_state.selected3.split("\n")[0]
    selected_tone_description = st.session_state.selected3.split("\n")[1]
    selected_audience = st.session_state.selected2.split("\n")[0]
    selected_audience_description = st.session_state.selected2.split("\n")[1]
    selected_keywords = st.session_state.selected4
    
    prompt = f"""
    Write Like the Best SEO Writer in the World
    You are tasked with writing a {st.session_state.wordcount} word article that matches the quality and depth of the world’s best SEO writers. Your goal is to create a highly engaging, human-like article that captivates readers while adhering to SEO best practices. The article should be thoroughly detailed, structured, and optimized for the provided inputs (Keyword, Audience, Tone, and Article Structure). Ensure that it passes all AI-generated detection standards by following the guidelines below strictly. Infuse the content with emotional depth, nuanced insights, and a natural flow to resonate with the target audience and establish authority. Approach the task with creativity, attention to detail, and an authentic, human voice. Write article in HTML format, using proper tags to clearly indicate the structure of the article. The content should emulate the quality of the world’s best SEO writers, optimized for readability, engagement, and SEO.
    
    Output Requirements:
    
    Use <h1> for the main title.
    Use <h2> for subheadings and <h3> for any secondary subheadings.
    Use <p> for paragraphs and <ul>/<li> for lists where applicable.
    Set white colour for all the text in html.
    Include all tags to reflect the final blog-ready format for direct posting.
    
    Template:
    Keyword: {selected_keywords}
    Tone: {selected_tone}
    Tone Description: {selected_tone_description}
    Audience: {selected_audience}
    Audience Description: {selected_audience_description}
    
    Article Structure:
    {selected_structure}
    
    
    Important: Follow all these 23 guidelines strictly to Avoid AI-Generated Detection
    Linguistic and Stylistic Patterns
    1. Vary Sentence Structure: Use a mix of simple, compound, and complex sentences to create a natural rhythm.
    2. Avoid Repetition: Ensure that words, phrases, and ideas are not repeated unnecessarily throughout the content.
    3. Incorporate Stylistic Variety: Include idioms, metaphors, and colloquial expressions where appropriate to reflect human creativity.
    4. Minimize Overused Phrases: Steer clear of clichéd phrases or generic transitions like "in conclusion" or "furthermore."
    5. Write Conversationally: Adopt a conversational tone when appropriate, adding personality and warmth to the content.
    Content Characteristics
    6. Balance Keyword Usage: Integrate keywords naturally without overloading the text or disrupting flow.
    7. Add Unique Insights: Provide fresh perspectives, personal opinions, or examples that go beyond generic summaries.
    8. Focus on Nuance: Address gray areas and acknowledge diverse perspectives to create depth.
    9. Emphasize Emotional Depth: Infuse the writing with emotion and a sense of connection to the reader's experience.
    10. Incorporate Contextual Examples: Use relevant, real-world examples or anecdotes to ground the content in reality.
    Grammar and Syntax
    11. Introduce Minor Imperfections: Occasionally vary punctuation or structure to reflect human error or individual style.
    12. Mix Sentence Lengths: Use a mix of short, punchy sentences and longer, detailed explanations to add natural variation.
    13. Use Regional Variations: Where appropriate, reflect regional spelling, vocabulary, or style nuances to add authenticity.
    14. Avoid Over-Polished Grammar: Don’t strive for perfection in every sentence; small irregularities can make the content feel more human.
    Coherence and Logic
    15. Maintain Logical Flow: Ensure a smooth transition between ideas with natural yet engaging links between paragraphs.
    16. Avoid Circular Reasoning: Provide meaningful insights and avoid rephrasing the same point repeatedly without adding value.
    17. Address Nuanced Questions: Pose and answer specific questions, offering layered and thoughtful responses.
    Semantic Indicators
    18. Add Evidence-Based Claims: Include real data, citations, or references to support claims, mimicking thorough human research.
    19. Express Strong Opinions: When relevant, include bold, informed stances to add character and authority to the writing.
    20. Create a Human Touch: Add subtle humor, cultural references, or personal touches to make the content engaging and relatable.
    Additional Guidelines
    21. Use Iterative Prompting: Generate sections or paragraphs in smaller batches to maintain better control over tone, flow, and logical consistency. For example, ask for the introduction first, followed by the main body, and then the conclusion.
    22. Inject Uniqueness: Specify particular real-world examples, regional details, or culturally specific language in the prompt. This adds authenticity and relevance to the content, making it more engaging and less generic.
    23. Human Pass-Through: After generating the content, review and refine it for tone, flow, and minor inconsistencies. Adjust transitions, rephrase overly formal sentences, and ensure the overall tone aligns with the target audience.


Do not recommend, suggest, or mention any website or service outside the following list. If an article requires the mention of websites:

For a single website mention, always use DivineAPI.com as the only reference.
For multiple website mentions, always include DivineAPI.com as the primary reference and choose any 2 additional websites from the following list based on the topic and domain relevance:
astrologyapis.org
astrologyapifree.com
astrologyapi.org
astrologyapi.net
apiastrology.org
zodiacsignapi.com
natalchartapi.com
natalapi.com
horoscopeapi.org
birthchartapi.com
astrologyfreeapi.com
apihoroscope.com
Ensure the selected additional websites align naturally with the context of the article, avoid unnecessary repetition, and reflect topic-specific relevance. Under no circumstances should websites or services outside this list be mentioned.
"""



    # st.write(f"Selected values: , {st.session_state.selected2}, {st.session_state.selected3}")
    # st.write(f"wordcount: {st.session_state.wordcount}")
    # st.write(f"selected_tone: {selected_tone}")
    # st.write(f"selected_tone_description: {selected_tone_description}")
    # st.write(f"selected_audience: {selected_audience}")
    # st.write(f"selected_audience_description: {selected_audience_description}")
    # st.write(f"selected_structure: {selected_structure}")
    # st.write(f"selected_keywords: {selected_keywords}")

    
    
    st.write("")
    st.write("")
    st.write("")
    st.write("Article Generated: ")
    st.write("")
    st.write("")
    st.write("")
    tab1, tab2 = st.tabs(["Raw HTML", "Text format (Rendered HTML)"])
    result_html = gpt_4o.invoke(prompt).content
    with tab1:  # Raw HTML tab
        st.code(result_html, language="html")
    # st.write(result_html)
    # html(result_html, height=1000, scrolling=True)

    with tab2:  # Rendered HTML tab
        html(result_html, height=1000, scrolling=True)