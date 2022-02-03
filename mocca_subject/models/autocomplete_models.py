from mocca_lists.models import ArvRegimens as BaseArvRegimens


class ArvRegimens(BaseArvRegimens):
    class Meta:
        proxy = True
