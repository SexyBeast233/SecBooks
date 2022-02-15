### Tomcat getServletPath()的处理

在getServletPath()函数中是调用了Request.getServletPath()函数的：

![](./resource/TomcatgetServletPath()的处理/media/rId21.png)

跟进去，看到是直接返回前面Tomcat已经处理过后的提取处理的Servlet路径，注意这里是获取MappingData类对象中的wrapperPath属性值：

![](./resource/TomcatgetServletPath()的处理/media/rId22.png)
