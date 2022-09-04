from threading import Thread
from kafka import KafkaConsumer
from json import loads


class KafkaMessageListener:
    threads = []
    consumers = []

    def init_app(self, app):
        # topic, broker list
        consumer = KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        self.consumers.append(consumer)
        thread = Thread(target=self.process_message, args=(consumer, "test"))
        self.threads.append(thread)
        for job in self.threads:
            job.start()

    def process_message(self, consumer, topic):
        # consumer list를 가져온다
        print('[begin] get consumer list')
        consumer.subscribe(topic)
        try:
            for message in consumer:        # blocking method
                print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" % (
                    message.topic, message.partition, message.offset, message.key, message.value
                ))
        except InterruptedError as ex:
            print('[end] interrupted: %s'.format(ex))
            pass
        print('[end] get consumer list')

    def shutdown(self):
        pass
