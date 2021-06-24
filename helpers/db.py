import MySQLdb
from enum import Enum
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS
import logging


# SUPER CAN ADD FULL ADMINS
# FULL CAN ADD ONLY GROUP ADMINS
class AdminType(Enum):
    SUPER = 0
    FULL = 1
    GROUP = 2
    NOT_ADMIN = 100
    BAN = 200
    GBAN = 400


class DBHandler:
    """

    """

    _conn = None
    _cur = None

    def __init__(self):
        self._create_connection()

    def _create_connection(self):
        self._conn = MySQLdb.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASS,
            db=DB_NAME,
        )
        self._conn.autocommit(True)

    def _get_cursor(self):
        try:
            self._conn.ping(True)
        except MySQLdb.Error:
            # reconnect your cursor
            self._create_connection()
        self._cur = self._conn.cursor()

    async def set_admtype(self, user_id, admin_type, group_id):
        sql = f'INSERT INTO admins (user_id, admin_type, group_id) VALUES ({user_id},{admin_type},{group_id}) ON DUPLICATE KEY UPDATE admin_type = "{admin_type}"'
        logging.info(sql)
        self._get_cursor()
        self._cur.execute(sql)

    async def get_admin_type(self, user_id, group_id=0):
        sql = f'SELECT admin_type FROM admins WHERE user_id={user_id} AND group_id={group_id}'
        logging.info(sql)
        self._get_cursor()
        self._cur.execute(sql)
        admin_type = self._cur.fetchone()
        if admin_type:
            return admin_type[0]
        else:
            return 100

    # Allow_admis allows group admins to use bot commands
    # allow_all allows all group members to use bot commands
    # default is only GROUP, FULL or SUPER can use bot commands
    async def set_allowed(self, group_id, allow_admins=0, allow_all=0):
        sql = f'INSERT INTO groups (group_id, allow_admins, allow_all) VALUES ({group_id},{allow_admins},{allow_all}) ON DUPLICATE KEY UPDATE allow_admins={allow_admins}, allow_all={allow_all}'
        logging.info(sql)
        self._get_cursor()
        self._cur.execute(sql)

    async def get_allowed(self, group_id):
        allowed = {
            'admin': 0,
            'all': 0,
        }
        sql = f'SELECT allow_admins, allow_all FROM `groups` WHERE group_id={group_id}'
        logging.info(sql)
        self._get_cursor()
        self._cur.execute(sql)
        result = self._cur.fetchone()
        if result:
            allowed = {
                'admin': int(result[0]),
                'all': int(result[1]),
            }
        return allowed
