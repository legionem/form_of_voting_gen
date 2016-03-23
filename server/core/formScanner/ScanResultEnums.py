#РЕЗУЛЬТАТ РАСПОЗНАВАНИЯ
#------------------------------------
# Информация о токене занесена в базу,
# но само распознавание еще не начато.
BEFORE_SCAN = 'BEFORE_SCAN'

# Идет распознавание бланка.
IN_PROGRESS = 'IN_PROGRESS'

# Распознавание успешно завершено.
SUCCESS = 'SUCCESS'

# На бланке не был обнаружен большой QR код (некорректный бланк)
FAILED_BIG_QR_CODE = 'THERE_IS_NOTHING_ABOUT_BIG_QR_CODE'

# На бланке не обнарудены маленькие QR коды.
# Возникновение подобной ситуации возможно ТОЛЬКО после нахождения
# большого кода. Соответственно, можно сделать выводы о плохом качестве
# фото в области маленьких QR кодов.
FILED_SMALL_QR_CODE = 'THERE_IS_NOTHING_ABOUT_SMALL_QR_CODE'

# Что-то пошло не так в распознавании бланка (помимо вышеописанных ситуаций
# с QR кодами).
FAILED = 'FAILED'

# Запись о результет распознавания НЕДЕЙСТВИТЕЛЬНА.
# Она не присутствует в базе.
# Возможно это по причине не правильно указанного маркера.
UNAVAILABLE_SCAN_RESULT_RECORD = 'UNAVAILABLE_SCAN_RESULT_RECORD'
#------------------------------------

#Имя файла, в который будет записан результат распознавания по маркеру
RESULTS_FILE_NAME = 'TokenData'

#
SCAN_RESULT_IS_NOT_AVAILABLE = 0
SCAN_RESULT_IS_AVAILABLE = 1
