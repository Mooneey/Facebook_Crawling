FROM nginx:stable

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install uwsgi

WORKDIR /etc/nginx

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

# 443 or 80 포트 개방
EXPOSE 80