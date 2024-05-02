#pip install python_imagesearch
#pip install pyautogui
#pip install keyboard

from python_imagesearch.imagesearch import imagesearch_numLoop
import pyautogui
from time import strftime, localtime, sleep
import keyboard

print("Начало цикла, для запуска использовать ALT+Z")


def del_user():
    print("push start")
    #self.i += 1
    #self.label_2.setText("Сколько раз запустили: " + str(self.i))
    def locate_and_click(image_path):
        pos = imagesearch_numLoop(image_path, 0.2, 7)
        if pos[0] != -1:
            print("position: ", pos[0], pos[1])
            #logging.info("position: %s, %s", pos[0], pos[1])
            pyautogui.click(pos[0] + 5, pos[1] + 5)
            sleep(0.5)
            return True
        else:
            print(" Изображение не найдено")
            #logging.warning("Изображение не найдено")
            sleep(0.5)
            return False
    # while True:
    sleep(0.5)
    #logging.info("--------Начало цикла--------")
    # sleep(1)
    if locate_and_click("pict/is1.png"):
        # print("Найдена картинка Изменить свойства, кликаем на него")
        #logging.info("Найдена картинка Изменить свойства, кликаем на него")
        if locate_and_click("pict/zpp1.png"):
            # print("Нашли запрет приема платежей без галочки, кликаем по нему")
            #logging.info("Нашли запрет приема платежей без галочки, кликаем по нему")
            pyautogui.scroll(-400)
            sleep(0.5)
            # print("Скролим вниз страницы")
            #logging.info("Скролим вниз страницы")
            if locate_and_click("pict/save.png"):
                # print("Нашли сохранить и кликнули по ней")
                #logging.info("Нашли сохранить и кликнули по ней")
                if locate_and_click("pict/is1.png"):
                    # print("Нашли свойства 2")
                    #logging.info("Нашли свойства 2")
                    if locate_and_click("pict/ik1.png"):
                        # print("Нашли изменение класса и кликнули по нему")
                        #logging.info("Нашли изменение класса и кликнули по нему")
                        if locate_and_click("pict/del.png"):
                            # print("Нашли кнопку удаление и кликаем по ней")
                            #logging.info("Нашли кнопку удаление и кликаем по ней")
                            if locate_and_click("pict/oi1.png"):
                                # print("Нашли основную информацию, кликаем на нее")
                                #logging.info("Нашли основную информацию, кликаем на нее")
                                #logging.info("Скриншот удаленной учетки")
                                sleep(0.5)
                                pyautogui.screenshot(
                                    'screen/' + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                                #self.j += 1
                                #self.label_3.setText("Успешных удалений: " + str(self.j))
                                #self.i1 += 1
                                #self.label_4.setText("Удалений за сеанс: " + str(self.i1))
                                #self.toast = ToastNotifier()
                                #self.toast.show_toast("Удаление абонента", "Удаление абонента прошло успешно",
                                #                      duration=3, icon_path="113.ico")
                                # self.i += 1
                                # self.label_2.setText("Удалили абонентов: " + str(self.i) + " раз")
                            else:
                                print("Не найдена основная информация")
                                #logging.error("Не найдена основная информация")
                                pyautogui.screenshot(
                                    'screen/' + "Ошибка 6 _ " + strftime('%Y-%m-%d_%H.%M.%S',
                                                                         localtime()) + '.jpg')
                        else:
                            print("Не найдена кнопка удаления")
                            #logging.error("Не найдена кнопка удаления")
                            pyautogui.screenshot(
                                'screen/' + "Ошибка 6 _ " + strftime('%Y-%m-%d_%H.%M.%S',
                                                                     localtime()) + '.jpg')
                    else:
                        print("Не найдено изменение класса")
                        #logging.error("Не найдено изменение класса")
                        pyautogui.screenshot(
                            'screen/' + "Ошибка 5 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                else:
                    print("Не нашли свойства 2")
                    #logging.error("Не нашли свойства 2")
                    pyautogui.screenshot(
                        'screen/' + "Ошибка 4 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
            else:
                print("Не нашли кнопку сохранить")
                #logging.error("Не нашли кнопку сохранить")
                pyautogui.screenshot(
                    'screen/' + "Ошибка 3 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
        else:
            print("не найдена картинка пустой запрет платежей")
            #logging.error("не найдена картинка пустой запрет платежей")
            pyautogui.screenshot(
                'screen/' + "Ошибка 2 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
    else:
        print("не найдена картинка изменить свойства")
        #logging.error("не найдена картинка изменить свойства")
        pyautogui.screenshot(
            'screen/' + "Ошибка 1 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')

keyboard.add_hotkey('alt+z', del_user)