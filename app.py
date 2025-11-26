from flask import Flask, render_template, request, redirect, url_for, session

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page (the fake bank front)
@app.route('/')
def index():
    # Renders the HTML template located in the 'templates' folder.
    # Jinja2 is used under the hood to serve this file [web:30].
    return render_template('index.html')

# Mock route to handle the sign-in 'action'
# This accepts POST requests from the login form.
@app.route('/login', methods=['POST'])
def login():
    # In a real scenario, you would validate credentials here.
    # For this prototype, we just print them to the console to verify data flow.
    username = request.form.get('username')
    password = request.form.get('password')
    
    print(f"[DEBUG] Attempted Login - User: {username} | Pass: {password}")
    
    # Redirect back to home or a 'dashboard' after 'login'
    return redirect(url_for('index'))

@app.route('/hiddenadmin')
def hidden_admin():
    return render_template('hiddenadmin.html')

@app.route('/employee-login', methods=['GET', 'POST'])
def employee_login():
    error_message = None
    if request.method == 'POST':
        empid = request.form.get('empid')
        emppassword = request.form.get('emppassword')
        if empid == 'admin' and emppassword == 'admin123':
            session['employee_logged_in'] = True
            return redirect(url_for('hidden_admin'))  # Or wherever you want to send successful logins
        else:
            error_message = "Invalid employee credentials."
    return render_template('employee_login.html', error=error_message)

# Run the application directly
if __name__ == '__main__':
    # debug=True allows for auto-reloading when you change code
    app.run(debug=True)
