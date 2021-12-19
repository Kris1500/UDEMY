try:
    name_of_device = input('Enter device name: ')
    watt_power = float(input('Watt power[w]: '))
    price_1kWh = float(input('1kwh price: '))
    dayly_time_of_use = float(input('How many hours a day Do You use it? '))
    weekly_time_of_use = int(input('How many days in the week? '))

    time_of_use_for_one_year = dayly_time_of_use * weekly_time_of_use * 52
    how_many_days = time_of_use_for_one_year / 24
    kWh = watt_power / 1000
    yearly_cost = price_1kWh * kWh * time_of_use_for_one_year
except:
    print('Calculations are not possible')


def count_kwh():
    print(f'You use {name_of_device} annually for {time_of_use_for_one_year} hours,'
          f' what gives {int(how_many_days)} days.')
    print(f'Annual energy consumption: {(kWh * time_of_use_for_one_year):.2f} kWh')
    print(f'What gives monthly cost: {(yearly_cost / 12):.2f}zł and annual cost: {yearly_cost:.2f}zł')
    print(f'Minute of device working cost: {(yearly_cost / 12 / 30 / 24):.5f}')


def save_kwh():
    file = open(r'C:\Users\Milka\PycharmProjects\UDEMY\Programy\kWh\kwH.txt', 'a')
    file.write(f'Device energy consumption report: {name_of_device}--watt power --{watt_power} W\n')
    file.write(f'You use {name_of_device} annually for {time_of_use_for_one_year:.2f} hours,'
               f' what gives {int(how_many_days)} days.\n')
    file.write(f'Annual energy consumption: {(kWh * time_of_use_for_one_year):.2f} kWh\n')
    file.write(f'What gives monthly cost: {(yearly_cost / 12):.2f}zł and annual cost: {yearly_cost:.2f}zł\n')
    file.write(f'Minute of device working cost: {(yearly_cost / 12 / 30 / 24):.3f}zł\n')
    file.write(f'____________________________\n')
    file.close()
    print('')
    print('The report was saved.')
