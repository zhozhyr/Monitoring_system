from django.db import models

"""
Пользователи и роли
"""


class Info(models.Model):
    """
    Модель для хранения информации о пользователях.
    """
    YES_NO_CHOICES = [
        (0, "Нет"),
        (1, "Да"),
    ]

    group_account = models.CharField(max_length=255, null=True, blank=True, verbose_name="Групповая учетная запись")
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="ФИО")
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name="Должность")
    specialist_expl_unit = models.CharField(choices=YES_NO_CHOICES, max_length=255, null=True, blank=True,
                                            verbose_name="Специалист эксплуатационного подразделения")
    head_expl_unit = models.CharField(choices=YES_NO_CHOICES, max_length=255, null=True, blank=True,
                                      verbose_name="Руководитель эксплуатационного подразделения")
    specialist_itc_service = models.CharField(choices=YES_NO_CHOICES, max_length=255, null=True, blank=True,
                                              verbose_name="Специалист службы ИТЦ")
    head_itc_service = models.CharField(choices=YES_NO_CHOICES, max_length=255, null=True, blank=True,
                                        verbose_name="Руководитель службы ИТЦ")
    production_diagnostic_department = models.CharField(choices=YES_NO_CHOICES, max_length=255, null=True, blank=True,
                                                        verbose_name="Производственно-диагностический отдел")
    head_corporate_supervision = models.CharField(choices=YES_NO_CHOICES, max_length=255, null=True, blank=True,
                                                  verbose_name="Руководитель корпоративного надзора")
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name="Email")
    access_rights_arm = models.BooleanField(default=False, max_length=255, null=True, blank=True,
                                            verbose_name="Наличие прав доступа к АРМ")
    active_account = models.BooleanField(default=True, verbose_name="Активный аккаунт")

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"

    def __str__(self):
        return self.full_name if self.full_name else "UserInfo object"


class Administrator(models.Model):
    """
    Модель для хранения информации об админимстраторах (?).
    """
    auto_card_number = models.IntegerField(null=True, blank=True, verbose_name="Номер карты")  # это что

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"

    def __str__(self):
        return f"Администратор {self.auto_card_number}" if self.auto_card_number else "Администратор (без номера)"


class UserRole(models.Model):
    """
    Модель, представляющая роль пользователя в системе.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Название роли")

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"

    def __str__(self):
        return self.name if self.name else f"Роль {self.id}"


class UserSetting(models.Model):
    """
    Модель для хранения конфигураций пользователя.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    network_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Сетевое имя")
    auto_card_number = models.IntegerField(null=True, blank=True, verbose_name="Номер автокарты")
    ini_file = models.BinaryField(null=True, blank=True, verbose_name="INI-файл")
    ini_file_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Название INI-файла")

    class Meta:
        verbose_name = "Настройка пользователя"
        verbose_name_plural = "Настройки пользователей"

    def __str__(self):
        return self.network_name or str(self.auto_card_number) or f"Настройки {self.id}"


class UsersList(models.Model):
    """
    Модель для хранения информации о списках пользователях.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    auto_card = models.IntegerField(null=True, blank=True, verbose_name="Номер карты")
    id_role = models.IntegerField(null=True, blank=True, verbose_name="ID роли")

    class Meta:
        verbose_name = "Список пользователей"
        verbose_name_plural = "Списки пользователей"

    def __str__(self):
        return str(self.auto_card) if self.auto_card else "UsersList object"


"""
Организационная структура
"""


class StructuralUnitTree(models.Model):
    """
    Модель, представляющая Дерево структурного подразделения.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    parent_unit = models.IntegerField(null=True, blank=True, verbose_name="Родительское подразделение")
    unit_code = models.IntegerField(null=True, blank=True, verbose_name="Код подразделения")
    level = models.SmallIntegerField(null=True, blank=True, verbose_name="Уровень в иерархии")
    firm_id = models.IntegerField(null=True, blank=True, verbose_name="ID организации")
    reporting_branch_number = models.IntegerField(null=True, blank=True, verbose_name="Номер отчетного филиала")
    reporting_branch_id = models.IntegerField(null=True, blank=True, verbose_name="ID отчетного филиала")

    class Meta:
        verbose_name = "Дерево структурного подразделения"
        verbose_name_plural = "Деревья структурных подразделений"

    def __str__(self):
        return f"Tree {self.id}"


