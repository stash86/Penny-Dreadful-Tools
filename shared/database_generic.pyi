# make_stub_files: Sun 31 Dec 2017 at 16:46:32
from typing import Any
class GenericDatabase:
    def execute(self, sql: str, args: Any) -> None: ...
    def value(self, sql: str, args: Any=None, default: Any=None, fail_on_missing: Any=bool) -> Any: ...
        #   0: return self.values(sql,args)[0]
        # ? 0: return self.values(sql, args)[number]
        #   1: return default
        # ? 1: return default
    def values(self, sql: str, args: Any=None) -> Any: ...
        #   0: return list(row.values())[0] for row in rs
        # ? 0: return List[row.values()][number] for row in rs
    def insert(self, sql: str, args: Any=None) -> None: ...
    def is_mysql(self) -> bool: ...
    def is_sqlite(self) -> bool: ...
    def supports_lock(self) -> bool: ...
