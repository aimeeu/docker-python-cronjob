FROM python:3.8.1
RUN apt-get update && apt-get -y install cron nano
# Set the time zone to the local time zone
RUN echo "America/Chicago" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

WORKDIR /app
COPY crontab /etc/cron.d/crontab
# COPY hello.py /app/hello.py
COPY . /app/
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["cron", "-f"]