class Position(models.Model):
    """
    Модель, представляющая должность сотрудника.
    Используется для хранения информации о должностях.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название должности")

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.title if self.title else f"Должность {self.id}"


class Appointment(models.Model):
    """
    Модель для хранения информации о назначениях (кого-то).
    """
    id = models.AutoField(primary_key=True, verbose_name="ID/код назначения")
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="Название назначения")
    accusative_case_title = models.CharField(max_length=250, null=True, blank=True,
                                             verbose_name="Название в винительном падеже")

    class Meta:
        verbose_name = "Назначение"
        verbose_name_plural = "Назначения"

    def __str__(self):
        return self.title if self.title else "Назначение (без названия)"


"""
Журналы
"""


class EPBJournal(models.Model):
    """
    Модель для хранения записей в журнале эксплуатационной безопасности (ЭПБ).
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    epb_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата ЭПБ")
    tu_id = models.IntegerField(null=True, blank=True, verbose_name="ID технического устройства")
    epb_conclusion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вывод ЭПБ")

    class Meta:
        verbose_name = "Журнал ЭПБ"
        verbose_name_plural = "Журналы ЭПБ"

    def __str__(self):
        return f"{self.epb_date} - {self.epb_conclusion}" if self.epb_conclusion else f"Журнал ЭПБ {self.id}"


