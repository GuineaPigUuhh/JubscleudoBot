from discord import Embed

from settings import *

class ErrorHandler:
    secret = 'SECRETO 😉'
    error = None
    def __init__(self, error:Exception) -> None:
        self.error = error

    def embed(self):
        exception = str(self.error).replace(KEY, self.secret).replace(AI_KEY, self.secret)

        error = Embed(
                        title="Oppsss... Um Erro Acontenceu!", 
                        description="Parece que o Aplicativo deu problema, volte mais tarde."
                    )
        error.add_field(name="Descrição do Erro:", value=exception, inline=True)
        error.set_author(name="GuineaPigUuhh", 
                        url="https://github.com/GuineaPigUuhh",
                        icon_url="https://avatars.githubusercontent.com/u/93527295?s=400&u=f05f46740b146732f2121e2acba51edb0bc6a8f5&v=4"
                        )
        return error