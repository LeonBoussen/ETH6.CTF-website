from flask import Flask, render_template, request, redirect, url_for, session

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'pass-seed'


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

#admin page
@app.route('/peacaboo')
def hidden_admin():
    return render_template('admin.html')

# admin login
@app.route('/UIFIioidfoifgogdshfghfhgfghrshtrst', methods=['GET', 'POST'])
def employeelogin():
    errormessage = None
    if request.method == 'POST':
        empid = request.form.get('empid')
        emppassword = request.form.get('emppassword')
        if empid == "john" and emppassword == "SPONGEBOB":
            session['employeeloggedin'] = True
            return redirect(url_for('panel'))  # <-- Redirect to "panel"
        else:
            errormessage = "Invalid employee credentials."
    return render_template('employee_login.html', error=errormessage)

@app.route('/panel')
def panel():
    if not session.get('employeeloggedin'):
        return redirect(url_for('index'))
    return render_template('panel.html')


# Run the application directly
if __name__ == '__main__':
    # debug=True allows for auto-reloading when you change code
    app.run(port=80,debug=True)
