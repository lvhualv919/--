# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------
''''''


''' 
    复习:
        A、新建 py文件 + 文件夹【directory】
            1、找到爸爸
            2、右键new -- python_file / directory
            
        B、删除 py文件 + 文件夹【directory】
            1、找到目标
            2、右键delete
'''

''' 
    1、代码头文件
        A、作用: 解决中文字符过多可能导致程序意外报错  
        B、位置: 必须要顶格写
        C、设置: 左上角的file -- settings -- 模板【Template】 -- python模板【Ptyhon Script】 -- 傻瓜式操作
        D、疑问: 头文件在爬虫班娱乐代码中
        设置 找到代码剪辑editor 找到模板file and code templates 找python模板python script 输入内容（随便找一个文件复制即可，可加自己内容 如author：）
'''

'''
    2、代码规范【了解】                      python规矩
        A、名字: PEP8规范
        B、内容: 我也不知道
        C、认知: 唯一要求: 等号两边必须要有空格, 逗号后面必须要有空格 -- 代码美观度  冒号后也要有一个空格
        D、黄色: 代码警告
                去掉方式: 右下角的小人 --> 《检测级别》 -- syntax
        E、红色: 红色波浪线报错, 绝对不允许的
                解决方式: 运用后期专业知识去解决
'''

''' 
    3、代码运行方式 -- 右键run
'''

''' 
    4、代码注释
        作用:      人为语言解释《下面》的代码                      
        标志:      #                        注释是不会执行
        群注释:    1、选中代码   2、按下 ctrl + /
        群解注释:  1、选中代码   2、按下 ctrl + /
'''

'''
    5、导包概念(No module named xxx库)                 ---- 重中之重【终生受用】
        A、期望: 正确执行别人书写的代码 -- 虽然我看不懂
        B、导包:
            1、包:
                a、概念:    
                    Python前辈写好的一些, 具有不同python功能的代码   
                b、内外:  
                    内置包: 昨天装python的时候, 默认下载的python代码
                    外置包: 昨天装python的时候, 没有下载的python代码
                c、读法:    包 == 库
                    内置包 = 内置库
                    外置包 = 外置库 = 第三方库
                d、处理:
                    python: python软件管家 -- 进行外置包的下载 -- pip           
                e、常用第三方库:
                    爬虫: requests, requests_html, lxml, jsonpath, scrapy, scrapy_redis
                    数分: pandas, numpy, skeam
                    人工: baidu-aip, opencv-python
                    画图: matplolib, styecloud
                    自动: selenium   
                f、操作:
                    1、打开: cmd or Terminal【终端】（左下角倒数第三行）
                    2、下载: pip   install 包名    后面加= =则指定下载哪个版本
                    3、卸载: pip uninstall 包名      
                g、pip list:    pip是python的软件管家
                    pip list   --- 查看当前装了哪些库（仍在终端中）

            2、导[import]: 
                A、直接导入: import 库名 
                B、间接导入: from 库名 import 函数/类
            A、import math
               a = math.sqrt(2)
               b = math.pow(a, 2)
               print(a, b)
            B、from math import sqrt
               c = sqrt(2)
               print(c)
            
            3、如何正常运行别人的代码
                A、运行一遍: 
                B、阅读错误: No module named 'xxx'
                C、解决错误: 你没有什么我就装什么      -- 如果报错了, 大胆猜测是一个简写
                D、百度一下: 
            
            pip换源:
               1、代码在哪里: 
               2、下载问题: 下载时候, 默认去国外下载, 下载特别慢
               3、解决方式:
                    豆瓣douban, 清华tsinghua, 阿里云aliyun    #looking in indexes:http...aliyun...就是访问指向是阿里云的 速度快些
                    解压到C -- 用户 -- 用户名lvhualv -- Appdata -- Roaming            
'''

#随机数生成
#常见小工具 random.randint(a,b)随机生成整数，a为起始位置，b为中止位置 random.choice(list) 随机选择列表元素
import random
num1 = random.randint(1, 10)
num2 = random.choice(['A', 'B', 'C', 'D'])
print(num1, num2)