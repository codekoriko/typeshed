from typing import List, Tuple, Optional, Callable, Union, IO, Any, Dict
from datetime import datetime, tzinfo

__all__ = ...  # type: List[str]


class parserinfo(object):
    JUMP = ...  # type: List[str]
    WEEKDAYS = ...  # type: List[Tuple[str, str]]
    MONTHS = ...  # type: List[Tuple[str, str]]
    HMS = ...  # type: List[Tuple[str, str, str]]
    AMPM = ...  # type: List[Tuple[str, str]]
    UTCZONE = ...  # type: List[str]
    PERTAIN = ...  # type: List[str]
    TZOFFSET = ...  # type: Dict[str, int]

    def __init__(self, dayfirst: bool=..., yearfirst: bool=...) -> None: ...
    def jump(self, name: unicode) -> bool: ...
    def weekday(self, name: unicode) -> Union[int, None]: ...
    def month(self, name: unicode) -> Union[int, None]: ...
    def hms(self, name: unicode) -> Union[int, None]: ...
    def ampm(self, name: unicode) -> Union[int, None]: ...
    def pertain(self, name: unicode) -> bool: ...
    def utczone(self, name: unicode) -> bool: ...
    def tzoffset(self, name: unicode) -> Union[int, None]: ...
    def convertyear(self, year: int) -> int: ...
    def validate(self, res: datetime) -> bool: ...

class parser(object):
    def __init__(self, info: Optional[parserinfo] = ...) -> None: ...
    def parse(self, timestr: Union[str, unicode, IO[unicode]],
              default: Optional[datetime] = ...,
              ignoretz: bool = ..., tzinfos: Optional[Dict[Union[str, unicode], tzinfo]] = None,
              **kwargs: Any) -> datetime: ...

DEFAULTPARSER = ...  # type: parser
def parse(timestr: Union[str, unicode, IO[unicode]],
          parserinfo: Optional[parserinfo] = ...,
          **kwargs: Any) -> datetime: ...
