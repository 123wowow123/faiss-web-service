FROM continuumio/anaconda3

RUN conda install -c pytorch faiss-cpu
RUN conda install -c conda-forge sentence-transformers

COPY resources /opt/faiss-web-service/resources
COPY src /opt/faiss-web-service/src

ENTRYPOINT ["python", "/opt/faiss-web-service/src/app.py"]
