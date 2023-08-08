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
request: /  
response: id，url


