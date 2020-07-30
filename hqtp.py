import time
import cv2
import canndy_test
from selenium import webdriver
from selenium.webdriver import ActionChains

# 新建selenium浏览器对象，后面是geckodriver.exe下载后本地路径
browser = webdriver.Firefox()

# 网站登陆页面
url = 'https://www.om.cn/login'

# 浏览器访问登录页面
browser.get(url)

handle = browser.current_window_handle

# 等待3s用于加载脚本文件
browser.implicitly_wait(3)

# 点击登陆按钮，弹出滑动验证码
btn = browser.find_element_by_class_name('login_btn1')
btn.click()

# 获取iframe元素，切到iframe
frame = browser.find_element_by_id('tcaptcha_iframe')
browser.switch_to.frame(frame)

time.sleep(1)

# 获取背景图src
targetUrl = browser.find_element_by_id('slideBg').get_attribute('src')

# 获取拼图src
tempUrl = browser.find_element_by_id('slideBlock').get_attribute('src')


# 新建标签页
browser.execute_script("window.open('');")
# 切换到新标签页
browser.switch_to.window(browser.window_handles[1])

# 访问背景图src
browser.get(targetUrl)
time.sleep(3)
# 截图
browser.save_screenshot('temp_target.png')

w = 680
h = 390

img = cv2.imread('temp_target.png')

size = img.shape

top = int((size[0] - h) / 2)
height = int(h + ((size[0] - h) / 2))
left = int((size[1] - w) / 2)
width = int(w + ((size[1] - w) / 2))

cropped = img[top:height, left:width]

# 裁剪尺寸
cv2.imwrite('temp_target_crop.png', cropped)

# 新建标签页
browser.execute_script("window.open('');")

browser.switch_to.window(browser.window_handles[2])

browser.get(tempUrl)
time.sleep(3)

browser.save_screenshot('temp_temp.png')

w = 136
h = 136

img = cv2.imread('temp_temp.png')

size = img.shape

top = int((size[0] - h) / 2)
height = int(h + ((size[0] - h) / 2))
left = int((size[1] - w) / 2)
width = int(w + ((size[1] - w) / 2))

cropped = img[top:height, left:width]

cv2.imwrite('temp_temp_crop.png', cropped)

browser.switch_to.window(handle)

# 模糊匹配两张图片
move = canndy_test.matchImg('temp_target_crop.png', 'temp_temp_crop.png')

# 计算出拖动距离
distance = int(move / 2 - 27.5) + 2

draggable = browser.find_element_by_id('tcaptcha_drag_thumb')

ActionChains(browser).click_and_hold(draggable).perform()

# 拖动
ActionChains(browser).move_by_offset(xoffset=distance, yoffset=0).perform()

ActionChains(browser).release().perform()

time.sleep(10)