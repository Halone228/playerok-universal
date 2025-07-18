from __future__ import annotations

from typing import *
import json

from .account import Account
from . import parser
from .enums import *
from pydantic import BaseModel

class FileObject(BaseModel):
    """
    Объект файла.

    :param id: ID файла.
    :type id: `str`

    :param url: URL файла.
    :type url: `str`

    :param filename: Имя файла.
    :type filename: `str` or `None`

    :param mime: Mime файла.
    :type mime: `str` or `None`
    """
    id: str
    """ ID файла. """
    url: str
    """ URL файла. """
    filename: str | None
    """ Имя файла. """
    mime: str | None
    """ Mime файла. """

class AccountBalance(BaseModel):
    """
    Подкласс, описывающий баланс аккаунта.

    :param id: ID баланса.
    :type id: `str`

    :param value: Сумма баланса.
    :type value: `int`

    :param frozen: Сумма замороженного баланса.
    :type frozen: `int`

    :param available: Сумма доступного баланса.
    :type available: `int`

    :param withdrawable: Сумма баланса, доступного для вывода.
    :type withdrawable: `int`

    :param pending_income: Ожидаемый доход.
    :type pending_income: `int`
    """
    id: str
    """ ID баланса. """
    value: int
    """ Сумма общего баланса. """
    frozen: int
    """ Сумма замороженного баланса. """
    available: int
    """ Сумма доступного баланса. """
    withdrawable: int
    """ Сумма баланса, доступного для вывода. """
    pending_income: int
    """ Ожидаемый доход. """

class AccountIncomingDealsStats(BaseModel):
    """
    Подкласс, описывающий статистику входящих сделок аккаунта.

    :param total: Всего исходящих сделок.
    :type total: `int`

    :param finished: Завершённых исходящих сделок.
    :type finished: `int`
    """
    total: int
    """ Всего исходящих сделок. """
    finished: int
    """ Кол-во завершённых исходящих сделок. """

class AccountOutgoingDealsStats(BaseModel):
    """
    Подкласс, описывающий статистику исходящих сделок аккаунта.

    :param total: Всего исходящих сделок.
    :type total: `int`

    :param finished: Завершённых исходящих сделок.
    :type finished: `int`
    """
    total: int
    """ Всего исходящих сделок. """
    finished: int
    """ Кол-во завершённых исходящих сделок. """

class AccountDealsStats(BaseModel):
    """
    Подкласс, описывающий статистику сделок аккаунта.

    :param incoming: Входящие сделки.
    :type incoming: `types.AccountIncomingDealsStats`

    :param outgoing: Исходящие сделки.
    :type outgoing: `types.AccountOutgoingDealsStats`
    """
    incoming: AccountIncomingDealsStats
    """ Входящие сделки. """
    outgoing: AccountOutgoingDealsStats
    """ Исходящие сделки. """

class AccountItemsStats(BaseModel):
    """
    Подкласс, описывающий статистику предметов аккаунта.

    :param total: Всего предметов.
    :type total: `int`

    :param finished: Завершённых предметов.
    :type finished: `int`
    """
    total: int
    """ Всего предметов. """
    finished: int
    """ Кол-во завершённых предметов. """

class AccountStats(BaseModel):
    """
    Подкласс, описывающий статистику аккаунта.

    :param items: Статистика предметов.
    :type items: `types.AccountItemsStats`

    :param deals: Статистика сделок.
    :type deals: `types.AccountDealsStats`
    """
    items: AccountItemsStats
    """ Статистика предметов. """
    deals: AccountDealsStats
    """ Статистика сделок. """

class AccountProfile(BaseModel):
    """
    Класс, описывающий профиль аккаунта.

    :param id: ID аккаунта.
    :type id: `str`

    :param username: Никнейм аккаунта.
    :type username: `str`

    :param email: Почта аккаунта.
    :type email: `str`

    :param balance: Объект баланса аккаунта.
    :type balance: `types.AccountBalance`

    :param stats: Статистика аккаунта.
    :type stats: `str`

    :param role: Роль аккаунта.
    :type role: `enums.UserTypes`

    :param avatar_url: URL аватара аккаунта.
    :type avatar_url: `str`

    :param is_online: В онлайне ли сейчас аккаунт.
    :type is_online: `bool`

    :param is_blocked: Заблокирован ли аккаунт.
    :type is_blocked: `bool`

    :param is_blocked_for: Причина блокировки.
    :type is_blocked_for: `str`

    :param is_verified: Верифицирован ли аккаунт.
    :type is_verified: `bool`

    :param rating: Рейтинг аккаунта (0-5).
    :type rating: `int`

    :param reviews_count: Кол-во отзывов на аккаунте.
    :type reviews_count: `int`

    :param created_at: Дата создания аккаунта.
    :type created_at: `str`

    :param support_chat_id: ID чата поддержки.
    :type support_chat_id: `str`

    :param system_chat_id: ID системного чата.
    :type system_chat_id: `str`

    :param has_frozen_balance: Заморожен ли баланс на аккаунте.
    :type has_frozen_balance: `bool`

    :param has_enabled_notifications: Включены ли уведомления на аккаунте.
    :type has_enabled_notifications: `bool`
    """
    id: str
    """ ID аккаунта. """
    username: str
    """ Никнейм аккаунта. """
    email: str
    """ Почта аккаунта. """
    balance: AccountBalance
    """ Объект баланса аккаунта. """
    stats: AccountStats
    """ Статистика аккаунта. """
    role: UserTypes 
    """ Роль аккаунта. """
    avatar_url: str
    """ URL аватара аккаунта. """
    is_online: bool
    """ В онлайне ли сейчас аккаунт. """
    is_blocked: bool
    """ Заблокирован ли аккаунт. """
    is_blocked_for: bool
    """ Причина блокировки аккаунта. """
    is_verified: bool
    """ Верифицирован ли аккаунт. """
    rating: int
    """ Рейтинг аккаунта (0-5). """
    reviews_count: int
    """ Кол-во отзывов на аккаунте. """
    created_at: str
    """ Дата создания аккаунта. """
    support_chat_id: str
    """ ID чата поддержки аккаунта. """
    system_chat_id: str
    """ ID системного чата аккаунта. """
    has_frozen_balance: bool
    """ Заморожен ли баланс на аккаунте. """
    has_enabled_notifications: bool
    """ Включены ли уведомления на аккаунте. """

