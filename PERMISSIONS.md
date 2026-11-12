# Разрешения в Django REST Framework

DRF проверяет `permission_classes` перед вызовом обработчика APIView. Собственный
пермишен наследуется от `BasePermission`; метод `has_permission(request, view)`
возвращает `True` для разрешённого запроса и `False` для отказа.

В этом проекте `IsAdminOnly` разрешает запросы только аутентифицированным
пользователям с ролью `ADMIN`, а `IsUserOnly` — только с ролью `USER`.
Проверяется именно поле `role`, а не `is_staff` или `is_superuser`. В случае
отказа API возвращает `403 Forbidden`. Для ограничения доступа к конкретному
объекту можно дополнительно реализовать `has_object_permission`.

Материалы для чтения:

- [DRF: Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [DRF: APIView](https://www.django-rest-framework.org/api-guide/views/)
- [Django: Customizing authentication](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/)

## Запуск и проверка

Из корневой папки проекта:

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test users
```

Для суперпользователя автоматически устанавливается роль `ADMIN`. В Postman
проверьте `GET /admin-panel/` и `GET /user-dashboard/`, выбрав **Authorization
→ Basic Auth** и учетные данные пользователей с разными ролями. Успешный доступ
вернёт `200 OK`, неподходящая роль или анонимный запрос — `403 Forbidden`.
