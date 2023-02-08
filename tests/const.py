
driverPathChrome = 'chromedriver'
baseUrl = 'https://b2c.passport.rt.ru'

registerFormKeysFirstName = ['A', 'Ab', '!&^%$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', 'Евгений']
registerFormKeysLastName = ['A', 'Ab', '!&^%$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', 'Иванов']
registerFormKeysAddress = ['A', '!&^%$', 'aбвгдеёжзиклмнопрстуфхчшщъыьэюя', '7788775544', 'lolo@gg.ru']
registerFormPassword = ['а', 'аааааааа', 'abcdefgh', 'abcdefgh1', 'Abcdefgh1', chr(10) + chr(11) + chr(7)
                        +chr(12) +'LlLff' + chr(1066)]

registerKeysDict = {
    'firstName': registerFormKeysFirstName,
    'lastName': registerFormKeysLastName
}

registerErrorsName = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
registerErrorsAddress = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
registerErrorsPasswordConfirm = 'Пароли не совпадают'
regErPass = 'Длина пароля должна быть не менее 8 символов'

tabButtonsId = ['t-btn-tab-phone', 't-btn-tab-mail', 't-btn-tab-login', 't-btn-tab-ls']
placeholderInputsValue = ['Мобильный телефон', 'Электронная почта', 'Логин', 'Лицевой счёт']
tabTitles = ['Телефон', 'Почта', 'Логин', 'Лицевой счёт']
sendedKeys = ['79111234567', 'lol@gg.ru', '0999777323', 'textSample']
placeValue = ['Мобильный телефон', 'Электронная почта', 'Лицевой счёт', 'Логин']
tabTitlesAuth = ['Телефон', 'Почта', 'Лицевой счёт', 'Логин']
activeTab = 'rt-tab--active'