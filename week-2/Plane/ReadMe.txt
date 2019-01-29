2019/1/27
LI Xiang
lx02140105@163.com
飞机大战
    使用pygame的模块实现 飞机大战


程序的 注意点 和 疑问

'''
基础:
    1、创建主窗口
    2、添加键盘事件
    3、放置英雄飞机(玩家)
    4、实现子弹发射
    5、随机放置敌机
    6、实现子弹与敌机的碰撞检测

拓展:
    1、爆炸(用time.sleep的方式动态的显示爆炸)
    2、选择以鼠标/键盘, 控制飞机
    3、撞机重新开始
    3、score, 50,100, 换子弹
'''

'''
主要对象: screen, hero_plane, bullet, enemy_plane,
    screen: 注意滚动
    hero_plane: 注意获取键盘事件, 当前坐标位置, 子弹
    enemy_plane: 注意hero_plane的位置(hero_plane坠毁, 子弹都不见) , 子弹位置(enemy_plane击毁, 当前子弹不见)
    bullet: 当子弹出屏幕的时候, 销毁
    keyboard: 按一次 和 长按
    score: 积分, 积分换子弹
'''

'''
疑问
    为什么 子弹和敌机的 move() 会让对象自动移动
'''
