FROM php:7.4-fpm-alpine3.10

WORKDIR /app

COPY ./worker /app


RUN apk update && apk add --no-cache php-bcmath \
    mc \
    nano \
    php-json \
    php-mbstring \
    php-tokenizer \
    php-xml \
    php-curl \
    php7-dev \
    php7-dev \
    libmemcached-dev \
    libpng-dev \
    zlib-dev \
    && docker-php-ext-install gd mysqli


RUN chmod 0644 /app/ping_res.php
RUN crontab -l | { cat; echo "*/1 * * * * php /app/ping_res.php"; } | crontab -
CMD crond -f

#RUN apt-get update && apt-get install && apt-get install -y iputils-ping && apt-get install -y nano

#RUN apt-get install php-curl php-memcached php-mysql php-pgsql php-gd php-imagick php-intl php-mcrypt php-xml php-zip php-mbstring