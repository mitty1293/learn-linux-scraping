FROM python:3.9.0-slim-buster
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
COPY main.py /work/
RUN RUN apt-get update && \
    apt-get install -y cron && \
    pip3 install --upgrade pip && \
    pip3 install requests==2.25.1
RUN echo '00 4 * * * root /usr/local/bin/python /work/main.py > /work/cron.log 2>&1' >> /etc/crontab
CMD [ "cron", "-f"]