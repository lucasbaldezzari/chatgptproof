def contar_tokens(prompt, respuesta, costo_por_token):
    prompt_tokens = len(prompt.split())
    respuesta_tokens = len(respuesta.split())
    total_tokens = prompt_tokens + respuesta_tokens
    costo_total = total_tokens * costo_por_token
    return costo_total