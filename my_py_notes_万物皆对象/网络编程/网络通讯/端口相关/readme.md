# 端口

## 什么是端口
端口就好一个房子的门，是出入这间房子的必经之路
![](https://i.loli.net/2019/09/01/pXAowi7vD3rCyNK.png)

## 端口号
端口是通过端口号来标记的，端口号只有整数，范围是从0到65535

## 端口是怎样分配的

端口号不是随意使用的，而是按照一定的规定进行分配。

端口的分类标准有好几种，我们这里不做详细讲解，只介绍一下知名端口和动态端口

## 知名端口（Well Known Ports）

知名端口是众所周知的端口号，范围从0到1023
```
80端口分配给HTTP服务
21端口分配给FTP服务
```
一般情况下，如果一个程序需要使用知名端口的需要有root权限

## 动态端口（Dynamic Ports）

动态端口的范围是从1024到65535

之所以称为动态端口，是因为它一般不固定分配某种服务，而是动态分配。

##小总结

实际上是通过“IP地址+端口号”来区分不同的服务的。 需要注意的是，端口并不是一一对应的。