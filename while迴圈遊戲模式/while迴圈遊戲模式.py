while True:
	mode = input('請輸入遊戲模式')
	if mode == 'q':
		break
	elif mode == '1':
		print('開啟遊戲模式一')
	elif mode == '2':
		print('開啟遊戲模式二')
	else:
		print('只能輸入q/1/2')
