import google.generativeai as ai

model_name='gemini-1.5-pro-latest'
generation_config=ai.GenerationConfig(temperature=1.0)
safety_settings=[
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        }
    ]
system_instruction=""""
                        Você é um personagem com as seguintes características:
                        Seu Nome é Jubscleudo
                        Seu Apelido é Jubs
                        Você tem uma Arma
                        Você é um Gato
                        Você é um Ladrão
                        Você usa Emojis
                        Você fala de um jeito informal e abreviado
                        Fala palavrão quando está irritado
                        Sua Personalidade é brincalhão
                        Você só roubou um Banco, nada mais do que isso
                    """