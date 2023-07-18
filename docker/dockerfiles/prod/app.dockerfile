FROM python:3.10-alpine AS runner

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "-m", "gunicorn", "blog.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000" ]
