# GoogleFormAutomation
Googleフォーム提出を自動化
Lambdaと連携して定期イベント化しています

# How to use
#### Local
```
$ pip install selenium
$ pip install chromedriver-binary==84.0.4147.30.0
$ python main.py
```
#### Lambda
- Upload zip/headless-chrome.zip to Lambda Layer
- Upload zip/selenium.zip to Lambda Layer
- Make Lambda function and paste main_lambda.py
- Set headless-chrome and selenium to Layers
- Set Environment Variable ```MY_GMAIL = {Your Gmail Address}```,```MY_PASSWORD = {Your Gmail Password}```
