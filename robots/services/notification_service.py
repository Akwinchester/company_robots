import smtplib
from email.message import EmailMessage

from R4C.config import EMAIL_SENDER, EMAIL_PASSWORD


class NotificationService:

    def get_matching_orders(self, robot, Order):
        orders = Order.objects.filter(
            robot__isnull=True,
            robot_serial__contains=f"{robot.model}-{robot.version}"
        )
        return orders

    def update_order_status(self, order, robot):
        order.status = 'available'
        order.notified = True
        order.robot = robot
        order.save()

    def send_notification(self, order, robot):
        message = f"""
        Добрый день!
        Недавно вы интересовались нашим роботом модели {robot.model},  
        версии {robot.version}.
        Этот робот теперь в наличии. Если вам подходит этот вариант -   
        пожалуйста, свяжитесь с нами
        """

        email_sender = EMAIL_SENDER
        email_password = EMAIL_PASSWORD

        email_receiver = order.customer.email

        subject = "Уведомление о поступлении робота на склад"
        body = message

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(em)

    def handle_new_robot(self, robot, Order):
       orders = self.get_matching_orders(robot, Order)

       for order in orders:
          self.update_order_status(order, robot)
          self.send_notification(order, robot)