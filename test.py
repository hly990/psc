from selenium import webdriver

import time

# 创建Chrome的驱动对象
driver = webdriver.Chrome('/Users/helingyun/codebase/opensource/psc/chromedriver')

# 加载页面 百度首页
driver.get("http://www.baidu.com")
# 保存当前界面
driver.save_screenshot("baidu.png")


time.sleep(3)

# 关闭当前窗口
# driver.close()
# 退出浏览器
driver.quit()