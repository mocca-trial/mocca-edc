from mocca_lists.models import ArvRegimens as BaseArvRegimens


class ArvRegimens(BaseArvRegimens):
    class Meta:
        proxy = True
        verbose_name = "ARV Regimens"
        verbose_name_plural = "ARV Regimens"
