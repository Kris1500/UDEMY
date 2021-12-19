import def_kWh


def go():
    try:
        def_kWh.count_kwh()
        def_kWh.save_kwh()
    except:
        print('The report has not been saved.')


go()
