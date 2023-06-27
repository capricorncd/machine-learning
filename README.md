# machine-learning

## 开发环境搭建

https://www.anaconda.com/

安装好anaconda后，在VSCode中指定Python版本为`3.10.9(base:conda)`

## 使用Jupyter

### 启动Jupyter Notebook

- 启动`anaconda-navigator` 
- Home 
- Jupyter Notebook 
- launch

 或者

```bash
# https://jupyter.org/install#jupyter-notebook
jupyter notebook 
```

### 快捷键

- m 切换为 Markdown语法输入

### Jupyter 魔法命令

#### %run

执行python文件

```
%run dir/filename.py
```

#### %timeit

性能测试（单行代码执行的时间）

- `%timeit`会根据程序的复杂度自己决定执行1次或多次。
- `%time`只会执行1次。

```
%timeit L = [i**2 for i in range(1000)]
```

运行结果

```
164 µs ± 3.79 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

执行多行代码（单元格中所有代码执行的时间）

```
%%timeit
L = []
for n in range(1000):
  L.append(n ** 2)
```

- 同一只希望其执行一次，可以使用`%time`。

#### 其他魔法命令

```
%lsmagic
```

#### 查看文档

```
%run?
```

## 创建Python模块

模块目录中创建`__init__.py`即可

```
├── somemodule
├──── ├── __init__.py
├──── └── submodule.py
```

