from flask import Flask, request, jsonify

app = Flask(__name__)

# Define sample products
products = {
    '1001': {'name': 'Product 1', 'price': 50},
    '1002': {'name': 'Product 2', 'price': 75},
    '1003': {'name': 'Product 3', 'price': 100},
}

# Define chatbot responses
responses = {
    'hi': 'Hello! How can I help you today?',
    'list': 'Here are the products we have: ' + ', '.join(products.keys()),
    'buy': 'Sure, which product would you like to buy?',
    'thanks': 'You are welcome! Have a great day.',
    'bye': 'Goodbye! Thank you for shopping with us.'
}

# Define chatbot logic
#3
def chatbot(query):
    if 'hi' in query.lower():
        return responses['hi']
    elif 'list' in query.lower():
        return responses['list']
    elif 'buy' in query.lower():
        return responses['buy']
    elif '1001' in query.lower():
        return 'Product 1 costs $' + str(products['1001']['price'])
    elif '1002' in query.lower():
        return 'Product 2 costs $' + str(products['1002']['price'])
    elif '1003' in query.lower():
        return 'Product 3 costs $' + str(products['1003']['price'])
    elif 'thanks' in query.lower():
        return responses['thanks']
    elif 'bye' in query.lower():
        return responses['bye']
    else:
        return 'I am sorry, I did not understand that.'

# Define route for chatbot API
    #2
@app.route('/chatbot', methods=['POST','GET'])
def ecommerce_chatbot():
    query = request.json['question']
    response = chatbot(query) #3 -->chatbot fn.
    #4
    return jsonify({'response': response})

#1
if __name__ == '__main__':
    app.run(debug=True)
