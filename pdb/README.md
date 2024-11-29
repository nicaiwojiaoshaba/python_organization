## python pdb(debugger)

* **c | continue**: 继续执行程序，直到遇到下一个断点或程序结束。
* **n | next**: 执行下一行代码，但不会进入函数内部。
* **s | step**: 执行下一行代码，如果下一行是函数调用，则进入该函数内部。
* **r | return**: 继续执行直到当前函数返回。
* **l | list**: 显示当前代码上下文，通常显示当前行周围的代码。
* **p | print**: 打印变量或表达式的值。
* **whatis variable_name**: 显示变量的类型。
* **type(variable_name)**: 显示变量的类型。
* **b | break**: 设置断点。
```python
    b function_name        # 在函数开头设置断点
    b filename: linenumber  # 在文件的某一行设置断点
    b linenumber           # 在当前文件的某一行设置断点
```
* **cl | clear**: 清除断点。
```python
    cl breakpoint_number   # 清除指定编号的断点
    cl *                   # 在文件的某一行设置断点
```
* **q | quit**: 退出调试器。
* **h | help**: 显示帮助信息。
