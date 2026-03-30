# **序：**



一款游戏论坛app令gou欲罢不能——它太方便了。



查游戏信息、看折扣、找同好，它简直是游戏爱好者的天堂......



直到最近，讨论游戏的贴文越来越少了，取而代之的是散播焦虑与制造对立的内容。



gou逐渐意识到，他在这些内容上花费的时间，已经远远超过了看游戏内容的时间。



也许，是时候远离这里了。



但问题是，app的游戏数据太过齐全，难以割舍。



最终，在无数次卸载重装后，gou产生了一个想法——



既然我只需要这些数据，那为什么不**自己做一个数据库**？



# **自己做！**



gou立刻发表重要讲话：游戏数据库必须要有游戏！

✍✍✍✍✍



手机就是苹果！编程语言就是python！数据库就是MongoDB！查询就是XPath！

✍✍✍✍✍



宁缺毋滥！字段要精简！



* "name"：游戏名
* "price"：游戏现价
* "original\_price"：游戏原价

✍✍✍✍✍



# **核心代码示例**



## 数据爬取部分：



def scrape\_game(url):

&#x20;   logging.info('scraping %s...',url)

&#x20;   game = {}

&#x20;   try:

&#x20;       response = requests.get(url)

&#x20;       if response.status\_code == 200:

&#x20;           tree = etree.HTML(response.text)

&#x20;           name = tree.xpath('//span\[@itemprop="name"]/text()')

&#x20;           price = tree.xpath('(//div\[@class="discount\_final\_price"])\[1]/text()')

&#x20;           o\_price = tree.xpath('(//div\[@class="discount\_original\_price"])\[1]/text()')

&#x20;           if name:

&#x20;               game\["name"]=name\[0]

&#x20;               if o\_price:

&#x20;                   game\["original\_price"]=o\_price\[0]

&#x20;                   game\["price"]=price\[0]

&#x20;               else:

&#x20;                   game\["original\_price"]=price\[0]

&#x20;                   game\["price"]=price\[0]

&#x20;               return game

&#x20;       logging.error('get invalid status code%s while scraping %s',response.status\_code, url)

&#x20;   except requests.RequestException:

&#x20;       logging.error('error occurred while scraping %s',url,exc\_info=True)



## 获取链接与数据写入部分：



for n in range(10,100):

&#x20;   number = str(n).zfill(7)

&#x20;   url = f'https://store.steampowered.com/app/{number}'

&#x20;   game = scrape\_game(url)

&#x20;   if game and game.get("name"):

&#x20;       collection.update\_one(

&#x20;           {"name":game\["name"]},

&#x20;           {"$set":game},

&#x20;           upsert=True

&#x20;       )



### 关于logging

这是gou第一次尝试用logging模块，相对于print，它的优势在于：

* 自动记录时间
* 区分日志等级
* 更适合调试



### 关于价格判断

为什么要加个 if o\_price？

因为gou发现没打折的游戏是没有discount\_original\_price这一属性的。

如果不加判断，就会在爬取到原价游戏时报错。



### 关于链接结构

gou注意到，steam游戏的链接由固定前缀+7位数字组成，所以他用了遍历和zfill()方法，用于批量生成链接。



### 关于update\_one

其实gou最开始用的是insert\_one，但他马上发现这会产生一个bug——insert不会去重，所以数据库会有很多同名游戏，

于是他改用了update\_one方法，利用游戏名查重，每次运行程序新数据都会覆盖旧的。



## **未来计划：**



数据库雏形完成，gou在GouNest中的第二篇博文末尾进一步指明了steam游戏数据库的前进方向：



牢牢把握"**三个字段**"，"**两个功能**"！



**三个字段：** 

* 好评率字段
* 好评数量字段
* 游戏tag字段



**两个功能：** 

* 查询游戏数据功能 
* 筛选游戏数据功能



2026年03月30日





