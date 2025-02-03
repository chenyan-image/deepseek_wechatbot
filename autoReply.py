import pyautogui
import pyperclip
import keyboard
import time
import cv2

from ollama import chat
from ollama import ChatResponse

# 设置pyautogui的默认延迟为最小值
pyautogui.PAUSE = 0.1
pyautogui.MINIMUM_DURATION = 0.1

def Ollama_response(input):
    # 使用更小的模型来加快响应速度
    response: ChatResponse = chat(
        model='deepseek-r1:8b',  # 换用更轻量的模型
        messages=[{
            'role': 'user',
            'content': input,
        }]
    )
    res = response['message']['content']
    pos = res.find('</think>',0,len(res)) + 10
    return res[pos:len(res)]

print('程序即将开始，请打开微信!')

# 缓存图像识别结果
last_news_location = None
last_icons_location = None
last_reset_location = None

def findNews():
    global last_news_location
    try:
        # 先尝试使用缓存的位置
        if last_news_location:
            try:
                if pyautogui.locateOnScreen("news.png", region=last_news_location, confidence=0.8):
                    left, top, width, height = last_news_location
                    pyautogui.click(left + 20, top + 20)
                    print('发现了新消息')
                    return True
            except:
                last_news_location = None

        # 如果缓存失效，搜索整个屏幕
        location = pyautogui.locateOnScreen("news.png", confidence=0.8)
        if location:
            last_news_location = location
            left, top, width, height = location
            pyautogui.click(left + 20, top + 20)
            print('发现了新消息')
            return True
        return False
    except Exception as e:
        print(f'查找新消息时出错: {str(e)}')
        return False

def sendMsg():
    global last_icons_location, last_reset_location
    try:
        # 使用缓存的图标位置
        if not last_icons_location:
            last_icons_location = pyautogui.locateOnScreen('icons.png', confidence=0.8)
        
        left, top, width, height = last_icons_location
        X = left + width
        
        # 快速执行点击操作
        pyautogui.rightClick(X, top - 40)
        pyautogui.click(X + 10, top - 40 + 10)
        
        friendMsg = pyperclip.paste()
        print('好友的消息：' + friendMsg)
        
        print('正在思考如何回复...')
        reply = Ollama_response(friendMsg)
        print('即将发送的消息：' + reply)
        
        pyperclip.copy(reply)
        pyautogui.click(X, top + 50)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        print('发送成功!')
        
        # 使用缓存的重置按钮位置
        if not last_reset_location:
            last_reset_location = pyautogui.locateOnScreen('reset.png', confidence=0.8)
        
        if last_reset_location:
            left, top, width, height = last_reset_location
            pyautogui.click(left + 20, top + 20)
            print('恢复原始状态')
            
    except Exception as e:
        # 清除缓存的位置
        last_icons_location = None
        last_reset_location = None
        print(f'发送消息时出错: {str(e)}')

# 主循环
while True:
    if keyboard.is_pressed('backspace'):
        print('按下了退格键，程序即将结束')
        break
    
    try:
        if findNews():
            sendMsg()
        else:
            # 很短的延迟，减少CPU使用
            time.sleep(0.1)
    except Exception as e:
        print(f'运行时出错: {str(e)}')
        time.sleep(0.1)

pyautogui.alert(text='Python程序已结束!', title='提示', button='好的')
print("程序已结束!")