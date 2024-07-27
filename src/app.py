from flask import Flask, jsonify, request

app = Flask(__name__)

# Global variable 'todos' containing at least one task item
todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    
    # Add the new todo item to the todos list
    todos.append(request_body)
    
    # Return the updated list of todos
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    # Remove the task from the list of todos by position
    if 0 <= position < len(todos):
        del todos[position]
    else:
        return jsonify({"error": "Position out of range"}), 400
    
    # Return the updated list of todos
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
