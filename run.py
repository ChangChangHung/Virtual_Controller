from gpio_control.gpio_controller import GPIOController
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def password():
    return render_template('password.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    password = request.form.get('password')

    # 在這裡添加密碼驗證邏輯
    if password == '2024':
        # 密碼正確，重定向到遙控介面
        return redirect(url_for('remote_control'))
    else:
        # 密碼錯誤，返回密碼頁面
        return redirect(url_for('password'))

# 創建 GPIOController 實例
try:
    gpio_controller = GPIOController()
except:
    print('failed on create controller')

@app.route('/remote_control')
def remote_control():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    # 獲取按鈕名稱
    button_pressed = request.json.get('command')

    # 根據按鈕名稱調用相應的 GPIO 控制方法
    if button_pressed == 'turn_left':
        gpio_controller.turn_left()
    elif button_pressed == 'turn_right':
        gpio_controller.turn_right()
    elif button_pressed == 'speed_up':
        gpio_controller.speed_up()
    elif button_pressed == 'speed_down':
        gpio_controller.speed_down()

    # 返回首頁或其他適當的頁面
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
