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

## python中lambda函数的特点是什么

* 是一个匿名函数，可以有多个参数但只能有一个表达式，表达式结果就是返回值
* lambda无法debug,阅读起来不便于理解

## 元组和列表的区别

* 元组是不可变的，列表是可变的
* 元组的访问速度比列表快，因为元组不可变，所以在内存中是连续存储的，列表的元素是分散存储的

## 什么是python装饰器

* 为被装饰函数添加新的功能
* 作用：就是在不修改被装饰对象源代码和调用方式的前提下为被装饰对象添加额外的功能
* 使用场景：插入日志、性能测试、事务处理、缓存、权限校验
* 装饰器可以极大程度的复用代码，但是原函数的元信息会丢失，例如（__name__,__doc__）等，可以使用functools库中的wraps方法解决，将原函数的元信息拷贝到装饰器函数中。

## python多进程之前如何进行通信

* 队列（Queue）:多个进程可以共享一个队列，一个进程往队列中写入数据，另一个进程从队列中读取数据。
* 管道（pipe）:管道是一种双向通信机制，可以在两个进程之前传递数据。
* 共享内存（Shard Memory）:多个进程可以共享一块内存区域，一个进程往内存中写入数据，另一个进程从内存中读取数据。
* 文件（File）:多个进程可以通过读写同一个文件来进行通信。
* 套接字（Socket）:多个进程可以通过套接字进行通信，套接字可以在同一台机器上的不同进程之间进行通信，也可以在不同机器之间进行通信。

## 什么是闭包函数？

* 一个函数的返回值是另外一个函数，返回的函数调用了父函数内部的变量，如果返回的函数在外部被执行，就产生了闭包。
* 闭包的优点：使函数外部能够访问函数内部并传入属性和方法。
* 闭包的缺点：闭包操作导致整个函数的内部环境被长久保存，占用大量内存。

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
    
  在上文中说到，super会按照\_\_mor__属性中的顺序去查找方法，super(type, obj)两个参数中type作用是定义在\_\_mor__数组的哪个位置开始找，obj定义的是用哪个类的\_\_mor__元素

  结合上题，D类的__mro__顺序是D->B->C->A,在D类中调用fun方法，然后在D类的fun方法中遇到super(D, self).fun(),其中self是D类的实例化对象，所以采用D类的__mor__顺序，其中指明D后面是B,
  所以继续调用B类的fun方法，遇到super(B , self).fun()，这时候需要注意，这里的self还是原来的D类实例（千万注意不是B类实例），所以还是用D类的__mro__顺序，那就继续调用下一个C类的fun方法，
  ，同理继续调用下一个父类，也就是A类的fun方法，执行完A类的fun方法后，回到C的fun方法中，打印输出，然后回到B类的fun方法，直到D类的fun方法打印输出完。
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

