from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.get_json()  # Get JSON data from the request
    name = data.get('name')
    email = data.get('email')
    date = data.get('date')
    time = data.get('time')
    
    # Process the appointment (e.g., save to a database)
    print(f"Appointment booked: {name} ({email}) on {date} at {time}")
    
    # Send a response back to the client
    return jsonify({'message': 'Appointment booked successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
