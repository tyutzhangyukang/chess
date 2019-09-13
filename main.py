#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2019 Nancyqinglan <Nancyqinglan@NANCYQINGLAN-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from chess import Mychess
from button import Mybutton
from settings import Settings
import game_function as gf

#from __future__ import print_function
import pygame
import pygame.font
import traceback
from pygame.locals import *
import sys
import math
import panda3d.core 
import direct.showbase.ShowBase #Panda显示模块
import direct.gui.OnscreenText
import direct.task.Task #Panda任务模块
import direct.interval.LerpInterval
import direct.gui.DirectCheckButton
import collections


def main():
	
	#初始化pygame、设置和屏幕对象
	pygame.init()
	s = Settings()
	#创建一个窗口
	screen = pygame.display.set_mode([s.screen_width, 
									s.screen_height])
	# 设置窗口标题
	pygame.display.set_caption("中国象棋")
	
	#开始游戏的主循环
	while True:
		Mychess.draw_chessboard(s, screen)
		Mychess.draw_all_chessman(s.r, screen, s.red_label, s.black_label)
		Mybutton.draw_button(screen)
		clock = pygame.time.Clock()
		gf.check_events(s, screen)#监听所有事件
		if s.order == 1:
			#红棋落子
			gf.red_order(s, screen)
		elif s.order == -1:
			#黑棋落子
			gf.black_order(s, screen)
		if s.red_backup:
			#红框选中
			pygame.draw.rect(screen, [255, 0, 0], 
				[s.red_label[s.red_backup[0]]['cur_loc'][0] - 45, 
				s.red_label[s.red_backup[0]]['cur_loc'][1] - 45, 87, 87], 5)
		elif s.black_backup:
			#黑框选中
			pygame.draw.rect(screen, [0, 0, 0], 
				[s.black_label[s.black_backup[0]]['cur_loc'][0] - 45, 
				s.black_label[s.black_backup[0]]['cur_loc'][1] - 45, 87, 87], 5)
		#红方胜利
		if s.result == 1:
			gf.red_victory(s, screen)
		#黑方胜利
		elif s.result == -1:
			gf.black_victory(s, screen)
		elif s.result == 100:
			gf.peace(s, screen)
		pygame.display.flip()


if '__main__' == __name__:
	main()


if __name__ == "__main__":
	try:
		main()
	except SystemExit:
		pass
	except:
		traceback.print_exc()
		pygame.quit()
		input()
