# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import datetime
import logging
import allure
import time
import os

#调用时返回截图路径及文件名
def path():
    return './Test_report/' + datetime.datetime.now().strftime('%Y-%m-%d %H;%M;%S;%f') + ".png"

class Keywork:

    #初始化操作
    def __init__(self):
        logging.info('初始化浏览器')
        # 懒加载模式
        capa = DesiredCapabilities.CHROME
        capa["pageLoadStrategy"] = "none"
        self.driver = webdriver.Chrome(desired_capabilities=capa)
        # 修改webdriver特征码
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
							Object.defineProperty(navigator, 'browser', {
							  get: () => undefined
							})
						  """
        })

        self.driver.maximize_window()

# ------------------------------------------------------------------------------------------
    # 截图
    def scr(self, log):
        p = path()
        try:
            result = EC.alert_is_present()(self.driver)
            if result:
                pass
            elif not result:
                self.driver.get_screenshot_as_file(p)
                if os.path.exists(p):
                    pass
                else:
                    logging.warning('截图异常')
                with open(p, mode='rb') as f:
                    file = f.read()
                allure.attach(file, '元素截图:{}'.format(log), allure.attachment_type.PNG)
                os.remove(p)
        except Exception as e:
                logging.warning('导入Allure异常{}'.format(e))


    # 浏览器操作
# ------------------------------------------------------------------------------------------

    # 打开浏览器
    def open(self, url):
        logging.info('打开网址{}'.format(url))
        self.driver.get(url)

    # 退出浏览器
    def quit(self, second=0):
        self.wait(second)
        logging.info('退出浏览器')
        self.driver.quit()

    # 前进浏览器
    def forwrod(self):
        logging.info('快进浏览器')
        self.driver.forward()

    # 后退浏览器
    def back(self):
        logging.info('快退浏览器')
        self.driver.back()

    # 浏览器最大化
    def max_window(self):
        logging.info('浏览器最大化')
        self.driver.maximize_window()

    # 最小化浏览器
    def min_window(self):
        logging.info('浏览器最小化')
        self.driver.minimize_window()

    # 元素操作
# ------------------------------------------------------------------------------------------
    # 元素定位
    def loc(self, by, element):
        return self.driver.find_element(by, element)

    # 点击元素
    def click(self, by, element):
        ele = (by, element)
        logging.info('查看{}元素{}是否可以被点击'.format(by, element))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(ele))
        logging.info('点击{}元素{}'.format(by, element))
        self.loc(by, element).click()
        self.scr('点击')

    # 输入元素
    def input(self, by, element, test):
        ele = (by, element)
        logging.info('查看{}元素{}是否可以被点击'.format(by, element))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(ele))
        logging.info('输入{}元素{}，文本:{}'.format(by, element, test))
        self.loc(by, element).clear()
        self.loc(by, element).send_keys(test)
        self.scr('输入')

    # 拖动操作
    def drag(self, by, element, xoffset, yoffset):
        loc = self.loc(by, element)
        ele = (by, element)
        logging.info('查看{}元素{}是否可以被点击'.format(by, element))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(ele))
        logging.info('拖动{}元素{}，X轴{}，Y轴{}'.format(by, element, xoffset, yoffset))
        self.scr('拖动元素前')
        ActionChains(self.driver).drag_and_drop_by_offset(loc, xoffset, yoffset).perform()
        self.scr('拖动元素后')

    # 悬停在元素上
    def remain(self, by, element):
        ele = (by, element)
        logging.info('查看{}元素{}是否可以被点击'.format(by, element))
        WebDriverWait(self.driver, 15).until(visibility_of_element_located(ele))
        logging.info('悬停在{}元素{}上'.format(by, element))
        ActionChains(self.driver).move_to_element(self.driver.find_element(by, element)).perform()
        self.scr('悬停')

    # 等待操作
# ------------------------------------------------------------------------------------------

    # 强制等待
    @staticmethod
    def wait(second):
        if second == 0:
            pass
        else:
            logging.info('强制等待{}秒'.format(second))
            time.sleep(second)

    # 隐式等待
    def i_wait(self, second):
        logging.info('隐式等待{}秒'.format(second))
        self.driver.implicitly_wait(second)

    # iframe操作
#------------------------------------------------------------------------------------------
    # 进入frame
    def into(self, iframe):
        logging.info('进入嵌套页{}'.format(iframe))
        WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it(iframe))


    # 退出frame到主界面
    def out(self):
        logging.info('退出嵌套页至首页')
        self.driver.switch_to.default_content()


# ------------------------------------------------------------------------------------------
    # 断言页面跳转
    def v_url(self, ourl, curl, eurl):
        self.wait(1)
        p = path()
        url = self.driver.current_url
        if url == ourl:
            assert url == ourl
            logging.info("URL未跳转:{}".format(url))
            self.driver.get_screenshot_as_file(p)
            with open(p, mode='rb') as f:
                file = f.read()
            allure.attach(file, 'URL未跳转截图', allure.attachment_type.PNG)
            os.remove(p)
        elif url == curl:
            logging.info('URL成功跳转:{}'.format(ourl))
            self.driver.get_screenshot_as_file(p)
            with open(p, mode='rb') as f:
                file = f.read()
            allure.attach(file, 'URL成功跳转', allure.attachment_type.PNG)
            os.remove(p)
        elif url == eurl:
            logging.info('URL失败跳转:{}'.format(curl))
            self.driver.get_screenshot_as_file(p)
            with open(p, mode='rb') as f:
                file = f.read()
            allure.attach(file, 'URL失败跳转截图', allure.attachment_type.PNG)
            os.remove(p)
        elif url != ourl or curl or eurl:
            self.driver.get_screenshot_as_file(p)
            logging.warning('URL跳转异常')
            with open(p, mode='rb') as f:
                file = f.read()
            allure.attach(file, 'URL跳转异常截图', allure.attachment_type.PNG)
            os.remove(p)

    # 输入日期到日历控件
    def cld(self, i, test):
        js = 'document.getElementById("{}").removeAttribute("readonly")'.format(str(id))
        self.driver.execute_script(js)
        self.driver.find_element('id',i).clear()
        self.driver.find_element('id',i).send_keys(test)
        self.scr('输入日历控件')
        logging.info('输入日历控件:{}'.format(test))

    # 下拉列表操作
    def down(self, by, element, test):
        if test == '':
            pass
            logging.info('没有输入值，略过下拉列表操作')
        else:
            ele = (by, element)
            try:
                WebDriverWait(self.driver, 15).until(element_to_be_clickable(ele))
                Select(self.loc(by, element)).select_by_visible_text(test)
                self.scr('下拉框选择:{}'.format(test))
            except:
                logging.info('下拉列表选择异常,选择值:{}'.format(test))

    # 弹窗处理
    def alert(self,test=1 or 0):
        p = path()
        try:
            result = EC.alert_is_present()(self.driver)
            if not result:
                logging.info('找不到弹窗')
                self.scr('弹窗后')
            elif test == 0:
                alert = self.driver.switch_to.alert
                a = alert.text
                alert.dismiss()
                logging.info('确定弹窗,返回文本:{}'.format(a))
                self.scr('取消弹窗后')
            elif test == 1:
                alert = self.driver.switch_to.alert
                a = alert.text
                logging.info('确定弹窗,返回文本:{}'.format(a))
                alert.accept()
                self.scr('确定弹窗后')
        except:
            self.driver.get_screenshot_as_file(p)
            with open(p,'rb') as f:
                file = f.read()
                allure.attach(file,'点击弹窗异常',allure.attachment_type.PNG)
                os.remove(p)


#------------------------------------------------------------------------------------------
