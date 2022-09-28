# Name: Greisy Virgen Larios
# Description:  This mini project is meant to take user input and allow for Spanish and
#               English inputs to tell the user what the weather is based on an input in
#               either Celsius or Fahrenheit and give the output in English or Spanish.

# Here I will take input to determine the language course of the program
class LanguageChoice:
    def __init__(self):
        print("Para Español presione 1. \nFor English, press 2.")
        language_choice = input()
        self.prompt(language_choice)
        # celsius = None
        # fahrenheit = None

    def prompt(self, language):
        # print("Para Español presione 1. \nFor English, press 2.")
        # language_choice = input()

        if language == '1':
            self.spanish()
        elif language == '2':
            self.english()
        else:
            self.__init__()

    def spanish(self):
        print("Hola! Hoy le ayudare a saber el clima de hoy deacuerdo con "
              "su manera preferida, ya sea Celsius o Fahrenheit ")
        temp_preference = input("Porfavor elija de que manera le gustaria saber la temperatura. "
                    "Presione 1 para Celsius o Presione 2 para Fahrenheit: ")

        if temp_preference == '1':
            # This means they want to convert to Celsius
            temp_val = input("Porfavor escriba la temperatura en Fahrenheit: ")

            temp_val.lower()

            # This checks if they typed in any
            # words, so that they're not accounted for
            for i in temp_val:
                if 'a' <= i <= 'z':
                    del i

            # Now we can do the math conversion from Fahrenheit to Celsius
            # C = 5/9(F-32)
            celsius = (int(temp_val) - 32) * 5/9
            self.result(celsius, "Celsius", 'spanish')

        elif temp_preference == '2':
            # This means they want to convert to Fahrenheit
            temp_val = input("Porfavor escriba la temperatura en Celsius: ")

            temp_val.lower()

            for i in temp_val:
                if 'a' <= i <= 'z':
                    del i

            # Now can do the math °F = (°C × 9/5) + 32
            fahrenheit = (int(temp_val) * 9/5) + 32
            self.result(fahrenheit, "Fahrenheit", 'spanish')

        elif temp_preference != '1' or temp_preference != '2':
            print("La tecla presionada es incorrecta.")
            self.spanish()

    def english(self):

        print("Hi! I'll help you know the weather based on your preference, either Celsius or Fahrenheit ")
        temp_preference = input("Please choose your preferred conversion. Press 1 to convert to Celsius or "
                                "Press 2 to convert to Fahrenheit: ")

        if temp_preference == '1':
            # This means they want to convert to Celsius

            temp_val = input("Please write your temperature in Fahrenheit: ")

            temp_val.lower()
            for i in temp_val:
                if 'a' <= i <= 'z':
                    del i

            # Now we can do the math conversion from Fahrenheit to Celsius
            # C = 5/9(F-32)
            celsius = (int(temp_val) - 32) * 5 / 9
            self.result(celsius, "Celsius", 'english')

        elif temp_preference == '2':
            # This means they want to convert to Fahrenheit
            temp_val = input("Please write tour temperature in Celsius: ")

            temp_val.lower()
            for i in temp_val:
                if 'a' <= i <= 'z':
                    del i

            # Now can do the math °F = (°C × 9/5) + 32
            fahrenheit = (int(temp_val) * 9 / 5) + 32
            self.result(fahrenheit, "Fahrenheit", 'english')
            # return fahrenheit

        elif temp_preference != '1' or temp_preference != '2':
            print("Wrong key.")
            self.english()

    def result(self, temperature: float, type_temp: str, language: str):
        if language == "spanish":
            print(f"Tu temperatura en {type_temp} es: {temperature} {type_temp}")

            continue_temp = input("Te gustaria segir convirtiendo temperaturas correctamente? "
                                  "Presiona 1 si quieres continuar, o Presiona 2 para terminar: ")
            if continue_temp == '1':
                return self.__init__()
            else:
                return self.end_conversion("spanish")

        elif language == "english":
            print(f"Your temperature in {type_temp} is: {temperature} {type_temp}")

            continue_temp = input("Would you like to continue playing? Press 1 for Yes or Press 2 for No: ")
            if continue_temp == '1':
                return self.__init__()
            else:
                return self.end_conversion("english")

    def end_conversion(self, language: str):
        if language == 'english':
            print("Thanks for doing some conversions with me! Bye bye :)")
        elif language == "spanish":
            print("Gracias por averiguar la temperatura conmigo! Adios :)")
        return


print(LanguageChoice())
