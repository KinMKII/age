driving = input('請問你有沒有開過車? (有/沒有)')
if driving != '有' or driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪, 你怎麽會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了, 怎麽還不去考')
	else:
		print('你再等幾年就可以去考了')
