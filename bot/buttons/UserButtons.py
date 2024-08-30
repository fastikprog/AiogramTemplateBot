from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


class UserButtons(

):
    def __init__(
        self,
        default_back_button=True,
        changing_lang_buttons=True,
        max_items_for_line=3
    ):
        # По умольчанию есть ли кнопка назад
        self._default_back_only = default_back_button
        # Есть ли кнопка для смены языка
        self._changing_lang_buttons = changing_lang_buttons
        self._max_items_for_line = max_items_for_line  # Макс кнопок в строку
        self._max_items_for_page = self._max_items_for_line * \
            5  # Макс кол кнопок на странице

    def one_button_inline(
        self,
        ButtonText: str = "❌ Закрыть",
        ButtonCall: str = "close"
    ) -> InlineKeyboardMarkup:
        button = [
            [
                InlineKeyboardButton(
                    text=ButtonText,
                    callback_data=ButtonCall
                )
            ]
        ]

        return InlineKeyboardMarkup(inline_keyboard=button)

    def one_button_keyboard(
        self,
        ButtonText: str = "🏠Главное меню🏠"
    ) -> ReplyKeyboardMarkup:
        button = [
            [
                KeyboardButton(
                    text=ButtonText
                )
            ]
        ]

        return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)

    def start_inline_button(
        self,
        language_code='ru',
        IsAdmin: bool = False
    ) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton(
                    text="👥 Реферальная система",
                    callback_data='ref_system'
                )
            ]
        ]

        if self._changing_lang_buttons:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🌐 Сменить язык",
                        callback_data="change_lang"
                    )
                ]
            )

        buttons.append(
            [
                InlineKeyboardButton(
                    text="🧑‍💻 Информация о разработчике",
                    callback_data='dev_info'
                )
            ]
        )

        return InlineKeyboardMarkup(inline_keyboard=buttons)

    def ref_system_inline_button(
        self,
        language_code: str = 'ru',
        back_button: bool = None
    ) -> InlineKeyboardMarkup:
        """ 
            Кнопки для рефералной системы
        """
        buttons = [
            [
                InlineKeyboardButton(
                    text="📜 Список рефералов",
                    callback_data="ref_list"
                )
            ]
        ]

        if back_button is not None:
            if back_button:
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text="🏠 В меню",
                            callback_data="menu"
                        )
                    ]
                )
        elif self._default_back_only:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🏠 В меню",
                        callback_data="menu"
                    )
                ]
            )

        return InlineKeyboardMarkup(
            inline_keyboard=buttons
        )

    def dev_inline_button(
        self,
        back_button: bool = None
    ) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🧑‍💻 Разработчик",
                    url="tg://user?id=5549357927"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌟 История изменения",
                    url="https://github.com/fastikprog/AiogramTemplateBot/commits/main/"
                ),
                InlineKeyboardButton(
                    text="⚙️ Использовать шаблон",
                    url="https://github.com/new?template_name=AiogramTemplateBot&template_owner=fastikprog"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗄 Репозитория",
                    url="https://github.com/fastikprog/AiogramTemplateBot"
                )
            ]
        ]

        if back_button is not None:
            if back_button:
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text="🏠 В меню",
                            callback_data="menu"
                        )
                    ]
                )
        elif self._default_back_only:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🏠 В меню",
                        callback_data="menu"
                    )
                ]
            )

        return InlineKeyboardMarkup(inline_keyboard=buttons)
