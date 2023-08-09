# Touhou-Emoticon-Database
# 东方表情包数据库企划

## 开发目标
1. 以东方表情包为主要内容的带标签的图片储存
2. 支持进行标签搜索（返回符合标签的所有图片）、随机返回图片、随机返回符合标签的图片
3. 支持由用户自行编辑标签、上传图片

## 开发计划
1. 设计数据库
2. 用Web框架编写增删改查api, 在查的基础上增加应用。
3. 部署并测试
4. 编写WebUI和其他客户端

## Jsonapi
提交POST请求到/api/来使用Jsonapi  
用method字段指定调用的api方法：```{“method”:"xxx"}```, 如果方法名无效, 会返回```{"message":"连接成功"}```  

### **方法列表：**

#### **getRandomUrl**  
随机获取单张图片的url和id  
**request:** /  
**response:** id, url


大部分针对单张图片的api会返回图片所有需要展示的信息：
```json
{
    "id": 114, 
    "url": "http://i0.hdslb.com/bfs/article/6fc6163c746a38556c7481a98d4c911c0d84b43a.jpg", 
    "author": null, 
    "character": "#\u604b\u604b#\u53e4\u660e\u5730\u604b", 
    "tags": null, 
    "likes": 0
}
```
下文中这些信息被称为stditem


#### **getRandomItem**  
> 随机获取单张图片的url和tag信息  
**request:** /  
**response:** stditem

#### **getItemById**  
> 使用id查询单张图片的信息  
**request:** id  
**response:** stditem / message “Not found”

#### **getItemByName**  
> 使用文件名查询单张图片的信息  
**request:** name  
**response:** stditem / message “Not found”

#### **ifExist**  
> 使用文件的md5(32个字符)哈希查询是否在数据库中存在  
**request:** hash  
**response:** exist ("true" or "false") / message “error”

#### **addTag**  
> 为图片增加tag  
**request:** id, (at least one in) anthor, character, tags  
**response:** stditem / message “error” "Too Long" "Invalid Text" "Not Found"  
用#分隔单个的标签：```{"character":"#恋恋#古明地恋"}```

#### **editTag**  
> 编辑图片的tag  
**request:** id, (at least one in) anthor, character, tags  
**response:** stditem / message “error” "Too Long" "Invalid Text" "Not Found"  
提交标签的格式同上  

**Warning:** 该操作将覆盖数据库中原有的标签, 提交```{"tags":""}```会将tags标签组编辑为空, 如果不想编辑某个tag组, 请不要在请求中加入tag组的字段

#### **randomItemByTag**  
> 返回随机的符合搜索条件的图片  
**request:** (at least one in) anthor, character, tags  
**response:** stditem / message “error” "Not Found"  
可以提交多个标签、来自不同标签组的标签, 所有标签间为与关系

#### **searchByTag**  
> 返回符合搜索条件的id  
**request:** (at least one in) anthor, character, tags, (optional default=1)page, (optional default="id")order
**response:** ids(a list of id) / message “error” "Not Found"  
可以提交多个标签、来自不同标签组的标签, 所有标签间为与关系  
page为从1开始的整数, 表示访问搜索结果的页数, 一页20个结果  
order从"random"、"id"、"likes"中选择, 表示按随机、id、点赞数升序排序, "id_r"、"likes_r"为降序

#### **report**  
> 举报图片  
**request:** id, reason, (optional)detail  
**response:** message ":\)" / "Not Found"

#### **likes**  
> 为图片点赞  
**request:** id  
**response:** message ":\)" / "Not Found" 

#### **similar**  
> 汇报相似的图片  
**request:** id_main, ids(a list of id similar to the main picture)  
**response:** message ":\)" / "Not Found" 

#### **upload**  
> 向数据库添加图片  
**request:** name, (optional)anthor, (optional)character, (optional)tags, (optional)md5  
**response:** stditem / message: "error"  

如何添加图片：  
1. 在 https://www.imgtp.com/ 上传你的图片  
2. 查看网页返回的图片url，eg:```https://img1.imgtp.com/2023/08/09/mDIAOlyS.jpg```，选择不包含域名的部分作为name字段```{"name":"2023/08/09/mDIAOlyS.jpg"}```   
3. (optional)填写标签和md5(可在网站 登录-图片管理-图片信息 查看，或自行计算)  

如果提交的md5已经存在，会返回当前数据库中md5匹配的stditem
