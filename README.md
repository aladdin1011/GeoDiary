# GeoDiary: Интерактивный дневник путешествий (MVP)

GeoDiary — это платформа для ведения интерактивного дневника путешествий, которая позволяет пользователям фиксировать свои впечатления, добавлять мультимедиа, отслеживать маршруты на карте и делиться историями в формате карты

---

## **Основные функции**
1. **Регистрация и аутентификация пользователей**
   - Регистрация через email.
   - Вход с использованием email/пароля.
   - Авторизация через социальные сети (Google, Facebook и другие).

2. **Создание и управление записями**
   - Добавление текстов, фото, видео и геометок.
   - Редактирование и удаление записей.

3. **Маршруты и карты**
   - Автоматическое или ручное добавление маршрутов.
   - Визуализация точек путешествия на карте.

4. **Социальные взаимодействия**
   - Обмен дневниками через ссылки.
   - Лента активности с обновлениями друзей.

5. **Приватность и настройки**
   - Настройка видимости записей: публичные, по ссылке, личные.

6. **Геймификация**
   - Достижения и награды за активность.
   - Баллы за посещение новых мест.

7. **Премиум-функции**
   - Расширенное хранилище.
   - Уникальные шаблоны оформления.
   - Генерация видеоисторий.

---

## **Технологии**
- **Frontend**: React,Vie.
- **Backend**: FastAPI  
- **База данных**: SUPABASE 
- **Облачное хранилище**: AWS S3 (или аналог)  
- **API для карт**: Google Maps API

---

## **User Stories**

### **Категория 0: Авторизация и регистрация**
1. **Регистрация нового пользователя**  
   _Как новый пользователь, я хочу зарегистрироваться, чтобы получить доступ ко всем функциям платформы._  
   - **Контекст**: Заполнение email, имени, пароля; подтверждение через email.  
   - **Технически**: FastAPI обрабатывает запрос, хэширует пароль, сохраняет данные в PostgreSQL.
   - **Сервис**: Для подтверждение почты будет использовано SendGrid.

2. **Авторизация зарегистрированного пользователя**  
   _Как пользователь, я хочу войти в свой аккаунт, чтобы работать с дневниками._  
   - **Контекст**: Ввод email и пароля, получение доступа через JWT-токен.  
   - **Технически**: FastAPI проверяет данные и выдаёт токен.  

3. **Авторизация через социальные сети**  
   _Как пользователь, я хочу входить через Google/Facebook для удобства._  
   - **Контекст**: OAuth2 для авторизации, сохранение данных в PostgreSQL.  
   - **Технически**: Будет использовано Supabase.

4. **Сброс пароля**  
   _Как пользователь, я хочу сбросить пароль, чтобы восстановить доступ._  
   - **Контекст**: Получение ссылки для сброса пароля через email.  
   - **Технически**: Генерация временного токена, обновление пароля в базе.  

---

### **Категория 1: Управление дневником путешествий**
1. **Создание дневника**  
   _Как пользователь, я хочу создать новый дневник, чтобы структурировать свои путешествия._  
   - **Контекст**: Добавление названия, описания, обложки.  
   - **Технически**: FastAPI сохраняет данные дневника в PostgreSQL.  

2. **Добавление мультимедиа**  
   _Как пользователь, я хочу загружать фото и видео для визуализации записей._  
   - **Контекст**: Загрузка файлов, их просмотр перед сохранением.  
   - **Технически**: FFastAPI отправляет файлы в облачное хранилище (Supabase Storage Buckets)
3. **Организация записей**  
   _Как пользователь, я хочу упорядочивать записи по дням и местам._  
   - **Контекст**: Добавление даты и местоположения к записи.  
   - **Технически**: Записи связываются с дневником через внешние ключи.  

4. **Автоматическое отслеживание маршрутов (возможно)**  
   _Как пользователь, я хочу автоматически записывать маршруты с использованием GPS._  
   - **Контекст**: Включение GPS для реального времени.  
   - **Технически**: FastAPI принимает данные через WebSocket или POST-запросы.  

---

### **Категория 2: Социальные взаимодействия**
1. **Обмен дневниками**  
   _Как пользователь, я хочу делиться дневниками через уникальную ссылку._  
   - **Контекст**: Генерация ссылки с токеном доступа.  
   - **Технически**: FastAPI предоставляет временный токен доступа.  

2. **Лента активности**  
   _Как пользователь, я хочу видеть обновления друзей._  
   - **Контекст**: Лента показывает новые записи и дневники друзей.  
   - **Технически**: Пагинированный список через FastAPI.  

---

### **Категория 3: Интерактивные функции**
1. **Визуализация маршрутов**  
   _Как пользователь, я хочу видеть свои маршруты на карте._  
   - **Контекст**: Карта отображает точки с медиафайлами.  
   - **Технически**: Использование Google Maps API или Mapbox.  

---

### **Категория 4: AI-функции**
1. **Автоматическое описание мест**  
   _Как пользователь, я хочу получать описание достопримечательностей на фото._  
   - **Контекст**: Распознавание объектов на изображениях.  
   - **Технически**: Google Vision API для анализа.  

## 2. Рекомендации по маршрутам

### 1. Контентная фильтрация  
- Анализ характеристик мест (категории, описания).  
- Используются TF-IDF и косинусное сходство для определения схожести.  
- **Пример**: Рекомендация мест с описанием, похожим на "пляж с чистой водой".  

### 2. Фильтрация по категориям  
- Выбор мест из определенной категории (например, "Природа", "Культура").  
- **Пример**: Выбор категории "Природа" предлагает пляжи, горы и парки.  

### 3. Рекомендации по популярности  
- Сортировка мест по популярности (рейтинг, количество посещений).  
- **Пример**: Предложение самых популярных достопримечательностей в регионе.  

### 4. Комбинированный подход  
- Объединение методов: фильтрация по категориям и популярности.  
- **Пример**: Для категории "Культура" рекомендуются популярные музеи.  
---

## **Роли пользователей**

### **1. Пользователь (User)**
- **Описание**: Основной пользователь системы.  
- **Права**:
  - Создание, редактирование и удаление записей, маршрутов.
  - Добавление мультимедиа.
  - Настройка приватности записей.
  - Приглашение друзей.

### **2. Премиум-пользователь (Premium User)**
- **Описание**: Пользователь с доступом к платным функциям.  
- **Права**:
  - Расширенное хранилище.
  - Эксклюзивные шаблоны оформления.
  - Генерация видеоисторий.

### **3. Гость (Guest)**
- **Описание**: Незарегистрированный пользователь.  
- **Права**:
  - Просмотр общедоступных записей.
  - Нет доступа к редактированию.

### **4. Администратор (Admin)**
- **Описание**: Управляет системой и контентом.  
- **Права**:
  - Управление пользователями.
  - Модерация контента.

---

## **Сущности**

### **1. Путешествие (Trip)**
- **Данные**:  
  - ID, название, описание, даты, приватность, маршруты.
- **Операции**:
  - Создание, просмотр, обновление, удаление.

### **2. Запись (Entry)**
- **Данные**:  
  - ID, текст, медиафайлы, геометки, дата.
- **Операции**:
  - Создание, просмотр, обновление, удаление.

### **3. Пользователь (User)**
- **Данные**:  
  - ID, имя, email, подписка, достижения.
- **Операции**:
  - Регистрация, просмотр, обновление, удаление.
