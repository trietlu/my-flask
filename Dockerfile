FROM python:onbuild
COPY requirements.txt .
copy helloworld/ /
ENV PORT 8080
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["/usr/src/app/flaskrun.py"]
