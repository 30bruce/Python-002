#### Pandas 两个数据结构
- **Series**：类似于Excel中的一列
- **DataFrame**： 类似于Excel中的多行多列

#### 为DataFrame自定义索引时，长度必须与元素个数一致
```Python
df = pd.DataFrame([
        ['a', 'b'],
        ['c', 'd'],
    ])
# 自定义列索引
df.columns = ['one']  # 运行报错，df数据有2列，这里做了一个索引
# 自定义行索引
df.index = ['first', 'second', 'third']  # 运行报错，df数据有2行，这里做了3个索引
```

#### Pandas 数据导入
支持多种数据格式的导入，用 read_*() 的形式，例如
- pd.read_excel(r'1.xlsx')
- pd.read_csv(r'file.csv' sep='', nrows=10, encoding='utf-8')
- pd.read_sql(sql, conn)  

注意，read_excel方法依赖 xlrd 包，使用 pip install xlrd 安装。  


#### Pandas 输出编码
Linux 及 Mac 建议使用 UTF-8；Windows 建议使用 GBK；