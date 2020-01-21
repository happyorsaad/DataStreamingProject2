import producer_server


BOOTSTRAP_SERVER_URL = 'localhost:9092'
TOPIC_NAME = 'police.service'
CLIENT_ID = "police.service.broker.id"

def run_kafka_server():
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC_NAME,
        bootstrap_servers=BOOTSTRAP_SERVER_URL,
        client_id=CLIENT_ID
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