class UserProfile(BaseModel):
    """
    Класс, описывающий профиль пользователя.

    :param id: ID пользователя.
    :type id: `str`

    :param username: Никнейм пользователя.
    :type username: `str`

    :param role: Роль пользователя.
    :type role: `enums.UserTypes`

    :param avatar_url: URL аватара пользователя.
    :type avatar_url: `str`

    :param is_online: В онлайне ли сейчас пользователь.
    :type is_online: `bool`

    :param is_blocked: Заблокирован ли пользователь.
    :type is_blocked: `bool`

    :param rating: Рейтинг пользователя (0-5).
    :type rating: `int`

    :param reviews_count: Кол-во отзывов пользователя.
    :type reviews_count: `int`

    :param support_chat_id: ID чата поддержки.
    :type support_chat_id: `str` or `None`

    :param system_chat_id: ID системного чата.
    :type system_chat_id: `str` or `None`

    :param created_at: Дата создания аккаунта пользователя.
    :type created_at: `str`
    """
    id: str
    """ ID пользователя. """
    username: str
    """ Никнейм пользователя. """
    role: UserTypes
    """ Роль пользователя. """
    avatar_url: str
    """ URL аватара. """
    is_online: bool
    """ В онлайне ли сейчас пользователь. """
    is_blocked: bool
    """ Заблокирован ли пользователь. """
    rating: int
    """ Рейтинг пользователя (0-5). """
    reviews_count: int
    """ Кол-во отзывов пользователя. """
    support_chat_id: str | None
    """ ID чата поддержки. """
    system_chat_id: str | None
    """ ID системного чата. """
    created_at: str
    """ Дата создания аккаунта пользователя. """

    _account: Account | None
    """ Объект аккаунта (для методов). """

    def set_account(self, acc: Account):
        self._account = acc

    @property
    def __account(self):
        return self.__account

    def get_items(self, count: int = 24, statuses: list[ItemStatuses] | None = None,
                  after_cursor: str | None = None) -> ItemProfileList:
        """
        Получает предметы пользователя.

        :param count: Кол-во предеметов, которые нужно получить (не более 24 за один запрос), _опционально_.
        :type count: `int`

        :param status: Массив типов предметов, которые нужно получить. Некоторые статусы можно получить только, если это профиль вашего аккаунта. Если не указано, получает сразу все возможные.
        :type status: `list[enums.ItemStatuses]`

        :param after_cursor: Курсор, с которого будет идти парсинг (если нету - ищет с самого начала страницы), _опционально_.
        :type after_cursor: `str` or `None`
        
        :return: Страница профилей предметов.
        :rtype: `PlayerokAPI.types.ItemProfileList`
        """
        payload_status = [] if statuses else None
        if statuses:
            for status in statuses:
                payload_status.append(status.name)
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.__account.base_url
        }
        payload = {
            "operationName": "items",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"userId": self.id, "status": payload_status}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": "d79d6e2921fea03c5f1515a8925fbb816eacaa7bcafe03eb47a40425ef49601e"}}, ensure_ascii=False)
        }
        r = self.__account.request("get", f"{self.__account.base_url}/graphql", headers, payload).json()
        return parser.item_profile_list(r["data"]["items"])

    def get_reviews(self, count: int = 24, status: ReviewStatuses = ReviewStatuses.APPROVED, 
                                        comment_required: bool = False, rating: int | None = None, game_id: str | None = None, 
                    category_id: str | None = None, min_item_price: int | None = None, max_item_price: int | None = None, 
                    sort_direction: SortDirections = SortDirections.DESC, sort_field: str = "createdAt", after_cursor: str | None = None) -> ReviewList:
        """
        Получает отзывы пользователя.

        :param count: Кол-во отзывов, которые нужно получить (не более 24 за один запрос), _опционально_.
        :type count: `int`

        :param status: Тип отзывов, которые нужно получить.
        :type status: `enums.ReviewStatuses`

        :param comment_required: Обязателен ли комментарий в отзыве, _опционально_.
        :type comment_required: `bool`

        :param rating: Рейтинг отзывов (1-5), _опционально_.
        :type rating: `int` or `None`

        :param game_id: ID игры отзывов, _опционально_.
        :type game_id: `str` or `None`

        :param category_id: ID категории отзывов, _опционально_.
        :type category_id: `str` or `None`

        :param min_item_price: Минимальная цена предмета отзыва, _опционально_.
        :type min_item_price: `bool` or `None`

        :param max_item_price: Максимальная цена предмета отзыва, _опционально_.
        :type max_item_price: `bool` or `None`

        :param sort_direction: Тип сортировки.
        :type sort_direction: `enums.SortDirections`

        :param sort_field: Поле, по которому будет идти сортировка (по умолчанию `createdAt` - по дате)
        :type sort_field: `str`

        :param after_cursor: Курсор, с которого будет идти парсинг (если нету - ищет с самого начала страницы), _опционально_.
        :type after_cursor: `str` or `None`
        
        :return: Страница отзывов.
        :rtype: `PlayerokAPI.types.ReviewList`
        """
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.__account.base_url,
        }

        filters = {"userId": self.id, "status": [status.name] if status else None}
        if comment_required is not None:
            filters["hasComment"] = comment_required
        if game_id is not None:
            filters["gameId"] = game_id
        if category_id is not None:
            filters["categoryId"] = category_id
        if rating is not None:
            filters["rating"] = rating
        if min_item_price is not None or max_item_price is not None:
            item_price = {}
            if min_item_price is not None:
                item_price["min"] = min_item_price
            if max_item_price is not None:
                item_price["max"] = max_item_price
            filters["itemPrice"] = item_price
        payload = {
            "operationName": "testimonials",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": filters, "sort": {"direction": sort_direction.name if sort_direction else None, "field": sort_field}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": "bd4f2f6b77502701689193a1ab4cee28b683fc66164c54fba96fd01873b08a01"}}, ensure_ascii=False)
        }
        r = self.__account.request("get", f"{self.__account.base_url}/graphql", headers, payload).json()
        return parser.review_list(r["data"]["testimonials"])

