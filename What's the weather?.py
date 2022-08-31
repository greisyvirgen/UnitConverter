# Name: Greisy Virgen Larios
# Description:  This mini project is meant to take user input and allow for Spanish and
#               English inputs to tell the user what the weather is based on an input in
#               either Celsius or Fahrenheit and give the output in English or Spanish.

# Here I will take input to determine the language course of the program
class LanguageChoice:
    def __int__(self):
        celsius = None
        fahrenheit = None

    def prompt(self):
        print("Para Español presione 1. \nFor English, press 2.")
        language_choice = input()

        if language_choice == '1':
            self.spanish()
        # else:
        #     self.english()

    def spanish(self):
        print("Hola! Hoy le ayudare a saber el clima de hoy deacuerdo con "
              "su manera preferida, ya sea Celsius or Fahrenheit ")
        temp_preference = input("Porfavor elija de que manera le gustaria saber la temperatura. "
                    "Presione 1 para Celsius o Presione 2 para Fahrenheit: ")

        if temp_preference == '1':
            # This means they want to convert to Celsius
            temp_val = input("Porfavor escriba la temperatura que quiere convertir de "
                  "Celsius a Fahrenheit: ")

            temp_val.lower()
            for i in temp_val:
                if 'a' <= i <= 'z':
                    del i
            temp_val = int(temp_val)

            # Now we can do the math conversion from Fahrenheit to Celsius
            # C = 5/9(F-32)
            celsius = (temp_val - 32) * 5/9
            self.result(celsius, "Celsius")
            # return celsius

        elif temp_preference == '2':
            # This means they want to convert to Fahrenheit
            temp_val = input("Porfavor escriba la temperatura que quiere convertir de "
                             "Fahrenheit a Celsius: ")

            temp_val.lower()
            for i in temp_val:
                if 'a' <= i <= 'z':
                    del i

            temp_val = int(temp_val)

            # Now can do the math °F = (°C × 9/5) + 32
            fahrenheit = (temp_val * 9/5) + 32
            self.result(fahrenheit, "Fahrenheit")
            # return fahrenheit

        elif temp_preference != '1' or temp_preference != '2':
            print("La tecla presionada es incorrecta.")
            self.spanish()
    # def english(self):

    def result(self, temperature: float, type_temp: str):
        return print(f"Tu temperatura en {type_temp} es: {temperature} {type_temp}")


entry_prompt = LanguageChoice()
entry_prompt.prompt()
