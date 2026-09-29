name = input("What is your name?: ")
print("Nice to meet you " + name + "!")
print("Here is a car searching site of Porsche. This contains cars that showed in 2000~2026.")

while True:
    try:
        choosen_year = int(input(
            "\nPlease choose year: \n"
            "Choose 1 for 2000-2004 car \n"
            "Choose 2 for 2005-2010 car \n"
            "Choose 3 for 2011-2019 car \n"
            "Choose 4 for 2020-2026 car \n"
            "Please choose 5 to exit > "
        ))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choosen_year == 1:
        try:
            choosen_car = int(input(
                "Choose 1 for Porsche Turbo (996) \n"
                "Choose 2 for Porsche GT2 (996) \n"
                "Choose 3 for Porsche Cayenne (9PA) \n"
                "Choose 4 for Porsche Carrera GT (980) \n"
                "Choose 5 for Porsche (997 gen)\n > "
            ))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choosen_car == 1:
            print("The Porsche Turbo (996), produced between 2000 and 2004, marks a major historic milestone as the first-ever water-cooled Turbo. While the standard 996 models initially faced mixed reviews for their redesign, the Turbo variant secured its legendary status by offering supercar-level performance and exceptional daily drivability.")
        elif choosen_car == 2:
            print("The Porsche GT2 (996 generation), first introduced in 2001, was the most powerful road-going Porsche of its era. Dubbed the ultimate expression of the 996 lineup, it combined the raw power of a twin-turbocharged engine with a lightweight, rear-wheel-drive layout. Because it lacked electronic driver aids, it earned a reputation as a fierce, uncompromising driver's car.")
        elif choosen_car == 3:
            print("The Porsche Cayenne (9PA generation), first introduced in 2002, was a revolutionary turning point for the German automaker. At a time when Porsche faced severe financial instability, the brand took a massive gamble by entering the luxury SUV market. Co-developed with Volkswagen (sharing a platform with the Touareg), the Cayenne became a massive global sales success that effectively saved Porsche from financial ruin and pioneered the modern performance-SUV segment.")
        elif choosen_car == 4:
            print("The Porsche Carrera GT (Project Code 980), produced between 2003 and 2006, is widely regarded as one of the greatest analog hypercars ever created. With only 1,270 units manufactured globally, it stands as a pinnacle of pure, driver-focused performance. It was born directly out of a canceled Le Mans racing program, bringing genuine motorsport technology to the street without the filter of modern electronic traction and stability aids.")
        elif choosen_car == 5:
            print("The Porsche (997 generation), produced from 2004 to 2012, is widely celebrated as the sweet spot of the modern lineage. Following the controversial 996 generation, which introduced liquid cooling and the criticized fried-egg headlights, the 997 returned to the traditional round bug-eye headlights. It successfully married classic proportions with modern reliability and technology, making it one of the most sought-after generations on the used sports car market today.")
        else:
            print("Something went wrong... \nRestarting.....")

    elif choosen_year == 2:
        try:
            choosen_car = int(input(
                "Choose 1 for Porsche Cayman (987) \n"
                "Choose 2 for Porsche 911 GT3 / GT3 RS (997.1) \n"
                "Choose 3 for Porsche Panamera (970) \n > "
            ))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choosen_car == 1:
            print("The Porsche Cayman (987) is the first-generation Cayman (coupe), produced from 2005 to 2012 as a hardtop sibling to the 987 Boxster roadster. Featuring a mid-engine, rear-wheel-drive (MR) layout, it is celebrated for its near-perfect weight distribution, high torsional rigidity, and precise handling that rivaled the flagship Porsche sports car of its era. It remains highly sought after as a pure, analog sports car.")
        elif choosen_car == 2:
            print("The Porsche 911 GT3 and GT3 RS (997.1 generation), produced between 2006 and 2008, are widely celebrated as some of the most visceral, driver-focused sports cars ever built. They represent the pinnacle of Porsche's purist era, blending a motorsport-derived engine with a traditional 6-speed manual transmission and hydraulic steering.")
        elif choosen_car == 3:
            print("The Porsche Panamera (970) is the first-generation Panamera, manufactured and sold from 2009 to 2016. It made history as Porsche's first full-size, four-door (5-door hatchback) luxury sports sedan, blending the high-performance DNA of a sports car with the comfort and prestige of an executive saloon.")
        else:
            print("Something went wrong... \nRestarting.....")

    elif choosen_year == 3:
        try:
            choosen_car = int(input(
                "Choose 1 for Porsche 911 (991 Generation) \n"
                "Choose 2 for Porsche 918 Spyder \n"
                "Choose 3 for Porsche Macan (95B) \n"
                "Choose 4 for Porsche 718 Boxster & Cayman (982) \n"
                "Choose 5 for Porsche 911 (992 Generation)\n"
                "Choose 6 for Porsche Taycan (9J1) \n > "
            ))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choosen_car == 1:
            print("The Porsche 911 (991 model) is the seventh generation 911, produced from 2011 to 2019. It is a perfectly balanced 911 that combines the exhilarating driving experience of a traditional sports car with the modern comfort of everyday use.")
        elif choosen_car == 2:
            print("The Porsche 918 Spyder is a limited edition plug-in hybrid (PHEV) hypercar, with only 918 units produced worldwide from 2013 to 2015.")
        elif choosen_car == 3:
            print("The Porsche Macan (model: 95B) is an extremely popular performance compact crossover SUV in the Porsche lineup.")
        elif choosen_car == 4:
            print("The Porsche 718 Boxster & Cayman (model: 982) introduced mid-engined turbocharged 4-cylinder driving dynamics with surgical handling balance.")
        elif choosen_car == 5:
            print("The 992 model, the eighth generation of the Porsche 911 in service since 2018, features a wide body design across all models and an advanced digital cockpit.")
        elif choosen_car == 6:
            print("The Porsche Taycan (9J1), Porsche's first mass-produced all-electric sports car, is a 4-door sedan and 5-door CUV with an 800V electrical system and overwhelming acceleration performance.")
        else:
            print("Something went wrong... \nRestarting.....")

    elif choosen_year == 4:
        try:
            choosen_car = int(input(
                "Choose 1 for Porsche 911 Turbo S (992.1 Generation) \n"
                "Choose 2 for Porsche 911 GT3 (992.1 Generation) \n"
                "Choose 3 for Porsche 718 Cayman GT4 RS \n"
                "Choose 4 for Porsche 911 GTS & GT3 RS (992.1) \n"
                "Choose 5 for Porsche Panamera \n"
                "Choose 6 for Porsche Taycan \n > "
            ))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choosen_car == 1:
            print("The Porsche 911 Turbo S (992.1 model) is the 992 generation flagship supercar, equipped with a 3.7-liter horizontally opposed six-cylinder twin-turbo engine that produces a maximum output of 650 PS.")
        elif choosen_car == 2:
            print("The Porsche 911 GT3 (992.1 model) is a high-performance sports car equipped with a 4.0-liter naturally aspirated engine that produces 510 horsepower.")
        elif choosen_car == 3:
            print("The Porsche 718 Cayman GT4 RS is the top-of-the-line model in Porsche's mid-engine sports car series, incorporating racing technology without compromise.")
        elif choosen_car == 4:
            print("While the Carrera GTS is described as the ultimate practical all-around sports car, the GT3 RS is clearly defined as a genuine racing car with a license plate.")
        elif choosen_car == 5:
            print("The Porsche Panamera is a large, luxurious four-door sports sedan combining driving performance with executive comfort.")
        elif choosen_car == 6:
            print("The Porsche Taycan Turbo GT is the flagship model in Porsche's all-electric sports car lineup, boasting the highest performance ever.")
        else:
            print("Something went wrong... \nRestarting.....")

    elif choosen_year == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please pick a number from 1 to 5.")
