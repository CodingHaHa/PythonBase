#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

#1：生成配置文件
import configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)


#2：配置文件的操作（add，delelete,update,query）
import configparser
#创建一个配置文件
config = configparser.ConfigParser()

#---------------------------------------------查
print(config.sections())   #[]

config.read('example.ini')

print(config.sections())   #['bitbucket.org', 'topsecret.server.com']

print('bytebong.com' in config)# False

print(config['bitbucket.org']['User']) # hg

print(config['DEFAULT']['Compression']) #yes

print(config['topsecret.server.com']['ForwardX11'])  #no


for key in config['bitbucket.org']:
    print(key)


# user
# serveraliveinterval
# compression
# compressionlevel
# forwardx11


print(config.options('bitbucket.org'))#['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']
print(config.items('bitbucket.org'))  #[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'hg')]

print(config.get('bitbucket.org','compression'))#yes


#---------------------------------------------删,改,增(config.write(open('i.cfg', "w")))


config.add_section('yuan')

config.remove_section('topsecret.server.com')
config.remove_option('bitbucket.org','user')

config.set('bitbucket.org','k1','11111')

config.write(open('i.cfg', "w"))