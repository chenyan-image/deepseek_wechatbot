# deepseek_wechatbot
## 本地deepseek模型当作聊天机器人充当微信聊天机器人

1.下载ollama 
    https://ollama.com/ 里下载， 下载完成之后在命令行里输入ollama -v 有输出即为下载成功
  
2.本地部署deepseek
      
      deepseek-r1:671b	671B	ollama run deepseek-r1:671b	需要极高的硬件配置，显存需求超过336GB
      
      deepseek-r1:1.5b	1.5B	ollama run deepseek-r1:1.5b	最低配置：8GB RAM，无显卡加速；适合老旧设备
      
      deepseek-r1:7b	  7B	  ollama run deepseek-r1:7b	最低配置：16GB RAM，8GB显存（GPU加速）
      
      deepseek-r1:8b  	8B  	ollama run deepseek-r1:8b	最低配置：16GB RAM，8GB显存（GPU加速）
      
      deepseek-r1:14b	  14B	  ollama run deepseek-r1:14b	最低配置：32GB RAM，26GB显存（GPU加速）
      
      deepseek-r1:32b	  32B  	ollama run deepseek-r1:32b	最低配置：64GB RAM，64GB显存（GPU加速）
      
      deepseek-r1:70b	  70B	  ollama run deepseek-r1:70b	最低配置：128GB RAM，140GB显存（GPU加速）
      
      我的电脑是4060 8G显存  32GB RAM 实测8b可以带动
      
      命令行输入ollama run deepseek-r1:8b 即可
3.git代码后先将三张图片替换为自己的微信图片

      先安装工具库， pyautogui，pyperclip，keyboard，ollama，opencv-python 
      运行autoReply.py即可
      
