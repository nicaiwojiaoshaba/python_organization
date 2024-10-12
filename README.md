## 目录

- [1.lambda表达式](#python中lambda函数的特点是什么)
- [2.元组和列表](#元组和列表的区别)
- [3.装饰器](#什么是python装饰器)
- [4.多进程通信](#python多进程之前如何进行通信)
- [5.闭包函数](#什么是闭包函数)
- [6.nonlocal 语句](#nonlocal语句)
- [7.迭代器和生成器]
- [8.新式类和经典类]
- [9.单例模式](#单例模式)
- [10.super与mro机制](#super与mro机制)

## python中lambda函数的特点是什么

* lambda 表达式在Python中提供了一种简洁的方式来定义简单的函数，特别适合用于需要一次性使用的简短逻辑。
* ### 使用场景
  * **简短的函数**：当函数只需要一行代码就能完成时。
  * **作为参数传递**：当需要将函数作为参数传递给其他函数时，如 map、filter、sorted 等。
  * **一次性的使用**：当函数只在一处使用，不需要命名时。
* ### lambda缺点
  * 无法Debug,不容易调试。

## 元组和列表的区别

* 元组是不可变的，列表是可变的
* 元组的访问速度比列表快，因为元组不可变，所以在内存中是连续存储的，列表的元素是分散存储的

## 什么是python装饰器

* 为被装饰函数添加新的功能
* 作用：就是在不修改被装饰对象源代码和调用方式的前提下为被装饰对象添加额外的功能
* 使用场景：插入日志、性能测试、事务处理、缓存、权限校验
* 装饰器可以极大程度的复用代码，但是原函数的元信息会丢失，例如（__name__,__doc__）等，可以使用functools库中的wraps方法解决，将原函数的元信息拷贝到装饰器函数中。

  __一.不带参数装饰器简单实现__
  ```python
  def decorator(func):
      def wrapper(*args, **kwargs):
          print("装饰器追加功能")
          func(*args, **kwargs)
      return wrapper

  @decorator
  def show(name, age):
      print(f"我叫{name}, 今年{age}岁")

  show("张三", 22)
  ```
  @无参装饰器执行顺序拆解：
  
  1.@decorator相当于show = decorator(show)。也就是说，我们在进行不带参数的装饰器的调用时，相当于把下面的函数名当做参数传给了@后面的函数，@decorator也就相当于执行了decorator(show)。  
  
  2.decorator()函数返回了wrapper函数的内存地址。下面的show(name, age)其实就是调用了"闭包"wrapper(*args, **kwargs),进行了wrapper(*args, **kwargs)函数里面的操作  
  
  3.简单描述就是show("张三", 22)其实调用的是decorator()函数中的wrapper()函数，wrapper()函数中的func()函数是被装饰的show()函数

  __二.带参数装饰器__
  ```python
  def wrapper_out(parameter):
      print(parameter)

      def wrapper(func):
          def inner(*args, **kwargs):
              ret = func(*args, **kwargs)
              return ret
          return inner
  
      return wrapper

  @wrapper_out('QQ')
  def qq():
      print('成功登录qq')

  qq()
  ```
  @带参装饰器执行顺序拆解：
    
  1.执行wrapper_out('QQ')这个函数，把相应的参数'QQ'传给parameter，并且得到返回值wrapper函数名
    
  2.将@与wrapper结合，得到之前熟悉的标准版的装饰器，按照装饰器的执行流程执行。
  
  __三.多个装饰器修改一个函数__
  ```python
  @outter_1
  @outter_2
  @outter_3
  def show_1():
      print("show_1")
  ```
  如果多个装饰器修饰同一个函数，采用就近原则从下往上传参，然后从上往下执行代码。
## python多进程之前如何进行通信

* 队列（Queue）:多个进程可以共享一个队列，一个进程往队列中写入数据，另一个进程从队列中读取数据。
* 管道（pipe）:管道是一种双向通信机制，可以在两个进程之前传递数据。
* 共享内存（Shard Memory）:多个进程可以共享一块内存区域，一个进程往内存中写入数据，另一个进程从内存中读取数据。
* 文件（File）:多个进程可以通过读写同一个文件来进行通信。
* 套接字（Socket）:多个进程可以通过套接字进行通信，套接字可以在同一台机器上的不同进程之间进行通信，也可以在不同机器之间进行通信。

## 什么是闭包函数？
* 在Python中，闭包（Closure）是一种特殊的函数，它引用了其外部作用域中的变量，并且即使外部函数已经执行完毕，这些变量仍然存在。闭包使得这些变量在外部函数执行结束后依然可以被访问和修改。
* ### 1.基本概念
  * **嵌套函数**：闭包通常是由一个外部函数和一个内部函数组成。
  * **引用外部作用域变量**：内部函数可以访问其外部作用域中的变量。
  * **返回内部函数**：外部函数通常返回内部函数的一个引用。
* ### 2.闭包的作用
  * 闭包的一个主要用途是创建私有的状态或数据，这些状态或数据只能通过闭包函数本身访问。这样可以保护数据不受外部作用域的影响，并实现封装。
* ### 3.闭包的工作机制
  * **非局部变量**：内部函数可以访问外部函数的作用域中的变量。
  * **持久存储**：当外部函数执行完毕后，内部函数仍然可以访问这些变量，因为它们存在于闭包的作用域中。
  * **返回引用**：外部函数返回内部函数的引用，而不是直接执行内部函数。
* ### 4.闭包的内存管理
  * 在Python中，当没有引用指向某个对象时，该对象会被垃圾回收。闭包中的变量之所以在外部函数执行完毕后仍然存在，是因为内部函数仍然引用着这些变量。
* ### 5.闭包的应用场景
  * **创建工厂函数**：用于生成具有特定状态的函数。
  * **实现私有成员**：在类中可以使用闭包来创建私有属性和方法。
  * **缓存机制**：利用闭包保存计算结果，避免重复计算。
* ### 6.闭包的缺点
  * 闭包操作导致整个函数的内部环境被长久保存，占用大量内存。

## nonlocal语句

* 在python的函数内，可以引用外部变量，但不能改写外部变量，因此如果在闭包中直接改写父函数的变量，会报错。
* python3中引入了nonlocal语句，与global的区别在于nonlocal会去搜寻本地变量与全局变量之间的变量，会优先寻找层级关系与闭包作用域最近的外部变量

## 新式类和经典类

* 新式类是在创建的时候继承内置object对象(或者是从内置类型，如list,dict等)，而经典类是直接声明的。使用dir()函数可以看出新式类比经典类多出很多属性和方法，这些都是从object继承过来的。
* 新式类除了拥有经典类的全部特性之外，还有一些新的特性。比如__init__发生了变化，新增了静态方法__new__。
    ```python
    '''
    cls是一个类对象，当你调用C(*args, **kargs)来创建一个类C的实例时，python的内部调用是C.__new__(C, *args, **kargs)，
    然后返回值是类C的实例c，在确认c是C的实例后，python再调用C.__init__(c, *args, **kargs)来初始化实例c。
    '''
    cls = CLS.__new__(C, 2)  # 调用__new__创建类实例
    if isinstance(cls, CLS): # 判断cls是CLS的实例
      CLS.__init__(cls, 23)  #__init__第一个参数要为实例对象
    ```
* 新式类中的__slots__属性
## 单例模式
1. __new__实现单例模式
    ```python
    class Singleton():
        def __new__(cls, *args, **kw):
            if not hasattr(cls, '_instance'):
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
            return cls._instance
    ```
    ```python
    # 加锁版本
    import threading
    class Singleton():
        _instance = None
        _lock = threading.RLock() # 定义锁
        def __new__(cls, *args, **kw):
            if cls._instance: # 如果有实例，就不在抢锁，避免IO等待
                return cls._instance
            with cls._lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super().__new__(cls, *args **kw)
                return cls._instance
    ```
2. 模块导入方式
     ```python
     # 当导入一个py文件时，会执行这个模块的代码，然后将这个模块的名称空间加载到内存。再次导入时，不会再执行该文件，而是在内存中找
     # cls_singleton.py
     class singleton():
         pass

     instance = singleton()

     # test.py
     import cls_singleton
     c1 = cls_sinleton.instance
     c2 = cls_sinleton.instance
     print(c1 is c2)
     ```
3. 元类方式
     ```python
     class singletonMeta(type):
         _instances = {}
         def __call__(cls, *args, **kw):
             if cls not in cls._instances:
                 cls._instances[cls] = super(singletonMeta, cls).__call__(*args, **kw)
             return cls._instances[cls]

     class singletonClass(metaclass=singletonMeta):
         pass
    ```
4. 装饰器
    ```python
    def singleton(cls):
        _instance = {}

      def warrper(*args, **kwargs):
          if cls not in _instance:
              _instance[cls] = cls(*args, **kwargs)
          return _instance[cls]
      return warrper

   @singleton
   class Myclass():
       a = 1
    ```
## super与mro机制
* 先看一道题
    ```python
    class A:
        def fun(self):
            print('A.fun')
     
    class B(A):                                
        def fun(self):
            super(B , self).fun()
            print('B.fun')
 
    class C(A):
        def fun(self):
            super(C , self).fun()
            print('C.fun')
 
    class D(B , C):
        def fun(self):
            super(D , self).fun()
            print('D.fun')
  
    D().fun()
    # 输出结果如下：
    A.fun C.fun B.fun D.fun
    ```  
    为什么输出顺序是A->C->B->D而不是A->B->C->D呢？
* __mro机制__
  
  事实上，在每个类声明之后，Python都会自动为创建一个名为“\_\_mro__”的内置属性，这个属性就是Python的MRO机制生成的，该属性是一个tuple，定义的是该类的方法解析顺序（继承顺序），当用super调用父类的方法时，会按照\_\_mro__属性中的元素顺序去挨个查找方法。
        
  在Python新式类中（Python3中也只存在新式类了），采用的是C3算法（可不是广度优先，更不是深度优先）。我们通过如下图所示的继承关系来简单介绍C3算法（箭头指向父类）

  ![image](https://github.com/nicaiwojiaoshaba/python_organization/assets/38779020/ddd59d2f-68db-42f2-be07-99bc3946a1f0)

  C3算法过程如下
  >1. 将入度（指向该节点的箭头数量）为0的D节点放入列表,并将D节点和D节点有关的箭头从上图树中删除
  >2. 继续找入度为0的节点，B和C满足，左侧优先，将B放入现有列表，并删除B节点和有关箭头
  >3. 此时入度为0的节点为C节点，将C放入列表
  >4. 最后将A放入列表
    
  所以上图中经过C3算法计算得出的继承顺序为D->B->C->A

  继承顺序决定后，剩下的就是代码输出顺序的问题，所以需要了解super的用法。

* __super__  
  super是一个类（不是方法），实例化之后得到的是一个代理的对象，而不是得到了父类，并且我们使用这个代理对象来调用父类或者兄弟类的方法。

  super的几种传参方式
  > super()  
  > super(type, obj)  
  > super(type_1, type_2)

  一. __super(type , obj)__
    
  在上文中说到，super会按照\_\_mor__属性中的顺序去查找方法，super(type, obj)两个参数中**type作用是定义在\_\_mor__数组的哪个位置开始找**，**obj定义的是用哪个类的\_\_mor__元素**

  结合上题，D类的__mro__顺序是D->B->C->A,在D类中调用fun方法，然后在D类的fun方法中遇到super(D, self).fun(),其中self是D类的实例化对象，所以采用D类的__mor__顺序，其中指明D后面是B,
  所以继续调用B类的fun方法，遇到super(B , self).fun()，这时候需要注意，这里的self还是原来的D类实例（千万注意不是B类实例），所以还是用D类的__mro__顺序，那就继续调用下一个C类的fun方法，
  ，同理继续调用下一个父类，也就是A类的fun方法，执行完A类的fun方法后，回到C的fun方法中，打印输出，然后回到B类的fun方法，直到D类的fun方法打印输出完。
    
  二. __super()__
    
  super()事实上是懒人版的super(type , obj)，这种方式只能用在类体内部，Python会自动把两个参数填充上，**type指代当前类**，**obj指导当前类的实例对象(即使用当前类的\_\_mor__元素)**

  三. __super(type_1 , type_2)__
    
  当super传入的两个参数都是类名是，type_2必须是type_1的子类。
  当super传入两个类时，得到的时一个指向继承顺序下的类的代理，所以调用类方法时还需传入实例
  ```python
  super(D, D).fun(D())
  # 输出A fun C fun B fun
  super(D, D).fun(B())
  # 输出A fun B fun
  ```
## 魔法函数
* **\_\_call__**  
  把对象当成函数来使用的时候会自动调用。也就是说把类的实例化对象，变成一个可以调用的对象，可以让实例对象像函数一样被调用。
  ```python
  class A():
      def __call__(self, attr):
          print("把对象当成函数使用：", attr)

  a = A()
  a("调用方法一")
  a.__call__("调用方法二")
  ```

