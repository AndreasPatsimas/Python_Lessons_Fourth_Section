from translate import Translator
#before import python translate install pip3 install translate in cmd
#if error then install microsoft c++ build tools or problem with python version

translator = Translator(to_lang="Greek")

try:
    with open("C:/Directory1/test.txt", mode="r") as my_file:
        #text = my_file.write(":)")
        text = my_file.read()
        text = translator.translate(text)
        print(text)
except FileNotFoundError as err:
    raise err
