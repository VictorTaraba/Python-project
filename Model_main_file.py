from tkinter import *
from Data_for_model import GOOG_prices, TSLA_prices, GM_prices, IBM_prices, AMZN_prices #імпортуємо списки з цінами акцій 
from PIL import Image, ImageTk

global IBM_amount, GM_amount, AMZN_amount, GOOG_amount, TSLA_amount, month, CAPITAL, i, PROFIT_per_MONTH, CAPITAL_pr_month

#глобальні змінні - кількість акцій у портфелі фонду
TSLA_amount = 0
GOOG_amount = 0
AMZN_amount = 0
IBM_amount = 0
GM_amount = 0

#потрібно для проходження по списку з цінами; початок з 2, щоб уже на першому кроці відображалися попередні ціни - за два останні місяці 2010 року
i = 2

#потрібно для відображення кількості місяціів, які пройшли з початку моделювання
month = 1

#стартовий капітал фонду
CAPITAL = 100000

#капітал на початок минулого місяця - потрібен, аби вирахвати прибутковість
CAPITAL_pr_month = 0

# щомісячна прибутковість
PROFIT_per_MONTH = 0

#графічний інтерфейс
class Invest_model(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.setUI()

	#основна частина програми - робота з графічним інтерфейсом
	def setUI(self):
		self.parent.title("Модель роботи інвестиційного фонду")
		self.parent.iconbitmap(r'USD.ico')
		self.pack(fill = BOTH, expand=1)
		self.centerWindow()

		#встановлюємо на екрані кнопки, написи, фотографію; визначаємо шрифт, колір тощо
		self.label_0 = Label(self, text='Вітаю!', font=('Arial', 30, 'bold'), fg='blue')
		self.label_0.place(x=250, y=15)
		self.label = Label(self, text="--- Ви - керівник інвестиційного фонду ---\nCтартовий капітал фонду - 100 000 доларів.\nВи можете купувати і продавати акції 5 компаній:\nTSLA (Tesla), GOOG (Alphabet), GM (General Motors),\nIBM (International Business Machines), AMZN (Amazon).", font = ('Arial', 16))
		self.label.place(x=45, y=80)
		self.label_1 = Label(self, text='Ви будете мати доступ де реальних біржових цін\nна акції в період з 01/01/2011 до 01/12/2012 включно.\nПеріод моделювання - 24 місяці.', font = ('Arial', 16))
		self.label_1.place(x=45, y=235)
		self.label_2 = Label(self, text='Після завершення періоду моделювання Ви зможете ознайомитися\nіз фінансовими даними.\n\nP. S. Не забувайте оновлювати структуру інвестиційного портфеля,\nнатискаючи на синю кнопку "Оновити".', font = ('Arial', 17))
		self.label_2.place(x=100, y=350)
		self.next_Button = Button(self, text="Далі", font = ('Arial', 18, 'bold'), fg='white', bg='blue', command = self.next_window)
		self.next_Button.place(x=450, y=495)
		self.photo_text = Label(self, text="Нью-Йоркська фондова біржа", font=('Arial', 12), fg='blue')
		self.photo_text.place(x=643, y=285)
		photo = Image.open("NYSE.jpg")
		photo1 = ImageTk.PhotoImage(photo, master=self.parent)
		self.label_photo = Label(self, image=photo1)
		self.label_photo.image = photo1
		self.label_photo.place(x=595, y=20)

	#переходимо до основного вікна програми (функціонал кнопки next_Button)
	def next_window(self):
		#знищуємо усі елементи попереднього вікна
		self.label_0.destroy()
		self.label.destroy()
		self.label_1.destroy()
		self.label_2.destroy()
		self.next_Button.destroy()
		self.label_photo.destroy()
		self.photo_text.destroy()

		#встановлюємо кнопки для купівлі та продажу акцій
		self.buy_TSLA_Button = Button(self, text="   Купити акції TSLA     ", font = ('Arial', 11, 'bold'), fg='green', bg='white', command=self.goto_buyTSLA)
		self.buy_TSLA_Button.place(x=20, y=20)
		self.sell_TSLA_Button = Button(self, text="  Продати акції TSLA   ", font = ('Arial', 11, 'bold'), fg='red', bg='white', command=self.goto_sellTSLA)
		self.sell_TSLA_Button.place(x=20, y=55)

		self.buy_GOOG_Button = Button(self, text="   Купити акції GOOG   ", font = ('Arial', 11, 'bold'), fg='green', bg='white', command=self.goto_buyGOOG)
		self.buy_GOOG_Button.place(x=20, y=115)
		self.sell_GOOG_Button = Button(self, text="  Продати акції GOOG ", font = ('Arial', 11, 'bold'), fg='red', bg='white', command=self.goto_sellGOOG)
		self.sell_GOOG_Button.place(x=20, y=150)

		self.buy_AMZN_Button = Button(self, text="   Купити акції AMZN    ", font = ('Arial', 11, 'bold'), fg='green', bg='white', command=self.goto_buyAMZN)
		self.buy_AMZN_Button.place(x=20, y=210)
		self.sell_AMZN_Button = Button(self, text="  Продати акції AMZN  ", font = ('Arial', 11, 'bold'), fg='red', bg='white', command=self.goto_sellAMZN)
		self.sell_AMZN_Button.place(x=20, y=245)

		self.buy_IBM_Button = Button(self, text="   Купити акції IBM        ", font = ('Arial', 11, 'bold'), fg='green', bg='white', command=self.goto_buyIBM)
		self.buy_IBM_Button.place(x=20, y=305)
		self.sell_IBM_Button = Button(self, text="  Продати акції IBM      ", font = ('Arial', 11, 'bold'), fg='red', bg='white', command=self.goto_sellIBM)
		self.sell_IBM_Button.place(x=20, y=340)

		self.buy_GM_Button = Button(self, text="   Купити акції GM         ", font = ('Arial', 11, 'bold'), fg='green', bg='white', command=self.goto_buyGM)
		self.buy_GM_Button.place(x=20, y=400)
		self.sell_GM_Button = Button(self, text="  Продати акції GM       ", font = ('Arial', 11, 'bold'), fg='red', bg='white', command=self.goto_sellGM)
		self.sell_GM_Button.place(x=20, y=435)

		#встановлюємо кнопки та написи, які з кожним кроком моделювання будуть показувати оновлену статистичну інформацію
		self.refresh = Button(self, text="Оновити структуру\nінвестиційного\nпортфеля", font = ('Arial', 13, 'bold'), fg='white', bg='blue', command=self.refresh)
		self.refresh.place(x=20, y=505)

		self.label_month = Label(self, text=" --- Місяць (з початку торгівлі): ---\n{}".format(month), font = ('Arial', 11, 'bold'))
		self.label_month.place(x=550, y=180)
		self.label_capital = Label(self, text=" --- Загальний капітал фонду: ---\n{:.2f}".format(CAPITAL), font = ('Arial', 11, 'bold'), fg='blue')
		self.label_capital.place(x=550, y=240)
		self.next_month_Button = Button(self, text="   Підтвердити введені дані і перейти\n до наступного місяця", font = ('Arial', 11, 'bold'), bg='white', fg='blue', command=self.next_month)
		self.next_month_Button.place(x=590, y=525)

		#встановлюємо табло з цінами акцій - для поточного місяця і двох попередніх (аби мати змогу приймати виважені інвестиційні рішенн)
		self.label_stock_prices_1 = Label(self, text="--- Ціна акцій цього місяця ---", font = ('Arial', 11, 'bold'))
		self.label_stock_prices_1.place(x=230, y=20)
		self.label_TSLA_1 = Label(self, text=' '*16+'TSLA:'+'  '+str(TSLA_prices[i])+' USD')
		self.label_TSLA_1.place(x=230, y=60)
		self.label_GOOG_1 = Label(self, text=' '*16+'GOOG:'+'  '+str(GOOG_prices[i])+' USD')
		self.label_GOOG_1.place(x=230, y=80)
		self.label_AMZN_1 = Label(self, text=' '*16+'AMZN:'+'  '+str(AMZN_prices[i])+' USD')
		self.label_AMZN_1.place(x=230, y=100)
		self.label_IBM_1 = Label(self, text=' '*16+'IBM:'+'  '+str(IBM_prices[i])+' USD')
		self.label_IBM_1.place(x=230, y=120)
		self.label_GM_1 = Label(self, text=' '*16+'GM:'+'  '+str(GM_prices[i])+' USD')
		self.label_GM_1.place(x=230, y=140)

		self.label_stock_prices_2 = Label(self, text="--- Ціна акцій минулого місяця ---", font = ('Arial', 11, 'bold'))
		self.label_stock_prices_2.place(x=230, y=180)
		self.label_TSLA_2 = Label(self, text=' '*16+'TSLA:'+'  '+str(TSLA_prices[i-1])+' USD')
		self.label_TSLA_2.place(x=230, y=220)
		self.label_GOOG_2 = Label(self, text=' '*16+'GOOG:'+'  '+str(GOOG_prices[i-1])+' USD')
		self.label_GOOG_2.place(x=230, y=240)
		self.label_AMZN_2 = Label(self, text=' '*16+'AMZN:'+'  '+str(AMZN_prices[i-1])+' USD')
		self.label_AMZN_2.place(x=230, y=260)
		self.label_IBM_2 = Label(self, text=' '*16+'IBM:'+'  '+str(IBM_prices[i-1])+' USD')
		self.label_IBM_2.place(x=230, y=280)
		self.label_GM_2 = Label(self, text=' '*16+'GM:'+'  '+str(GM_prices[i-1])+' USD')
		self.label_GM_2.place(x=230, y=300)

		self.label_stock_prices_3 = Label(self, text="--- Ціна акцій позаминулого місяця ---", font = ('Arial', 11, 'bold'))
		self.label_stock_prices_3.place(x=230, y=340)
		self.label_TSLA_3 = Label(self, text=' '*16+'TSLA:'+'  '+str(TSLA_prices[i-2])+' USD')
		self.label_TSLA_3.place(x=230, y=380)
		self.label_GOOG_3 = Label(self, text=' '*16+'GOOG:'+'  '+str(GOOG_prices[i-2])+' USD')
		self.label_GOOG_3.place(x=230, y=400)
		self.label_AMZN_3 = Label(self, text=' '*16+'AMZN:'+'  '+str(AMZN_prices[i-2])+' USD')
		self.label_AMZN_3.place(x=230, y=420)
		self.label_IBM_3 = Label(self, text=' '*16+'IBM:'+'  '+str(IBM_prices[i-2])+' USD')
		self.label_IBM_3.place(x=230, y=440)
		self.label_GM_3 = Label(self, text=' '*16+'GM:'+'  '+str(GM_prices[i-2])+' USD')
		self.label_GM_3.place(x=230, y=460)

		#встановлюємо кнопки та написи, які з кожним кроком моделювання будуть показувати оновлену статистичну інформацію
		#визначаємо розмір і тип шрифту для кожної кнопки та напису
		self.label_statistic = Label(self, text='--- Ваші результати за минулий місяць: ---')
		self.label_statistic.config(font = ('Arial', 11, 'bold'))
		self.label_statistic.place(x=550, y=20)
		self.label_statistic_1 = Label(self, text=' '*6+'Капітал Вашого фонду на початку минулого місяця:  '+str(0))
		self.label_statistic_1.place(x=550, y=60)
		self.label_statistic_2 = Label(self, text=' '*6+'Капітал Вашого фонду під кінець минулого місяця:  '+str(0))
		self.label_statistic_2.place(x=550, y=80)
		self.label_statistic_3 = Label(self, text=' '*6+'Прибутковість за минулий місяць (у %):  {0:.2f}'.format(PROFIT_per_MONTH))
		self.label_statistic_3.place(x=550, y=100)

		self.invest_balance = Label(self, text='--- Структура вашого інвестиційного портфеля: ---', bg='blue', fg='white')
		self.invest_balance.config(font = ('Arial', 11, 'bold'))
		self.invest_balance.place(x=550, y=340)
		self.balance_label_TSLA = Label(self, text=' '*19+'TSLA:'+' '*7+str(0)+' шт.')
		self.balance_label_TSLA.place(x=550, y=380)
		self.balance_label_GOOG = Label(self, text=' '*19+'GOOG:'+' '*4+str(0)+' шт.')
		self.balance_label_GOOG.place(x=550, y=400)
		self.balance_label_AMZN = Label(self, text=' '*19+'AMZN:'+' '*4+str(0)+' шт.')
		self.balance_label_AMZN.place(x=550, y=420)
		self.balance_label_IBM = Label(self, text=' '*19+'IBM:'+' '*8+str(0)+' шт.')
		self.balance_label_IBM.place(x=550, y=440)
		self.balance_label_GM = Label(self, text=' '*19+'GM:'+' '*9+str(0)+' шт.')
		self.balance_label_GM.place(x=550, y=460)

		self.quitButton = Button(self, text="   Вийти з програми\n  (без виведення даних) ", font = ('Arial', 11, 'bold'), bg='white', fg='blue', command = self.quit)
		self.quitButton.place(x=270, y=525)

	# описуємо функціонал кнопки "Оновити" - вона оновлює структуру інвестиційного портфеля і виводить суму інвестицій
	def refresh(self):
		global i
		if i <= 25:
			global CAPITAL, TSLA_amount, AMZN_prices, GOOG_amount, IBM_amount, GM_amount

			TSLA_amount_USD = TSLA_amount*TSLA_prices[i]
			AMZN_amount_USD = AMZN_amount*AMZN_prices[i]
			GOOG_amount_USD = GOOG_amount*GOOG_prices[i]
			GM_amount_USD = GM_amount*GM_prices[i]
			IBM_amount_USD = IBM_amount*IBM_prices[i]

			self.balance_label_TSLA["text"] = ' '*19+'TSLA:'+' '*7+str(TSLA_amount)+' шт.'+'    {:.2f} USD'.format(TSLA_amount_USD)
			self.balance_label_AMZN["text"] = ' '*19+'AMZN:'+' '*4+str(AMZN_amount)+' шт.'+'     {:.2f} USD'.format(AMZN_amount_USD)
			self.balance_label_GOOG["text"] = ' '*19+'GOOG:'+' '*4+str(GOOG_amount)+' шт.'+'     {:.2f} USD'.format(GOOG_amount_USD)
			self.balance_label_GM["text"] = ' '*19+'GM:'+' '*9+str(GM_amount)+' шт.'+'    {:.2f} USD'.format(GM_amount_USD)
			self.balance_label_IBM["text"] = ' '*19+'IBM:'+' '*8+str(IBM_amount)+' шт.'+'    {:.2f} USD'.format(IBM_amount_USD)
		else:
			self.end_the_game()

	#описує функціонал кнопки "Перефти до наступного місяця"
	#проводимо необхідні підрахунки, оновлюємо дані на екрані
	def next_month(self):
		global i, month
		month = month + 1
		i = i + 1

		if i <=25:
			global CAPITAL, TSLA_amount, AMZN_prices, GOOG_amount, IBM_amount, GM_amount, CAPITAL_pr_month

			TSLA_amount_USD = TSLA_amount*TSLA_prices[i]
			AMZN_amount_USD = AMZN_amount*AMZN_prices[i]
			GOOG_amount_USD = GOOG_amount*GOOG_prices[i]
			GM_amount_USD = GM_amount*GM_prices[i]
			IBM_amount_USD = IBM_amount*IBM_prices[i]

			CAPITAL_pr_month = CAPITAL
			new_CAPITAL = (CAPITAL-IBM_amount*IBM_prices[i-1]-GM_amount*GM_prices[i-1]-GOOG_amount*GOOG_prices[i-1]-AMZN_amount*AMZN_prices[i-1]
				-TSLA_amount*TSLA_prices[i-1])+IBM_amount_USD+GM_amount_USD+GOOG_amount_USD+AMZN_amount_USD+TSLA_amount_USD
			CAPITAL = new_CAPITAL

			#підрахунок прибутковості за минулий місяць
			self.profit_for_month()

			self.label_statistic_1["text"] =' '*6+'Капітал Вашого фонду на початку минулого місяця:  {:.2f}'.format(CAPITAL_pr_month)
			self.label_statistic_2["text"] =' '*6+'Капітал Вашого фонду під кінець минулого місяця:  {:.2f}'.format(CAPITAL)
			self.label_statistic_3["text"] =' '*6+'Прибутковість за минулий місяць (у %):  {0:.2f}'.format(PROFIT_per_MONTH)
			self.label_capital["text"] = " --- Загальний капітал фонду: ---\n{:.2f}".format(CAPITAL)

			self.label_month["text"] = " --- Місяць (з початку торгівлі): ---\n{}".format(month)
			self.balance_label_TSLA["text"] = ' '*19+'TSLA:'+' '*7+str(TSLA_amount)+' шт.'+'    {:.2f} USD'.format(TSLA_amount_USD)
			self.balance_label_AMZN["text"] = ' '*19+'AMZN:'+' '*4+str(AMZN_amount)+' шт.'+'    {:.2f} USD'.format(AMZN_amount_USD)
			self.balance_label_GOOG["text"] = ' '*19+'GOOG:'+' '*4+str(GOOG_amount)+' шт.'+'    {:.2f} USD'.format(GOOG_amount_USD)
			self.balance_label_GM["text"] = ' '*19+'GM:'+' '*9+str(GM_amount)+' шт.'+'    {:.2f} USD'.format(GM_amount_USD)
			self.balance_label_IBM["text"] = ' '*19+'IBM:'+' '*8+str(IBM_amount)+' шт.'+'    {:.2f} USD'.format(IBM_amount_USD)

			self.label_TSLA_1["text"] = ' '*16+'TSLA:'+'  '+str(TSLA_prices[i])+' USD'
			self.label_GOOG_1["text"] = ' '*16+'GOOG:'+'  '+str(GOOG_prices[i])+' USD'
			self.label_AMZN_1["text"] = ' '*16+'AMZN:'+'  '+str(AMZN_prices[i])+' USD'
			self.label_IBM_1["text"] = ' '*16+'IBM:'+'  '+str(IBM_prices[i])+' USD'
			self.label_GM_1["text"] = ' '*16+'GM:'+'  '+str(GM_prices[i])+' USD'

			self.label_TSLA_2["text"] = ' '*16+'TSLA:'+'  '+str(TSLA_prices[i-1])+' USD'
			self.label_GOOG_2["text"] = ' '*16+'GOOG:'+'  '+str(GOOG_prices[i-1])+' USD'
			self.label_AMZN_2["text"] = ' '*16+'AMZN:'+'  '+str(AMZN_prices[i-1])+' USD'
			self.label_IBM_2["text"] = ' '*16+'IBM:'+'  '+str(IBM_prices[i-1])+' USD'
			self.label_GM_2["text"] = ' '*16+'GM:'+'  '+str(GM_prices[i-1])+' USD'

			self.label_TSLA_3["text"] = ' '*16+'TSLA:'+'  '+str(TSLA_prices[i-2])+' USD'
			self.label_GOOG_3["text"] = ' '*16+'GOOG:'+'  '+str(GOOG_prices[i-2])+' USD'
			self.label_AMZN_3["text"] = ' '*16+'AMZN:'+'  '+str(AMZN_prices[i-2])+' USD'
			self.label_IBM_3["text"] = ' '*16+'IBM:'+'  '+str(IBM_prices[i-2])+' USD'
			self.label_GM_3["text"] = ' '*16+'GM:'+'  '+str(GM_prices[i-2])+' USD'
		else:
			#якщо моделювання завершено - перейти до наступного вікна
			self.end_the_game()

	#перше з вікон, які виводяться після завершення терміну моделювання
	def end_the_game(self):
		self.next_month_Button["text"] = "Вивести статистичні дані", 	
		if i == 27:
			#знищуємо усе, що залишилося від попереднього вікна
			self.quitButton.destroy()
			self.label_month.destroy()
			self.buy_TSLA_Button.destroy()
			self.sell_TSLA_Button.destroy()
			self.buy_GOOG_Button.destroy()
			self.sell_GOOG_Button.destroy()
			self.buy_AMZN_Button.destroy()
			self.sell_AMZN_Button.destroy()
			self.buy_IBM_Button.destroy()
			self.sell_IBM_Button.destroy()
			self.buy_GM_Button.destroy()
			self.sell_GM_Button.destroy()
			self.refresh.destroy()
			self.label_month.destroy()
			self.label_capital.destroy()
			self.next_month_Button.destroy()
			self.label_stock_prices_1.destroy()
			self.label_TSLA_1.destroy()
			self.label_GOOG_1.destroy()
			self.label_AMZN_1.destroy()
			self.label_IBM_1.destroy()
			self.label_GM_1.destroy()
			self.label_stock_prices_2.destroy()
			self.label_TSLA_2.destroy()
			self.label_GOOG_2.destroy()
			self.label_AMZN_2.destroy()
			self.label_IBM_2.destroy()
			self.label_GM_2.destroy()
			self.label_stock_prices_3.destroy()
			self.label_TSLA_3.destroy()
			self.label_GOOG_3.destroy()
			self.label_AMZN_3.destroy()
			self.label_IBM_3.destroy()
			self.label_GM_3.destroy()
			self.label_statistic.destroy()
			self.label_statistic_1.destroy()
			self.label_statistic_2.destroy()
			self.label_statistic_3.destroy()
			self.invest_balance.destroy()
			self.balance_label_TSLA.destroy()
			self.balance_label_GOOG.destroy()
			self.balance_label_AMZN.destroy()
			self.balance_label_IBM.destroy()
			self.balance_label_GM.destroy()

			#завантажуємо два графіки з цінами акцій і встановлюємо на екрані
			photo01 = Image.open("AMZN.jpg")
			photo1 = ImageTk.PhotoImage(photo01, master=self.parent)
			self.label_photo = Label(self, image=photo1)
			self.label_photo.image = photo1
			self.label_photo.place(x=0, y=100)

			photo02 = Image.open("AMZN_day.jpg")
			photo2 = ImageTk.PhotoImage(photo02, master=self.parent)
			self.label_photo_1 = Label(self, image=photo2)
			self.label_photo_1.image = photo2
			self.label_photo_1.place(x=470, y=100)

			#встановлюємо написи, визначаємо функціонал кнопок
			self.button_next = Button(self, text='Далі', font = ('Arial', 18, 'bold'), bg='white', fg='blue', command=self.next_end_window)
			self.button_next.place(x=580, y=500)
			self.quitButton = Button(self, text="Вийти з програми", font = ('Arial', 18, 'bold'), bg='white', fg='blue', command = self.quit)
			self.quitButton.place(x=280, y=500)

			self.label = Label(self, text='\n--- Графік цін акції AMZN ---\n(побудовано за місячними цінами закриття)\n', font = ('Arial', 12, 'bold'))
			self.label.place(x=60, y=20)
			self.label_0 = Label(self, text='\n--- Графік цін акції AMZN ---\n(побудовано за цінами закриття для кожного дня)\n', font = ('Arial', 12, 'bold'))
			self.label_0.place(x=500, y=20)

	#наступне вікно зі статистичною інформацією
	def next_end_window(self):
		self.label_photo.destroy()
		self.label_photo_1.destroy()
		self.button_next.destroy()

		#встановлюємо графіки для акції TSLA
		photo01 = Image.open("TSLA.jpg")
		photo1 = ImageTk.PhotoImage(photo01, master=self.parent)
		self.label_photo = Label(self, image=photo1)
		self.label_photo.image = photo1
		self.label_photo.place(x=0, y=100)

		photo02 = Image.open("TSLA_day.jpg")
		photo2 = ImageTk.PhotoImage(photo02, master=self.parent)
		self.label_photo_1 = Label(self, image=photo2)
		self.label_photo_1.image = photo2
		self.label_photo_1.place(x=470, y=100)

		self.button_next = Button(self, text='Далі', font = ('Arial', 18, 'bold'), bg='white', fg='blue', command=self.next_end_window_1)
		self.button_next.place(x=580, y=500)

		self.label["text"] = '\n--- Графік цін акції TSLA ---\n(побудовано за місячними цінами закриття)\n'
		self.label_0["text"] = '\n--- Графік цін акції TSLA ---\n(побудовано за цінами закриття для кожного дня)\n'

	#наступне вікно зі статистичною інформацією
	def next_end_window_1(self):
		self.label_photo.destroy()
		self.label_photo_1.destroy()
		self.button_next.destroy()

		#завантажуємо графіки для акції GM
		photo01 = Image.open("GM.jpg")
		photo1 = ImageTk.PhotoImage(photo01, master=self.parent)
		self.label_photo = Label(self, image=photo1)
		self.label_photo.image = photo1
		self.label_photo.place(x=0, y=100)

		photo02 = Image.open("GM_day.jpg")
		photo2 = ImageTk.PhotoImage(photo02, master=self.parent)
		self.label_photo_1 = Label(self, image=photo2)
		self.label_photo_1.image = photo2
		self.label_photo_1.place(x=470, y=100)

		self.button_next = Button(self, text='Далі', font = ('Arial', 18, 'bold'), bg='white', fg='blue', command=self.next_end_window_2)
		self.button_next.place(x=580, y=500)

		self.label["text"] = '\n--- Графік цін акції GM ---\n(побудовано за місячними цінами закриття)\n'
		self.label_0["text"] = '\n--- Графік цін акції GM ---\n(побудовано за цінами закриття для кожного дня)\n'

	#наступне вікно зі статистичною інформацією; функціонал такий же, як і в попередніх;
	def next_end_window_2(self):
		self.label_photo.destroy()
		self.label_photo_1.destroy()
		self.button_next.destroy()

		photo01 = Image.open("IBM.jpg")
		photo1 = ImageTk.PhotoImage(photo01, master=self.parent)
		self.label_photo = Label(self, image=photo1)
		self.label_photo.image = photo1
		self.label_photo.place(x=0, y=100)

		photo02 = Image.open("IBM_day.jpg")
		photo2 = ImageTk.PhotoImage(photo02, master=self.parent)
		self.label_photo_1 = Label(self, image=photo2)
		self.label_photo_1.image = photo2
		self.label_photo_1.place(x=470, y=100)

		self.button_next = Button(self, text='Далі', font = ('Arial', 18, 'bold'), bg='white', fg='blue', command=self.next_end_window_3)
		self.button_next.place(x=580, y=500)

		self.label["text"] = '\n--- Графік цін акції IBM ---\n(побудовано за місячними цінами закриття)\n'
		self.label_0["text"] = '\n--- Графік цін акції IBM ---\n(побудовано за цінами закриття для кожного дня)\n'

	#наступне вікно зі статистичною інформацією; функціонал такий же, як і в попередніх;
	def next_end_window_3(self):
		self.label_photo.destroy()
		self.label_photo_1.destroy()
		self.button_next.destroy()

		photo01 = Image.open("GOOG.jpg")
		photo1 = ImageTk.PhotoImage(photo01, master=self.parent)
		self.label_photo = Label(self, image=photo1)
		self.label_photo.image = photo1
		self.label_photo.place(x=0, y=100)

		photo02 = Image.open("GOOG_day.jpg")
		photo2 = ImageTk.PhotoImage(photo02, master=self.parent)
		self.label_photo_1 = Label(self, image=photo2)
		self.label_photo_1.image = photo2
		self.label_photo_1.place(x=470, y=100)

		self.button_next = Button(self, text='Далі', font = ('Arial', 18, 'bold'), bg='white', fg='blue', command=self.final_window)
		self.button_next.place(x=580, y=500)

		self.label["text"] = '\n--- Графік цін акції GOOG ---\n(побудовано за місячними цінами закриття)\n'
		self.label_0["text"] = '\n--- Графік цін акції GOOG ---\n(побудовано за цінами закриття для кожного дня)\n'

	#останнє вікно зі статистичною інформацією
	def final_window(self):
		self.label_photo.destroy()
		self.label_photo_1.destroy()
		self.button_next.destroy()
		self.label.destroy()
		self.label_0.destroy()
		self.button_next.destroy()
		self.quitButton.destroy()
		
		#рахуємо прибутковість за 2 роки
		final_profit = CAPITAL - 100000
		final_percent = (CAPITAL*100)/100000-100

		#прощальні слова
		self.label = Label(self, text='Коли Ви почали працювати в інвестиційному фонді,\nкапітал фонду становив 100000.00 USD.\nТепер - {:.2f} USD.\n\nПрибутковість фонду за 2 роки - {:.2f} USD\nабо {:.2f} %.'.format(CAPITAL, final_profit, final_percent), font=('Arial', 23))
		self.label.place(x=100, y=100)
		self.label1 = Label(self, text='Моделювання завершено', font=('Arial', 27, 'bold'), fg='blue')
		self.label1.place(x=260, y=20)
		self.label3 = Label(self, text='Якщо під час роботи програми Ви виявили помилки\nабо маєте пропозиції щодо покращення програми,\nпишіть на пошту: victorabcd@ukr.net', font=('Arial', 24))
		self.label3.place(x=100, y=350)
		self.quitButton = Button(self, text="Вийти з програми", font = ('Arial', 24, 'bold'), bg='white', fg='blue', command = self.quit)
		self.quitButton.place(x=320, y=500)

	#рахує прибутковість за місяць
	def profit_for_month(self):
		global PROFIT_per_MONTH
		global CAPITAL
		global CAPITAL_pr_month

		try:
			if CAPITAL != CAPITAL_pr_month:
				PROFIT_per_MONTH = (CAPITAL*100)/CAPITAL_pr_month - 100
			else:
				PROFIT_per_MONTH = 0
		except:
			#на 1 місяці виникає ділення на 0 - тут ми уникаємо цієї помилки і просто встановлюємо нульову прибутковість
			PROFIT_per_MONTH = 0

	#встановлює вікно по центру екрана
	def centerWindow(self):
		w = 950
		h = 600
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	#функціонал кнопки "Купити акції" - перехід до вікна  введення
	def goto_buyTSLA(self):
		window = Toplevel(self.parent)
		my_window = BuyTSLA(window)

	#функціонал кнопки "Продати акції" - перехід до вікна  введення
	def goto_sellTSLA(self):
		window = Toplevel(self.parent)
		my_window = SellTSLA(window)

	#функціонал кнопки "Купити акції" - перехід до вікна  введення
	def goto_buyAMZN(self):
		window = Toplevel(self.parent)
		my_window = BuyAMZN(window)

	#функціонал кнопки "Продати акції" - перехід до вікна  введення
	def goto_sellAMZN(self):
		window = Toplevel(self.parent)
		my_window = SellAMZN(window)

	#функціонал кнопки "Купити акції" - перехід до вікна  введення
	def goto_buyGOOG(self):
		window = Toplevel(self.parent)
		my_window = BuyGOOG(window)

	#функціонал кнопки "Продати акції" - перехід до вікна  введення
	def goto_sellGOOG(self):
		window = Toplevel(self.parent)
		my_window = SellGOOG(window)

	#функціонал кнопки "Купити акції" - перехід до вікна  введення
	def goto_buyGM(self):
		window = Toplevel(self.parent)
		my_window = BuyGM(window)

	#функціонал кнопки "Продати акції" - перехід до вікна  введення
	def goto_sellGM(self):
		window = Toplevel(self.parent)
		my_window = SellGM(window)

	#функціонал кнопки "Купити акції" - перехід до вікна  введення
	def goto_buyIBM(self):
		window = Toplevel(self.parent)
		my_window = BuyIBM(window)

	#функціонал кнопки "Продати акції" - перехід до вікна  введення
	def goto_sellIBM(self):
		window = Toplevel(self.parent)
		my_window = SellIBM(window)

#вікно, яке відповідає за покупку акцій і викликається натисканням на відповідну кнопку
class BuyTSLA():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій TSLA,\nяку ви б хотіли придбати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	#встановлюємо по центру
	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	#перевіряємо дані, якщо потрібно - виводимо повідомлення про нестачу коштів або некоректне введення; якщо все - правильно - зберігаємо дані і повертаємося до головного вікна
	def myquit(self):
		global TSLA_amount

		try:
			TSLA_bought = int(self.amount.get())
			CAPITAL_ = CAPITAL - GOOG_amount*GOOG_prices[i] - AMZN_amount*AMZN_prices[i] - GM_amount*GM_prices[i] - IBM_amount*IBM_prices[i]
			if TSLA_bought < 0:
				raise ValueError
			elif (TSLA_amount + TSLA_bought)*TSLA_prices[i] > CAPITAL_:
				raise SyntaxError
			TSLA_amount = TSLA_amount + TSLA_bought
			self.parent.destroy()
		except SyntaxError:
			TSLA_possible = int(CAPITAL_/TSLA_prices[i])
			self.label_incorrect["text"] = "Недостатньо коштів на рахунку. Ви можете\nкупити лише {} акцій (спробуйте\nпродати інші акції, аби звільнити кошти)".format(TSLA_possible-TSLA_amount)
			self.label_incorrect.place(x=15, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

#вікно, яке відповідає за продаж акцій і викликається натисканням на відповідну кнопку
class SellTSLA():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій TSLA,\nяку ви б хотіли продати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	#перевіряємо введені дані, якщо вони коректні = зберігаємо, якщо ні - виводимо написом на екрані відповідне повідомлення
	def myquit(self):
		global TSLA_amount

		try:
			Night_King = TSLA_prices[i]
			TSLA_sold = int(self.amount.get())
			if TSLA_sold < 0:
				raise ValueError
			elif TSLA_sold > TSLA_amount:
				raise SyntaxError
			TSLA_amount = TSLA_amount - TSLA_sold
			self.parent.destroy()
		except SyntaxError:
			self.label_incorrect["text"] = "Ви не можете продати стільки акцій.\nВи володієте {} акціями.\nВведіть коректні дані".format(TSLA_amount)
			self.label_incorrect.place(x=30, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

#функціонал аналогічний попередньому, відрізняється лише назва акції
class BuyGOOG():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій GOOG,\nяку ви б хотіли придбати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def myquit(self):
		global GOOG_amount

		try:
			GOOG_bought = int(self.amount.get())
			CAPITAL_ = CAPITAL - TSLA_amount*TSLA_prices[i] - AMZN_amount*AMZN_prices[i] - GM_amount*GM_prices[i] - IBM_amount*IBM_prices[i]
			if GOOG_bought < 0:
				raise ValueError
			elif (GOOG_amount + GOOG_bought)*GOOG_prices[i] > CAPITAL_:
				raise SyntaxError
			GOOG_amount = GOOG_amount + GOOG_bought
			self.parent.destroy()
		except SyntaxError:
			GOOG_possible = int(CAPITAL_/GOOG_prices[i])
			self.label_incorrect["text"] = "Недостатньо коштів на рахунку. Ви можете\nкупити лише {} акцій (спробуйте\nпродати інші акції, аби звільнити кошти)".format(GOOG_possible-GOOG_amount)
			self.label_incorrect.place(x=15, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

#функціонал аналогічний попередньому, відрізняється лише назва акції
class SellGOOG():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій GOOG,\nяку ви б хотіли продати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def myquit(self):
		global GOOG_amount

		try:
			Night_King = TSLA_prices[i]
			GOOG_sold = int(self.amount.get())
			if GOOG_sold < 0:
				raise ValueError
			elif GOOG_sold > GOOG_amount:
				raise SyntaxError
			GOOG_amount = GOOG_amount - GOOG_sold
			self.parent.destroy()
		except SyntaxError:
			self.label_incorrect["text"] = "Ви не можете продати стільки акцій.\nВи володієте {} акціями.\nВведіть коректні дані".format(GOOG_amount)
			self.label_incorrect.place(x=30, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

#функціонал аналогічний попередньому, відрізняється лише назва акції
class BuyAMZN():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій AMZN,\nяку ви б хотіли придбати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def myquit(self):
		global AMZN_amount

		try:
			AMZN_bought = int(self.amount.get())
			CAPITAL_ = CAPITAL - GOOG_amount*GOOG_prices[i] - TSLA_amount*TSLA_prices[i] - GM_amount*GM_prices[i] - IBM_amount*IBM_prices[i]
			if AMZN_bought < 0:
				raise ValueError
			elif (AMZN_amount + AMZN_bought)*AMZN_prices[i] > CAPITAL_:
				raise SyntaxError
			AMZN_amount = AMZN_amount + AMZN_bought
			self.parent.destroy()
		except SyntaxError:
			AMZN_possible = int(CAPITAL_/AMZN_prices[i])
			self.label_incorrect["text"] = "Недостатньо коштів на рахунку. Ви можете\nкупити лише {} акцій (спробуйте\nпродати інші акції, аби звільнити кошти)".format(AMZN_possible-AMZN_amount)
			self.label_incorrect.place(x=15, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

#функціонал аналогічний попередньому, відрізняється лише назва акції
class SellAMZN():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій AMZN,\nяку ви б хотіли продати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def myquit(self):
		global AMZN_amount

		try:
			Night_King = TSLA_prices[i]
			AMZN_sold = int(self.amount.get())
			if AMZN_sold < 0:
				raise ValueError
			elif AMZN_sold > AMZN_amount:
				raise SyntaxError
			AMZN_amount = AMZN_amount - AMZN_sold
			self.parent.destroy()
		except SyntaxError:
			self.label_incorrect["text"] = "Ви не можете продати стільки акцій.\nВи володієте {} акціями.\nВведіть коректні дані".format(AMZN_amount)
			self.label_incorrect.place(x=30, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

#функціонал аналогічний попередньому, відрізняється лише назва акції
class BuyIBM():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій IBM,\nяку ви б хотіли придбати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def myquit(self):
		global IBM_amount

		try:
			IBM_bought = int(self.amount.get())
			CAPITAL_ = CAPITAL - GOOG_amount*GOOG_prices[i] - AMZN_amount*AMZN_prices[i] - GM_amount*GM_prices[i] - TSLA_amount*TSLA_prices[i]
			if IBM_bought < 0:
				raise ValueError
			elif (IBM_amount + IBM_bought)*IBM_prices[i] > CAPITAL_:
				raise SyntaxError
			IBM_amount = IBM_amount + IBM_bought
			self.parent.destroy()
		except SyntaxError:
			IBM_possible = int(CAPITAL_/IBM_prices[i])
			self.label_incorrect["text"] = "Недостатньо коштів на рахунку. Ви можете\nкупити лише {} акцій (спробуйте\nпродати інші акції, аби звільнити кошти)".format(IBM_possible-IBM_amount)
			self.label_incorrect.place(x=15, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

#функціонал аналогічний попередньому, відрізняється лише назва акції
class SellIBM():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій IBM,\nяку ви б хотіли продати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def myquit(self):
		global IBM_amount

		try:
			Night_King = TSLA_prices[i]
			IBM_sold = int(self.amount.get())
			if IBM_sold < 0:
				raise ValueError
			elif IBM_sold > IBM_amount:
				raise SyntaxError
			IBM_amount = IBM_amount - IBM_sold
			self.parent.destroy()
		except SyntaxError:
			self.label_incorrect["text"] = "Ви не можете продати стільки акцій.\nВи володієте {} акціями.\nВведіть коректні дані".format(IBM_amount)
			self.label_incorrect.place(x=30, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

#функціонал аналогічний попередньому, відрізняється лише назва акції
class BuyGM():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій GM,\nяку ви б хотіли придбати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

	def myquit(self):
		global GM_amount

		try:
			GM_bought = int(self.amount.get())
			CAPITAL_ = CAPITAL - GOOG_amount*GOOG_prices[i] - AMZN_amount*AMZN_prices[i] - TSLA_amount*TSLA_prices[i] - IBM_amount*IBM_prices[i]
			if GM_bought < 0:
				raise ValueError
			elif (GM_amount + GM_bought)*GM_prices[i] > CAPITAL_:
				raise SyntaxError
			GM_amount = GM_amount + GM_bought
			self.parent.destroy()
		except SyntaxError:
			GM_possible = int(CAPITAL_/GM_prices[i])
			self.label_incorrect["text"] = "Недостатньо коштів на рахунку. Ви можете\nкупити лише {} акцій (спробуйте\nпродати інші акції, аби звільнити кошти)".format(GM_possible-GM_amount)
			self.label_incorrect.place(x=15, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

#функціонал аналогічний попередньому, відрізняється лише назва акції
class SellGM():
	def __init__(self, parent):
		self.parent = parent
		self.centerWindow()
		self.parent.title("Введення даних")
		self.parent.iconbitmap(r'USD.ico')

		self.label = Label(self.parent, text="Введіть кількість акцій GM,\nяку ви б хотіли продати", font = ('Arial', 11, 'bold'))
		self.label.place(x=50, y=30)

		self.amount = Entry(self.parent)
		self.amount.place(x=100, y=80)

		self.button = Button(self.parent, text="Підтвердити введені дані", font = ('Arial', 11, 'bold'), bg='white', fg='green', command=self.myquit)
		self.button.place(x=59, y=110)

		self.label_incorrect = Label(self.parent, text="", font = ('Arial', 11, 'bold'), fg='red')
		self.label_incorrect.place(x=15, y=150)

	def myquit(self):
		global GM_amount

		try:
			Night_King = TSLA_prices[i]
			GM_sold = int(self.amount.get())
			if GM_sold < 0:
				raise ValueError
			elif GM_sold > GM_amount:
				raise SyntaxError
			GM_amount = GM_amount - GM_sold
			self.parent.destroy()
		except SyntaxError:
			self.label_incorrect["text"] = "Ви не можете продати стільки акцій.\nВи володієте {} акціями.\nВведіть коректні дані".format(GM_amount)
			self.label_incorrect.place(x=30, y=150)
		except ValueError:
			self.label_incorrect["text"] = "Введіть коректні дані !\n(невід'ємне число)"
			self.label_incorrect.place(x=80, y=150)
		except IndexError:
			self.label_incorrect["text"] = "Моделювання завершено"
			self.label_incorrect.place(x=80, y=150)

	def centerWindow(self):
		w = 340
		h = 220
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - w)/2
		y = (sh - h)/2
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
	root = Tk()
	app = Invest_model(root)
	root.mainloop()

if __name__ == "__main__":
	main()