## 使用python和开机自启动实现校园网自动登录

### 前提条件：会一些python的基础操作就可以了

### 正式开始：

   #### 1.获取到三个数据：Request  URL、Request Header和  Form Data。如何获取：(https://mubucm.com/doc/e_rq6P_CVe)
    
   #### 2.安装 python3.9.13 和  pycharm (可选)
    
   #### 3.使用pip安装requests库和Pyinstaller
    
   #### 4.重点讲一下Pyinstaller：Pyinstaller是将login.py文件打包成login.exe。简要教程：(https://mubucm.com/doc/4hqOsNUgODO)
   
   #### 5.最后一步，在桌面按CTRL+R，输入SHELL:STARTUP,将打包好的login.exe文件复制到启动文件夹中。
   
   #### 6.WiFi连接处，校园网要选择自动连接，不然可能会导致无法进入校园网登录界面。
   
   #### 7.成功。
---------------------------------------------------------------------------------------------------------------------------------------------------------------
### 附录：
  #### 1.原理：用request库模拟浏览器发起请求，然后登录。并且将源码打包成exe，用win10的[启动]实现开机自启动python脚本。
  #### 2.理论上所有的校园网都可以仿照这个教程
  #### 3.浅浅记录一下，主要是Pyinstaller不是很好用。
