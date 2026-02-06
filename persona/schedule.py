from datetime import datetime, time


WORK_START = time(10, 0)
WORK_END = time(18, 0)

SLEEP_START = time(23, 0)
SLEEP_END = time(7, 0)


def is_sleep_time(now: datetime | None = None) -> bool:
    now = now or datetime.now()
    t = now.time()

    return t >= SLEEP_START or t <= SLEEP_END


def is_work_time(now: datetime | None = None) -> bool:
    now = now or datetime.now()
    t = now.time()

    return WORK_START <= t <= WORK_END


def is_free_time(now: datetime | None = None) -> bool:
    return not is_work_time(now) and not is_sleep_time(now)
