#pip install python_imagesearch
#pip install pyautogui
#pip install keyboard


import logging
import time
from time import strftime, localtime, sleep
import keyboard
import pyautogui
from python_imagesearch.imagesearch import imagesearch_numLoop
#from win10toast import ToastNotifier

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#toast = ToastNotifier()

#toast.show_toast("Удаление абонента","Программа запущена, висит в памяти и нигде не отсвечивает. Для запуска используйте клавиши ALT+Z",duration=5,icon_path="113.ico")

print("Начало цикла, для запуска использовать ALT+Z")

def del_user(i):
    def locate_and_click(image_path):
        pos = imagesearch_numLoop(image_path, 0.2, 7)
        if pos[0] != -1:
            #print("position: ", pos[0], pos[1])
            logging.info("position: %s, %s", pos[0], pos[1])
            pyautogui.click(pos[0] + 5, pos[1] + 5)
            sleep(0.5)
            return True
        else:
            #print(" Изображение не найдено")
            logging.warning("Изображение не найдено")
            sleep(0.5)
            return False

    # while True:
    #print("Начало цикла, для запуска использовать ALT+Z")
    sleep(0.5)
    logging.info("--------Начало цикла--------")
    if locate_and_click("pict/is1.png"):
        logging.info("Найдена картинка Изменить свойства, кликаем на него")
        if locate_and_click("pict/zpp1.png"):
            logging.info("Нашли запрет приема платежей без галочки, кликаем по нему")
            pyautogui.scroll(-400)
            sleep(0.5)
            logging.info("Скролим вниз страницы")
            if locate_and_click("pict/save.png"):
                logging.info("Нашли сохранить и кликнули по ней")
                if locate_and_click("pict/is1.png"):
                    logging.info("Нашли свойства 2")
                    if locate_and_click("pict/ik1.png"):
                        logging.info("Нашли изменение класса и кликнули по нему")
                        if locate_and_click("pict/del.png"):
                            logging.info("Нашли кнопку удаление и кликаем по ней")
                            if locate_and_click("pict/oi1.png"):
                                logging.info("Нашли основную информацию, кликаем на нее")
                                logging.info("Скриншот удаленной учетки")
                                sleep(0.5)
                                pyautogui.screenshot('screen/' + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                                print(f'Удалено абонентов за сегодня: {i}')
                                # self.toast = ToastNotifier()
                                # self.toast.show_toast("Удаление абонента", "Удаление абонента прошло успешно",
                                #                      duration=3, icon_path="113.ico")
                            else:
                                logging.error("Не найдена основная информация")
                                pyautogui.screenshot(
                                   'screen/' + "Ошибка 6 _ " + strftime('%Y-%m-%d_%H.%M.%S',
                                                                        localtime()) + '.jpg')
                        else:
                            logging.error("Не найдена кнопка удаления")
                            pyautogui.screenshot(
                               'screen/' + "Ошибка 6 _ " + strftime('%Y-%m-%d_%H.%M.%S',
                                                                    localtime()) + '.jpg')
                    else:
                        logging.error("Не найдено изменение класса")
                        pyautogui.screenshot(
                           'screen/' + "Ошибка 5 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                else:
                    logging.error("Не нашли свойства 2")
                    pyautogui.screenshot(
                       'screen/' + "Ошибка 4 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
            else:
                logging.error("Не нашли кнопку сохранить")
                pyautogui.screenshot(
                   'screen/' + "Ошибка 3 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
        else:
            logging.error("не найдена картинка пустой запрет платежей")
            pyautogui.screenshot(
               'screen/' + "Ошибка 2 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
    else:
        logging.error("не найдена картинка изменить свойства")
        #pyautogui.screenshot(
        #    'screen/' + "Ошибка 1 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
        pyautogui.screenshot(f'screen/Ошибка 1 _ {strftime('%Y-%m-%d_%H.%M.%S', localtime())}.jpg')

def main():
    i = 0
    while True:
        keyboard.wait('Alt + Z')
        st = time.time()
        i += 1
        del_user(i)
        st = time.time() - st
        logging.info(f"Затраченное на удаление время: {st} секунд")
        print(f'Затраченное на итерацию время: {st} секунд.')

if __name__ == "__main__":
    main()