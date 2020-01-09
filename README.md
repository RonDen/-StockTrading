# 基于Django的个性化股票交易管理系统

Author: [LuoD](https://github.com/RonDen/)，何显，文淳正

## 安装说明

1. 克隆该项目
```bash
$ git clone https://github.com/RonDen/-StockTrading.git
```

2. 激活对应Python开发环境

```bash
$ conda activate Webdev
(Webdev)$ 
```

3. 创建对应数据库（stocktrading）和用户（trading）
```sql
create database stocktrading;
create user 'trading'@'localhost' identified by trading;
grant all privileges on stocktrading to 'trading'@'localhost';
flush privileges;
```

4. 执行迁移命令，创建模型数据表映射

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

5. 将`config/`下的sql文件导入数据库中

```sql
use stocktrading;
source stocktrading.sql;
```

6. 安装所需要的依赖包

```bash
pip install -r requirements.txt
```
本项目依赖的核心包有：Django 2.1.15与tushare pro，前者作为主要开发框架，后者是爬取股票数据的核心包。tushare需要依赖pandas等包，用于数据分析和处理。
my-fake-useragent用于生成伪请求头，爬取相应的新闻数据。
django-mptt用于生成树形多级评论。

7. 开始运行和测试

```bash
python manage.py runserver
```

打开localhost:8000端口即可查看应用。

## 运行情况

### 登录界面

![login](doc/login.png)

可以点击上方注册按钮注册。

### 注册页面

![register](doc/register.png)

输入相应信息即可完成注册。
但是考虑到已经导入数据库sql文件，那么数据库中应该有了相当数量可以直接登录的用户。可以任取一个进行测试。

username: `10071539640`
password: `65815609`

### 用户首页

![index1](doc/user_index1.png)![index2](doc/user_index2.png)

首页可以分为4个模块，传递的信息也是比较的丰富。分别是：
1. 热门牛股：根据每天的股票收盘价格和次日的开盘价格计算差值和涨幅，按照涨幅进行排序得到的前10只热门牛股；
2. 重大新闻：管理员自己发布或者通过爬虫获取到东方财富网上刊登的重大新闻简要信息，筛选后推荐给用户。可以点击`换一波瞅瞅`查看更多其他感兴趣的新闻资讯。有可以点击新闻标题进入新闻详情。
3. 看大盘模块：展示了通过tushare模块抓取的上证指数变化情况。
4. 我的评论模块：展示了我（该登录用户）近期所发布的对股票的评论信息。也可以点击评论标题进入评论详情。
5. 左侧的控制菜单面板，可通过该面板进入其他模块进行管理。


### 个人信息管理

![myprofile](doc/myprofile.png)

点击左侧`用户信息`或者上方导航栏的头像，可以进入用户信息界面，在此查看个人信息，并可以进行修改。若修改需要输入密码并确认密码。

点击修改头像可以修改头像。

![change_avatar](doc/change_avatar.png)

### 查看股票列表

![stock_list](doc/stock_list.png)

点击左侧`股票列表`即可查看股票列表，采用了DataTable组件进行列表展示。其中红色表示股价上涨的股票，
绿色表示下跌的股票。用户可以点击详情页面进行查看股票详情。

### 股票详情

![stock_detail](doc/stock_detail1.png)![stock_detail2](doc/stock_detail2.png)


用户在此页面可以进行买入操作，也可以查看返回到上级页面查看股票列表。
左上方图表显示了这支股票的股价变化日K线图与实时股价，右侧是该股票的股权占比，均是通过tushare
提供接口进行抓取获得的。

下方是关于股票的评论信息，同时用户可以发表自己关于这支股票的评论信息。


### 管理我的股票

![mystock_list](doc/mystock_list.png)


点击`管理我的股票`，即可查看已经购入的股票列表。
点击详情页面，进入抛售股票页面。

![out_stock](doc/out_stock.png)

### 管理我的评论

![mycomment](doc/mycomment.png)

点击`管理我的评论`，即可查看我已经发表过的评论信息。

详情页面可以查看所有对评论的回复信息，同时自己也可以回复自己的评论。

![mycomment_detail](doc/mycomment_detail.png)。

点击回复评论的用户名，可以查看该用户的详细信息，也可以为他(她)点赞。

![other_profile](doc/other_profile.png)

同时用户可以在`我的评论`列表将评论删除。


### 查看新闻详情

![view_news](doc/view_news.png)

点击新闻标题，可以进入新闻的详情页面。可以在这个页面点击查看上一条或者下一条新闻。

### 管理员首页

可以使用如下命令创建管理员：

```bash
python manage.py createsuperuser
```
提示输入用户名，邮箱与密码，
这里依次输入`superuser1`，空，`superuser1`。

这样就可以以超级管理员身份登录后台了。

![super_index1](doc/super_index1.png)![super_index](doc/super_index.png)


管理员界面与用户界面大同小异，只是内容更加丰富了一些。


### 用户信息管理

点击左侧`用户信息管理`进入用户信息管理详情页面。可以看到全部用户列表。

![adm_user](doc/adm_user.png)

点击`详情`进入用户信息详情。

![adm_user_detail](doc/adm_user_detail.png)

在此界面，管理员可以修改部分用户的信息，不包括密码。管理员可以冻结用户的账号，使其
无法参与股票交易，管理员也可以删除用户。

### 管理股票列表

![adm_stock_list](doc/adm_stock_list.png)

![adm_stock_detail](doc/adm_stock_detail.png)

### 管理交易记录

![adm_trading_list](doc/adm_trading_list.png)

### 股票信息维护

![uphold](doc/stock_uphold.png)![update](doc/update.png)


在此界面，管理员可以点击面板上的按钮，进行每天股票信息的维护操作。

点击`更新实时数据`按钮后，可以在控制台看到数据库更新的打印信息。

### 新闻管理

![adm_news](doc/adm_news.png)

在新闻管理页面，管理员可以添加新闻信息，也可以使用爬虫工具自动获取一些新闻信息，当然也可以进入新闻
页面的详情，对新闻的信息进行编辑或删除。

### 评论管理

![adm_comment](doc/adm_comment.png)