class Event(BaseModel):
    #TODO: Сделать класс ивента Event
    pass

class ItemDeal(BaseModel):
    """
    Объект сделки с предметом.

    :param id: ID сделки.
    :type id: `str`

    :param status: Статус сделки.
    :type status: `enums.ItemDealStatuses`

    :param status_expiration_date: Дата истечения статуса.
    :type status_expiration_date: `str` or `None`

    :param status_description: Описание статуса сделки.
    :type status_description: `str` or `None`

    :param direction: Направление сделки (покупка/продажа).
    :type direction: `enums.ItemDealDirections`

    :param obtaining: Получение сделки.
    :type obtaining: `str` or `None`

    :param has_problem: Есть ли проблема в сделке.
    :type has_problem: `bool`

    :param report_problem_enabled: Включено ли обжалование проблемы.
    :type report_problem_enabled: `bool` or `None`

    :param completed_user: Профиль пользователя, подтвердившего сделку.
    :type completed_user: `types.UserProfile` or `None`

    :param props: Реквизиты сделки.
    :type props: `str` or `None`

    :param previous_status: Предыдущий статус.
    :type previous_status: `enums.ItemDealStatuses` or `None`

    :param completed_at: Дата подтверждения сделки.
    :type completed_at: `str` or `None`

    :param created_at: Дата создания сделки.
    :type created_at: `str` or `None`

    :param logs: Логи сделки.
    :type logs: `list[types.ItemLog]` or `None`

    :param transaction: Транзакция сделки.
    :type transaction: `types.Transaction` or `None`

    :param user: Профиль пользователя, совершившего сделку.
    :type user: `types.UserProfile`

    :param chat: Чат сделки (передаётся только его ID).
    :type chat: `types.Chat` or `None`

    :param item: Предмет сделки.
    :type item: `types.Item`

    :param review: Отзыв по сделке.
    :type review: `types.Review` or `None`

    :param obtaining_fields: Получаемые поля.
    :type obtaining_fields: `dict` or `None`

    :param comment_from_buyer: Комментарий от покупателя.
    :type comment_from_buyer: `str` or `None`
    """
    id: str
    """ ID сделки. """
    status: ItemDealStatuses
    """ Статус сделки. """
    status_expiration_date: str | None
    """ Дата истечения статуса. """
    status_description: str | None
    """ Описание статуса сделки. """
    direction: ItemDealDirections
    """ Направление сделки (покупка/продажа). """
    obtaining: str | None
    """ Получение сделки. """
    has_problem: bool
    """ Есть ли проблема в сделке. """
    report_problem_enabled: bool | None
    """ Включено ли обжалование проблемы. """
    completed_user: UserProfile | None
    """ Профиль пользователя, подтвердившего сделку. """
    props: str | None
    """ Реквизиты сделки. """
    previous_status: ItemDealStatuses | None
    """ Предыдущий статус. """
    completed_at: str | None
    """ Дата подтверждения сделки. """
    created_at: str | None
    """ Дата создания сделки. """
    logs: list[ItemLog] | None
    """ Логи сделки. """
    transaction: Transaction | None
    """ Транзакция сделки. """
    user: UserProfile
    """ Профиль пользователя, совершившего сделку. """
    chat: Chat | None
    """ Чат сделки (передаётся только его ID). """
    item: Item
    """ Предмет сделки. """
    review: Review | None
    """ Отзыв по сделке. """
    obtaining_fields: dict | None
    """ Получаемые поля. """
    comment_from_buyer: str | None
    """ Комментарий от покупателя. """

class ItemDealPageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице сделок.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class ItemDealList(BaseModel):
    """
    Класс, описывающий страницу отзывов.

    :param deals: Сделки страницы.
    :type deals: `list[types.ItemDeal]`

    :param page_info: Информация о странице.
    :type page_info: `types.ItemDealPageInfo`

    :param total_count: Всего сделок.
    :type total_count: `int`
    """
    deals: list[ItemDeal]
    """ Сделки страницы. """
    page_info: ItemDealPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего сделок. """

class GameCategoryAgreement(BaseModel):
    """
    Подкласс, описывающий соглашения покупателя.

    :param id: ID соглашения.
    :type id: `str`

    :param description: Описание соглашения.
    :type description: `str`

    :param icontype: Тип иконки соглашения.
    :type icontype: `enums.GameCategoryAgreementIconTypes`

    :param sequence: Последовательность соглашения.
    :type sequence: `str`
    """
    id: str
    """ ID соглашения. """
    description: str
    """ Описание соглашения. """
    icontype: GameCategoryAgreementIconTypes
    """ Тип иконки соглашения. """
    sequence: str
    """ Последовательность соглашения. """

class GameCategoryAgreementPageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице соглашений покупателя.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class GameCategoryAgreementList(BaseModel):
    """
    Класс, описывающий страницу соглашений покупателя.

    :param agreements: Соглашения страницы.
    :type agreements: `list[types.GameCategoryAgreement]`

    :param page_info: Информация о странице.
    :type page_info: `types.GameCategoryAgreementPageInfo`

    :param total_count: Всего соглашений.
    :type total_count: `int`
    """
    agreements: list[GameCategoryAgreement]
    """ Соглашения страницы. """
    page_info: GameCategoryAgreementPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего соглашений. """

