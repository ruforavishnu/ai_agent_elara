from datetime import datetime, time


class TimeGuard:
    def __init__(self):
        # Work hours: 10:00 to 18:00
        self.work_start = time(10, 0)
        self.work_end = time(18, 0)

    def now(self) -> datetime:
        return datetime.now()

    def is_work_hours(self) -> bool:
        current_time = self.now().time()
        return self.work_start <= current_time < self.work_end

    def assert_allowed(self, task_type: str) -> None:
        """
        task_type: "work" or "off_hours"
        Raises an exception if task is not allowed.
        """

        if task_type == "work" and not self.is_work_hours():
            raise PermissionError(
                "This task is restricted to work hours (10:00–18:00)."
            )

        if task_type == "off_hours" and self.is_work_hours():
            raise PermissionError(
                "This task is only allowed after work hours."
            )