class InspectionJournal(models.Model):
    """
    Модель для хранения записей о проверках.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    inspection_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата проверки")
    technical_unit_id = models.IntegerField(null=True, blank=True, verbose_name="ID технического устройства")

    class Meta:
        verbose_name = "Журнал проверок"
        verbose_name_plural = "Журналы проверок"

    def __str__(self):
        return str(self.inspection_date) if self.inspection_date else f"Журнал проверок {self.id}"


"""
Технические устройства (ТУ) и связанные данные
"""


class TU(models.Model):
    """
    Модель технического устройства с основными характеристиками, идентификаторами,
    параметрами эксплуатации и документами.
    """
    YES_NO_CHOICES = [
        (0, "Нет"),
        (1, "Да"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID")

    # Основные сведения
    registration_number = models.CharField(max_length=200, null=True, blank=True,
                                           verbose_name="Регистрационный номер оборудования")
    serial_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Серийный номер")
    state_registration_number = models.CharField(max_length=200, null=True, blank=True,
                                                 verbose_name="Гос. регистрационный номер")
    factory_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Заводской номер")
    brand = models.CharField(max_length=500, null=True, blank=True, verbose_name="Марка")
    technical_characteristics = models.CharField(max_length=200, null=True, blank=True,
                                                 verbose_name="Краткие тех. характеристики")

    # Идентификация и схема
    gtt_registration_number = models.CharField(max_length=200, null=True, blank=True,
                                               verbose_name="Регистрационный номер ГТТ")
    scheme_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер по тех. схеме")

    # Годы эксплуатации
    manufacture_year = models.CharField(max_length=200, null=True, blank=True, verbose_name="Год изготовления")
    service_life_years = models.SmallIntegerField(null=True, blank=True,
                                                  verbose_name="Нормативный срок эксплуатации (лет)")
    commissioning_year = models.SmallIntegerField(null=True, blank=True, verbose_name="Год ввода в эксплуатацию")
    decommissioning_year = models.SmallIntegerField(null=True, blank=True, verbose_name="Год окончания эксплуатации")

    # Техническое состояние
    wear_percentage = models.FloatField(null=True, blank=True, verbose_name="Процент износа")
    last_epb_date = models.DateField(null=True, blank=True, verbose_name="Дата последнего ЭПБ")
    next_epb_date = models.DateField(null=True, blank=True, verbose_name="Дата следующего ЭПБ")
    last_inspection_date = models.DateField(null=True, blank=True, verbose_name="Дата очередной проверки")
    next_inspection_date = models.DateField(null=True, blank=True, verbose_name="Дата следующей проверки")
    permitted_service_life = models.SmallIntegerField(null=True, blank=True,
                                                      verbose_name="Разрешённый срок эксплуатации")

    # Предохранительные устройства
    has_safety_device = models.IntegerField(choices=YES_NO_CHOICES, null=True, blank=True,
                                            verbose_name="Наличие предохранительного устройства")
    safety_device_type = models.CharField(max_length=200, null=True, blank=True,
                                          verbose_name="Тип предохранительного устройства")

    # Параметры оборудования
    volume_m3 = models.FloatField(null=True, blank=True, verbose_name="Объём (м³)")
    object_pressure_mpa = models.FloatField(null=True, blank=True, verbose_name="Объектное давление (МПа)")
    dy_mm = models.FloatField(null=True, blank=True, verbose_name="Диаметр (мм)")
    type = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тип")
    subtype = models.CharField(max_length=200, null=True, blank=True, verbose_name="Подтип")
    lifting_capacity_t = models.FloatField(null=True, blank=True, verbose_name="Грузоподъёмность (т)")
    volume_t = models.FloatField(null=True, blank=True, verbose_name="Объём (т)")
    equipment_pressure_mpa = models.FloatField(null=True, blank=True, verbose_name="Давление оборудования (МПа)")
    modernization_year = models.SmallIntegerField(null=True, blank=True, verbose_name="Год модернизации")
    completed_measures = models.CharField(max_length=200, null=True, blank=True, verbose_name="Проведённые мероприятия")

    # Документы и разрешения
    rtn_permission_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер разрешения РТН")
    epb_conclusion_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер заключения ЭПБ")

    passport_present = models.IntegerField(choices=YES_NO_CHOICES, null=True, blank=True,
                                           verbose_name="Наличие паспорта")

    opo_info = models.CharField(max_length=200, null=True, blank=True, verbose_name="Сведения об ОПО")

    rtn_info = models.CharField(choices=YES_NO_CHOICES, null=True, blank=True, verbose_name="Информация РТН")

    compliance_certificate_present = models.IntegerField(choices=YES_NO_CHOICES, null=True, blank=True,
                                                         verbose_name="Наличие сертификата соответствия")
    rtn_certificate_present = models.IntegerField(choices=YES_NO_CHOICES, null=True, blank=True,
                                                  verbose_name="Наличие сертификата РТН")

    # Изготовитель
    manufacturer_id = models.BigIntegerField(null=True, blank=True, verbose_name="ID завода-изготовителя")
    manufacturer_country = models.CharField(max_length=200, null=True, blank=True, verbose_name="Страна-производитель")
    manufacturer_name = models.CharField(max_length=500, null=True, blank=True, verbose_name="Завод-изготовитель")

    # Прочее
    epb_conclusion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вывод ЭПБ")
    total_cycles = models.IntegerField(null=True, blank=True, verbose_name="Количество циклов")
    actual_cycles = models.IntegerField(null=True, blank=True, verbose_name="Фактическое количество циклов")
    replacement_id = models.IntegerField(null=True, blank=True, verbose_name="ID замены")
    replacement_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Номер замены")
    note1 = models.TextField(null=True, blank=True, verbose_name="Примечание 1")
    note2 = models.TextField(null=True, blank=True, verbose_name="Примечание 2")
    note3 = models.TextField(null=True, blank=True, verbose_name="Примечание 3")

    # Идентификаторы
    opo_id = models.BigIntegerField(verbose_name="ID ОПО")
    hazard_class_id = models.BigIntegerField(null=True, blank=True, verbose_name="ID класса опасности")
    device_type_id = models.BigIntegerField(null=True, blank=True, verbose_name="ID типа устройства")
    device_name_id = models.BigIntegerField(verbose_name="ID наименования устройства")
    rtn_id = models.IntegerField(null=True, blank=True, verbose_name="ID РТН")

    kind_device_id = models.BigIntegerField(verbose_name="ID вида устройства")
    kind_device_j_id = models.IntegerField(null=True, blank=True, verbose_name="ID вида устройства (J)")
    type_device_j_id = models.IntegerField(null=True, blank=True, verbose_name="ID типа устройства (J)")

    # Контроль
    sr_control_presence_id = models.IntegerField(null=True, blank=True, verbose_name="ID наличия СР контроля")
    cb_oncontrol = models.IntegerField(choices=YES_NO_CHOICES, default=0, verbose_name="На контроле")  # ?

    # Обновления
    date_updated = models.DateTimeField(null=True, blank=True, verbose_name="Дата обновления")
    updated_by = models.CharField(max_length=100, null=True, blank=True, verbose_name="Обновлено пользователем")
    is_deleted = models.IntegerField(choices=YES_NO_CHOICES, default=0, verbose_name="Удалено")  # ?

    class Meta:
        verbose_name = "Техническое устройство"
        verbose_name_plural = "Технические устройства"

    def __str__(self):
        return self.brand or self.registration_number or str(self.id)


class NameTU(models.Model):
    """
    Модель для хранения информации о наименованиях тех. устройств.
    """
    id = models.IntegerField(primary_key=True, default=0, verbose_name="ID")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")

    class Meta:
        verbose_name = "Название ТУ"
        verbose_name_plural = "Названия ТУ"

    def __str__(self):
        return self.name or str(self.id)


class KindTU(models.Model):
    """
    Модель для хранения информации о видах тех. устройств.
    """
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вид")

    is_for_journal = models.BooleanField(default=False, verbose_name="Для журнала")

    class Meta:
        verbose_name = "Вид ТУ"
        verbose_name_plural = "Виды ТУ"

    def __str__(self):
        return self.name or str(self.id)


# class KindTUJournal(models.Model):
#     """
#     Модель для хранения информации о видах тех. устройств, которые пойдут в журнал проверки (?)
#     """
#     id = models.IntegerField(null=True, blank=True, verbose_name="ID")
#     name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Вид (журнал)")
#
#     class Meta:
#         verbose_name = "Вид ТУ (журнал)"
#         verbose_name_plural = "Виды ТУ (журнал)"
#
#     def __str__(self):
#         return self.name or str(self.id)


