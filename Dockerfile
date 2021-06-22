FROM python:3.9.0-slim-buster
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends cron && \
    pip3 install --upgrade pip && \
    pip3 install requests==2.25.1
RUN echo '00 9 * * * root /usr/local/bin/python /usr/src/main.py > /usr/src/cron.log 2>&1' >> /etc/crontab
CMD [ "cron", "-f"]