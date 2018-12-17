from wxpy import *
bot = Bot(cache_path=True, console_qr=0.5)
#获取所有好友
friends = bot.friends()
# 获取所有群组
groups = bot.groups()
print('***************************************************')
print('*****此软件仅个人使用，请勿传播!---By Soulding*****')
print('***************************************************')
print('\n-------------------编辑发送内容--------------------------------')

while 1:
	msg = input('\n输入要发送的信息(空格表示换行，多个空格多次换行)：\n')
	msg1 = msg.replace(' ','\n')
	confirm = input('\n确认发送吗？:(y/n)\n')
	if confirm == 'y' or confirm == 'Y':
		break
#发送给全部好友
for friend in friends:
	friend.send(msg1)
#发送给所有群组
for group in groups:
	group.send(msg1)
print('\n-------------------发送的内容----------------------------------')
print(msg1)
print('\n-------------------发送的结果----------------------------------')
print('群组数：',len(groups),'好友数：',len(friends),'发送成功！')