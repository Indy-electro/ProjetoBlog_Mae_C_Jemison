from django.apps import AppConfig


class CadastroUsuarioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cadastroUsuario"

    def ready(self):
        import cadastroUsuario.signals
