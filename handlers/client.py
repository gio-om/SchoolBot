from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client_back, kb_client_start, kb_client_subject, kb_client_new_request
from sheet_interface.sheet_functions import get_algebra_sheet, get_geometry_sheet, get_specmat_sheet
import string

async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Выберите предмет по которому хотите узнать оценки', reply_markup=kb_client_start)
	except:
		await message.reply('Общение с ботом через ЛС')

async def command_back(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Выберите предмет по которому хотите узнать оценки', reply_markup=kb_client_back)
	except:
		await message.reply('Общение с ботом через ЛС')


async def command_subject(message : types.Message):
	global subject, resp_sheet
	if message.text == '/Алгебра':
		subject = 'Алгебра'
		resp_sheet = get_algebra_sheet()['values'].copy()

	if message.text == '/Геометрия':
		subject = 'Геометрия'
		resp_sheet = get_geometry_sheet()['values'].copy()

	if message.text == '/Спецмат':
		subject = 'Спецмат'
		resp_sheet = get_specmat_sheet()['values'].copy()

	await bot.send_message(message.from_user.id, 'Напишите свою фамилию', reply_markup=kb_client_subject)
	#print(resp_sheet)

async def command_last_name(message : types.Message):
	global resp_sheet
	last_name = message.text
	person_found = False
	for i in range(len(resp_sheet)):
		if last_name in resp_sheet[i][0]:

			answer = create_answer(last_name, i)

			await bot.send_message(message.from_user.id, answer, reply_markup=kb_client_new_request)
			person_found = True

	if not person_found:
		await bot.send_message(message.from_user.id, 'Пользователь не найден', reply_markup=kb_client_new_request)


def create_answer(last_name, person_index):
	answer = ""
	second_semestr_point = 0
	point_found = False
	summ_of_notes = 0
	amount_of_notes = 0

	if(subject == 'Спецмат'):
		second_semestr_point = 6
		point_found = True
	else:
		for i in range(len(resp_sheet[0])):
			if '1 предв' in resp_sheet[0][i]:
				second_semestr_point = i + 1
				point_found = True

	if not point_found:
		answer = 'Границу семестров не удалось найти'
		return answer

	answer = 'Оценки за 2 триместр: '
	for i in range(second_semestr_point, len(resp_sheet[person_index])):
		if resp_sheet[person_index][i] != '':
			#resp_sheet[person_index][i]
			amount_of_notes = amount_of_notes + 1
			summ_of_notes  = summ_of_notes + float(resp_sheet[person_index][i].replace(',', '.'))

			answer = answer + ' ' + str(resp_sheet[person_index][i])

	if amount_of_notes == 0:
		answer = 'У вас нет оценок'
		return answer

	answer = answer + '\nСредний балл: ' + str(round(summ_of_notes / amount_of_notes, 2))

	return answer


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	dp.register_message_handler(command_back, commands=['назад'])
	dp.register_message_handler(command_subject, commands=['Алгебра', 'Геометрия', 'Спецмат'])
	dp.register_message_handler(command_last_name)


