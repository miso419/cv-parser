FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en

EXPOSE 4005
CMD ["python3", "/code/run.py"]
