from flask import Flask, request, render_template_string, escape

app = Flask(__name__)

# Vulnerable route (XSS)
@app.route('/vulnerable')
def vulnerable():
    # Get user input from the query parameter 'name'
    name = request.args.get('name', 'Guest')
    # Render the template without escaping the input (vulnerable to XSS)
    return render_template_string(f"<h1>Hello, {name}!</h1>")

# Secure route (XSS protected)
@app.route('/secure')
def secure():
    # Get user input from the query parameter 'name'
    name = request.args.get('name', 'Guest')
    # Escape the input to prevent XSS
    safe_name = escape(name)
    return render_template_string(f"<h1>Hello, {safe_name}!</h1>")

if __name__ == '__main__':
    app.run(debug=True)