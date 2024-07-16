from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.booking'

    def ready(self) -> None:
        import apps.booking.signals
