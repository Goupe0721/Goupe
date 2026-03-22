### 我为什么要做这个？



仅使用html编写博文效率低下，每篇文章需要重复编写页面结构，所以我制作了一个博客生成器自动完成这些重复工作，这让我可以将重心放在构思博文上，同时，它可以作为一个可迭代优化的项目，作为学习过程的记录。



### 功能介绍：



-遍历content文件夹，试别其中的txt和markdown文件

-将文件文本转换成html格式

-将转换后的html写入blog\_content下的同名文件



### 核心代码示例：



###### txt转html部分：



from pathlib import Path

import markdown



contents = Path("contents")

blog = Path("blog\_contents")

blog.mkdir(exist\_ok=True)

template = Path("template.html")

\#这里我使用了pathlib来管理文件路径，因为我对它比较熟悉。

...............................

for content in contents.iterdir():

&nbsp;   

&nbsp;   if content.suffix == ".txt":

&nbsp;       post\_content = content.read\_text(encoding="utf-8")

&nbsp;       html = blog/f"{content.stem}.html"

&nbsp;       html\_content = template\_content.replace("{content}",post\_content)

&nbsp;       html\_content = html\_content.replace("{title}",content.stem)

&nbsp;       html.write\_text(html\_content,encoding="utf-8")

................................



###### 我有一点疑惑，replace难道不会改变原模板文件的内容吗？

其实并不会，replace作用于字符串，并返回一个新的字符串对象，原始模板文件内容并不会改变。



### 错误回顾：



读写文件时没有指定编码格式，导致网页内容变成了乱码。由于不同系统默认编码不同，在读写文件时，显然统一使用encoding="utf-8"更合适。



html模板中，错误地将博文标题放在了head标签内，导致标题并没有受css影响。需要注意，head标签用于存放页面内的元信息，而显示内容都应在body标签内。



### 未来计划：



\-优化style.css，改进排版（间距、行距、字体等）。

\-为博文与列表页加入时间戳功能

2026年03月22日




