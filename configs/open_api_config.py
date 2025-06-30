from typing import Any, Final

OPEN_API_CONFIG: Final[dict[str, Any]] = {
    "title": "URL Shortener APP",
    "description": """__Este é um serviço de encurtamento de URLs, que permite transformar links longos em versões curtas e fáceis de compartilhar.__

  A API oferece endpoints para:
  - Criar uma URL encurtada a partir de um link original.
  - Redirecionar automaticamente ao link original a partir do código encurtado.""",
    "summary": "API para encurtamento e redirecionamento de URLs.",
    "version": "0.1.3",
    "openapi_tags": [
        {
            "name": "URLs",
            "description": "Operações relacionadas ao encurtamento, redirecionamento e gerenciamento de URLs.",
        }
    ],
}
