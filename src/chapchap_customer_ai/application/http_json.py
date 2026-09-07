import json

import httpx


def send_json(client: httpx.Client, request: httpx.Request, *, max_bytes: int = 65536):
    """No inherited client identity; never include external response bodies in errors."""
    response = client.send(request, auth=None, follow_redirects=False, stream=True)
    try:
        if (
            response.status_code != 200
            or response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
            != "application/json"
        ):
            raise ValueError("Invalid dependency response")
        content = bytearray()
        for block in response.iter_bytes():
            content.extend(block)
            if len(content) > max_bytes:
                raise ValueError("Dependency response exceeds size limit")
        return json.loads(content)
    finally:
        response.close()
