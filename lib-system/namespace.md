python作用域分4种情况： 

L：local，局部作用域，即函数中定义的变量；  
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；  
G：globa，全局变量，就是模块级别定义的变量；   
B：built-in，系统固定模块里面的变量，比如int, bytearray等。   

搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。