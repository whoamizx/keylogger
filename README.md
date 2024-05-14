# 键盘监听器
~~本人要出借电脑给别人,为了防一手就想记录键盘行为,然后写到一半突然发现可以写一个键盘监听软件出来,所以就搞了个这个出来~~

这是一个简单的Python脚本，用于记录键盘输入并将其发送到指定的邮箱。当您将电脑借给别人时，可以使用这个脚本来监控活动。(chatgpt修饰后的文本)

## 免责声明
**此脚本仅供学习用途。未经授权在您不拥有的设备上使用此脚本是违法的。使用风险自负。**

## 功能
- 记录键盘输入。
- 当满足某些条件（如按下Enter键或者鼠标点击时）时，将记录的按键发送到指定的邮箱。
- 可以在将电脑借给他人时监控活动。

## 使用方法

### 第一步：设置邮箱凭证

1. 打开脚本，并填入您的邮箱地址和授权码。

   ```python
   email = "your_email@example.com"
   password = "your_authorization_code"
   ```

2. 从您的邮箱提供商获取授权码。例如，对于QQ邮箱，您可以按照以下图片中的说明获取授权码。
![image](https://github.com/whoamizx/keylogger/assets/108825705/378e32ac-6c7a-4a8f-b102-93b5b356977b)
![image](https://github.com/whoamizx/keylogger/assets/108825705/68197837-8895-46f3-b81e-df01320f7af9)
![image](https://github.com/whoamizx/keylogger/assets/108825705/d0c1afc5-d336-4bea-bb82-03473265898c)


### 第二步：安装依赖

确保已安装所需的依赖。可以使用pip安装它们：

```bash
pip install smtplib pynput
```

### 第三步：运行脚本
~~python启动~~
将脚本保存为`keylogger.py`并使用Python运行它：

```bash
python keylogger.py
```

### 第四步：打包成可执行文件

您可以使用`pyinstaller`将脚本打包成可执行文件：

1. 安装`pyinstaller`：

   ```bash
   pip install pyinstaller
   ```

2. 进入脚本所在的文件夹并运行以下命令：

   ```bash
   pyinstaller -F -w keylogger.py
   ```

3. 在`dist`文件夹中，您将找到生成的`.exe`文件。您可以运行这个文件来启动键盘监听器。

### 第五步：结合Windows计划任务使用

~~之后可以自己配合windows计划任务食用更佳~~
您可以将生成的`.exe`文件与Windows计划任务结合使用，以便在特定时间自动启动。
