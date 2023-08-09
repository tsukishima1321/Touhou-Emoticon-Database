# Touhou-Emoticon-Database
# 东方表情包数据库企划

## 开发目标
1. 以东方表情包为主要内容的带标签的图片储存
2. 支持进行标签搜索（返回符合标签的所有图片）、随机返回图片、随机返回符合标签的图片
3. 支持由用户自行编辑标签、上传图片

## 开发计划
1. 设计数据库
2. 用Web框架编写增删改查api，在查的基础上增加应用。
3. 部署并测试
4. 编写WebUI和其他客户端

## Jsonapi
提交POST请求到/api/来使用Jsonapi  
用method字段指定调用的api方法：```{“method”:"xxx"}```，如果方法名无效，会返回```{"message":"连接成功"}```  

### **方法列表：**

#### **getRandomUrl**  
随机获取单张图片的url和id  
**request:** /  
**response:** id，url


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
随机获取单张图片的url和tag信息  
**request:** /  
**response:** stditem

#### **getItemById**  
使用id查询单张图片的信息  
**request:** id  
**response:** stditem / message “Not found”

#### **getItemByName**  
使用文件名查询单张图片的信息  
**request:** name  
**response:** stditem / message “Not found”

#### **ifExist**  
使用文件的sha1哈希查询是否在数据库中存在  
**request:** hash  
**response:** exist ("true" or "false") / message “error”

#### **addTag**  
为图片增加tag  
**request:** id，(at least one in) anthor，character，tags  
**response:** stditem / message “error” "Too Long" "Invalid Text" "Not Found"  
用#分隔单个的标签：```{"character":"#恋恋#古明地恋"}```

#### **editTag**  
编辑图片的tag  
**request:** id，(at least one in) anthor，character，tags  
**response:** stditem / message “error” "Too Long" "Invalid Text" "Not Found"  
提交标签的格式同上  
**Warning:** 该操作将覆盖数据库中原有的标签，提交```{"tags":""}```会将tags标签组编辑为空，如果不想编辑某个tag组，请不要在请求中加入tag组的字段