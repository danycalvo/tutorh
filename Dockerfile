FROM registry.access.redhat.com/ubi8/python-38
ADD requirements .
RUN python -m pip install -r requirements

WORKDIR /app
ADD . /app

ENV MI_DATA="DC says The result is:"
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000","--workers","2","app.app:app"]
