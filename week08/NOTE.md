#### 从使用内存的角度，数据类型分为
- 可变, 例如 list, dict
- 不可变, str, int, float, tuple

#### 从类型的定义角度，数据类型分为
- 序列    
    - 容器序列：list、tuple、collections.deque等，能存放不同类型的数据。容器序列存在深拷贝、浅拷贝问题。
    - 扁平序列： str、bytes、bytearray、memoryview(内存视图)、array.array等，存放的是相同类型的数据。

- 非序列 dict, set  