class TypeTU(models.Model):
    """
    Модель для хранения информации о типах тех. устройств.
    """
    id = models.IntegerField(primary_key=True, default=0, verbose_name="ID")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тип")

    is_for_journal = models.BooleanField(default=False, verbose_name="Для журнала")

    class Meta:
        verbose_name = "Тип ТУ"
        verbose_name_plural = "Типы ТУ"

    def __str__(self):
        return self.name or str(self.id)


# class TypeTUJournal(models.Model):
#     """
#     Модель для хранения информации о типах тех. устройств, которые пойдут в журнал проверки (?)
#     """
#     id = models.IntegerField(null=True, blank=True, verbose_name="ID")
#     name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Тип (журнал)")
#
#     class Meta:
#         verbose_name = "Тип ТУ (журнал)"
#         verbose_name_plural = "Типы ТУ (журнал)"
#
#     def __str__(self):
#         return self.name or str(self.id)


# class TU_RTN(models.Model):
#     """
#     Модель для хранения информации о том, пойдет ли устройство в отчет РТН
#     """
#     id = models.IntegerField(null=True, blank=True, verbose_name="ID")
#     txt = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вердикт")
#
#     class Meta:
#         verbose_name = "ТУ РТН"
#         verbose_name_plural = "ТУ РТН"
#
#     def __str__(self):
#         return self.txt or str(self.id)


class ControlNote(models.Model):
    """
    Модель для хранения заметок контроля.
    Содержит текст заметки, дату создания и связанную информацию.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    tu_id = models.IntegerField(null=True, blank=True, verbose_name="ID технического устройства")
    auto_card_number = models.IntegerField(null=True, blank=True, verbose_name="Номер карты пользователя")
    text = models.TextField(null=True, blank=True, verbose_name="Текст заметки")
    created_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заметка контроля"
        verbose_name_plural = "Заметки контроля"

    def __str__(self):
        return self.text[:50] if self.text else "Заметка контроля (без текста)"


# class Availability(models.Model):
#     """
#     Модель для хранения информации о наличии тех. устройств
#     """
#     id = models.IntegerField(primary_key=True, verbose_name="ID")
#     txt = models.CharField(max_length=20, null=True, blank=True, verbose_name="Есть/нет")
#
#     class Meta:
#         verbose_name = 'Наличие'
#         verbose_name_plural = 'Наличие'
#
#     def __str__(self):
#         return self.txt or str(self.id)


