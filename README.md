# appium_demo
基础入门
# 移动自动化常规用法
# 常用模拟器端口号
* 夜神模拟器端口号：62001 

* 逍遥模拟器端口号：21503

* MuMu模拟器端口号：7555 

# 连接设备
* adb connect 127.0.0.1:21503

## press_keycode无效
* 原因： 没有调起模拟器的输入法
* 解决：
    1. adb shell ime list -s 查看当前输入法
    2. os.system("adb shell ime set com.microvirt.memuime/.MemuIME") 设置输入法调起键盘
    3. driver.press_keycode(66)
