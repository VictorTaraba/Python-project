#ІЗ ДАНИХ У ФОРМАТІ CSV СТВОРЮЄ СПИСКИ З ЦІНАМИ АКЦІЙ, ЯКІ МОЖНА ВИКОРИСТОВУВАТИ ДЛЯ БЕЗПОСЕРЕДНЬОГО МОДЕЛЮВАННЯ

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from dateutil.relativedelta import relativedelta

#Назви файлів з данимим - потрібні для отримання даних задля побудови графіків і моделювання роботи інвестиційного фонду
adresses_list_GOOG = ['GOOG.csv']
adresses_list_TSLA = ['TSLA.csv']
adresses_list_IBM = ['IBM.csv']
adresses_list_GM = ['GM.csv']
adresses_list_AMZN = ['AMZN.csv']

adresses_list_AMZN_day = ['AMZN_day.csv']
adresses_list_GOOG_day = ['GOOG_day.csv']
adresses_list_TSLA_day = ['TSLA_day.csv']
adresses_list_IBM_day = ['IBM_day.csv']
adresses_list_GM_day = ['GM_day.csv']
adresses_list_AMZN_day = ['AMZN_day.csv']

#тут зберігатимуться дані в обробленому вигляді; саме ці списки будуть використовуватися в графічному інтерфейсі
GOOG_prices = []
TSLA_prices = []
GM_prices = []
IBM_prices = []
AMZN_prices = []

#отримуємо інформацію із csv файлу, створюємо список, кожен елемент якого - таблиця для однієї акції 
class get_data_1:
	def __init__(self, adresses):
		self.adress = adresses[0]

	def get_information_1(self):
		stocks_list = []
		stock = pd.DataFrame.from_csv(self.adress, index_col=None)
		stocks_list.append(stock)
		return stocks_list

#залишаємо в таблиці лише колнку із цінами закриття і номери рядків
class get_data_2(get_data_1):
	def __init__(self, adresses):
		super().__init__(adresses)

	def get_information_2(self):
		self.stocks_list = self.get_information_1()
		close_prices_list = []

		for i in range(len(self.stocks_list)):
			stocks = self.stocks_list[i]
			close = stocks['Close']
			close_prices_list.append(close)
		return close_prices_list

#трансформуємо таблицю з однією колонкою в список, елементи якого дорівнюють значенням рядків таблиці
class get_data_3(get_data_2):
	def __init__(self, adresses):
		super().__init__(adresses)

	def get_information_3(self):
		self.close_prices_list = self.get_information_2()
	
		list_of_stock_prices = []
		for element in self.close_prices_list[0]:
			list_of_stock_prices.append(element)
		return list_of_stock_prices

#створює список, елементи якого - дати, крок між сусідніми датами - один місяць; потрібен, аби намалювати графік
class Time_list_month:
	def __init__(self, list_of_stock_prices):
		self.list_of_stock_prices = list_of_stock_prices

	def time_return(self):
		some_day = dt.datetime(year=2010, month=10, day=1)
		time = [] #зберігатиме число місяців, які пройшли з початку торгівлі
		for i in range(len(self.list_of_stock_prices)):
			some_day += relativedelta(months=1)
			time.append(some_day)
		return time 

#створює список, елементи якого - дати, крок між сусідніми датами - 1.5 днів - аби врахувати вихідні та свята, 
#коли торгів немає; потрібен, аби намалювати графік
class Time_list_day:
	def __init__(self, list_of_stock_prices):
		self.list_of_stock_prices = list_of_stock_prices

	def time_return(self):
		some_day = dt.datetime(year=2010, month=11, day=15)
		time = [] #зберігатиме число місяців, які пройшли з початку торгівлі
		for i in range(len(self.list_of_stock_prices)):
			some_day += dt.timedelta(days=1.5)
			time.append(some_day)
		return time 

#малює графік за списком цін і списком дат; зберігає його як файл визначеного розміру у форматі jpg
class draw_graph:
	def __init__(self, list_of_stock_prices, time, name):
		self.list_of_stock_prices = list_of_stock_prices
		self.time = time
		self.name = name

	def draw(self):
		plt.plot(self.time, self.list_of_stock_prices)
		plt.xticks(rotation=90)
		plt.ylabel('\nЦіна однієї акції')
		plt.xlabel('\nДата')
		plt.savefig(self.name, dpi=200*0.38)
		plt.close()

#функція округляє елементи списку (ціни акцій) до 2 знаків після коми 
#потрібно для коректного відображення в графічному інтерфейсі
def round_list(data, my_list):
	for element in data:
		copy = round(element, 2)
		my_list.append(copy)

#отримує на список списків (із даними), список із датами(для осі абсцис) та список імен для майбутніх зображень
#і зберігає графіки з цими іменами
def save_few_graphs(stock_graph_list, time, name_list):
	for i in range(len(stock_graph_list)):
		c = draw_graph(stock_graph_list[i], time, name_list[i])
		c.draw()

#отримуємо оброблені дані для акцій кожної із 5 компаній, які використовуються в моделюванні (ціни по місяцях)
a = get_data_3(adresses_list_GOOG)
data_1 = a.get_information_3()
a = get_data_3(adresses_list_TSLA)
data_2 = a.get_information_3()
a = get_data_3(adresses_list_GM)
data_3 = a.get_information_3()
a = get_data_3(adresses_list_IBM)
data_4 = a.get_information_3()
a = get_data_3(adresses_list_AMZN)
data_5 = a.get_information_3()

#створюємо список з датами (в днях)
time = Time_list_month(data_5)
time = time.time_return()

stock_graph_list = [data_1, data_2, data_3, data_4, data_5]
name_list = ["GOOG.jpg", "TSLA.jpg", "GM.jpg", "IBM.jpg", "AMZN.jpg"]#назви для графіків

#зберігаємо графіки у тій же папці, що і код програми 
save_few_graphs(stock_graph_list, time, name_list)

#отримуємо оброблені дані для акцій кожної із 5 компаній, які використовуються в моделюванні
#тепер працюємо з цінами не за один місяць, а за один день - потрібно для побудови графіків і виведення статистичних даних
a = get_data_3(adresses_list_GOOG_day)
data_1_day = a.get_information_3()
a = get_data_3(adresses_list_TSLA_day)
data_2_day = a.get_information_3()
a = get_data_3(adresses_list_GM_day)
data_3_day = a.get_information_3()
a = get_data_3(adresses_list_IBM_day)
data_4_day = a.get_information_3()
a = get_data_3(adresses_list_AMZN_day)
data_5_day = a.get_information_3()

#створюємо список з датами (в днях)
time = Time_list_day(data_1_day)
time = time.time_return()

stock_graph_list = [data_1_day, data_2_day, data_3_day, data_4_day, data_5_day]
name_list = ["GOOG_day.jpg", "TSLA_day.jpg", "GM_day.jpg", "IBM_day.jpg", "AMZN_day.jpg"]#назви для графіків

#зберігаємо графіки у тій же папці, що і код програми 
save_few_graphs(stock_graph_list, time, name_list)

#округляємо елементи списків до другого знаку після коми
round_list(data_1, GOOG_prices)
round_list(data_2, TSLA_prices)
round_list(data_3, GM_prices)
round_list(data_4, IBM_prices)
round_list(data_5, AMZN_prices)