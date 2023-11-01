from confluent_kafka import Consumer

conf = {'bootstrap.servers': "my-kafka.kafka.svc.cluster.local:9092",
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)
topics = ["test"]

    

try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue
            else:
                print(msg.value().decode('utf-8'))   
finally:
        # Close down consumer to commit final offsets.
        consumer.close()