class GameCategoryObtainingType(BaseModel):
    """
    Подкласс, описывающий тип (способ) получения предмета в категории.

    :param id: ID способа.
    :type id: `str`

    :param name: Название способа.
    :type name: `str`

    :param description: Описание способа.
    :type description: `str`

    :param game_category_id: ID категории игры способа.
    :type game_category_id: `str`

    :param no_comment_from_buyer: Без комментария от покупателя?
    :type no_comment_from_buyer: `bool`

    :param instruction_for_buyer: Инструкция для покупателя.
    :type instruction_for_buyer: `str`

    :param instruction_for_seller: Инструкция для продавца.
    :type instruction_for_seller: `str`

    :param sequence: Последовательность способа.
    :type sequence: `int`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float`

    :param agreements: Соглашения покупателя на покупку/продавца на продажу.
    :type agreements: `list[types.GameCategoryAgreement]`

    :param props: Пропорции категории.
    :type props: `types.GameCategoryProps`
    """
    id: str
    """ ID способа. """
    name: str
    """ Название способа. """
    description: str
    """ Описание способа. """
    game_category_id: str
    """ ID категории игры способа. """
    no_comment_from_buyer: bool
    """ Без комментария от покупателя? """
    instruction_for_buyer: str | None
    """ Инструкция для покупателя. """
    instruction_for_seller: str | None
    """ Инструкция для продавца. """
    sequence: int
    """ Последовательность способа. """
    fee_multiplier: float
    """ Множитель комиссии. """
    agreements: list[GameCategoryAgreement]
    """ Соглашения покупателя на покупку/продавца на продажу. """
    props: GameCategoryProps
    """ Пропорции категории. """

class GameCategoryObtainingTypePageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице типов (способов) получения предмета в категории.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class GameCategoryObtainingTypeList(BaseModel):
    """
    Класс, описывающий страницу типов (способов) получения предмета в категории.

    :param obtaining_types: Способы страницы.
    :type obtaining_types: `list[types.GameCategoryObtainingType]`

    :param page_info: Информация о странице.
    :type page_info: `types.GameCategoryObtainingTypePageInfo`

    :param total_count: Всего способов.
    :type total_count: `int`
    """
    obtaining_types: list[GameCategoryObtainingType]
    """ Соглашения страницы. """
    page_info: GameCategoryAgreementPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего способов. """

class GameCategoryDataField(BaseModel):
    """
    Подкласс, описывающий поля с данными предмета в категории (которые отправляются после покупки).

    :param id: ID поля с данными.
    :type id: `str`

    :param label: Надпись-название поля.
    :type label: `str`

    :param type: Тип поля с данными.
    :type type: `enums.GameCategoryDataFieldTypes`

    :param input_type: Тип вводимого значения поля.
    :type input_type: `enums.GameCategoryDataFieldInputTypes`

    :param copyable: Разрешено ли копирование значения с поля.
    :type copyable: `bool`

    :param hidden: Скрыты ли данные в поле.
    :type hidden: `bool`

    :param required: Обязательно ли это поле.
    :type required: `bool`

    :param value: Значение данных в поле.
    :type value: `str` or `None`
    """
    id: str
    """ ID поля с данными. """
    label: str
    """ Надпись-название поля. """
    type: GameCategoryDataFieldTypes
    """ Тип поля с данными. """
    input_type: GameCategoryDataFieldInputTypes
    """ Тип вводимого значения поля. """
    copyable: bool
    """ Разрешено ли копирование значения с поля. """
    hidden: bool
    """ Скрыты ли данные в поле. """
    required: bool
    """ Обязательно ли это поле. """
    value: str | None
    """ Значение данных в поле. """

class GameCategoryDataFieldPageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице полей с данными предмета.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class GameCategoryDataFieldList(BaseModel):
    """
    Класс, описывающий страницу полей с данными предмета.

    :param data_fields: Поля с данными предмета в категории на странице.
    :type data_fields: `list[types.GameCategoryDataField]`

    :param page_info: Информация о странице.
    :type page_info: `types.GameCategoryDataFieldPageInfo`

    :param total_count: Всего полей с данными.
    :type total_count: `int`
    """
    data_fields: list[GameCategoryDataField]
    """ Поля с данными предмета в категории на странице. """
    page_info: GameCategoryDataFieldPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего полей с данными. """

class GameCategoryProps(BaseModel):
    """
    Подкласс, описывающий пропорции категории.

    :param min_reviews: Минимальное количество отзывов.
    :type min_reviews: `int`

    :param min_reviews_for_seller: Минимальное количество отзывов для продавца.
    :type min_reviews_for_seller: `int`
    """
    min_reviews: int
    """ Минимальное количество отзывов. """
    min_reviews_for_seller: int
    """ Минимальное количество отзывов для продавца. """

class GameCategoryOption(BaseModel):
    """
    Подкласс, описывающий опцию категории.

    :param id: ID опции.
    :type id: `str`

    :param group: Группа опции.
    :type group: `str`

    :param label: Надпись-название опции.
    :type label: `str`

    :param type: Тип опции.
    :type type: `enums.GameCategoryOptionTypes`

    :param field: Название поля (для payload запроса на сайт).
    :type field: `str`

    :param value: Значение поля (для payload запроса на сайт).
    :type value: `str`

    :param value_range_limit: Лимит разброса по значению.
    :type value_range_limit: `int` or `None`
    """
    id: str
    """ ID опции. """
    group: str
    """ Группа опции. """
    label: str
    """ Надпись-название опции. """
    type: GameCategoryOptionTypes
    """ Тип опции. """
    field: str
    """ Название поля (для payload запроса на сайт). """
    value: str
    """ Значение поля (для payload запроса на сайт). """
    value_range_limit: int | None
    """ Лимит разброса по значению. """

