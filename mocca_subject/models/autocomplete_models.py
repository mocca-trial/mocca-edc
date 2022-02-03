from mocca_lists.models import ArvRegimens


class Rx(ArvRegimens):
    class Meta:
        proxy = True
        verbose_name = "ARV Regimens"
        verbose_name_plural = "ARV Regimens"
