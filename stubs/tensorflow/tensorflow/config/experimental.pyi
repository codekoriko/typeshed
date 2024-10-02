import typing_extensions
from _typeshed import Incomplete
from typing import TypedDict

from tensorflow.config import PhysicalDevice

class _MemoryInfo(TypedDict):
    current: int
    peak: int

def get_memory_info(device: str) -> _MemoryInfo: ...
def reset_memory_stats(device: str) -> None: ...
@typing_extensions.deprecated("This function is deprecated in favor of tf.config.experimental.get_memory_info")
def get_memory_usage(device: PhysicalDevice) -> int: ...
def get_memory_growth(device: PhysicalDevice) -> bool: ...
def set_memory_growth(device: PhysicalDevice, enable: bool) -> None: ...
def __getattr__(name: str) -> Incomplete: ...
