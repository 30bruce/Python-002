#### Xpath 比 BeautifulSoup 性能更好
Python 中的 Xpath 常用的库是 lxml。BeautifulSoup 使用 Python 语言写的，是基于 DOM 的，会载入整个文档后解析整个 DOM 树；而 lxml 是用 C 语言写的，解析时只是进行局部遍历，时间和内存开销上都有优势。  

