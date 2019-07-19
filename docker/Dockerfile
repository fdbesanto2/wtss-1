FROM brazildatacube/geo:0.1

ADD . /bdc-wtss

WORKDIR /bdc-wtss

RUN pip3 install -r requirements.txt

VOLUME /data

EXPOSE 5000

CMD [ "python3", "manage.py", "run" ]