# class PassportTUAvailability(models.Model):
#     """
#     Модель для хранения информации о наличии паспорта тех. устройства
#     """
#     id = models.IntegerField(primary_key=True, verbose_name="ID")
#     txt = models.CharField(max_length=20, null=True, blank=True, verbose_name="Есть/нет")
#
#     class Meta:
#         verbose_name = 'Наличие паспорта ТУ'
#         verbose_name_plural = 'Наличия паспортов ТУ'
#
#     def __str__(self):
#         return self.txt or str(self.id)


class Certificate(models.Model):
    """
    Модель для хранения информации о сертификате ТУ
    """
    id = models.BigAutoField(primary_key=True, verbose_name="ID сертификата")
    type = models.CharField(max_length=500, verbose_name="Тип сертификата")
    number = models.CharField(max_length=200, verbose_name="Номер сертификата")
    date_from = models.DateField(null=True, blank=True, verbose_name="Дата выдачи")
    date_to = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    issued_by = models.CharField(max_length=500, verbose_name="Кем выдано")
    tu_id = models.BigIntegerField(verbose_name="ID ТУ")
    scan = models.BinaryField(null=True, blank=True, verbose_name="Скан-копия")

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.number or str(self.id)


class Manufacturer(models.Model):
    """
    Модель для хранения информации о заводах-изготовителях
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Название завода"
    )

    class Meta:
        verbose_name = "Завод-изготовитель"
        verbose_name_plural = "Заводы-изготовители"

    def __str__(self):
        return self.name or str(self.id)


"""
Опасные объекты и надзор
"""


class OPO(models.Model):
    """
    Модель для хранения информации об ОПО
    """
    id = models.BigIntegerField(primary_key=True, verbose_name="ID ОПО")
    type_id = models.BigIntegerField(verbose_name="ID типа ОПО")
    structural_unit_id = models.BigIntegerField(verbose_name="ID структурного подразделения")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    short_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Краткое название")
    reg_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Регистрационный номер")

    class Meta:
        verbose_name = "ОПО"
        verbose_name_plural = "ОПО"

    def __str__(self):
        return self.reg_number or self.name or str(self.id)


class TypeOPO(models.Model):
    """
    Модель для хранения информации о типах ОПО
    """
    id = models.IntegerField(primary_key=True, default=0, verbose_name="ID")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    short_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Краткое название")
    reg_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="Регистрационный номер")

    class Meta:
        verbose_name = "Тип ОПО"
        verbose_name_plural = "Типы ОПО"

    def __str__(self):
        return self.name or self.reg_number or str(self.id)


class HazardClass(models.Model):
    """
    Модель, представляющая класс опасности.
    Используется для классификации опасных объектов.
    """
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название класса опасности")

    class Meta:
        verbose_name = "Класс опасности"
        verbose_name_plural = "Классы опасности"

    def __str__(self):
        return self.name if self.name else "Класс опасности (без названия)"


"""
Разное (вспомогательные справочники и настройки)
"""


class Setup(models.Model):
    """
    Модель для хранения информации о структурном подразделении
    """
    id = models.IntegerField(primary_key=True, verbose_name="ID организации")
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название")
    short_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Краткое название")
    structure_parent_id = models.IntegerField(null=True, blank=True, verbose_name="ID родительского подразделения")

    class Meta:
        verbose_name = "Конфигурация подразделения"
        verbose_name_plural = "Конфигурация подразделений"

    def __str__(self):
        return self.name or self.short_name or str(self.id)

# class YesNo(models.Model):
#     """
#     Какая-то гадость для приклеивания вердикта да/нет, когда это надо
#     """
#     id = models.IntegerField(null=True, blank=True)
#     txt = models.CharField(max_length=50, null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Да/Нет'
#         verbose_name_plural = 'Да/Нет'
#
#     def __str__(self):
#         return self.txt or str(self.id)
