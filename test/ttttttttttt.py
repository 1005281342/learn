import pyttsx3

engine = pyttsx3.init()
engine.say('君不见，黄河之水天上来，奔流到海不复回。')
engine.say('君不见，高堂明镜悲白发，朝如青丝暮成雪。')
# 运行并且等待
engine.runAndWait()
