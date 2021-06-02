import logging

(logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='myapp1.log', filemode='w+'))

logging.info("Lorem Ipsum is simply dummy text of the printing and typesetting industry. ")

logging.info("Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled")

logging.info("It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.")

with open(r"C:\Users\ASUS\Desktop\91 Social\myapp1.log" , 'r') as f:
    for line in f:
      print (line)