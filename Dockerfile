FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    HF_HOME=/data/huggingface TOKENIZERS_PARALLELISM=false
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir '.[rag]' \
    && groupadd --gid 10001 app \
    && useradd --uid 10001 --gid 10001 --create-home app \
    && mkdir -p /data/chroma /data/runtime /data/huggingface \
    && chown -R 10001:10001 /data
USER 10001:10001
EXPOSE 8085
CMD ["uvicorn", "chapchap_customer_ai.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8085", "--workers", "1"]
