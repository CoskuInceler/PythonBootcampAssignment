import time
from plyer import notification

Title = "Reminder"
Message = "It is time to start working"
TimeOut = 5

notification.notify(
    title = Title,
    message = Message,
    timeout = TimeOut
)
time.sleep(10)
