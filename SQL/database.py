from os import getenv
from dotenv import load_dotenv
from icecream import ic

load_dotenv()


class DBMYSQL:
    """Класс который хранит в себе параметры из .env связанные с БД, создает строку подключения к БД.
    Может одновременно работать в асинхронном и синхронном режиме исполльзуя два движка подключения

    Note:
        Для работы с двумя  и более разными СУБД можно наследоваться от этого класса,
         переопределив необходимые атрибуты

    Attributes:
    ----------
    DB_IS_CREATED : str
        По этому параметру определяется будет ли созданы и пересозданы таблицы в БД(если True)
        В .env используется строка True/False для перевода в bool использовать метод get_db_is_created
    DB_HOST : str
        Хост сервера с БД
    DB_PORT : str
        Порт подключения к БД
    DB_USER : str
        Логин пользователя у которого есть доступ к БД
    DB_PASS : str
        пароль учетной записи которой  находится в переменной DB_USER
    DB_NAME : str
        Имя бд к которой подключаемся
    DB_SQLite : str
        Путь и имя файла к БД SQL lite (name_db.db)
    DB_DBMS : str
        Основной тип СУБД для работы (MYSQL/PGSQL/SQLite)
    ECHO_DB : str
        Отключение логирования движка

    Methods:
    -------
    get_dsn()
        Необходим для получения строки подключения(dsn)

    get_db_is_created()
        Понадобится что бы перевести строку .env в bool python
    """

    DB_IS_CREATED: str = getenv('DB_IS_CREATED')
    DB_HOST: str = getenv('DB_HOST')
    DB_PORT: str = getenv('DB_PORT')
    DB_USER: str = getenv('DB_USER')
    DB_PASS: str = getenv('DB_PASS')
    DB_NAME: str = getenv('DB_NAME')
    DB_SQLite: str = getenv('DB_SQLite')
    DB_DBMS: str = getenv('DB_DBMS')
    ECHO_DB: str = getenv('ECHO_DB')

    def get_dsn(self) -> str:
        """Метод для получения строки подключения из .env
        :return: строку подключения (str)
        """

        driver = ""
        db_params = f"{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        match self.DB_DBMS:
            case  'MYSQL':
                driver = f"mysql+mysqlconnector://"
            case 'PGSQL':
                driver = f"postgresql+psycopg://"
            case 'SQLite':
                driver = f"sqlite+pysqlite://"
                db_params = f"/{self.DB_SQLite}"
        dsn_self = f"{driver}{db_params}"
        return dsn_self

    def get_async_dsn(self) -> str:
        """Метод для получения строки асинхронного подключения из .env
        :return: строку асинхронного подключения (str)
        """

        driver = ""
        db_params = f"{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        match self.DB_DBMS:
            case 'MYSQL':
                driver = f"mysql+aiomysql://"
            case 'PGSQL':
                driver = f"postgresql+asyncpg://"
            case 'SQLite':
                driver = f"sqlite+aiosqlite://"
                db_params = f"/{self.DB_SQLite}"
        dsn_self = f"{driver}{db_params}"
        return dsn_self

    def get_db_is_created(self) -> bool:
        """
        Переводит строку из .env в python bool
        :return: Возвращает True когда DB_IS_CREATED=True, в остальных случаях -> False
        """
        if self.DB_IS_CREATED == 'True':
            return True
        else:
            return False

    def get_db_is_echo(self) -> bool:
        """
        Переводит строку из .env в python bool
        :return: Возвращает True когда DB_IS_CREATED=True, в остальных случаях -> False
        """
        if self.ECHO_DB == 'True':
            return True
        else:
            return False
