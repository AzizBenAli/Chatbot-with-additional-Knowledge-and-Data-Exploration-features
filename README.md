# AI-Assistant-for-Knowledge-and-Data-Exploration

## Table of Contents
- [Overview](#overview)
- [App Functionalities](#app-functionalities)
  - [Conversational Ability](#conversational-ability)
  - [Latest News Feature](#latest-news-feature)
  - [CSV Upload and Query](#csv-upload-and-query)
  - [PDF Upload and Chat](#pdf-upload-and-chat)
- [Implementation Details](#implementation-details)
    - [Agents](#agents)
         - [Calculator Agent](#calculator-agent)
         - [Python Code Execution Agent](#python-code-execution-agent)
         - [Time Agent](#time-agent)
         - [Web Search Agent](#web-search-agent)
         - [CSV Analysis Agent](#csv-analysis-agent)
    - [RAG Pipeline](#rag-pipeline)
- [Technologies Used](#technologies-used)  
- [Contributions](#contributions)
- [Contact Information](#contact-information)

## Overview
This AI assistant is a versatile tool designed to cater to various needs, offering a user-friendly interface for:
- Knowledge-based queries
- Mathematical problem-solving
- Latest news updates
- Conversational interactions
- CSV data analysis
- PDF content exploration


### App Functionalities
The app exhibits a wide range of functionalities, ensuring adaptability and versatility across various tasks.
It supports knowledge-based queries, mathematical problem-solving, provides the latest news updates, engages in conversations, analyzes CSV data, and explores PDF content.

<h1>Explore the chatbot's capabilities by watching this short video</h1>

<a href="https://github.com/AzizBenAli/AI-Assistant-for-Knowledge-and-Data-Exploration/assets/1229eec4-8d0d-40ee-a52b-bd7d53ba7294" target="_blank"><img src="path_to_your_image.png" alt="Video Thumbnail" width="900" height="300"></a>

### Conversational Ability
The AI assistant's ability to engage in real discussions with users, setting it apart from traditional question-and-answer chatbots.
It offers an interactive and conversational experience, making it more than just a Q&A chatbot.

<p align="center">
<img src="https://github.com/AzizBenAli/AI-Assistant-for-Knowledge-and-Data-Exploration/assets/116091818/213d9f90-41cc-4b35-bc5d-3639fa360d61" alt="Conversational Ability" width="900">
</p>
Description: Highlighting the AI Assistant's conversational capabilities.

### Latest News Feature
The AI Assistant also enables users to access the latest news, enhancing its utility as a multifaceted tool.
Users can stay updated on current affairs and trending topics within the app.

<p align="center">
<img src="https://github.com/AzizBenAli/AI-Assistant-for-Knowledge-and-Data-Exploration/assets/116091818/59958af9-f914-4b8b-a6cc-282822614f02" alt="Search" width="900">
</p>
Description: Showcasing the AI Assistant's ability to provide users with the latest news updates, expanding its functionality beyond conventional use cases. 

### CSV Upload and Query
Users can upload CSV files and query the AI Assistant for specific information and insights.
The AI Assistant analyzes the uploaded CSV data and provides relevant answers based on the user's queries.

<p align="center">
<img src="https://github.com/AzizBenAli/AI-Assistant-for-Knowledge-and-Data-Exploration/assets/116091818/f6716140-36db-4dd1-ba58-3f9c516e6e7c" alt="CSV Upload and Query" width="900">
</p>
Description: Querying the AI Assistant using a CSV file.

### PDF Upload and Chat
An essential feature includes the ability to upload multiple PDFs and interact with the AI Assistant for queries.
Users can have conversations with the AI Assistant based on the content of the uploaded PDFs, receiving detailed and relevant information.

<p align="center">
<img src="https://github.com/AzizBenAli/AI-Assistant-for-Knowledge-and-Data-Exploration/assets/116091818/d3fb5ef5-ce21-4a5a-a772-b3d0b5f943a8" alt="PDF Upload and Chat" width="900">
</p>
Description: Interacting with the AI Assistant using uploaded PDFs for queries.

## Implementation Details

### Agents [website](https://python.langchain.com/docs/modules/agents/agent_types/)
We have developed agents to enhance the performance of the large language model and reduce hallucination:

- **Calculator Agent**: Improves the AI Assistant's performance in mathematical problem-solving.

- **Python Code Execution Agent**: Allows users to execute Python code directly within the AI Assistant.

- **Time Agent**: Provides the current time and date information.

- **Web Search Agent**: Enables the AI Assistant to search the web for information to answer user queries.

- **CSV Analysis Agent**: Reads CSV files and answers questions based on the data. Recently enhanced to provide advanced plot generation capabilities based on user input.This implementation was carried out to offer users a more transparent and informative experience when interacting with the AI Assistant.

### RAG Pipeline [Paper](https://arxiv.org/pdf/2005.11401.pdf)
We utilize a RAG (Retrieval-Augmented Generation) pipeline to extract information from PDF files, enhancing the AI Assistant's ability to understand and respond to user queries. The pipeline leverages open-source embeddings from Hugging Face and the Mistral open-source model for processing the retrieval and generation steps.

## Technologies Used
- Ultra-2 Language Model from AI21 Studio: It powers the conversational capabilities and drives the AI's intelligence.  
- Mixtral 8×7B: Utilized to answer queries based on CSV and PDF files, enhancing data interaction capabilities.   
- Hugging Face Transformers and Embeddings: Crucial components for various NLP tasks, contributing to the AI's intelligence and understanding.  
- Python: Employed for backend logic due to its versatility, extensive libraries, and robust functionality.  
- Streamlit: Utilized to create the user-friendly interface, ensuring an interactive and seamless user experience.  
- Langchain: Used for developing prompts and agents, enriching the AI Assistant's functionality and adaptability.


# **Commands**
- Running the app locally from this repository   
- clone this repository    
- Create a new Python environment provided with pip    
- run pip install -r requirements.txt    
- run streamlit run app.py    
- Now open the 'External URL' in your browser. Enjoy the bot.   
<br>
<img width="600" alt="streamlit_app" src="https://github.com/AzizBenAli/YouTubeChat-App/assets/116091818/c6c859b4-f4cd-4b34-8bc2-6ceb567de0de">   
<br>
## Contributions 
Contributions to enhance features or add new capabilities are welcome! Fork the repository, make your changes, and submit a pull request.

## Contact Information
For inquiries or feedback, reach out to [benaliazizaba000@gmail.com] 







 

 








