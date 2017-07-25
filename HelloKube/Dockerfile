FROM python:2.7-slim
LABEL maintainer="giovanni@syscode.uk"

WORKDIR /app
COPY hellokube.py /app
RUN pip install flask

ENTRYPOINT [ "python" ]
CMD [ "hellokube.py" ]

EXPOSE 9000
