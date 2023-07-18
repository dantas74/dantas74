FROM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

FROM nginx:stable-alpine AS runner

WORKDIR /app

COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/staticfiles ./static

EXPOSE 80

