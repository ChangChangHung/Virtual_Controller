from gpio_control.gpio_controller import GPIOController
try:
    g = GPIOController()
    g.Forward()
except:
    print('failed on create controller')

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def password():
    return render_template('password.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    password = request.form.get('password')
    if password == '2024':
        return redirect(url_for('remote_control'))
    else:
        return redirect(url_for('password'))

@app.route('/remote_control')
def remote_control():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    value = request.json.get('command')
    if 'speed' in value:
        value=value.replace('speed','')
        # g.speed_change(value)
    elif 'turning' in value:
        value=value.replace('turning','')
        # g.turn_change(value)
    print(value)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
