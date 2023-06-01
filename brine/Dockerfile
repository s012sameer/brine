FROM python:3.10-alpine

WORKDIR /order_analyser
ADD src src
ADD test test
RUN pip3 install -r src/requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/order_analyser/src"

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["src/app.py"]