class GameCategoryInstruction(BaseModel):
    """
    Подкласс, описывающий информацию о странице инструкии по продаже/покупке в категории.

    :param id: ID инструкции.
    :type id: `str`

    :param text: Текст инструкции.
    :type text: `str`
    """
    id: str
    """ ID инструкции. """
    text: str
    """ Текст инструкции. """

class GameCategoryInstructionPageInfo(BaseModel):
    """
    Подкласс, описывающий инструкцию по продаже/покупке в категории.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class GameCategoryInstructionList(BaseModel):
    """
    Класс, описывающий страницу инструкций по продаже/покупке в категории.

    :param instructions: Инструкции страницы.
    :type instructions: `list[types.GameCategoryInstruction]`

    :param page_info: Информация о странице.
    :type page_info: `types.GameCategoryInstructionPageInfo`

    :param total_count: Всего инструкций.
    :type total_count: `int`
    """
    instructions: list[GameCategoryInstruction]
    """ Соглашения страницы. """
    page_info: GameCategoryInstructionPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего инструкций. """

class GameCategory(BaseModel):
    """
    Объект категории игры/приложения.

    :param id: ID категории.
    :type id: `str`

    :param slug: Имя страницы категории.
    :type slug: `str`

    :param name: Название категории.
    :type name: `str`

    :param category_id: ID другой категории (?).
    :type category_id: `str` or `None`

    :param game_id: ID игры категории.
    :type game_id: `str` or `None`

    :param obtaining: Тип получения.
    :type obtaining: `str` or `None` or `None`

    :param options: Опции категории.
    :type options: `list[types.GameCategoryOption]` or `None`

    :param props: Пропорции категории.
    :type props: `types.GameCategoryProps` or `None`

    :param no_comment_from_buyer: Без комментария от покупателя?
    :type no_comment_from_buyer: `bool` or `None`

    :param instruction_for_buyer: Инструкция для покупателя.
    :type instruction_for_buyer: `str` or `None`

    :param instruction_for_seller: Инструкция для продавца.
    :type instruction_for_seller: `str` or `None`

    :param use_custom_obtaining: Используется ли кастомное получение.
    :type use_custom_obtaining: `bool`

    :param auto_confirm_period: Период авто-подтверждения сделки этой категории.
    :type auto_confirm_period: `enums.GameCategoryAutoConfirmPeriods` or `None`

    :param auto_moderation_mode: Включена ли автоматическая модерация.
    :type auto_moderation_mode: `bool` or `None`

    :param agreements: Соглашения покупателя.
    :type agreements: `list[types.GameCategoryAgreement]` or `None`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float` or `None`
    """
    id: str
    """ ID категории. """
    slug: str
    """ Имя страницы категории. """
    name: str
    """ Название категории. """
    category_id: str | None
    """ ID другой категории (?). """
    game_id: str | None
    """ ID игры категории. """
    obtaining: str | None
    """ Тип получения. """
    options: list[GameCategoryOption] | None
    """ Опции категории. """
    props: str | None
    """ Пропорции категории. """
    no_comment_from_buyer: bool | None
    """ Без комментария от покупателя? """
    instruction_for_buyer: str | None
    """ Инструкция для покупателя. """
    instruction_for_seller: str | None
    """ Инструкция для продавца. """
    use_custom_obtaining: bool
    """ Используется ли кастомное получение. """
    auto_confirm_period: GameCategoryAutoConfirmPeriods | None
    """ Период авто-подтверждения сделки этой категории. """
    auto_moderation_mode: bool | None
    """ Включена ли автоматическая модерация. """
    agreements: list[GameCategoryAgreement] | None
    """ Соглашения покупателя. """
    fee_multiplier: float | None
    """ Множитель комиссии. """

class Game(BaseModel):
    """
    Объект игры/приложения.

    :param id: ID игры/приложения.
    :type id: `str`

    :param slug: Имя страницы игры/приложения.
    :type slug: `str`

    :param name: Название игры/приложения.
    :type name: `str`

    :param type: Тип: игра или приложение.
    :type type: `enums.GameTypes`

    :param logo: Лого игры/приложения.
    :type logo: `types.FileObject`

    :param banner: Баннер игры/приложения.
    :type banner: `FileObject`

    :param categories: Список категорий игры/приложения.
    :type categories: `list[types.GameCategory]`

    :param created_at: Дата создания.
    :type created_at: `str`
    """
    id: str
    """ ID игры/приложения. """
    slug: str
    """ Имя страницы игры/приложения. """
    name: str
    """ Название игры/приложения. """
    type: GameTypes
    """ Тип: игра или приложение. """
    logo: FileObject
    """ Лого игры/приложения. """
    banner: FileObject
    """ Баннер игры/приложения. """
    categories: list[GameCategory]
    """ Список категорий игры/приложения. """
    created_at: str
    """ Дата создания. """

class GameProfile(BaseModel):
    """
    Профиль игры/приложения.

    :param id: ID игры/приложения.
    :type id: `str`

    :param slug: Имя страницы игры/приложения.
    :type slug: `str`

    :param name: Название игры/приложения.
    :type name: `str`

    :param type: Тип: игра или приложение.
    :type type: `types.GameTypes`

    :param logo: Лого игры/приложения.
    :type logo: `types.FileObject`
    """
    id: str
    """ ID игры/приложения. """
    slug: str
    """ Имя страницы игры/приложения. """
    name: str
    """ Название игры/приложения. """
    type: GameTypes
    """ Тип: игра или приложение. """
    logo: FileObject
    """ Лого игры/приложения. """

class GamePageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице игр.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class GameList(BaseModel):
    """
    Класс, описывающий страницу игр.

    :param games: Игры/приложения страницы.
    :type games: `list[types.Game]`

    :param page_info: Информация о странице.
    :type page_info: `types.ChatPageInfo`

    :param total_count: Всего игр.
    :type total_count: `int`
    """
    games: list[Game]
    """ Игры/приложения страницы. """
    page_info: ChatPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего игр. """

class ItemPriorityStatusPriceRange(BaseModel):
    """
    Подкласс, описывающий ценовой диапазон предмета, подходящего для опред. статуса приоритета.

    :param min: Минимальная цена предмета.
    :type min: `int`

    :param max: Максимальная цена предмета.
    :type max: `int`
    """
    min: int
    """ Минимальная цена предмета (в рублях). """
    max: int
    """ Максимальная цена предмета (в рублях). """

class ItemPriorityStatus(BaseModel):
    """
    Класс, описывающий статус приоритета предмета.

    :param id: ID статуса приоритета.
    :type id: `str`

    :param price: Цена статуса (в рублях).
    :type price: `int`

    :param name: Название статуса.
    :type name: `str`

    :param type: Тип статуса.
    :type type: `enums.PriorityTypes`

    :param period: Длительность статуса (в днях).
    :type period: `str`

    :param price_range: Ценовой диапазон предмета статуса.
    :type price_range: `types.ItemPriorityStatusPriceRange`
    """
    id: str
    """ ID статуса приоритета. """
    price: int
    """ Цена статуса (в рублях). """
    name: str
    """ Название статуса. """
    type: PriorityTypes
    """ Тип статуса. """
    period: int
    """ Длительность статуса (в днях). """
    price_range: ItemPriorityStatusPriceRange
    """ Ценовой диапазон предмета статуса. """

class ItemLog(BaseModel):
    """
    Подкласс, описывающий лог действия с предметом.
    
    :param id: ID лога.
    :type id: `str`
    
    :param event: Событие лога.
    :type event: `enums.ItemLogEvents`
    
    :param created_at: Дата создания лога.
    :type created_at: `str`
    
    :param user: Профиль пользователя, совершившего лог.
    :type user: `types.UserProfile`
    """
    id: str
    """ ID лога. """
    event: ItemLogEvents
    """ Событие лога. """
    created_at: str
    """ Дата создания лога. """
    user: UserProfile
    """ Профиль пользователя, совершившего лог. """

class Item(BaseModel):
    """
    Объект предмета.

    :param id: ID предмета.
    :type id: `str`

    :param status: Имя страницы предмета.
    :type status: `enums.ItemStatuses`

    :param name: Название предмета.
    :type name: `str`

    :param description: Описание предмета.
    :type description: `str`

    :param obtaining_type: Способ получения.
    :type obtaining_type: `types.GameCategoryObtainingType` or `None`

    :param price: Цена предмета.
    :type price: `int`

    :param raw_price: Цена без учёта скидки.
    :type raw_price: `int`

    :param priority_position: Приоритетная позиция.
    :type priority_position: `int`

    :param attachments: Файлы-приложения.
    :type attachments: `list[types.FileObject]`

    :param attributes: Аттрибуты предмета.
    :type attributes: `dict`

    :param buyer: Профиль покупателя предмета (если продан).
    :type buyer: `types.UserProfile`

    :param category: Категория игры предмета.
    :type category: `types.GameCategory`

    :param comment: Комментарий предмета.
    :type comment: `str` or `None`

    :param data_fields: Поля данных предмета.
    :type data_fields: `list[types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float`

    :param game: Профиль игры предмета.
    :type game: `types.GameProfile`

    :param seller_type: Тип продавца.
    :type seller_type: `enums.UserTypes`

    :param slug: Имя страницы предмета.
    :type slug: `str`

    :param user: Профиль продавца.
    :type user: `types.UserProfile`
    """
    id: str
    """ ID предмета. """
    slug: str
    """ Имя страницы предмета. """
    name: str
    """ Название предмета. """
    description: str
    """ Описание предмета. """
    obtaining_type: GameCategoryObtainingType | None
    """ Способ получения. """
    price: int
    """ Цена предмета. """
    raw_price: int
    """ Цена без учёта скидки. """
    priority_position: int
    """ Приоритетная позиция. """
    attachments: list[FileObject]
    """ Файлы-приложения. """
    attributes: dict
    """ Аттрибуты предмета. """
    buyer: UserProfile
    """ Профиль покупателя предмета (если продан). """
    category: GameCategory
    """ Категория игры предмета. """
    comment: str | None
    """ Комментарий предмета. """
    data_fields: list[GameCategoryDataField] | None
    """ Поля данных предмета. """
    fee_multiplier: float
    """ Множитель комиссии. """
    game: GameProfile
    """ Профиль игры предмета. """
    seller_type: UserTypes
    """ Тип продавца. """
    slug: str
    """ Имя страницы предмета. """
    status: ItemStatuses
    """ Статус предмета. """
    user: UserProfile
    """ Профиль продавца. """

class ItemProfile(BaseModel):
    """
    Профиль предмета.

    :param id: ID предмета.
    :type id: `str`

    :param slug: Имя страницы предмета.
    :type slug: `str`

    :param priority: Приоритет предмета.
    :type priority: `enums.PriorityTypes`

    :param status: Статус предмета.
    :type status: `enums.ItemStatuses`

    :param name: Название предмета.
    :type name: `str`

    :param price: Цена предмета.
    :type price: `int`

    :param raw_price: Цена без учёта скидки.
    :type raw_price: `int`

    :param seller_type: Тип продавца.
    :type seller_type: `enums.UserTypes`

    :param attachment: Файл-приложение.
    :type attachment: `types.FileObject`

    :param user: Профиль продавца.
    :type user: `types.UserProfile`

    :param approval_date: Дата одобрения.
    :type approval_date: `str`

    :param priority_position: Приоритетная позиция.
    :type priority_position: `int`

    :param views_counter: Количество просмотров.
    :type views_counter: `int` or `None`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float`

    :param created_at: Дата создания.
    :type created_at: `str`
    """
    id: str
    """ ID предмета. """
    slug: str
    """ Имя страницы предмета. """
    priority: PriorityTypes
    """ Приоритет предмета. """
    status: ItemStatuses
    """ Статус предмета. """
    name: str
    """ Название предмета. """
    price: int
    """ Цена предмета. """
    raw_price: int
    """ Цена без учёта скидки. """
    seller_type: UserTypes
    """ Тип продавца. """
    attachment: FileObject
    """ Файл-приложение. """
    user: UserProfile
    """ Профиль продавца. """
    approval_date: str
    """ Дата одобрения. """
    priority_position: int
    """ Приоритетная позиция. """
    views_counter: int | None
    """ Количество просмотров. """
    fee_multiplier: float
    """ Множитель комиссии. """
    created_at: str
    """ Дата создания. """

class ItemProfilePageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице предметов.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class ItemProfileList(BaseModel):
    """
    Профиль страницы предметов.

    :param items: Предметы страницы.
    :type items: `list[types.Item]`

    :param page_info: Информация о странице.
    :type page_info: `types.ItemProfilePageInfo`

    :param total_count: Всего предметов.
    :type total_count: `int`
    """
    items: list[ItemProfile]
    """ Предметы страницы. """
    page_info: ItemProfilePageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего предметов. """

class Transaction(BaseModel):
    """
    Объект транзакции.

    :param id: ID транзакции.
    :type id: `str`

    :param operation: Тип выполненной операции.
    :type operation: `enums.TransactionOperations`

    :param direction: Направление транзакции.
    :type direction: `enums.TransactionDirections`

    :param provider_id: ID платёжного провайдера.
    :type provider_id: `enums.TransactionProviderIds`

    :param status: Статус обработки транзакции.
    :type status: `enums.TransactionStatuses`

    :param value: Сумма транзакции.
    :type value: `int`

    :param created_at: Дата создания транзакции.
    :type created_at: `str`

    :param payment_method_id: ID способа оплаты.
    :type payment_method_id: `str` or `None`

    :param status_expiration_date: Дата истечения статуса транзакции.
    :type status_expiration_date: `str` or `None`
    """
    id: str
    """ ID транзакции. """
    operation: TransactionOperations
    """ Тип выполненной операции. """
    direction: TransactionDirections
    """ Направление транзакции. """
    provider_id: TransactionProviderIds
    """ ID платёжного провайдера. """
    status: TransactionStatuses
    """ Статус обработки транзакции. """
    value: int
    """ Сумма транзакции. """
    created_at: str
    """ Дата создания транзакции. """
    payment_method_id: str | None
    """ ID способа оплаты. """
    status_expiration_date: str | None
    """ Дата истечения статуса транзакции. """

class Moderator(BaseModel):
    # TODO: Сделать класс модератора Moderator
    pass

class ChatMessageButton(BaseModel):
    """
    Объект кнопки сообщения.

    :param type: Тип кнопки.
    :type type: `types.ChatMessageButtonTypes`

    :param url: URL кнопки.
    :type url: `str` or None

    :param text: Текст кнопки.
    :type text: `str`
    """
    type: ChatMessageButtonTypes
    """ Тип кнопки. """
    url: str | None
    """ URL кнопки. """
    text: str
    """ Текст кнопки. """

class ChatMessage(BaseModel):
    """
    Класс, описывающий сообщение в чате.

    :param id: ID сообщения.
    :type id: `str`

    :param text: Текст сообщения.
    :type text: `str`

    :param created_at: Дата создания сообщения.
    :type created_at: `str`

    :param deleted_at: Дата удаления сообщения.
    :type deleted_at: `str` or `None`

    :param is_read: Прочитано ли сообщение.
    :type is_read: `bool`

    :param is_suspicious: Подозрительное ли сообщение.
    :type is_suspicious: `bool`

    :param is_bulk_messaging: Массовая ли это рассылка.
    :type is_bulk_messaging: `bool`

    :param game: Игра, к которой относится сообщение.
    :type game: `str` or `None`

    :param file: Файл, прикреплённый к сообщению.
    :type file: `types.FileObject` or `None`

    :param user: Пользователь, который отправил сообщение.
    :type user: `types.UserProfile`

    :param deal: Сделка, к которой относится сообщение.
    :type deal: `types.Deal` or `None`

    :param item: Предмет, к которому относится сообщение (обычно передаётся только сама сделка в переменную deal).
    :type item: `types.Item` or `None`

    :param transaction: Транзакция сообщения.
    :type transaction: `types.Transaction` or `None`

    :param moderator: Модератор сообщения.
    :type moderator: `types.Moderator`

    :param event_by_user: Ивент от пользователя.
    :type event_by_user: `types.UserProfile` or `None`

    :param event_to_user: Ивент для пользователя.
    :type event_to_user: `types.UserProfile` or `None`

    :param is_auto_response: Авто-ответ ли это.
    :type is_auto_response: `bool`

    :param event: Ивент сообщения.
    :type event: `types.Event` or `None`

    :param buttons: Кнопки сообщения.
    :type buttons: `list[types.MessageButton]`
    """
    id: str
    """ ID сообщения. """
    text: str
    """ Текст сообщения. """
    created_at: str
    """ Дата создания сообщения. """
    deleted_at: str | None
    """ Дата удаления сообщения. """
    is_read: bool
    """ Прочитано ли сообщение. """
    is_suspicious: bool
    """ Подозрительное ли сообщение. """
    is_bulk_messaging: bool
    """ Массовая ли это рассылка. """
    game: Game | None 
    """ Игра, к которой относится сообщение. """
    file: FileObject | None 
    """ Файл, прикреплённый к сообщению. """
    user: UserProfile
    """ Пользователь, который отправил сообщение. """
    deal: ItemDeal | None
    """ Сделка, к которой относится сообщение. """
    item: ItemProfile | None
    """ Предмет, к которому относится сообщение (обычно передаётся только сама сделка в переменную deal). """
    transaction: Transaction | None
    """ Транзакция сообщения. """
    moderator: Moderator
    """ Модератор сообщения. """
    event_by_user: UserProfile | None
    """ Ивент от пользователя. """
    event_to_user: UserProfile | None
    """ Ивент для пользователя. """
    is_auto_response: bool
    """ Авто-ответ ли это. """
    event: Event | None
    """ Ивент сообщения. """
    buttons: list[ChatMessageButton]
    """ Кнопки сообщения. """

class ChatMessagePageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице сообщений.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class ChatMessageList(BaseModel):
    """
    Класс, описывающий страницу сообщений чата.

    :param messages: Сообщения страницы.
    :type messages: `list[types.ChatMessage]`

    :param page_info: Информация о странице.
    :type page_info: `types.ChatMessagePageInfo`

    :param total_count: Всего сообщений в чате.
    :type total_count: `int`
    """
    messages: list[ChatMessage]
    """ Сообщения страницы. """
    page_info: ChatMessagePageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего сообщений в чате. """

class Chat(BaseModel):
    """
    Объект чата.

    :param id: ID чата.
    :type id: `str`

    :param type: Тип чата.
    :type type: `enums.ChatTypes`

    :param status: Статус чата.
    :type status: `enums.ChatStatuses` or `None`

    :param unread_messages_counter: Количество непрочитанных сообщений.
    :type unread_messages_counter: `int`

    :param bookmarked: В закладках ли чат.
    :type bookmarked: `bool` or `None`

    :param is_texting_allowed: Разрешено ли писать в чат.
    :type is_texting_allowed: `bool` or `None`

    :param owner: Владелец чата (только если это чат с ботом).
    :type owner: `bool` or `None`

    :param deals: Сделки в чате.
    :type deals: `list[types.ItemDeal]` or `None`

    :param last_message: Объект последнего сообщения в чате
    :type last_message: `types.ChatMessage` or `None`

    :param users: Участники чата.
    :type users: `list[UserProfile]`

    :param started_at: Дата начала диалога.
    :type started_at: `str` or `None`

    :param finished_at: Дата завершения диалога.
    :type finished_at: `str` or `None`
    """
    id: str
    """ ID чата. """
    type: ChatTypes
    """ Тип чата. """
    status: ChatStatuses | None
    """ Статус чата. """
    unread_messages_counter: int
    """ Количество непрочитанных сообщений. """
    bookmarked: bool | None
    """ В закладках ли чат. """
    is_texting_allowed: bool | None
    """ Разрешено ли писать в чат. """
    owner: UserProfile
    """ Владелец чата. """
    deals: list[ItemDeal] | None
    """ Сделки в чате. """
    last_message: ChatMessage | None
    """ Объект последнего сообщения в чате. """
    users: list[UserProfile]
    """ Участники чата. """
    started_at: str | None
    """ Дата начала диалога. """
    finished_at: str | None
    """ Дата завершения диалога. """

class ChatPageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице чатов.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class ChatList(BaseModel):
    """
    Класс, описывающий страницу чатов.

    :param chats: Чаты страницы.
    :type chats: `list[types.Chat]`

    :param page_info: Информация о странице.
    :type page_info: `types.ChatPageInfo`

    :param total_count: Всего чатов.
    :type total_count: `int`
    """
    chats: list[Chat]
    """ Чаты страницы. """
    page_info: ChatPageInfo
    """ Информация о странице. """
    total_count: int
    """ Всего чатов. """

class Review(BaseModel):
    """
    Объект отзыва.

    :param id: ID отзыва.
    :type id: `str`

    :param status: Статус отзыва.
    :type status: `enums.ReviewStatuses`

    :param text: Текст отзыва.
    :type text: `str` or `None`

    :param rating: Рейтинг отзыва.
    :type rating: `int`

    :param created_at: Дата создания отзыва.
    :type created_at: `str`

    :param updated_at: Дата изменения отзыва.
    :type updated_at: `str`

    :param deal: Сделка, связанная с отзывом.
    :type deal: `Deal`

    :param creator: Профиль создателя отзыва.
    :type creator: `UserProfile`

    :param moderator: Модератор, обработавший отзыв.
    :type moderator: `Moderator` or `None`

    :param user: Профиль продавца, к которому относится отзыв.
    :type user: `UserProfile`
    """
    id: str
    """ ID отзыва. """
    status: ReviewStatuses
    """ Статус отзыва. """
    text: str | None
    """ Текст отзыва. """
    rating: int
    """ Рейтинг отзыва. """
    created_at: str
    """ Дата создания отзыва. """
    updated_at: str
    """ Дата изменения отзыва. """
    deal: ItemDeal
    """ Сделка, связанная с отзывом. """
    creator: UserProfile
    """ Профиль создателя отзыва. """
    moderator: Moderator | None
    """ Модератор, обработавший отзыв. """
    user: UserProfile
    """ Профиль продавца, к которому относится отзыв. """

class ReviewPageInfo(BaseModel):
    """
    Подкласс, описывающий информацию о странице отзывов.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """
    start_cursor: str
    """ Курсор начала страницы. """
    end_cursor: str
    """ Курсор конца страницы. """
    has_previous_page: bool
    """ Имеет ли предыдущую страницу. """
    has_next_page: bool
    """ Имеет ли следующую страницу. """

class ReviewList(BaseModel):
    """
    Класс, описывающий страницу отзывов.

    :param reviews: Отзывы страницы.
    :type reviews: `list[types.Review]`

    :param page_info: Информация о странице.
    :type page_info: `types.ReviewPageInfo`

    :param total_count: Всего отзывов.
    :type total_count: `int`
    """
    reviews: list[Review]
    """ Отзывы страницы. """
    page_info: ReviewPageInfo
    """ Информация о странице. """
    total_count: int

