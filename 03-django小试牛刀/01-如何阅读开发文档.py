"""
DJango的开发文档中 分出了  MOdel  View   模板和Form  剩下的都是功能性模块，   pagination分页   caching缓存模板

Model模板：
Models
QuerySets:
Model Instances:  Model 实例
Migrations： 表结构调整  makemigration   migrate
Advanced: 自定义Manager（Model.objects.all()中的objects)
Other  ： Legacy databases 对于遗留版本问题可以用吃直接生成Model，然后在写admin CMS就出来了
         Optimize databases access  详见http://www.the5fire.com/djnago-database-access-optimization.html



view部分：
在Django的文档中，View部分包含了URL配置、http request、http response以及处理请求的View函数和类级的View等部分。下面我们一一列举。

The basics - URL配置，view方法，以及常用装饰器，比如想给这个接口增加缓存、或者要增加限制（只允许GET请求）等。

Reference  - 一些参考，内置的view（比如静态文件处理，404页面处理等），Request和Response对象介绍，TemplateResponse对象介绍。

File uploads - 文件上传是Web开发中常遇到的问题，Django中可以通过这一节来看如何处理文件上传，它提供了一些内置的模块来帮你处理上传上来的文件，不过它也会告诉你如何来自定义后端存储。

Class-based views - 这部分可以理解为更复杂的View函数，只不过这儿是类。通过类可以提供更好的复用，从而避免自己要写很多代码。当你发现你的View中有太多的业务代码时，你可以考虑参考这一节把代码改造为ClassBase View（简称:CBV），如果你的代码中有很多类似的View函数，可以考虑这么做。这部分的文档就是告诉你Django中，如何来更好的构建你的View，以及复用你的View。

Advanced - 更高级的部分，就是告诉你如何把数据导出为CSV或者PDF，冠名为更高级可能是因为用的少。（瞧，高级没什么难的）

Middleware - 中间件（中间层），无论怎么翻译，你得理解它的作用，这一部分代码作用于WSGI（或者Socket连接）和View之间，还记得我们第二章讲的WSGI中间件的部分吗，一样的逻辑，还是对View函数做了一个包装，但是稍微复杂了一些。Django中安全的部分，Session的部分，整站缓存的部分，都在这一块了。




Template部分:
这是Django声称对设计师友好的部分，因为它提供的语法很简单，任何人都可以很快上手，即便是不同编程的人，也可以很容易学习和使用。

The basics - 这部分介绍了Django模板的基本配置，以及基本的模板语法，还有看起来可配置的如何替换为jinja2模板引擎的说明。

For designers - 说是给设计师看的，但是你也应该看一看，基础的控制语句、注释，还有内置的filter和tag，还有最重要的针对用户友好的数字的展示。

For programmers - 这个程序员更应该看看了，如何传递数据到模板中，如何配置模板，以至于能够在view中更好的渲染模板，还有就是如何对现有模板所提供的简单的功能最更多的定制。


Forms部分
对于传统的，需要通过form来提交数据的页面，Form还是挺好用的。就像是ORM（关于ORM是什么不清楚的可以看:什么是ORM？）一样。Form是对html中Form表单的抽象。在下面几节中我们会稍加演示。

The basics - 基础的API的介绍，里面有类似于Model的Field的部分，还有组件（Widgets）的部分。

Advanced - 更丰富的使用，如何把Form同Model结合(Model也有Field，Form也有Field，用一个不行？），以及如何把媒体资源渲染到页面上呢，如果form足够好用，其实我们不需要更多的操作模板了不是吗。还有如何布局你的字段，一行展示一个还是一行展示多个，还有更加细节、深入的部分就是如何定义字段级别的验证功能。比如页面上只允许输入数字的地方如何验证。


这部分在开发admin时很常用，因为admin跟Model结合紧密，我们如果需要去改模板的话成本会有点高，所以更好的做法是通过自定义Form以及自定义Widget来实现我们需要的功能。在前台（针对用户的界面）以为我们直接写的模板，所以更加灵活，并且我们也很少使用form表单来提交数据，所以用的较少。


"""""


