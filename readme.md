# MultiPDF Chat App


## Introduction
------------
The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

## How It Works
------------

![MultiPDF Chat App Diagram](./docs/PDF-LangChain.jpg)


The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation
----------------------------
To install the MultiPDF Chat App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Instuction to use this code
-----
To use the MultiPDF Chat App, follow these steps:

1. Clone the repository to your local machine.

2. Ensure that you have the OpenAI API key and installed the required dependencies.

3. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```
   
4. The application will launch in your default web browser, displaying the user interface.

## Instructions to use the app
-------------------------------
![MultiPDF Chat App screenshot](./docs/Screenshot 2024-02-27 233824.png)
1. Get your OpenAI API key from OpenAI website 
2. Enter your OpenAI API key
3. Browse pdfs from your directory and enter process button
4. Lets chat with the AI about the pdfs you have provided

## License
-------
The MultiPDF Chat App is released under the [MIT License](https://opensource.org/licenses/MIT).