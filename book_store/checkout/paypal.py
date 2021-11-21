import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AXh8m1Y-nMI2tniu6qPIHzF9lTzof_hc-QeLcp2ibW0S_uWjTkc8FAeHjtrrYjeFBKY5e0NamSkNkE0R"
        self.client_secret = ""
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
