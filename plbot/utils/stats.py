from datetime import datetime
from typing import Union



stats = {
    "bot_launch_time": datetime.now(),
    "orders_completed": 0,
    "orders_refunded": 0,
    "active_orders": 0,
    "earned_money": 0,
}

# Legacy support
def get_stats() -> dict[str, Union[int, str]]:
    """ Возвращает статистику """
    return stats

def set_stats(new_data):
    """ Устанавливает новую статистику """
    global stats
    stats = new_data
