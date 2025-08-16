import os
from flask import Flask, request, jsonify, render_template
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai_api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    
    prompt = ChatPromptTemplate.from_messages([
        {"role": "user", "content": user_input}
    ])
    
    response = chat_model.generate(prompt)
    answer = response['choices'][0]['message']['content']
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)